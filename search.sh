MODEL=${1:-'resnet18'} # should be one of resnet18, resnext29_2x64d, efficientnet_v2_s, densenet121, gpt2
NUM_GPUS=${2:-"$(nvidia-smi --list-gpus | wc -l)"}

if [ $MODEL == 'resnet18' ]; then
    MODEL_PROVIDER="torchvision"
    KAS_SERVER_ARGS="--kas-acc-lower-bound 0.4 --kas-acc-upper-bound 0.7 --kas-max-flops-ratio 0.9 --kas-min-flops-ratio 0.15 --kas-max-enumerations 5 --kas-max-finalizations 2 --kas-depth 12 --kas-max-reductions 5 --kas-max-merges 1 --kas-max-splits 3 --kas-max-shifts 2 --kas-max-strides 0 --kas-max-size-multiplier 4 --kas-max-variables-in-size 3 --kas-max-chain-length 6 --kas-max-shift-rhs 2 --kas-max-expansion-merge-multiplier 2048 --kas-min-weight-share-dim 8 --kas-max-weight-share-dim 8 --kas-min-unfold-ratio 2.3 --client-mem-limit 10.0"
elif [ $MODEL == 'resnext29_2x64d' ]; then
    MODEL_PROVIDER="torchvision"
    KAS_SERVER_ARGS="--kas-acc-lower-bound 0.2 --kas-acc-upper-bound 0.7 --kas-max-flops-ratio 0.95 --kas-min-flops-ratio 0.15 --kas-max-enumerations 5 --kas-max-finalizations 2 --kas-depth 12 --kas-max-reductions 5 --kas-max-merges 2 --kas-max-splits 3 --kas-max-shifts 2 --kas-max-strides 0 --kas-max-size-multiplier 4 --kas-max-variables-in-size 3 --kas-max-chain-length 6 --kas-max-shift-rhs 2 --kas-max-expansion-merge-multiplier 4096 --kas-min-weight-share-dim 8 --kas-max-weight-share-dim 8 --kas-min-unfold-ratio 2.3 --client-mem-limit 5.0"
elif [ $MODEL == 'efficientnet_v2_s' ]; then
    MODEL_PROVIDER="torchvision"
    KAS_SERVER_ARGS="--kas-acc-lower-bound 0.3 --kas-acc-upper-bound 0.7 --kas-max-flops-ratio 0.9 --kas-min-flops-ratio 0.5 --kas-max-enumerations 5 --kas-max-finalizations 2 --kas-depth 12 --kas-max-reductions 5 --kas-max-merges 1 --kas-max-splits 3 --kas-max-shifts 2 --kas-max-strides 0 --kas-max-size-multiplier 4 --kas-max-variables-in-size 3 --kas-max-chain-length 6 --kas-max-shift-rhs 2 --kas-max-expansion-merge-multiplier 6144 --kas-min-weight-share-dim 8 --kas-max-weight-share-dim 24 --kas-min-unfold-ratio 2.3 --client-mem-limit 8.0"
elif [ $MODEL == 'densenet121' ]; then
    MODEL_PROVIDER="torchvision"
    KAS_SERVER_ARGS="--kas-acc-lower-bound 0.3 --kas-acc-upper-bound 0.7  --kas-max-flops-ratio 1.0 --kas-min-flops-ratio 0.15  --kas-max-enumerations 5 --kas-max-finalizations 2 --kas-depth 12 --kas-max-reductions 5 --kas-max-merges 1 --kas-max-splits 3 --kas-max-shifts 2 --kas-max-strides 0 --kas-max-size-multiplier 4 --kas-max-variables-in-size 3 --kas-max-chain-length 6 --kas-max-shift-rhs 2 --kas-max-expansion-merge-multiplier 5120 --kas-min-weight-share-dim 8 --kas-max-weight-share-dim 8 --kas-min-unfold-ratio 2.3 --client-mem-limit 8.0"
elif [ $MODEL == 'gpt2' ]; then
    MODEL_PROVIDER="gpt"
    KAS_SERVER_ARGS="--kas-max-flops-ratio 1.2 --kas-target loss --kas-max-enumerations 5 --kas-max-finalizations 2 --kas-depth 7 --kas-max-reductions 5 --kas-max-merges 2 --kas-max-splits 2 --kas-max-shifts 2 --kas-max-strides 0 --kas-max-size-multiplier 4 --kas-max-variables-in-size 3 --kas-max-chain-length 5 --kas-max-shift-rhs 2 --kas-max-expansion-repeat-multiplier 5 --kas-allow-tile --kas-max-expansion-merge-multiplier 6144 --kas-min-weight-share-dim 8 --kas-max-weight-share-dim 8 --kas-min-unfold-ratio 2.3 --kas-min-weight-nparams 100000 --client-mem-limit 10.0"
else
    echo "$MODEL is not supported. "
    exit 1
fi

if [ $MODEL == 'gpt2' ]; then
    KAS_CLIENT_ARGS="--batch-size 1 --lr 3e-4 --weight-decay 0.1 --grad-norm-clip 1.0 --dataset lm1b --compile --gpt-seq-len 2048 --gpt-tokenizer gpt2-large --gpt-max-iters 0 --gpt-max-minutes 30  --gpt-max-loss 6.9"
else
    KAS_CLIENT_ARGS="--sched cosine --epoch 100 --batch-size 128 \
    --warmup-epochs 0 --cooldown-epochs 0 --lr 0.1 --momentum 0.9 --weight-decay 0.001 --dataset cifar100 --num-classes 100 --compile"
fi

SCRIPT_PATH="$(dirname "$(readlink -f "$0")")"

mkdir -p $SCRIPT_PATH/results/$MODEL-session

bash $SCRIPT_PATH/run_tmux.sh $NUM_GPUS syno-$MODEL server \
    --kas-server-addr 0.0.0.0 --kas-server-port 7070 --kas-server-save-dir $SCRIPT_PATH/results/$MODEL-session --kas-server-save-interval 1800\
    --kas-search-algo MCTS \
    --model $MODEL_PROVIDER/$MODEL \
    --kas-sampler-workers 400 --kas-num-virtual-evaluator 4 \
    --kas-reward-power 4 $KAS_CLIENT_ARGS $KAS_SERVER_ARGS