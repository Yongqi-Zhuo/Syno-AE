# Environment Setup

To setup the environment, clone this repo and go to the root directory. Then
```bash
docker build -t syno .
docker run -it --gpus all --shm-size=16.00gb -v $PWD/AE:/workspace/Syno/AE syno
cd Syno/AE
```
All our scripts are stored in the `AE` folder. 

Also, a stable network connection is needed, because we will download several datasets from torchvision and huggingface. 

# Searching

To reproduce the search experiments on Syno, run `bash search.sh $MODEL` for `$MODEL` in `resnet18`, `resnet34`, `resnext29_2x64d`, `densenet121`, `efficientnet_v2_s`, and `gpt2`. Note that the datasets will be automatically downloaded. 

Namely, the following commands should be used: 
```bash
bash search.sh resnet18
bash search.sh resnet34
bash search.sh resnext29_2x64d
bash search.sh efficientnet_v2_s
bash search.sh densenet121
bash search.sh gpt2
```

Each of the searching experiments should take at least one day on a machine with 8 A100 GPUs. If the search can last longer, then Syno can potentially find more kernels. The result will be stored in `AE/results/$MODEL-session`. 

# Reevaluation

From all kernels we've found during the searching, we need to pick kernels with high accuracy, and removed those with similar semantics. Then we reevaluate them on larger datasets (for vision models) or longer training steps (for GPT-2). 

## Vision Models

We assumed that the kernels found from the previous step is stored in `exp_data/vision/mdev/good-kernels-cifar100`. 

We also provide our data in `data/vision/mdev/good-kernels-cifar100`, then please copy it to `exp_data/vision/mdev/good-kernels-cifar100`, i.e., 

```bash
mkdir -p exp_data/vision/mdev
cp -r data/vision/mdev/good-kernels-cifar100 exp_data/vision/mdev/good-kernels-cifar100
```

Note that the kernels inside `data/vision/mdev/good-kernels-cifar100` are named as `01234_xxx`, where the first part is the accuracy and the second part is the kernel hash. Across different runs, the accuracy might change, but the hash should be the same. Therefore, you can also expect to find those kernel hashes in your search session. 

We use [FFCV](https://github.com/libffcv/ffcv) and [FFCV-ImageNet](https://github.com/libffcv/ffcv-imagenet) for fast ImageNet training, so preprocessing is needed as follows. If you have preprocessed imagenet on your machine, then the first two steps can be skipped. 

1. Download [ImageNet](https://image-net.org/challenges/LSVRC/2012/2012-downloads.php), i.e. in the link, download "Training images (Task 1 & 2)" and "Validation images (all tasks)" and untar those files. 
2. Preprocess the file to make it a PyTorch-style dataset. One can follow the instructions provided on https://github.com/MadryLab/pytorch-imagenet-dataset. 
3. Clone the repo [FFCV-ImageNet](https://github.com/libffcv/ffcv-imagenet), run
```bash
export IMAGENET_DIR=/path/to/pytorch/format/imagenet/directory/
export WRITE_DIR=/path/to/ffcv/format/imagenet/directory/

cd examples && ./write_imagenet.sh 400 0.10 90
```
where `$IMAGENET_DIR` contains the path to the imagenet dataset and the preprocessed dataset will be written into `$WRITE_DIR/train_400_0.10_90.ffcv` and `$WRITE_DIR/val_400_0.10_90.ffcv`. 
4. Finally, we register those files to the training configurations. Namely, go to `experiments/ffcv-imagenet/rn18_configs/rn18_88_epochs.yaml` and change line 5-6 to
```yaml
train_dataset: $WRITE_DIR/train_400_0.10_90.ffcv
val_dataset: $WRITE_DIR/val_400_0.10_90.ffcv
```
where `$WRITE_DIR` should be replaced with the path to the preprocessed dataset. 

To reevaluate those kernels on imagenet, run

```bash
export SOURCE_FOLDER="exp_data/vision/mdev/good-kernels-cifar100"
export TARGET_FOLDER="exp_data/vision/mdev/good-kernels-imagenet"

bash reevaluate_vision.sh resnet18 7070 $SOURCE_FOLDER/resnet $TARGET_FOLDER/resnet18
bash reevaluate_vision.sh resnet34 7070 $SOURCE_FOLDER/resnet $TARGET_FOLDER/resnet34
bash reevaluate_vision.sh resnext29_2x64d 7070 $SOURCE_FOLDER/resnext29_2x64d $TARGET_FOLDER/resnext29_2x64d
bash reevaluate_vision.sh efficientnet_v2_s 7070 $SOURCE_FOLDER/efficientnet_v2_s $TARGET_FOLDER/efficientnet_v2_s
bash reevaluate_vision.sh densenet121 7070 $SOURCE_FOLDER/densenet121 $TARGET_FOLDER/densenet121
```

Each Imagenet evaluation might take 15-30 hours, so in total it will take several days on a machine with 8 A100 GPUs. 

# GPT-2

For GPT-2, we pick one kernel `data/gpt2/good_kernels_lm1b/05675_10993262425417760381` and reevaluate it for 100,000 iterations. 

```bash
bash reevaluate_gpt.sh data/gpt2/good_kernels_lm1b/05675_10993262425417760381 logs/gpt_syno_losses.log
```

To evaluate other kernels searched by Syno, simply replacing `data/gpt2/good_kernels_lm1b/05675_10993262425417760381` with the other kernel. We also provide the loss curve in `data/gpt2/good_kernels_lm1b/gpt_syno_losses.log`.

# Obtain the accuracy for baseline

The accuracy for all baseline models are recorded in `experiments/analysis/baseline.json`. 

To obtain the baseline accuracies, one can use 
```bash
bash train_baseline.sh $MODEL $DATASET
```
where `$MODEL` is one of `resnet18`, `resnet34`, `resnext29_2x64d`, `densenet121`, `efficientnet_v2_s`, and `gpt2`; `$DATASET` is one of `imagenet` and `cifar100`. The logs will be found in `logs/$DATASET-baseline/$MODEL.log`, where you can find the accuracy at the end. 

# Obtain the accuracy for quantized models

The accuracy for quantized models and tiled conv are recorded in `experiments/analysis/plot-quantization.py:L47-52`. The following steps can be followed if you want to reproduce those numbers. 

For the quantization experiments, we trained the baseline, stacked convolution, and Operator 1 with resnet18 on imagenet. If you successfully run the previous step, you should be able to find the baseline checkpoint in `logs/resnet18-baseline/$UID/weights_90.pt`, where `$UID` is some random ids. Please copy the weight to `exp_data/vision/ckpt/resnet18_orig.pt`. Or, consider using our checkpoints provided in `data/vision/ckpt/resnet18_orig.pt`. 

To train stacked convolution, run `bash train_custom.sh resnet18 data/vision/mdev/Conv2d_Conv1d`. You will find the accuracy at the end of `logs/Conv2d_Conv1d/resnet18.log`.

To train Operator 1, run `bash train_custom.sh resnet18 data/vision/mdev/kernel_07889`. Similarly, you will find the accuracy at the end of `logs/kernel_07889/resnet18.log`.

To obtain the accuracy numbers for quantized resnet18, please run `bash eval_quantize.sh`. You will find the accuracy at the end of `logs/quant/resnet18.log`.

# Tuning with TVM and TorchInductor

TODO: @Yongqi-Zhuo

# Plot

To reproduce the plots in our paper with the data we provided, simply use `bash plot.sh`. The data is expected to be stored in `exp_data` with the same format of `data`. You can also use `data` if you prefer. 

As the performance are created in imagenet folders, we copy them to the corresponding folders in cifar100. Run
```bash
bash copy_perf.sh mdev
bash copy_perf.sh a100
```

The script will produce 5 figures in `AE/plots`: 
1. `end-to-end-performance.pdf`: Figure 5. 
2. `imagenet-performance.pdf`: Figure 6. 
3. `case-study.pdf`: Figure 8. 
4. `kernel-performance.pdf`: Figure 9. 
5. `gpt-loss.pdf`: Figure 10. 