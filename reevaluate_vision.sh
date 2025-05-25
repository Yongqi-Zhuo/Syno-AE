SCRIPT_PATH="$(dirname "$(readlink -f "$0")")"

MODEL=${1:-'resnet18'} # should be one of resnet18, resnet34, resnext29_2x64d, efficientnet_v2_s, densenet121
SERVER_PORT=${2:-"7070"}
SRC_DIR=${3:-"$SCRIPT_PATH/data/good_kernels_cifar100/$MODEL"}
DEST_DIR=${4:-"$SCRIPT_PATH/data/good_kernels_imagenet/$MODEL"}
NUM_GPUS=${5:-"$(nvidia-smi --list-gpus | wc -l)"}

if [[ "$SRC_DIR" != /* ]]; then
  SRC_DIR="$PWD/$SRC_DIR"
fi
if [[ "$DEST_DIR" != /* ]]; then
  DEST_DIR="$PWD/$DEST_DIR"
fi

if [ $MODEL == 'resnet18' ]; then
    MODEL_PROVIDER="torchvision"
    KAS_SERVER_ARGS="--kas-acc-lower-bound 0.4 --kas-acc-upper-bound 0.7 --kas-max-flops-ratio 0.9 --kas-min-flops-ratio 0.15 --kas-max-enumerations 5 --kas-max-finalizations 2 --kas-depth 12 --kas-max-reductions 5 --kas-max-merges 1 --kas-max-splits 3 --kas-max-shifts 2 --kas-max-strides 0 --kas-max-size-multiplier 4 --kas-max-variables-in-size 3 --kas-max-chain-length 6 --kas-max-shift-rhs 2 --kas-max-expansion-merge-multiplier 2048 --kas-min-weight-share-dim 8 --kas-max-weight-share-dim 8 --kas-min-unfold-ratio 2.3 --client-mem-limit 10.0"
elif [ $MODEL == 'resnet34' ]; then
    MODEL_PROVIDER="torchvision"
    KAS_SERVER_ARGS="--kas-acc-lower-bound 0.4 --kas-acc-upper-bound 0.7 --kas-max-flops-ratio 0.9 --kas-min-flops-ratio 0.15 --kas-max-enumerations 5 --kas-max-finalizations 2 --kas-depth 12 --kas-max-reductions 5 --kas-max-merges 1 --kas-max-splits 3 --kas-max-shifts 2 --kas-max-strides 0 --kas-max-size-multiplier 4 --kas-max-variables-in-size 3 --kas-max-chain-length 6 --kas-max-shift-rhs 2 --kas-max-expansion-merge-multiplier 2048 --kas-min-weight-share-dim 8 --kas-max-weight-share-dim 8 --kas-min-unfold-ratio 2.3 --client-mem-limit 20.0"
elif [ $MODEL == 'resnext29_2x64d' ]; then
    MODEL_PROVIDER="torchvision"
    KAS_SERVER_ARGS="--kas-acc-lower-bound 0.2 --kas-acc-upper-bound 0.7 --kas-max-flops-ratio 0.95 --kas-min-flops-ratio 0.15 --kas-max-enumerations 5 --kas-max-finalizations 2 --kas-depth 12 --kas-max-reductions 5 --kas-max-merges 2 --kas-max-splits 3 --kas-max-shifts 2 --kas-max-strides 0 --kas-max-size-multiplier 4 --kas-max-variables-in-size 3 --kas-max-chain-length 6 --kas-max-shift-rhs 2 --kas-max-expansion-merge-multiplier 4096 --kas-min-weight-share-dim 8 --kas-max-weight-share-dim 8 --kas-min-unfold-ratio 2.3 --client-mem-limit 5.0"
elif [ $MODEL == 'efficientnet_v2_s' ]; then
    MODEL_PROVIDER="torchvision"
    KAS_SERVER_ARGS="--kas-acc-lower-bound 0.3 --kas-acc-upper-bound 0.7 --kas-max-flops-ratio 0.9 --kas-min-flops-ratio 0.5 --kas-max-enumerations 5 --kas-max-finalizations 2 --kas-depth 12 --kas-max-reductions 5 --kas-max-merges 1 --kas-max-splits 3 --kas-max-shifts 2 --kas-max-strides 0 --kas-max-size-multiplier 4 --kas-max-variables-in-size 3 --kas-max-chain-length 6 --kas-max-shift-rhs 2 --kas-max-expansion-merge-multiplier 6144 --kas-min-weight-share-dim 8 --kas-max-weight-share-dim 24 --kas-min-unfold-ratio 2.3 --client-mem-limit 8.0"
elif [ $MODEL == 'densenet121' ]; then
    MODEL_PROVIDER="torchvision"
    KAS_SERVER_ARGS="--kas-acc-lower-bound 0.3 --kas-acc-upper-bound 0.7  --kas-max-flops-ratio 1.0 --kas-min-flops-ratio 0.15  --kas-max-enumerations 5 --kas-max-finalizations 2 --kas-depth 12 --kas-max-reductions 5 --kas-max-merges 1 --kas-max-splits 3 --kas-max-shifts 2 --kas-max-strides 0 --kas-max-size-multiplier 4 --kas-max-variables-in-size 3 --kas-max-chain-length 6 --kas-max-shift-rhs 2 --kas-max-expansion-merge-multiplier 5120 --kas-min-weight-share-dim 8 --kas-max-weight-share-dim 8 --kas-min-unfold-ratio 2.3 --client-mem-limit 8.0"
else
    echo "$MODEL is not supported. "
    exit 1
fi

mkdir -p $SCRIPT_PATH/logs/imagenet
KAS_CLIENT_ARGS="--dataset imagenet --imagenet-log-folder $SCRIPT_PATH/logs/imagenet/$MODEL-reevaluate --num-classes 1000 --batch-size 1024 --compile"

bash $SCRIPT_PATH/run_tmux.sh $NUM_GPUS syno-reevaluate-$MODEL reevaluator \
    --dirs $SRC_DIR --kas-server-save-dir $DEST_DIR\ --kas-server-save-interval 1800\
    --kas-server-addr 0.0.0.0 --kas-server-port $SERVER_PORT\
    --kas-search-algo MCTS \
    --model $MODEL_PROVIDER/$MODEL \
    --kas-sampler-workers 4 --kas-num-virtual-evaluator 1 \
    --kas-reward-power 4 $KAS_CLIENT_ARGS $KAS_SERVER_ARGS