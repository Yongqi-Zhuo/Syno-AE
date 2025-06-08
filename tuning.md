To help reviewers run the tuning step, we provide the following detailed instructions.

# Tuning on a 8xA100 machine for A100 inference performance numbers

First make sure you have our reference operators stored in `/workspace/Syno/AE/exp_data`. The simplest way to do this is to copy from the reference data directory `/workspace/Syno/AE/data`. The second way is to follow the instructions in the reevaluation step (pay attention to the "prepare for tuning" sub-step); if this is the case, do not copy again (which would overwrite your existing inference accuracy numbers).

Then, follow the steps below.

```bash
# Stay in this directory for the rest of the tuning
cd /workspace/Syno/experiments/performance

# Run the preparation script
/workspace/Syno/AE/setup_tuning.sh
```

## Tuning with TVM

First, the preparation steps.

```bash
# Set up the RPC tracker and servers
tmux new -d -s tracker "python -m tvm.exec.rpc_tracker --host=0.0.0.0 --port=9190"
for i in {0..7}; do
    tmux new -d -s "server$i" "env CUDA_VISIBLE_DEVICES=$i python -m tvm.exec.rpc_server --tracker=127.0.0.1:9190 --key=a100"
done

# Modify the tuning config file to exclude models other than ResNet.
echo > /workspace/Syno/AE/grid_tune.a100.json << EOF
{
    "targets": [
        {
            "rpc_key": "a100",
            "prefix": "/workspace/Syno/AE/exp_data/vision/a100",
            "baseline_dir": "./baseline-latency",
            "target": "cuda -arch=sm_80 -max_threads_per_block=1024 -max_num_threads=2048 -thread_warp_size=32 -max_shared_memory_per_block=49152 -registers_per_block=65536",
            "target_host": "llvm -mtriple=x86_64-pc-linux-gnu -num-cores=128",
            "device": "cuda"
        }
    ],
    "kernels_dirs": {
        "resnet_18": [
            "./good-kernels-imagenet/resnet18/06705_7106109518359021661",
            "./good-kernels-imagenet/resnet18/06708_14619554982559354367",
            "./good-kernels-imagenet/resnet18/06726_11877750221072847753",
            "./good-kernels-imagenet/resnet18/06738_10756581942128284194",
            "./good-kernels-imagenet/resnet18/06747_10949904241425474452",
            "./good-kernels-imagenet/resnet18/06772_10923347917424993262",
            "./good-kernels-imagenet/resnet18/06864_6292075666050645745",
            "./good-kernels-imagenet/resnet18/06906_7346917085106034487",
            "./good-kernels-imagenet/resnet18/06937_14356514157639530665",
            "./good-kernels-imagenet/resnet18/06953_12025277355725566799",
            "./good-kernels-imagenet/resnet18/06970_4536540647343069734",
            "./good-kernels-imagenet/resnet18/07045_4438388019704064842",
            "./manual_kernels/bs1/Conv2d_Conv1d"
        ],
        "resnet_34": [
            "./good-kernels-imagenet/resnet34/07029_3040503201941035733",
            "./good-kernels-imagenet/resnet34/07089_13102253380479934281",
            "./good-kernels-imagenet/resnet34/07096_10053342605815977959",
            "./good-kernels-imagenet/resnet34/07125_3502276718624296764",
            "./good-kernels-imagenet/resnet34/07138_1877672947194075639",
            "./good-kernels-imagenet/resnet34/07140_2587021473300072582",
            "./good-kernels-imagenet/resnet34/07239_540923922250864272",
            "./good-kernels-imagenet/resnet34/07265_14255823118256370300",
            "./good-kernels-imagenet/resnet34/07269_1779381308580904793",
            "./good-kernels-imagenet/resnet34/07276_13077825069573843390",
            "./good-kernels-imagenet/resnet34/07320_17745232846920762718",
            "./good-kernels-imagenet/resnet34/07352_2791079409490542986"
        ],
        "resnet_34_layers": [
            "./good-kernels-imagenet/resnet34/07352_2791079409490542986",
            "./good-kernels-imagenet/resnet34/07029_3040503201941035733",
            "./nas-pte/seq_1",
            "./nas-pte/seq_2",
            "./nas-pte/seq_3"
        ]
    }
}
EOF

# Clear existing tuning results (which are shipped with the repo); you can also see what will be tuned.
python grid_tune.py --config /workspace/Syno/AE/grid_tune.a100.json --dry-run --clear
```

Then, start tuning. It is recommended to run the tuning in a tmux session, as it will take a long time.

```bash
# Recommeded: run the tuning in a tmux session
tmux new -s tuner

# To avoid the tuner starting too many threads.
export OPENBLAS_NUM_THREADS=1

# Start the tuning.
python grid_tune.py --config /workspace/Syno/AE/grid_tune.a100.json --rpc-host 127.0.0.1 --rpc-port 9190
```

Note that some of the tuning may fail due to TVM bugs. Rerun the tuning command to see if there are failed tunings. If there are, you may need to append `--overwrite` to the command to overwrite the failed tunings. Repeat the tuning command until all tunings are successful.

The quantized model requires a separate tuning command.

```bash
tmux new -s tuner
export OPENBLAS_NUM_THREADS=1
python quantize.py --target-preset "a100_gpu" --rpc --rpc-host 127.0.0.1 --rpc-port 9190 --rpc-key a100 --working-dir /workspace/Syno/AE/exp_data/vision/a100/baseline-latency
```

## Tuning with TorchInductor

Prepare. Clear all shipped tuning results. You can also see all the models that will be tuned.

```bash
python grid_torch.py --config /workspace/Syno/AE/grid_tune.a100.json --dry-run --clear
```

Then start tuning.

```bash
python grid_torch.py --config /workspace/Syno/AE/grid_tune.a100.json
```

The tuning command may also need to be rerun multiple times to ensure all tunings are successful. However, it is known that due to bugs in TorchInductor, certain models fail to tune unconditionally.

# Tuning on NVIDIA Jetson Orin Nano

Since tuning on NVIDIA Jetson Orin Nano is extremely slow (it took me 3 weeks to tune all the models), and you need to share the device with other reviewers, we simply recommend you to skip tuning on this device, or only tune a few models that you are interested in. However, for completeness, we provide the steps below.

To not waste your A100 GPU time, we recommend you to first `rsync` the whole `/workspace/Syno/AE` directory to your local machine, and run the tuner on your own machine (also in a Docker container).

The preparation steps are the same as above.

```bash
cd /workspace/Syno/experiments/performance
/workspace/Syno/AE/setup_tuning.sh
```

Also, let us call the NVIDIA Jetson Orin Nano device `jetson` for convenience. You can add it to your `~/.ssh/config` file as follows:

```
Host jetson
    HostName 101.6.96.180
    User root
    Port <your-ssh-port>
```

## Tuning with TVM

First, the preparation steps.

```bash
# Set up the RPC tracker and servers
tmux new -d -s tracker "python -m tvm.exec.rpc_tracker --host=0.0.0.0 --port=9190"
# Forward the local port 9190 to remote port (9190 + <reviewer-id>).
REVIEWER_ID=<your-reviewer-id> # 1, 2, 3, to avoid contention with other reviewers.
TRACKER_PORT=$((9190 + REVIEWER_ID))
tmux new -d -s server "ssh -R $TRACKER_PORT:127.0.0.1:9190 jetson \"python -m tvm.exec.rpc_server --tracker=127.0.0.1:$TRACKER_PORT --key=jetson-orin-nano\""

# Modify the tuning config file to exclude models other than ResNet.
echo > /workspace/Syno/AE/grid_tune.mdev.json << EOF
{
    "targets": [
        {
            "rpc_key": "jetson-orin-nano",
            "prefix": "/workspace/Syno/AE/exp_data/vision/mdev",
            "baseline_dir": "./baseline-latency",
            "target": "cuda -arch=sm_87 -max_threads_per_block=1024 -max_num_threads=1024 -thread_warp_size=32 -max_shared_memory_per_block=49152 -registers_per_block=65536",
            "target_host": "llvm -mtriple=aarch64-linux-gnu -mcpu=cortex-a78 -mattr=+neon -num-cores=6",
            "device": "cuda"
        },
        {
            "rpc_key": "jetson-orin-nano",
            "prefix": "/workspace/Syno/AE/exp_data/vision/mdev",
            "baseline_dir": "./baseline-latency",
            "target": "llvm -mtriple=aarch64-linux-gnu -mcpu=cortex-a78 -mattr=+neon -num-cores=6",
            "device": "cpu"
        }
    ],
    "kernels_dirs": {
        "resnet_18": [
            "./good-kernels-imagenet/resnet18/06705_7106109518359021661",
            "./good-kernels-imagenet/resnet18/06708_14619554982559354367",
            "./good-kernels-imagenet/resnet18/06726_11877750221072847753",
            "./good-kernels-imagenet/resnet18/06738_10756581942128284194",
            "./good-kernels-imagenet/resnet18/06747_10949904241425474452",
            "./good-kernels-imagenet/resnet18/06772_10923347917424993262",
            "./good-kernels-imagenet/resnet18/06864_6292075666050645745",
            "./good-kernels-imagenet/resnet18/06906_7346917085106034487",
            "./good-kernels-imagenet/resnet18/06937_14356514157639530665",
            "./good-kernels-imagenet/resnet18/06953_12025277355725566799",
            "./good-kernels-imagenet/resnet18/06970_4536540647343069734",
            "./good-kernels-imagenet/resnet18/07045_4438388019704064842",
            "./manual_kernels/bs1/Conv2d_Conv1d"
        ],
        "resnet_34": [
            "./good-kernels-imagenet/resnet34/07029_3040503201941035733",
            "./good-kernels-imagenet/resnet34/07089_13102253380479934281",
            "./good-kernels-imagenet/resnet34/07096_10053342605815977959",
            "./good-kernels-imagenet/resnet34/07125_3502276718624296764",
            "./good-kernels-imagenet/resnet34/07138_1877672947194075639",
            "./good-kernels-imagenet/resnet34/07140_2587021473300072582",
            "./good-kernels-imagenet/resnet34/07239_540923922250864272",
            "./good-kernels-imagenet/resnet34/07265_14255823118256370300",
            "./good-kernels-imagenet/resnet34/07269_1779381308580904793",
            "./good-kernels-imagenet/resnet34/07276_13077825069573843390",
            "./good-kernels-imagenet/resnet34/07320_17745232846920762718",
            "./good-kernels-imagenet/resnet34/07352_2791079409490542986"
        ],
        "resnet_34_layers": [
            "./good-kernels-imagenet/resnet34/07352_2791079409490542986",
            "./good-kernels-imagenet/resnet34/07029_3040503201941035733",
            "./nas-pte/seq_1",
            "./nas-pte/seq_2",
            "./nas-pte/seq_3"
        ]
    }
}
EOF

# Clear existing tuning results (which are shipped with the repo); you can also see what will be tuned.
python grid_tune.py --config /workspace/Syno/AE/grid_tune.mdev.json --dry-run --clear
```

Then, start tuning. It is recommended to run the tuning in a tmux session, as it will take a long time.

```bash
# Recommeded: run the tuning in a tmux session
tmux new -s tuner

# To avoid the tuner starting too many threads.
export OPENBLAS_NUM_THREADS=1

# Start the tuning.
python grid_tune.py --config /workspace/Syno/AE/grid_tune.mdev.json --rpc-host 127.0.0.1 --rpc-port 9190
```

Note that some of the tuning may fail due to TVM bugs. Rerun the tuning command to see if there are failed tunings. If there are, you may need to append `--overwrite` to the command to overwrite the failed tunings. Repeat the tuning command until all tunings are successful.

The quantized model requires a separate tuning command.

```bash
tmux new -s tuner
export OPENBLAS_NUM_THREADS=1
python quantize.py --target-preset "jetson_orin_nano-gpu" --rpc --rpc-host 127.0.0.1 --rpc-port 9190 --rpc-key jetson-orin-nano --working-dir /workspace/Syno/AE/exp_data/vision/mdev/baseline-latency
python quantize.py --target-preset "jetson_orin_nano-cpu" --rpc --rpc-host 127.0.0.1 --rpc-port 9190 --rpc-key jetson-orin-nano --working-dir /workspace/Syno/AE/exp_data/vision/mdev/baseline-latency
```

## Tuning with TorchInductor

Since TorchInductor tuning can only be done on the local host, you need to ssh into the NVIDIA Jetson Orin Nano device.

```bash
ssh jetson
# You also need to make sure that the reference operators are stored in `/workspace/Syno/AE/exp_data`.
cp -r /workspace/Syno/AE/data /workspace/Syno/AE/exp_data
cd /workspace/Syno/experiments/performance
/workspace/Syno/AE/setup_tuning.sh
# Modify the tuning config file to exclude models other than ResNet.
echo > /workspace/Syno/AE/grid_tune.mdev.json << EOF
{
    "targets": [
        {
            "rpc_key": "jetson-orin-nano",
            "prefix": "/workspace/Syno/AE/exp_data/vision/mdev",
            "baseline_dir": "./baseline-latency",
            "target": "cuda -arch=sm_87 -max_threads_per_block=1024 -max_num_threads=1024 -thread_warp_size=32 -max_shared_memory_per_block=49152 -registers_per_block=65536",
            "target_host": "llvm -mtriple=aarch64-linux-gnu -mcpu=cortex-a78 -mattr=+neon -num-cores=6",
            "device": "cuda"
        },
        {
            "rpc_key": "jetson-orin-nano",
            "prefix": "/workspace/Syno/AE/exp_data/vision/mdev",
            "baseline_dir": "./baseline-latency",
            "target": "llvm -mtriple=aarch64-linux-gnu -mcpu=cortex-a78 -mattr=+neon -num-cores=6",
            "device": "cpu"
        }
    ],
    "kernels_dirs": {
        "resnet_18": [
            "./good-kernels-imagenet/resnet18/06705_7106109518359021661",
            "./good-kernels-imagenet/resnet18/06708_14619554982559354367",
            "./good-kernels-imagenet/resnet18/06726_11877750221072847753",
            "./good-kernels-imagenet/resnet18/06738_10756581942128284194",
            "./good-kernels-imagenet/resnet18/06747_10949904241425474452",
            "./good-kernels-imagenet/resnet18/06772_10923347917424993262",
            "./good-kernels-imagenet/resnet18/06864_6292075666050645745",
            "./good-kernels-imagenet/resnet18/06906_7346917085106034487",
            "./good-kernels-imagenet/resnet18/06937_14356514157639530665",
            "./good-kernels-imagenet/resnet18/06953_12025277355725566799",
            "./good-kernels-imagenet/resnet18/06970_4536540647343069734",
            "./good-kernels-imagenet/resnet18/07045_4438388019704064842",
            "./manual_kernels/bs1/Conv2d_Conv1d"
        ],
        "resnet_34": [
            "./good-kernels-imagenet/resnet34/07029_3040503201941035733",
            "./good-kernels-imagenet/resnet34/07089_13102253380479934281",
            "./good-kernels-imagenet/resnet34/07096_10053342605815977959",
            "./good-kernels-imagenet/resnet34/07125_3502276718624296764",
            "./good-kernels-imagenet/resnet34/07138_1877672947194075639",
            "./good-kernels-imagenet/resnet34/07140_2587021473300072582",
            "./good-kernels-imagenet/resnet34/07239_540923922250864272",
            "./good-kernels-imagenet/resnet34/07265_14255823118256370300",
            "./good-kernels-imagenet/resnet34/07269_1779381308580904793",
            "./good-kernels-imagenet/resnet34/07276_13077825069573843390",
            "./good-kernels-imagenet/resnet34/07320_17745232846920762718",
            "./good-kernels-imagenet/resnet34/07352_2791079409490542986"
        ],
        "resnet_34_layers": [
            "./good-kernels-imagenet/resnet34/07352_2791079409490542986",
            "./good-kernels-imagenet/resnet34/07029_3040503201941035733",
            "./nas-pte/seq_1",
            "./nas-pte/seq_2",
            "./nas-pte/seq_3"
        ]
    }
}
EOF
```

Then, you can run the tuning command directly on the device.

Prepare. Clear all shipped tuning results. You can also see all the models that will be tuned.

```bash
python grid_torch.py --config /workspace/Syno/AE/grid_tune.mdev.json --dry-run --clear
```

Then start tuning.

```bash
python grid_torch.py --config /workspace/Syno/AE/grid_tune.mdev.json
```

The tuning command may also need to be rerun multiple times to ensure all tunings are successful. However, it is known that due to bugs in TorchInductor, certain models fail to tune unconditionally.

After the tuning, you need to manually copy the tuning results back to your local host. They are located in `/workspace/Syno/AE/exp_data/vision/mdev/**/inductor-*`.
