# Artifact Evaluation Repository for Syno: Structured Synthesis for Neural Operators

This repository contains the necessary steps to reproduce the results in the ASPLOS '25 paper "Syno: Structured Synthesis for Neural Operators".

# Environment Setup

To setup the environment, clone [Syno](https://github.com/tsinghua-ideal/Syno) recursively (including this repo as a submodule), and build the docker image.

```bash
git clone --recursive https://github.com/tsinghua-ideal/Syno.git
cd Syno
docker build -t syno .
# All the output data will go to Syno/AE, so bind this directory.
docker run -it --gpus all --shm-size=16.00gb -v $PWD/AE:/workspace/Syno/AE syno
cd Syno/AE
```

All our scripts are stored in the `AE` folder.

Also, a stable network connection is needed, because we will download several datasets from torchvision and huggingface.

For Jetson Orin Nano performance evaluation, you should build the image with the `--build-arg BASE_IMAGE=nvcr.io/nvidia/pytorch:25.04-py3-igpu` argument, which is the base image for Jetson Orin Nano. And you need to specify the runtime as `nvidia` because Jetson Orin Nano has an integrated GPU.

```bash
# Build command
docker build -t syno --build-arg BASE_IMAGE=nvcr.io/nvidia/pytorch:25.04-py3-igpu .
# Run command
docker run -it --runtime=nvidia --gpus all -v $PWD/AE:/workspace/Syno/AE syno
```

# High-Level Overview

The reproduction can be broken down into 4 steps. Each part can be skipped, if you use the data we provided in `AE/data`.

- Searching: Run the search. This step consumes a lot of computational resources. This step will produce operators in `AE/results`, and you need to cherry-pick the operators you like into `AE/exp_data`. Alternatively, copy the data we provided in `AE/data` to `AE/exp_data`.
- Reevaluation: To obtain the accuracy of Syno-optimized models on ImageNet (for vision models) or longer training steps (for GPT-2), we need to reevaluate the operators. This step will produce the accuracy of Syno-optimized models in `AE/exp_data`. Alternatively, copy the data we provided in `AE/data` to `AE/exp_data`.
- Tuning: To obtain the performance of Syno-optimized models on different devices, we need to tune the model with TVM and TorchInductor. This step will produce the performance of Syno-optimized models in `AE/exp_data`. Alternatively, copy the data we provided in `AE/data` to `AE/exp_data`.
- Plotting: Finally, we plot the results. This step will produce the plots in `AE/plots`.

# Searching

## Running the Search

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

Each of the searching experiments should take at least one day on a machine with 8 A100 GPUs. If the search can last longer, then Syno can potentially find more operators. The result will be stored in `AE/results/$MODEL-session`.

## Cherry-picking Operators

Next, from all operators we've found during the searching, you need to cherry-pick operators that produce high accuracy on vision models or low loss on GPT-2. During the search, we have already set FLOPs as a constraint so they are definitely fast so don't worry. Also, there may be a class of operators that look really similar, and you can only pick one of them to save your time. However there should not be too many, because of the canonicalization step in Syno.

### Vision Models

Pick the operators in vision model experiments and copy them to `exp_data/vision/mdev/good-kernels-cifar100`.

Alternatively, use the operators we obtained from our experiments, by copying them from `data` to `exp_data/vision/mdev/good-kernels-cifar100`, i.e.,

```bash
mkdir -p exp_data/vision/mdev
cp -r data/vision/mdev/good-kernels-cifar100 exp_data/vision/mdev/good-kernels-cifar100
```

Note that the operators inside `data/vision/mdev/good-kernels-cifar100` are named as `01234_xxx`, where the first part is the accuracy and the second part is the operator hash. Across different runs, the accuracy might change, but the hash should be the same. Therefore, you can also expect to find those operator hashes in your search session.

### GPT-2

Pick the operators from GPT-2 and copy them to `exp_data/gpt2/good_kernels_lm1b`. Alternatively, use the operators we obtained from our experiments, by copying them from `data` to `exp_data/gpt2/good_kernels_lm1b`, i.e.,

```bash
mkdir -p exp_data/gpt2
cp -r data/gpt2/good_kernels_lm1b exp_data/gpt2/good_kernels_lm1b
```

# Reevaluation

## Vision Models

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
4. Finally, register those files to the training configurations, with `bash set_imagenet_dir.sh $WRITE_DIR`.

To reevaluate those operators on imagenet, run

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

## Prepare for Tuning

The tuning step requires operators to be of batch size 1. As during reevaluation the batch size is set to 1024, you need to regenerate the operator kernels with

```bash
bash re_codegen.sh exp_data/vision/mdev/good-kernels-imagenet
```

Copy the accuracy to the a100 folder for later use in the tuning step.
```bash
mkdir -p exp_data/vision/a100
cp -r exp_data/vision/mdev/good-kernels-cifar100 exp_data/vision/a100
cp -r exp_data/vision/mdev/good-kernels-imagenet exp_data/vision/a100
```

## GPT-2

Use the following command to reevaluate the operator on GPT-2 with 100,000 iterations. Replace `05675_10993262425417760381` with the name of the operator you want to reevaluate.

```bash
OPERATOR_NAME=05675_10993262425417760381
bash reevaluate_gpt.sh exp_data/gpt2/good_kernels_lm1b/$OPERATOR_NAME$ exp_data/gpt2/good_kernels_lm1b/$OPERATOR_NAME$/loss.log
```

Alternatively, use the operator we obtained from our experiments. In our evaluation, we only chose one operator `data/gpt2/good_kernels_lm1b/05675_10993262425417760381`. Copy it to `exp_data/gpt2/good_kernels_lm1b` to use it directly. We also provide the loss curve in `data/gpt2/good_kernels_lm1b/05675_10993262425417760381/loss.log`.

## About Baselines

We have shipped the accuracy of baseline models for you. However, you can also reproduce the accuracy of the baselines yourself. To make the baseline accuracy comparable with the optimized models, the baseline models are trained with the same hyperparameters as the Syno-optimized models.

### Obtain the Accuracy for Baselines

The accuracy for all baseline models are recorded in `experiments/analysis/baseline.json`.

To obtain the baseline accuracies, one can use
```bash
bash train_baseline.sh $MODEL $DATASET
```
where `$MODEL` is one of `resnet18`, `resnet34`, `resnext29_2x64d`, `densenet121`, `efficientnet_v2_s`, and `gpt2`; `$DATASET` is one of `imagenet` and `cifar100`. The logs will be found in `logs/$DATASET-baseline/$MODEL.log`, where you can find the accuracy at the end.

### Obtain the accuracy for quantized models

The accuracy for quantized models and tiled conv are recorded in `experiments/analysis/plot-quantization.py:L47-52`. The following steps can be followed if you want to reproduce those numbers.

For the quantization experiments, we trained the baseline, stacked convolution, and Operator 1 with resnet18 on imagenet. If you successfully run the previous step, you should be able to find the baseline checkpoint in `logs/resnet18-baseline/$UID/weights_90.pt`, where `$UID` is some random ids. Please copy the weight to `exp_data/vision/ckpt/resnet18_orig.pt`. Or, consider using our checkpoints provided in `data/vision/ckpt/resnet18_orig.pt`.

Stacked convolution is manually implemented in `experiments/base/models/manual_kernels.py`, and we've generated the operator in `data/vision/mdev/manual_kernels/bs1024/Conv2d_Conv1d`. To train ResNet-18 with stacked convolution, run `bash train_custom.sh resnet18 data/vision/mdev/manual_kernels/bs1024/Conv2d_Conv1d`. You will find the accuracy at the end of `logs/Conv2d_Conv1d/resnet18.log`.

Operator 1 is `data/vision/mdev/good-kernels-cifar100/resnet/07889_15252107013978896537` and we manually reimplemented it in `data/vision/mdev/manual_kernels/bs1024/kernel_07889`. To train ResNet-18 with Operator 1, run `bash train_custom.sh resnet18 data/vision/mdev/manual_kernels/bs1024/kernel_07889`. Similarly, you will find the accuracy at the end of `logs/kernel_07889/resnet18.log`.

If you prefer to construct those operators manually, please run `bash gen_manual_kernels.sh exp_data/vision/mdev/manual_kernels 1024` and `bash gen_manual_kernels.sh exp_data/vision/a100/manual_kernels 1024`. The operators will be generated under `exp_data/vision/mdev`. Then you can use `bash train_custom.sh resnet18 exp_data/vision/mdev/manual_kernels/bs1024/Conv2d_Conv1d` and `bash train_custom.sh resnet18 exp_data/vision/mdev/manual_kernels/bs1024/kernel_07889` to run the above experiments.

To obtain the accuracy numbers for quantized resnet18, please run `bash eval_quantize.sh`. You will find the accuracy at the end of `logs/quant/resnet18.log`.

# Performance Tuning with TVM and TorchInductor

## Prerequisites

Note that you have to stay in `Syno/experiments/performance` to run the following commands.

```bash
cd /workspace/Syno/experiments/performance
```

The below preparation steps have been aggregated into `/workspace/Syno/AE/setup_tuning.sh`, but we explain them here for clarity.

You need to copy NAS-PTE operators to the results directory.

```bash
mkdir -p /workspace/Syno/AE/exp_data/vision/a100/nas-pte
cp -r ./external/nas-pte/* /workspace/Syno/AE/exp_data/vision/a100/nas-pte/
mkdir -p /workspace/Syno/AE/exp_data/vision/mdev/nas-pte
cp -r ./external/nas-pte/* /workspace/Syno/AE/exp_data/vision/mdev/nas-pte/
```

Manually generate the ablation operators.

```bash
pushd /workspace/Syno/AE
bash gen_manual_kernels.sh exp_data/vision/mdev/manual_kernels 1
bash gen_manual_kernels.sh exp_data/vision/a100/manual_kernels 1
popd
```

Export the TVM Relax models.

```bash
python export_relax.py --batch-size 1 --model torchvision/resnet18
python export_relax.py --batch-size 1 --model torchvision/resnet34
python export_relax.py --batch-size 1 --model torchvision/resnext29_2x64d
python export_relax.py --batch-size 1 --model torchvision/efficientnet_v2_s
python export_relax.py --batch-size 1 --model torchvision/densenet121
```

## Config Files

Because the performance tuning takes very long time, and there are just too many configurations to use, we have prepared grid tuners for you. The grid tuners read configuration files in JSON format. The configuration files are located in the `AE` directory.

`/workspace/Syno/AE/grid_tune.json` contains both the A100 configurations and the NVIDIA Jetson Orin Nano configurations.

`/workspace/Syno/AE/grid_tune.a100.json` contains only the A100 configurations.

`/workspace/Syno/AE/grid_tune.mdev.json` contains only the NVIDIA Jetson Orin Nano configurations.

The configuration files can be customized to cater to your needs. The configuration files are structured as follows:
```json
{
    "targets": [
        {
            "rpc_key": "a100",
            "prefix": "/workspace/Syno/AE/exp_data/vision/a100",
            "baseline_dir": "./baseline-latency",
            "target": "cuda -arch=sm_80 -max_threads_per_block=1024 -max_num_threads=2048 -thread_warp_size=32 -max_shared_memory_per_block=49152 -registers_per_block=65536",
            "target_host": "llvm -mtriple=x86_64-pc-linux-gnu -num-cores=128",
            "device": "cuda"
        },
        {
            "rpc_key": "jetson-orin-nano",
            "prefix": "/workspace/Syno/AE/exp_data/vision/mdev",
            "baseline_dir": "./baseline-latency",
            "target": "cuda -arch=sm_87 -max_threads_per_block=1024 -max_num_threads=1024 -thread_warp_size=32 -max_shared_memory_per_block=49152 -registers_per_block=65536",
            "target_host": "llvm -mtriple=aarch64-linux-gnu -mcpu=cortex-a78 -mattr=+neon -num-cores=6",
            "device": "cuda"
        },
        {
            "rpc_key": "jetson-orin-nano",
            "prefix": "/workspace/Syno/AE/exp_data/vision/mdev",
            "baseline_dir": "./baseline-latency",
            "target": "llvm -mtriple=aarch64-linux-gnu -mcpu=cortex-a78 -mattr=+neon -num-cores=6",
            "device": "cpu"
        }
    ],
    "kernels_dirs": {
        "resnet_18": [
            "./good-kernels-imagenet/resnet18/07045_4438388019704064842",
            ...
        ],
        ...
    },
}
```

The `targets` field contains the tuning target devices and their configurations. The fields are as follows:
- `prefix`: This field is shared by TVM and TorchInductor tuners. It specifies the the prefix of all directories, so that we can distinguish the results on A100 and NVIDIA Jetson Orin Nano. Our plotting script relies on the preset value so you need not change this field.
- `baseline_dir`: This field is shared by TVM and TorchInductor tuners. It specifies the relative location of the tuning results for baseline models. Our plotting script relies on the preset value so you need not change this field.
- `rpc_key`: This field is used by TVM to connect to specific RPC servers. You need not change this field.
- `target`: This field is used by TVM to specify the compilation target. For GPU targets, you need to specify the SM architecture and many other parameters, or alternatively specify a device name. Please refer to the TVM source code for more details. `target_host` field is required for GPU targets, which specifies the host platform of the GPU. For CPU targets, you need to specify the target triple, and **number of cores** (if you did not specify the correct number of cores, the performance can vary significantly). Also refer to the TVM source code for more details. If you only specified `target` without `target_host`, we replicate `target` for `target_host`. Also, there are several `target_preset`s, which are predefined in the code, but may not suit your hardware, so use `target` and `target_host` whenever possible. If you need to tune for performance on a different device than we provided (for example, a different GPU than A100, or if you do not want to use Jetson Orin Nano), you can change the `target` and `target_host` fields accordingly. In other cases, you can leave them unchanged.
- `device`: This field is used by TorchInductor to specify the device type. It can be either `cuda` or `cpu`. Usually, you can leave it unchanged.

The `kernels_dirs` field specifies the directories of all the operators you want to tune. You can provide a list of operators for each model. The tuning results (`benchmark_results.csv` for TVM and `.txt` for TorchInductor) for each operator will be placed in the very directory of the operator.

The grid tuners we provide will use the cartesian product of `targets` and `kernels_dirs` as tuning tasks. The performance numbers will be written to `prefix + baseline_dir` for baseline, and `prefix + kernels_dir` for the optimized models.

## Grid Tuners

The grid tuner for TVM is `grid_tune.py`, and the grid tuner for TorchInductor is `grid_torch.py`. The grid tuners will skip the tasks that have been done, so you can run them multiple times without worrying about overwriting the results.

The common arguments are as follows:
- `--config`: The path to the configuration file.
- `--dry-run`: If specified, the tuner will only print the tasks to be run, without actually running them. This is useful for checking if the configuration file is correct.
- `--clear`: If specified, the tuner will clear all previous results once run. Use with caution, as this will delete all previous results. However, if you decide to use the provided data in `AE/data`, you need to clear the previous results first, because we have shipped the tuning results as well.

Other options can be queried with the `--help` option.

## Tuning with TVM

TVM has been built into the docker image, with our patch.

### Setting up RPC tracker and RPC server

We use RPC to connect to multiple devices to make tuning faster. So you need:

1 RPC tracker running on your host. (Anywhere is OK but you need its ip address and port number)
Note that this tracker should be kept running.
```bash
python -m tvm.exec.rpc_tracker --host=0.0.0.0 --port=9190
# TRACKER_HOST=127.0.0.1
# TRACKER_PORT=9190
```

1 RPC server per device. It should be able to connect to the tracker.
Note that all RPC servers should be kept running.
```bash
# If you have an 8xA100 machine, use these
CUDA_VISIBLE_DEVICES=0 python -m tvm.exec.rpc_server --tracker=127.0.0.1:9190 --key=a100
CUDA_VISIBLE_DEVICES=1 python -m tvm.exec.rpc_server --tracker=127.0.0.1:9190 --key=a100
# ...

# If you have a Jetson Orin Nano, use this
# Note that you should avoid running the server, tracker or tuner on the Jetson Orin Nano, because it may hurt performance.
python -m tvm.exec.rpc_server --tracker=$TRACKER_HOST:$TRACKER_PORT --key=jetson-orin-nano
```

### Running the grid tuner

First, clear all previous results (if you use the data we provided), and check for tasks to run.
```bash
python grid_tune.py --config /workspace/Syno/AE/grid_tune.json --dry-run --clear
```

Then, run the grid tuner. This will take some time.
```bash
# If you have your A100 machine and Jetson Orin Nano both connected to your RPC tracker, you can run the following command to tune both at the same time.
python grid_tune.py --config /workspace/Syno/AE/grid_tune.json
# Otherwise, if you only have one type of device connected, you should use the corresponding config file.
# On A100
python grid_tune.py --config /workspace/Syno/AE/grid_tune.a100.json
# On NVIDIA Jetson Orin Nano
python grid_tune.py --config /workspace/Syno/AE/grid_tune.mdev.json
```

Note: if you encounter errors like
```
OpenBLAS blas_thread_init: RLIMIT_NPROC 2062971 current, 2062971 max
OpenBLAS blas_thread_init: pthread_create failed for thread 62 of 64: Resource temporarily unavailable
OpenBLAS blas_thread_init: ensure that your address space and process count limits are big enough (ulimit -a)
OpenBLAS blas_thread_init: or set a smaller OPENBLAS_NUM_THREADS to fit into what you have available
```

Do as it suggests before running the grid tuner:
```bash
export OPENBLAS_NUM_THREADS=1
```

### Alternative: Running without the grid tuner

You can actually tune the operators one by one.

```bash
python MetaScheduleTuner.py --target-preset "jetson_orin_nano-gpu" --rpc --rpc-host $TRACKER_HOST --rpc-port $TRACKER_PORT --rpc-key jetson-orin-nano --working-dir /workspace/Syno/AE/exp_data/vision/mdev/baseline-latency --progress --model torchvision/resnet18 --num-trials 10000 --vanilla
python MetaScheduleTuner.py --target-preset "jetson_orin_nano-gpu" --rpc --rpc-host $TRACKER_HOST --rpc-port $TRACKER_PORT --rpc-key jetson-orin-nano --working-dir /workspace/Syno/AE/exp_data/vision/mdev/baseline-latency --progress --model torchvision/resnet18 --num-trials 10000 --kernels-dir /workspace/Syno/AE/exp_data/vision/mdev/good-kernels-imagenet/resnet18/07045_4438388019704064842
```

The required command line arguments can be obtained by running `python grid_tune.py --config /workspace/Syno/AE/grid_tune.json --dry-run`.

### Tuning the quantized models

```bash
python quantize.py --target-preset "jetson_orin_nano-gpu" --rpc --rpc-host $TRACKER_HOST --rpc-port $TRACKER_PORT --rpc-key jetson-orin-nano --working-dir /workspace/Syno/AE/exp_data/vision/mdev/baseline-latency
python quantize.py --target-preset "jetson_orin_nano-cpu" --rpc --rpc-host $TRACKER_HOST --rpc-port $TRACKER_PORT --rpc-key jetson-orin-nano --working-dir /workspace/Syno/AE/exp_data/vision/mdev/baseline-latency
python quantize.py --target-preset "a100_gpu" --rpc --rpc-host $TRACKER_HOST --rpc-port $TRACKER_PORT --rpc-key a100 --working-dir /workspace/Syno/AE/exp_data/vision/a100/baseline-latency
```

## Tuning with TorchInductor

First, clear all previous results (if you use the data we provided), and check for tasks to run.
```bash
python grid_torch.py --config /workspace/Syno/AE/grid_tune.json --dry-run --clear
```

Then, run the grid tuner. This will take some time. Note that different from TVM, you can only run TorchInductor tuning locally on the device you want to benchmark. So you need to run the following commands on the corresponding device.
```bash
# On A100
python grid_torch.py --config /workspace/Syno/AE/grid_tune.a100.json
# On NVIDIA Jetson Orin Nano
python grid_torch.py --config /workspace/Syno/AE/grid_tune.mdev.json
```

After the tuning is done, you need to copy (or `rsync`) the results back to your host machine.

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
