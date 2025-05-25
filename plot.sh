SCRIPT_PATH="$(dirname "$(readlink -f "$0")")"

RESULT_ROOT=${1:-"$SCRIPT_PATH/good_kernels_imagenet"}
OUTPUT_DIR=${2:-"$SCRIPT_PATH/plots"}

mkdir -p $OUTPUT_DIR

cd $SCRIPT_PATH/../experiments

python analysis/plot-models.py \
 --dirs resnet18 resnet34 densenet121 resnext29_2x64d efficientnet_v2_s\
 --models resnet18-imagenet resnet34-imagenet densenet121-imagenet resnext29_2x64d-imagenet efficientnet_v2_s-imagenet\
 --output $OUTPUT_DIR --max-acc-decrease 0.1 --latency \
 --mdev-path $SCRIPT_PATH/data/vision/mdev/good-kernels-imagenet\
 --a100-path $SCRIPT_PATH/data/vision/a100/good-kernels-imagenet\
 --baseline-latency-folder-mdev $SCRIPT_PATH/data/vision/mdev/baseline-latency\
 --baseline-latency-folder-a100 $SCRIPT_PATH/data/vision/a100/baseline-latency

python analysis/end_to_end_perf_plot.py --latency --output $OUTPUT_DIR\
 --mdev-path $SCRIPT_PATH/data/vision/mdev/good-kernels-cifar100\
 --a100-path $SCRIPT_PATH/data/vision/a100/good-kernels-cifar100\
 --baseline-latency-folder-mdev $SCRIPT_PATH/data/vision/mdev/baseline-latency\
 --baseline-latency-folder-a100 $SCRIPT_PATH/data/vision/a100/baseline-latency

python analysis/layerwise.py --output $OUTPUT_DIR\
 --mdev-path $SCRIPT_PATH/data/vision/mdev/good-kernels-cifar100\
 --a100-path $SCRIPT_PATH/data/vision/a100/good-kernels-cifar100\
 --baseline-latency-folder-mdev $SCRIPT_PATH/data/vision/mdev/baseline-latency\
 --baseline-latency-folder-a100 $SCRIPT_PATH/data/vision/a100/baseline-latency\
 --mdev-nas-pte-path $SCRIPT_PATH/data/vision/mdev/nas-pte\
 --a100-nas-pte-path $SCRIPT_PATH/data/vision/a100/nas-pte

python analysis/plot-loss.py --output $OUTPUT_DIR\
 --baseline-gpt-loss $SCRIPT_PATH/data/gpt2/baseline/gpt_orig_losses.log\
 --syno-gpt-loss $SCRIPT_PATH/data/gpt2/good_kernels_lm1b/gpt_syno_losses.log

python analysis/plot-quantization.py --output $OUTPUT_DIR\
 --mdev-path $SCRIPT_PATH/data/vision/mdev/good-kernels-cifar100\
 --a100-path $SCRIPT_PATH/data/vision/a100/good-kernels-cifar100\
 --baseline-latency-folder-mdev $SCRIPT_PATH/data/vision/mdev/baseline-latency\
 --baseline-latency-folder-a100 $SCRIPT_PATH/data/vision/a100/baseline-latency\
 --mdev-tiledconv-path $SCRIPT_PATH/data/vision/mdev/Conv2d_Conv1d\
 --a100-tiledconv-path $SCRIPT_PATH/data/vision/a100/Conv2d_Conv1d