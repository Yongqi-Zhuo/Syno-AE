SCRIPT_PATH="$(dirname "$(readlink -f "$0")")"
SRC_DIR=${1:-"$SCRIPT_PATH/data/selected_kernels_gpt2/06297_45523330860059992"}
LOG_DIR=${2:-"$SCRIPT_PATH/logs/gpt_syno_losses.log"}

if [[ "$SRC_DIR" != /* ]]; then
  SRC_DIR="$PWD/$SRC_DIR"
fi
if [[ "$DEST_DIR" != /* ]]; then
  LOG_DIR="$PWD/$LOG_DIR"
fi

cd $SCRIPT_PATH/../experiments
python test_run.py --model gpt/gpt2\
 --batch-size 1 --lr 3e-4 --weight-decay 0.1 --grad-norm-clip 1.0 --dataset lm1b --compile --gpt-seq-len 2048 --gpt-tokenizer gpt2-large --gpt-max-iters 100000 --gpt-max-loss 10\
 --kas-test-path $SRC_DIR\
 --gpt-loss-output $LOG_DIR