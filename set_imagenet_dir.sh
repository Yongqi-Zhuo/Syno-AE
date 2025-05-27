WRITE_DIR=$1
SCRIPT_PATH="$(dirname "$(readlink -f "$0")")"

sed -i -E 's@train_dataset.*@train_dataset: '"$WRITE_DIR"'/train_400_0.10_90.ffcv@' $SCRIPT_PATH/../experiments/ffcv-imagenet/rn18_configs/rn18_88_epochs.yaml
sed -i -E 's@val_dataset.*@val_dataset: '"$WRITE_DIR"'/val_400_0.10_90.ffcv@' $SCRIPT_PATH/../experiments/ffcv-imagenet/rn18_configs/rn18_88_epochs.yaml