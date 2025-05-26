DEVICE=${1:-"mdev"}

python ../experiments/analysis/sync_perf.py\
 --dirs \
 exp_data/vision/$DEVICE/good-kernels-imagenet/resnet18\
 exp_data/vision/$DEVICE/good-kernels-imagenet/resnext29_2x64d\
 exp_data/vision/$DEVICE/good-kernels-imagenet/densenet121\
 exp_data/vision/$DEVICE/good-kernels-imagenet/efficientnet_v2_s\
 --destinations \
 exp_data/vision/$DEVICE/good-kernels-cifar100/resnet\
 exp_data/vision/$DEVICE/good-kernels-cifar100/resnext29_2x64d\
 exp_data/vision/$DEVICE/good-kernels-cifar100/densenet121\
 exp_data/vision/$DEVICE/good-kernels-cifar100/efficientnet_v2_s