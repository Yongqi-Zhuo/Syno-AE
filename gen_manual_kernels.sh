SCRIPT_PATH="$(dirname "$(readlink -f "$0")")"
OUTPUT_DIR=${1:-"$SCRIPT_PATH/exp_data/vision/mdev/manual_kernels"}
BATCH_SIZE=${2:-1}

if [[ "$ROOTDIR" != /* ]]; then
  OUTPUT_DIR="$PWD/$OUTPUT_DIR"
fi

mkdir -p "$OUTPUT_DIR/bs$BATCH_SIZE"

if [ -d "$OUTPUT_DIR/bs$BATCH_SIZE/Conv2d_Conv1d" ]; then
  rm -rf $OUTPUT_DIR/bs$BATCH_SIZE/Conv2d_Conv1d
fi

if [ -d "$OUTPUT_DIR/bs$BATCH_SIZE/kernel_07889" ]; then
  rm -rf $OUTPUT_DIR/bs$BATCH_SIZE/kernel_07889
fi

cd ../experiments
KERNELS="Conv2d_Conv1d,kernel_07889" python base/unit_tests/benchmark.py --model torchvision/resnet18 --kas-acc-lower-bound 0.4 --kas-acc-upper-bound 0.7 --kas-max-flops-ratio 0.9 --kas-min-flops-ratio 0.15 --kas-max-enumerations 5 --kas-max-finalizations 2 --kas-depth 12 --kas-max-reductions 5 --kas-max-merges 1 --kas-max-splits 3 --kas-max-shifts 2 --kas-max-strides 0 --kas-max-size-multiplier 4 --kas-max-variables-in-size 3 --kas-max-chain-length 6 --kas-max-shift-rhs 2 --kas-max-expansion-merge-multiplier 2048 --kas-min-weight-share-dim 8 --kas-max-weight-share-dim 8 --kas-min-unfold-ratio 2.3 --client-mem-limit 10.0 --batch-size $BATCH_SIZE --kas-scheduler-cache-dir "$OUTPUT_DIR/bs$BATCH_SIZE"

mkdir $OUTPUT_DIR/bs$BATCH_SIZE/kernel_scheduler_dir
mv $OUTPUT_DIR/bs$BATCH_SIZE/Conv2d_Conv1d/* $OUTPUT_DIR/bs$BATCH_SIZE/kernel_scheduler_dir
mv $OUTPUT_DIR/bs$BATCH_SIZE/kernel_scheduler_dir $OUTPUT_DIR/bs$BATCH_SIZE/Conv2d_Conv1d

mkdir $OUTPUT_DIR/bs$BATCH_SIZE/kernel_scheduler_dir
mv $OUTPUT_DIR/bs$BATCH_SIZE/kernel_07889/* $OUTPUT_DIR/bs$BATCH_SIZE/kernel_scheduler_dir
mv $OUTPUT_DIR/bs$BATCH_SIZE/kernel_scheduler_dir $OUTPUT_DIR/bs$BATCH_SIZE/kernel_07889