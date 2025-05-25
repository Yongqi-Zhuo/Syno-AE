SCRIPT_PATH="$(dirname "$(readlink -f "$0")")"

MODEL=${1:-'resnet18'} # should be one of resnet18, resnet34, resnext29_2x64d, efficientnet_v2_s, densenet121, gpt2
CKPT_PATH=${2:-"$SCRIPT_PATH/exp_data/vision/ckpt/resnet18_orig.pt"}
LOGDIR=${2:-"$SCRIPT_PATH/logs/quant"}

MODEL_PROVIDER="torchvision"
TRAIN_ARGS="--dataset imagenet --imagenet-log-folder logs/$MODEL-baseline --num-classes 1000 --batch-size 1024 --compile"

mkdir -p $LOGDIR

cd $SCRIPT_PATH/../experiments
python test_run.py --model $MODEL_PROVIDER/$MODEL --kas-use-orig-model $TRAIN_ARGS --ckpt-path $CKPT_PATH --quant > $LOGDIR/$MODEL.log 2>&1