SCRIPT_PATH="$(dirname "$(readlink -f "$0")")"

MODEL=${1:-'resnet18'} # should be one of resnet18, resnet34, resnext29_2x64d, efficientnet_v2_s, densenet121, gpt2
DATASET=${2:-'imagenet'} # should be one of imagenet, cifar100
LOGDIR=${2:-"$SCRIPT_PATH/logs/$DATASET-baseline"}

if [ $MODEL == 'gpt2' ]; then
    MODEL_PROVIDER="gpt"
    TRAIN_ARGS="--batch-size 1 --lr 3e-4 --weight-decay 0.1 --grad-norm-clip 1.0 --dataset lm1b --compile --gpt-seq-len 2048 --gpt-tokenizer gpt2-large --gpt-max-iters 100000 --gpt-max-loss 10.0"
else
    MODEL_PROVIDER="torchvision"
    if [ $DATASET == 'cifar100' ]; then
        TRAIN_ARGS="--sched cosine --epoch 100 --batch-size 128 --warmup-epochs 0 --cooldown-epochs 0 --lr 0.1 --momentum 0.9 --weight-decay 0.001 --dataset cifar100 --num-classes 100 --compile"
    elif [ $DATASET == 'imagenet' ]; then
        TRAIN_ARGS="--dataset imagenet --imagenet-log-folder $SCRIPT_PATH/logs/$MODEL-baseline --num-classes 1000 --batch-size 1024 --compile"
    else
        echo "$DATASET is not supported. "
        exit 1
    fi
fi

mkdir -p $LOGDIR

cd $SCRIPT_PATH/../experiments
python test_run.py --model $MODEL_PROVIDER/$MODEL --kas-use-orig-model $TRAIN_ARGS > $LOGDIR/$MODEL.log 2>&1