import torch
import random
"""
digraph kernel_preview {
newrank = true;

// Stage tensor.
subgraph cluster_subgraph_0 {
    label = "Subgraph 0";
    // Reductions.
    reduce_0x7fa7d4001828 [label="Sum", shape=box];
    reduce_0x7fa7d4001998 [label="Sum", shape=box];
    reduce_0x7fa7d40019b0 [label="Sum", shape=box];
    reduce_0x7fa7d4009288 [label="Sum", shape=box];
    // Output.
    subgraph cluster_subgraph_0_out {
        label = "";
        interface_0_out_0x563205df4ec0 [label="N", shape=none];
        interface_0_out_0x563205df4ee8 [label="C_out", shape=none];
        interface_0_out_0x563205df4f10 [label="H", shape=none];
        interface_0_out_0x563205df4f38 [label="H", shape=none];
    }
    {
        rank = same;
        reduce_0x7fa7d4001828;
        reduce_0x7fa7d4001998;
        reduce_0x7fa7d40019b0;
        reduce_0x7fa7d4009288;
        interface_0_out_0x563205df4ec0;
        interface_0_out_0x563205df4ee8;
        interface_0_out_0x563205df4f10;
        interface_0_out_0x563205df4f38;
    }
    // Input 0.
    subgraph cluster_subgraph_0_in_0 {
        label = "";
        interface_0_in_0x563205df4ec0 [label="N", shape=none];
        interface_0_in_0x56320589f6c0 [label="g", shape=none];
        interface_0_in_0x563205df4f10 [label="H", shape=none];
        interface_0_in_0x7faf04004910 [label="k_1", shape=none];
        interface_0_in_0x563205df4f38 [label="H", shape=none];
        interface_0_in_0x7faf04005540 [label="k_1", shape=none];
        interface_0_in_0x7faf04004a50 [label="g^-1*s^-1*C_out", shape=none];
    }
    // Input 1.
    subgraph cluster_subgraph_0_in_1 {
        label = "";
        interface_0_in_0x56320589f6d8 [label="g", shape=none];
        interface_0_in_0x7faf04004928 [label="k_1", shape=none];
        interface_0_in_0x7faf04005558 [label="k_1", shape=none];
        interface_0_in_0x56320593e738 [label="C_out", shape=none];
        interface_0_in_0x7faf04004a68 [label="g^-1*s^-1*C_out", shape=none];
    }
    {
        rank = same;
        interface_0_in_0x563205df4ec0;
        interface_0_in_0x56320589f6c0;
        interface_0_in_0x563205df4f10;
        interface_0_in_0x7faf04004910;
        interface_0_in_0x563205df4f38;
        interface_0_in_0x7faf04005540;
        interface_0_in_0x7faf04004a50;
        interface_0_in_0x56320589f6d8;
        interface_0_in_0x7faf04004928;
        interface_0_in_0x7faf04005558;
        interface_0_in_0x56320593e738;
        interface_0_in_0x7faf04004a68;
    }
    // Op's.
    op_0x56320589f6a0 [label="Share"];
    op_0x56320593e700 [label="Share"];
    op_0x563205bb3d58 [label="Expand"];
    op_0x7faf040048f0 [label="Share"];
    op_0x7faf04004a30 [label="Share"];
    op_0x7faf04005520 [label="Share"];
    // Dimension's.
    interface_0_in_0x56320589f6c0 -> op_0x56320589f6a0 [label="g"];
    interface_0_in_0x56320589f6d8 -> op_0x56320589f6a0 [label="g"];
    op_0x563205bb3d58 -> op_0x56320593e700 [label="C_out"];
    interface_0_in_0x56320593e738 -> op_0x56320593e700 [label="C_out"];
    interface_0_in_0x563205df4ec0 -> interface_0_out_0x563205df4ec0 [label="N"];
    op_0x56320593e700 -> interface_0_out_0x563205df4ee8 [label="C_out"];
    interface_0_in_0x563205df4f10 -> interface_0_out_0x563205df4f10 [label="H"];
    interface_0_in_0x563205df4f38 -> interface_0_out_0x563205df4f38 [label="H"];
    op_0x56320589f6a0 -> reduce_0x7fa7d4001828 [label="g"];
    op_0x7faf040048f0 -> reduce_0x7fa7d4001998 [label="k_1"];
    op_0x7faf04005520 -> reduce_0x7fa7d40019b0 [label="k_1"];
    op_0x7faf04004a30 -> reduce_0x7fa7d4009288 [label="g^-1*s^-1*C_out"];
    interface_0_in_0x7faf04004910 -> op_0x7faf040048f0 [label="k_1"];
    interface_0_in_0x7faf04004928 -> op_0x7faf040048f0 [label="k_1"];
    interface_0_in_0x7faf04004a50 -> op_0x7faf04004a30 [label="g^-1*s^-1*C_out"];
    interface_0_in_0x7faf04004a68 -> op_0x7faf04004a30 [label="g^-1*s^-1*C_out"];
    interface_0_in_0x7faf04005540 -> op_0x7faf04005520 [label="k_1"];
    interface_0_in_0x7faf04005558 -> op_0x7faf04005520 [label="k_1"];
}

// Stage tensor.
subgraph cluster_subgraph_1 {
    label = "Subgraph 1";
    // Reductions.
    // Output.
    subgraph cluster_subgraph_1_out {
        label = "";
        interface_1_out_0x563205df4ec0 [label="N", shape=none];
        interface_1_out_0x56320589f6c0 [label="g", shape=none];
        interface_1_out_0x563205df4f10 [label="H", shape=none];
        interface_1_out_0x7faf04004910 [label="k_1", shape=none];
        interface_1_out_0x563205df4f38 [label="H", shape=none];
        interface_1_out_0x7faf04005540 [label="k_1", shape=none];
        interface_1_out_0x7faf04004a50 [label="g^-1*s^-1*C_out", shape=none];
    }
    {
        rank = same;
        interface_1_out_0x563205df4ec0;
        interface_1_out_0x56320589f6c0;
        interface_1_out_0x563205df4f10;
        interface_1_out_0x7faf04004910;
        interface_1_out_0x563205df4f38;
        interface_1_out_0x7faf04005540;
        interface_1_out_0x7faf04004a50;
    }
    // Input 0.
    subgraph cluster_subgraph_1_in_0 {
        label = "";
        interface_1_in_0x563205df4ec0 [label="N", shape=none];
        interface_1_in_0x56320589f6c0 [label="g", shape=none];
        interface_1_in_0x563205887ca8 [label="H", shape=none];
        interface_1_in_0x563205df4f38 [label="H", shape=none];
        interface_1_in_0x7faf04005540 [label="k_1", shape=none];
        interface_1_in_0x7faf04004a50 [label="g^-1*s^-1*C_out", shape=none];
    }
    {
        rank = same;
        interface_1_in_0x563205df4ec0;
        interface_1_in_0x56320589f6c0;
        interface_1_in_0x563205887ca8;
        interface_1_in_0x563205df4f38;
        interface_1_in_0x7faf04005540;
        interface_1_in_0x7faf04004a50;
    }
    // Op's.
    op_0x563205887c80 [label="Unfold"];
    // Dimension's.
    interface_1_in_0x563205887ca8 -> op_0x563205887c80 [label="H"];
    interface_1_in_0x56320589f6c0 -> interface_1_out_0x56320589f6c0 [label="g"];
    interface_1_in_0x563205df4ec0 -> interface_1_out_0x563205df4ec0 [label="N"];
    op_0x563205887c80 -> interface_1_out_0x563205df4f10 [label="H"];
    interface_1_in_0x563205df4f38 -> interface_1_out_0x563205df4f38 [label="H"];
    op_0x563205887c80 -> interface_1_out_0x7faf04004910 [label="k_1"];
    interface_1_in_0x7faf04004a50 -> interface_1_out_0x7faf04004a50 [label="g^-1*s^-1*C_out"];
    interface_1_in_0x7faf04005540 -> interface_1_out_0x7faf04005540 [label="k_1"];
}

// Stage tensor.
subgraph cluster_subgraph_2 {
    label = "Subgraph 2";
    // Reductions.
    reduce_0x7fa7d4005b90 [label="Sum", shape=box];
    // Output.
    subgraph cluster_subgraph_2_out {
        label = "";
        interface_2_out_0x563205df4ec0 [label="N", shape=none];
        interface_2_out_0x56320589f6c0 [label="g", shape=none];
        interface_2_out_0x563205887ca8 [label="H", shape=none];
        interface_2_out_0x563205df4f38 [label="H", shape=none];
        interface_2_out_0x7faf04005540 [label="k_1", shape=none];
        interface_2_out_0x7faf04004a50 [label="g^-1*s^-1*C_out", shape=none];
    }
    {
        rank = same;
        reduce_0x7fa7d4005b90;
        interface_2_out_0x563205df4ec0;
        interface_2_out_0x56320589f6c0;
        interface_2_out_0x563205887ca8;
        interface_2_out_0x563205df4f38;
        interface_2_out_0x7faf04005540;
        interface_2_out_0x7faf04004a50;
    }
    // Input 0.
    subgraph cluster_subgraph_2_in_0 {
        label = "";
        interface_2_in_0x563205df4ec0 [label="N", shape=none];
        interface_2_in_0x563205bb9370 [label="C_in", shape=none];
        interface_2_in_0x563205887ca8 [label="H", shape=none];
        interface_2_in_0x563205df4f38 [label="H", shape=none];
        interface_2_in_0x7faf04005540 [label="k_1", shape=none];
        interface_2_in_0x7faf04004a50 [label="g^-1*s^-1*C_out", shape=none];
    }
    {
        rank = same;
        interface_2_in_0x563205df4ec0;
        interface_2_in_0x563205bb9370;
        interface_2_in_0x563205887ca8;
        interface_2_in_0x563205df4f38;
        interface_2_in_0x7faf04005540;
        interface_2_in_0x7faf04004a50;
    }
    // Op's.
    op_0x563205bb9330 [label="Split"];
    // Dimension's.
    interface_2_in_0x563205887ca8 -> interface_2_out_0x563205887ca8 [label="H"];
    op_0x563205bb9330 -> interface_2_out_0x56320589f6c0 [label="g"];
    interface_2_in_0x563205bb9370 -> op_0x563205bb9330 [label="C_in"];
    interface_2_in_0x563205df4ec0 -> interface_2_out_0x563205df4ec0 [label="N"];
    interface_2_in_0x563205df4f38 -> interface_2_out_0x563205df4f38 [label="H"];
    op_0x563205bb9330 -> reduce_0x7fa7d4005b90 [label="g^-1*C_in"];
    interface_2_in_0x7faf04004a50 -> interface_2_out_0x7faf04004a50 [label="g^-1*s^-1*C_out"];
    interface_2_in_0x7faf04005540 -> interface_2_out_0x7faf04005540 [label="k_1"];
}

// Stage tensor.
subgraph cluster_subgraph_3 {
    label = "Subgraph 3";
    // Reductions.
    // Output.
    subgraph cluster_subgraph_3_out {
        label = "";
        interface_3_out_0x563205df4ec0 [label="N", shape=none];
        interface_3_out_0x563205bb9370 [label="C_in", shape=none];
        interface_3_out_0x563205887ca8 [label="H", shape=none];
        interface_3_out_0x563205df4f38 [label="H", shape=none];
        interface_3_out_0x7faf04005540 [label="k_1", shape=none];
        interface_3_out_0x7faf04004a50 [label="g^-1*s^-1*C_out", shape=none];
    }
    {
        rank = same;
        interface_3_out_0x563205df4ec0;
        interface_3_out_0x563205bb9370;
        interface_3_out_0x563205887ca8;
        interface_3_out_0x563205df4f38;
        interface_3_out_0x7faf04005540;
        interface_3_out_0x7faf04004a50;
    }
    // Input 0.
    subgraph cluster_subgraph_3_in_0 {
        label = "";
        interface_3_in_0x563205df4ec0 [label="N", shape=none];
        interface_3_in_0x563205db3460 [label="C_in", shape=none];
        interface_3_in_0x563205887ca8 [label="H", shape=none];
        interface_3_in_0x563205df4f38 [label="H", shape=none];
        interface_3_in_0x563205db3a00 [label="k_1", shape=none];
    }
    // Input 1.
    subgraph cluster_subgraph_3_in_1 {
        label = "";
        interface_3_in_0x563205db3478 [label="C_in", shape=none];
        interface_3_in_0x563205db3a18 [label="k_1", shape=none];
        interface_3_in_0x563205db3338 [label="g^-1*s^-1*C_out", shape=none];
    }
    {
        rank = same;
        interface_3_in_0x563205df4ec0;
        interface_3_in_0x563205db3460;
        interface_3_in_0x563205887ca8;
        interface_3_in_0x563205df4f38;
        interface_3_in_0x563205db3a00;
        interface_3_in_0x563205db3478;
        interface_3_in_0x563205db3a18;
        interface_3_in_0x563205db3338;
    }
    // Op's.
    op_0x563205bb4118 [label="Expand"];
    op_0x563205db3300 [label="Share"];
    op_0x563205db3440 [label="Share"];
    op_0x563205db39e0 [label="Share"];
    // Dimension's.
    interface_3_in_0x563205887ca8 -> interface_3_out_0x563205887ca8 [label="H"];
    op_0x563205db3440 -> interface_3_out_0x563205bb9370 [label="C_in"];
    op_0x563205bb4118 -> op_0x563205db3300 [label="g^-1*s^-1*C_out"];
    interface_3_in_0x563205db3338 -> op_0x563205db3300 [label="g^-1*s^-1*C_out"];
    interface_3_in_0x563205db3460 -> op_0x563205db3440 [label="C_in"];
    interface_3_in_0x563205db3478 -> op_0x563205db3440 [label="C_in"];
    interface_3_in_0x563205db3a00 -> op_0x563205db39e0 [label="k_1"];
    interface_3_in_0x563205db3a18 -> op_0x563205db39e0 [label="k_1"];
    interface_3_in_0x563205df4ec0 -> interface_3_out_0x563205df4ec0 [label="N"];
    interface_3_in_0x563205df4f38 -> interface_3_out_0x563205df4f38 [label="H"];
    op_0x563205db3300 -> interface_3_out_0x7faf04004a50 [label="g^-1*s^-1*C_out"];
    op_0x563205db39e0 -> interface_3_out_0x7faf04005540 [label="k_1"];
}

// Stage tensor.
subgraph cluster_subgraph_4 {
    label = "Subgraph 4";
    // Reductions.
    // Output.
    subgraph cluster_subgraph_4_out {
        label = "";
        interface_4_out_0x563205df4ec0 [label="N", shape=none];
        interface_4_out_0x563205db3460 [label="C_in", shape=none];
        interface_4_out_0x563205887ca8 [label="H", shape=none];
        interface_4_out_0x563205df4f38 [label="H", shape=none];
        interface_4_out_0x563205db3a00 [label="k_1", shape=none];
    }
    {
        rank = same;
        interface_4_out_0x563205df4ec0;
        interface_4_out_0x563205db3460;
        interface_4_out_0x563205887ca8;
        interface_4_out_0x563205df4f38;
        interface_4_out_0x563205db3a00;
    }
    // Input 0.
    subgraph cluster_subgraph_4_in_0 {
        label = "";
        interface_4_in_0x563205df4ec0 [label="N", shape=none];
        interface_4_in_0x563205db3460 [label="C_in", shape=none];
        interface_4_in_0x563205887ca8 [label="H", shape=none];
        interface_4_in_0x7fa5fc00efa8 [label="H", shape=none];
    }
    {
        rank = same;
        interface_4_in_0x563205df4ec0;
        interface_4_in_0x563205db3460;
        interface_4_in_0x563205887ca8;
        interface_4_in_0x7fa5fc00efa8;
    }
    // Op's.
    op_0x7fa5fc00ef80 [label="Unfold"];
    // Dimension's.
    interface_4_in_0x563205887ca8 -> interface_4_out_0x563205887ca8 [label="H"];
    interface_4_in_0x563205db3460 -> interface_4_out_0x563205db3460 [label="C_in"];
    op_0x7fa5fc00ef80 -> interface_4_out_0x563205db3a00 [label="k_1"];
    interface_4_in_0x563205df4ec0 -> interface_4_out_0x563205df4ec0 [label="N"];
    op_0x7fa5fc00ef80 -> interface_4_out_0x563205df4f38 [label="H"];
    interface_4_in_0x7fa5fc00efa8 -> op_0x7fa5fc00ef80 [label="H"];
}

// Input tensor.
subgraph cluster_subgraph_5 {
    label = "Input 0";
    interface_5_out_0x563205df4ec0 [label="N", shape=none];
    interface_5_out_0x563205db3460 [label="C_in", shape=none];
    interface_5_out_0x563205887ca8 [label="H", shape=none];
    interface_5_out_0x7fa5fc00efa8 [label="H", shape=none];
}

interface_5_out_0x563205df4ec0 -> interface_4_in_0x563205df4ec0;
interface_5_out_0x563205db3460 -> interface_4_in_0x563205db3460;
interface_5_out_0x563205887ca8 -> interface_4_in_0x563205887ca8;
interface_5_out_0x7fa5fc00efa8 -> interface_4_in_0x7fa5fc00efa8;

interface_4_out_0x563205df4ec0 -> interface_3_in_0x563205df4ec0;
interface_4_out_0x563205db3460 -> interface_3_in_0x563205db3460;
interface_4_out_0x563205887ca8 -> interface_3_in_0x563205887ca8;
interface_4_out_0x563205df4f38 -> interface_3_in_0x563205df4f38;
interface_4_out_0x563205db3a00 -> interface_3_in_0x563205db3a00;

// Input tensor.
subgraph cluster_subgraph_6 {
    label = "Input 2";
    interface_6_out_0x563205db3478 [label="C_in", shape=none];
    interface_6_out_0x563205db3a18 [label="k_1", shape=none];
    interface_6_out_0x563205db3338 [label="g^-1*s^-1*C_out", shape=none];
}

interface_6_out_0x563205db3478 -> interface_3_in_0x563205db3478;
interface_6_out_0x563205db3a18 -> interface_3_in_0x563205db3a18;
interface_6_out_0x563205db3338 -> interface_3_in_0x563205db3338;

interface_3_out_0x563205df4ec0 -> interface_2_in_0x563205df4ec0;
interface_3_out_0x563205bb9370 -> interface_2_in_0x563205bb9370;
interface_3_out_0x563205887ca8 -> interface_2_in_0x563205887ca8;
interface_3_out_0x563205df4f38 -> interface_2_in_0x563205df4f38;
interface_3_out_0x7faf04005540 -> interface_2_in_0x7faf04005540;
interface_3_out_0x7faf04004a50 -> interface_2_in_0x7faf04004a50;

interface_2_out_0x563205df4ec0 -> interface_1_in_0x563205df4ec0;
interface_2_out_0x56320589f6c0 -> interface_1_in_0x56320589f6c0;
interface_2_out_0x563205887ca8 -> interface_1_in_0x563205887ca8;
interface_2_out_0x563205df4f38 -> interface_1_in_0x563205df4f38;
interface_2_out_0x7faf04005540 -> interface_1_in_0x7faf04005540;
interface_2_out_0x7faf04004a50 -> interface_1_in_0x7faf04004a50;

interface_1_out_0x563205df4ec0 -> interface_0_in_0x563205df4ec0;
interface_1_out_0x56320589f6c0 -> interface_0_in_0x56320589f6c0;
interface_1_out_0x563205df4f10 -> interface_0_in_0x563205df4f10;
interface_1_out_0x7faf04004910 -> interface_0_in_0x7faf04004910;
interface_1_out_0x563205df4f38 -> interface_0_in_0x563205df4f38;
interface_1_out_0x7faf04005540 -> interface_0_in_0x7faf04005540;
interface_1_out_0x7faf04004a50 -> interface_0_in_0x7faf04004a50;

// Input tensor.
subgraph cluster_subgraph_7 {
    label = "Input 1";
    interface_7_out_0x56320589f6d8 [label="g", shape=none];
    interface_7_out_0x7faf04004928 [label="k_1", shape=none];
    interface_7_out_0x7faf04005558 [label="k_1", shape=none];
    interface_7_out_0x56320593e738 [label="C_out", shape=none];
    interface_7_out_0x7faf04004a68 [label="g^-1*s^-1*C_out", shape=none];
}

interface_7_out_0x56320589f6d8 -> interface_0_in_0x56320589f6d8;
interface_7_out_0x7faf04004928 -> interface_0_in_0x7faf04004928;
interface_7_out_0x7faf04005558 -> interface_0_in_0x7faf04005558;
interface_7_out_0x56320593e738 -> interface_0_in_0x56320593e738;
interface_7_out_0x7faf04004a68 -> interface_0_in_0x7faf04004a68;

{
    rank = same;
    interface_5_out_0x563205df4ec0;
    interface_5_out_0x563205db3460;
    interface_5_out_0x563205887ca8;
    interface_5_out_0x7fa5fc00efa8;
    interface_7_out_0x56320589f6d8;
    interface_7_out_0x7faf04004928;
    interface_7_out_0x7faf04005558;
    interface_7_out_0x56320593e738;
    interface_7_out_0x7faf04004a68;
    interface_6_out_0x563205db3478;
    interface_6_out_0x563205db3a18;
    interface_6_out_0x563205db3338;
}
subgraph cluster_subgraph_output {
    label = "Output";
    interface_8_in_0x563205df4ec0 [label="N", shape=none];
    interface_8_in_0x563205df4ee8 [label="C_out", shape=none];
    interface_8_in_0x563205df4f10 [label="H", shape=none];
    interface_8_in_0x563205df4f38 [label="H", shape=none];
}
interface_0_out_0x563205df4ec0 -> interface_8_in_0x563205df4ec0;
interface_0_out_0x563205df4ee8 -> interface_8_in_0x563205df4ee8;
interface_0_out_0x563205df4f10 -> interface_8_in_0x563205df4f10;
interface_0_out_0x563205df4f38 -> interface_8_in_0x563205df4f38;

}

"""
class kernel_generated_0(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([32, 3, 3, 64, 1]),
			torch.randn([64, 3, 1]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]
		in_2 = self.weights[1]

		# No contraction needed.
		t_3 = in_0

		# [H]@Unfold90ae9d8acef524e0 -> [H]@Iteratorb0a1def4ad5784ec, [k_1]@Share63a88e0da5dce9dc
		t_3 = torch.reshape(t_3, (128, 3584, 56, 1, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (128, 64, 56, 3, 56, ))

		# Permute to match the output of this subgraph.
		t_3 = torch.permute(t_3, (0, 1, 2, 4, 3, ))

		# Perform contraction.
		t_4 = torch.einsum("mjlnk, jki -> mjlnki", t_3, in_2)

		# No contraction needed.
		t_5 = t_4

		# [C_in]@Splitc2d52f3525ba6cc4 -> [g]@Sharec7a8ce455b828537, [g^-1*C_in]@Reduceef9903cafc29eea1
		t_5 = torch.reshape(t_5, (128, 32, 2, 56, 56, 3, 1, ))

		# [g^-1*C_in]@Reduce
		t_5 = torch.sum(t_5, dim=(2, ))

		# No contraction needed.
		t_6 = t_5

		# [H]@Unfold4d77c1e3da5bca44 -> [H]@Iterator96123ba3184da39c, [k_1]@Share26cfa48d169008e4
		t_6 = torch.reshape(t_6, (128, 32, 56, 168, ))
		t_6 = torch.nn.functional.unfold(t_6, (3, 1, ), padding=(1, 0, ))
		t_6 = torch.reshape(t_6, (128, 32, 3, 56, 56, 3, 1, ))

		# Permute to match the output of this subgraph.
		t_6 = torch.permute(t_6, (0, 1, 3, 2, 4, 5, 6, ))

		# Perform contraction.
		t_7 = torch.einsum("niokpml, ikmjl -> nopj", t_6, in_1)

		# Permute to match the output of this subgraph.
		t_7 = torch.permute(t_7, (0, 3, 1, 2, ))

		# No need to crop the output tensor.
		y = t_7

		return y

class kernel_generated_1(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([32, 3, 3, 128, 2]),
			torch.randn([64, 3, 2]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]
		in_2 = self.weights[1]

		# No contraction needed.
		t_3 = in_0

		# [H]@Unfold90ae9d8acef524e0 -> [H]@Iteratorb0a1def4ad5784ec, [k_1]@Share63a88e0da5dce9dc
		t_3 = torch.reshape(t_3, (128, 1792, 28, 1, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (128, 64, 28, 3, 28, ))

		# Permute to match the output of this subgraph.
		t_3 = torch.permute(t_3, (0, 1, 2, 4, 3, ))

		# Perform contraction.
		t_4 = torch.einsum("mjlnk, jki -> mjlnki", t_3, in_2)

		# No contraction needed.
		t_5 = t_4

		# [C_in]@Splitc2d52f3525ba6cc4 -> [g]@Sharec7a8ce455b828537, [g^-1*C_in]@Reduceef9903cafc29eea1
		t_5 = torch.reshape(t_5, (128, 32, 2, 28, 28, 3, 2, ))

		# [g^-1*C_in]@Reduce
		t_5 = torch.sum(t_5, dim=(2, ))

		# No contraction needed.
		t_6 = t_5

		# [H]@Unfold4d77c1e3da5bca44 -> [H]@Iterator96123ba3184da39c, [k_1]@Share26cfa48d169008e4
		t_6 = torch.reshape(t_6, (128, 32, 28, 168, ))
		t_6 = torch.nn.functional.unfold(t_6, (3, 1, ), padding=(1, 0, ))
		t_6 = torch.reshape(t_6, (128, 32, 3, 28, 28, 3, 2, ))

		# Permute to match the output of this subgraph.
		t_6 = torch.permute(t_6, (0, 1, 3, 2, 4, 5, 6, ))

		# Perform contraction.
		t_7 = torch.einsum("niokpml, ikmjl -> nopj", t_6, in_1)

		# Permute to match the output of this subgraph.
		t_7 = torch.permute(t_7, (0, 3, 1, 2, ))

		# No need to crop the output tensor.
		y = t_7

		return y

class kernel_generated_2(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([32, 3, 3, 128, 2]),
			torch.randn([128, 3, 2]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]
		in_2 = self.weights[1]

		# No contraction needed.
		t_3 = in_0

		# [H]@Unfold90ae9d8acef524e0 -> [H]@Iteratorb0a1def4ad5784ec, [k_1]@Share63a88e0da5dce9dc
		t_3 = torch.reshape(t_3, (128, 3584, 28, 1, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (128, 128, 28, 3, 28, ))

		# Permute to match the output of this subgraph.
		t_3 = torch.permute(t_3, (0, 1, 2, 4, 3, ))

		# Perform contraction.
		t_4 = torch.einsum("mjlnk, jki -> mjlnki", t_3, in_2)

		# No contraction needed.
		t_5 = t_4

		# [C_in]@Splitc2d52f3525ba6cc4 -> [g]@Sharec7a8ce455b828537, [g^-1*C_in]@Reduceef9903cafc29eea1
		t_5 = torch.reshape(t_5, (128, 32, 4, 28, 28, 3, 2, ))

		# [g^-1*C_in]@Reduce
		t_5 = torch.sum(t_5, dim=(2, ))

		# No contraction needed.
		t_6 = t_5

		# [H]@Unfold4d77c1e3da5bca44 -> [H]@Iterator96123ba3184da39c, [k_1]@Share26cfa48d169008e4
		t_6 = torch.reshape(t_6, (128, 32, 28, 168, ))
		t_6 = torch.nn.functional.unfold(t_6, (3, 1, ), padding=(1, 0, ))
		t_6 = torch.reshape(t_6, (128, 32, 3, 28, 28, 3, 2, ))

		# Permute to match the output of this subgraph.
		t_6 = torch.permute(t_6, (0, 1, 3, 2, 4, 5, 6, ))

		# Perform contraction.
		t_7 = torch.einsum("niokpml, ikmjl -> nopj", t_6, in_1)

		# Permute to match the output of this subgraph.
		t_7 = torch.permute(t_7, (0, 3, 1, 2, ))

		# No need to crop the output tensor.
		y = t_7

		return y

class kernel_generated_3(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([32, 3, 3, 256, 4]),
			torch.randn([128, 3, 4]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]
		in_2 = self.weights[1]

		# No contraction needed.
		t_3 = in_0

		# [H]@Unfold90ae9d8acef524e0 -> [H]@Iteratorb0a1def4ad5784ec, [k_1]@Share63a88e0da5dce9dc
		t_3 = torch.reshape(t_3, (128, 1792, 14, 1, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (128, 128, 14, 3, 14, ))

		# Permute to match the output of this subgraph.
		t_3 = torch.permute(t_3, (0, 1, 2, 4, 3, ))

		# Perform contraction.
		t_4 = torch.einsum("mjlnk, jki -> mjlnki", t_3, in_2)

		# No contraction needed.
		t_5 = t_4

		# [C_in]@Splitc2d52f3525ba6cc4 -> [g]@Sharec7a8ce455b828537, [g^-1*C_in]@Reduceef9903cafc29eea1
		t_5 = torch.reshape(t_5, (128, 32, 4, 14, 14, 3, 4, ))

		# [g^-1*C_in]@Reduce
		t_5 = torch.sum(t_5, dim=(2, ))

		# No contraction needed.
		t_6 = t_5

		# [H]@Unfold4d77c1e3da5bca44 -> [H]@Iterator96123ba3184da39c, [k_1]@Share26cfa48d169008e4
		t_6 = torch.reshape(t_6, (128, 32, 14, 168, ))
		t_6 = torch.nn.functional.unfold(t_6, (3, 1, ), padding=(1, 0, ))
		t_6 = torch.reshape(t_6, (128, 32, 3, 14, 14, 3, 4, ))

		# Permute to match the output of this subgraph.
		t_6 = torch.permute(t_6, (0, 1, 3, 2, 4, 5, 6, ))

		# Perform contraction.
		t_7 = torch.einsum("niokpml, ikmjl -> nopj", t_6, in_1)

		# Permute to match the output of this subgraph.
		t_7 = torch.permute(t_7, (0, 3, 1, 2, ))

		# No need to crop the output tensor.
		y = t_7

		return y

class kernel_generated_4(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([32, 3, 3, 256, 4]),
			torch.randn([256, 3, 4]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]
		in_2 = self.weights[1]

		# No contraction needed.
		t_3 = in_0

		# [H]@Unfold90ae9d8acef524e0 -> [H]@Iteratorb0a1def4ad5784ec, [k_1]@Share63a88e0da5dce9dc
		t_3 = torch.reshape(t_3, (128, 3584, 14, 1, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (128, 256, 14, 3, 14, ))

		# Permute to match the output of this subgraph.
		t_3 = torch.permute(t_3, (0, 1, 2, 4, 3, ))

		# Perform contraction.
		t_4 = torch.einsum("mjlnk, jki -> mjlnki", t_3, in_2)

		# No contraction needed.
		t_5 = t_4

		# [C_in]@Splitc2d52f3525ba6cc4 -> [g]@Sharec7a8ce455b828537, [g^-1*C_in]@Reduceef9903cafc29eea1
		t_5 = torch.reshape(t_5, (128, 32, 8, 14, 14, 3, 4, ))

		# [g^-1*C_in]@Reduce
		t_5 = torch.sum(t_5, dim=(2, ))

		# No contraction needed.
		t_6 = t_5

		# [H]@Unfold4d77c1e3da5bca44 -> [H]@Iterator96123ba3184da39c, [k_1]@Share26cfa48d169008e4
		t_6 = torch.reshape(t_6, (128, 32, 14, 168, ))
		t_6 = torch.nn.functional.unfold(t_6, (3, 1, ), padding=(1, 0, ))
		t_6 = torch.reshape(t_6, (128, 32, 3, 14, 14, 3, 4, ))

		# Permute to match the output of this subgraph.
		t_6 = torch.permute(t_6, (0, 1, 3, 2, 4, 5, 6, ))

		# Perform contraction.
		t_7 = torch.einsum("niokpml, ikmjl -> nopj", t_6, in_1)

		# Permute to match the output of this subgraph.
		t_7 = torch.permute(t_7, (0, 3, 1, 2, ))

		# No need to crop the output tensor.
		y = t_7

		return y

class kernel_generated_5(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([32, 3, 3, 512, 8]),
			torch.randn([256, 3, 8]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]
		in_2 = self.weights[1]

		# No contraction needed.
		t_3 = in_0

		# [H]@Unfold90ae9d8acef524e0 -> [H]@Iteratorb0a1def4ad5784ec, [k_1]@Share63a88e0da5dce9dc
		t_3 = torch.reshape(t_3, (128, 1792, 7, 1, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (128, 256, 7, 3, 7, ))

		# Permute to match the output of this subgraph.
		t_3 = torch.permute(t_3, (0, 1, 2, 4, 3, ))

		# Perform contraction.
		t_4 = torch.einsum("mjlnk, jki -> mjlnki", t_3, in_2)

		# No contraction needed.
		t_5 = t_4

		# [C_in]@Splitc2d52f3525ba6cc4 -> [g]@Sharec7a8ce455b828537, [g^-1*C_in]@Reduceef9903cafc29eea1
		t_5 = torch.reshape(t_5, (128, 32, 8, 7, 7, 3, 8, ))

		# [g^-1*C_in]@Reduce
		t_5 = torch.sum(t_5, dim=(2, ))

		# No contraction needed.
		t_6 = t_5

		# [H]@Unfold4d77c1e3da5bca44 -> [H]@Iterator96123ba3184da39c, [k_1]@Share26cfa48d169008e4
		t_6 = torch.reshape(t_6, (128, 32, 7, 168, ))
		t_6 = torch.nn.functional.unfold(t_6, (3, 1, ), padding=(1, 0, ))
		t_6 = torch.reshape(t_6, (128, 32, 3, 7, 7, 3, 8, ))

		# Permute to match the output of this subgraph.
		t_6 = torch.permute(t_6, (0, 1, 3, 2, 4, 5, 6, ))

		# Perform contraction.
		t_7 = torch.einsum("niokpml, ikmjl -> nopj", t_6, in_1)

		# Permute to match the output of this subgraph.
		t_7 = torch.permute(t_7, (0, 3, 1, 2, ))

		# No need to crop the output tensor.
		y = t_7

		return y

class kernel_generated_6(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([32, 3, 3, 512, 8]),
			torch.randn([512, 3, 8]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]
		in_2 = self.weights[1]

		# No contraction needed.
		t_3 = in_0

		# [H]@Unfold90ae9d8acef524e0 -> [H]@Iteratorb0a1def4ad5784ec, [k_1]@Share63a88e0da5dce9dc
		t_3 = torch.reshape(t_3, (128, 3584, 7, 1, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (128, 512, 7, 3, 7, ))

		# Permute to match the output of this subgraph.
		t_3 = torch.permute(t_3, (0, 1, 2, 4, 3, ))

		# Perform contraction.
		t_4 = torch.einsum("mjlnk, jki -> mjlnki", t_3, in_2)

		# No contraction needed.
		t_5 = t_4

		# [C_in]@Splitc2d52f3525ba6cc4 -> [g]@Sharec7a8ce455b828537, [g^-1*C_in]@Reduceef9903cafc29eea1
		t_5 = torch.reshape(t_5, (128, 32, 16, 7, 7, 3, 8, ))

		# [g^-1*C_in]@Reduce
		t_5 = torch.sum(t_5, dim=(2, ))

		# No contraction needed.
		t_6 = t_5

		# [H]@Unfold4d77c1e3da5bca44 -> [H]@Iterator96123ba3184da39c, [k_1]@Share26cfa48d169008e4
		t_6 = torch.reshape(t_6, (128, 32, 7, 168, ))
		t_6 = torch.nn.functional.unfold(t_6, (3, 1, ), padding=(1, 0, ))
		t_6 = torch.reshape(t_6, (128, 32, 3, 7, 7, 3, 8, ))

		# Permute to match the output of this subgraph.
		t_6 = torch.permute(t_6, (0, 1, 3, 2, 4, 5, 6, ))

		# Perform contraction.
		t_7 = torch.einsum("niokpml, ikmjl -> nopj", t_6, in_1)

		# Permute to match the output of this subgraph.
		t_7 = torch.permute(t_7, (0, 3, 1, 2, ))

		# No need to crop the output tensor.
		y = t_7

		return y

