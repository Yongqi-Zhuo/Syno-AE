#!/bin/bash

SCRIPT_PATH="$(dirname "$(readlink -f "$0")")"

ROOTDIR=${1:-"$SCRIPT_PATH/exp_data/vision/mdev/good-kernels-imagenet"}
BATCH_SIZE=${2:-1}

if [[ "$ROOTDIR" != /* ]]; then
  ROOTDIR="$PWD/$ROOTDIR"
fi

echo "Using root directory: $ROOTDIR"

CACHE_DIR="$SCRIPT_PATH/.recodegen-scheduler-cache"

rm -rf $CACHE_DIR

cd $SCRIPT_PATH/../experiments

for MODEL in $ROOTDIR/*; do

MODEL=$(basename $MODEL)

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

echo "Regenerating kernel scheduler directories for $MODEL......"
python analysis/re_codegen.py --model torchvision/$MODEL --batch-size $BATCH_SIZE --kas-sampler-workers 400 \
 $KAS_SERVER_ARGS --kas-scheduler-cache-dir $CACHE_DIR \
 --dirs $ROOTDIR/$MODEL

rm -rf $CACHE_DIR

done
