#!/usr/bin/env bash

mkdir -p /workspace/Syno/AE/exp_data/vision/a100/nas-pte
cp -r ./external/nas-pte/* /workspace/Syno/AE/exp_data/vision/a100/nas-pte/
mkdir -p /workspace/Syno/AE/exp_data/vision/mdev/nas-pte
cp -r ./external/nas-pte/* /workspace/Syno/AE/exp_data/vision/mdev/nas-pte/

pushd /workspace/Syno/AE
bash gen_manual_kernels.sh exp_data/vision/mdev/manual_kernels 1
bash gen_manual_kernels.sh exp_data/vision/a100/manual_kernels 1
popd

python export_relax.py --batch-size 1 --model torchvision/resnet18
python export_relax.py --batch-size 1 --model torchvision/resnet34
python export_relax.py --batch-size 1 --model torchvision/resnext29_2x64d
python export_relax.py --batch-size 1 --model torchvision/efficientnet_v2_s
python export_relax.py --batch-size 1 --model torchvision/densenet121
