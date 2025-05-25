SCRIPT_PATH="$(dirname "$(readlink -f "$0")")"

MODEL=${1:-'resnet18'} # should be one of resnet18, resnet34, resnext29_2x64d, efficientnet_v2_s, densenet121, gpt2
KERNEL_PATH=${2:-"$SCRIPT_PATH/data/vision/mdev/kernel_07889"}
KERNEL_NAME=$(basename $KERNEL_PATH)
LOGDIR=${3:-"$SCRIPT_PATH/logs/$KERNEL_NAME"}

if [[ "$KERNEL_PATH" != /* ]]; then
  KERNEL_PATH="$PWD/$KERNEL_PATH"
fi

if [ $MODEL == 'gpt2' ]; then
    MODEL_PROVIDER="gpt"
    TRAIN_ARGS="--batch-size 1 --lr 3e-4 --weight-decay 0.1 --grad-norm-clip 1.0 --dataset lm1b --compile --gpt-seq-len 2048 --gpt-tokenizer gpt2-large --gpt-max-iters 100000 --gpt-max-loss 10.0"
else
    MODEL_PROVIDER="torchvision"
    if
    TRAIN_ARGS="--dataset imagenet --imagenet-log-folder logs/$MODEL-$KERNEL_NAME --num-classes 1000 --batch-size 1024 --compile"
fi

mkdir -p $LOGDIR

cd $SCRIPT_PATH/../experiments
python test_run.py --model $MODEL_PROVIDER/$MODEL --kas-test-path KAS-next/AE/data/vision/mdev/kernel_07889 $TRAIN_ARGS > $LOGDIR/$MODEL.log 2>&1