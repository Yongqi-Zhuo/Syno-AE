import torch
import random
"""
digraph kernel_preview {
newrank = true;

// Stage tensor.
subgraph cluster_subgraph_0 {
    label = "Subgraph 0";
    // Reductions.
    reduce_0x563e4b853f98 [label="Sum", shape=box];
    reduce_0x563e4b853ee0 [label="Sum", shape=box];
    reduce_0x563e4b853ef8 [label="Sum", shape=box];
    reduce_0x563e4b854050 [label="Sum", shape=box];
    // Output.
    subgraph cluster_subgraph_0_out {
        label = "";
        interface_0_out_0x563e48b9d610 [label="N", shape=none];
        interface_0_out_0x563e4b856690 [label="C_out", shape=none];
        interface_0_out_0x563e4b7d4f10 [label="H", shape=none];
        interface_0_out_0x563e4b7c4510 [label="H", shape=none];
    }
    {
        rank = same;
        reduce_0x563e4b853f98;
        reduce_0x563e4b853ee0;
        reduce_0x563e4b853ef8;
        reduce_0x563e4b854050;
        interface_0_out_0x563e48b9d610;
        interface_0_out_0x563e4b856690;
        interface_0_out_0x563e4b7d4f10;
        interface_0_out_0x563e4b7c4510;
    }
    // Input 0.
    subgraph cluster_subgraph_0_in_0 {
        label = "";
        interface_0_in_0x563e48b9d610 [label="N", shape=none];
        interface_0_in_0x563e48a36f90 [label="g", shape=none];
        interface_0_in_0x563e48a36ef0 [label="k_1", shape=none];
        interface_0_in_0x563e4b7d4f10 [label="H", shape=none];
        interface_0_in_0x563e48a36f40 [label="k_1", shape=none];
        interface_0_in_0x563e4b7c4510 [label="H", shape=none];
        interface_0_in_0x563e48a36fe0 [label="g^-1*s^-1*C_out", shape=none];
    }
    // Input 1.
    subgraph cluster_subgraph_0_in_1 {
        label = "";
        interface_0_in_0x563e48a36eb8 [label="C_out", shape=none];
        interface_0_in_0x563e48a36fa8 [label="g", shape=none];
        interface_0_in_0x563e48a36f08 [label="k_1", shape=none];
        interface_0_in_0x563e48a36f58 [label="k_1", shape=none];
        interface_0_in_0x563e48a36ff8 [label="g^-1*s^-1*C_out", shape=none];
    }
    {
        rank = same;
        interface_0_in_0x563e48b9d610;
        interface_0_in_0x563e48a36f90;
        interface_0_in_0x563e48a36ef0;
        interface_0_in_0x563e4b7d4f10;
        interface_0_in_0x563e48a36f40;
        interface_0_in_0x563e4b7c4510;
        interface_0_in_0x563e48a36fe0;
        interface_0_in_0x563e48a36eb8;
        interface_0_in_0x563e48a36fa8;
        interface_0_in_0x563e48a36f08;
        interface_0_in_0x563e48a36f58;
        interface_0_in_0x563e48a36ff8;
    }
    // Op's.
    op_0x563e48a36e80 [label="Share"];
    op_0x563e48a36ed0 [label="Share"];
    op_0x563e48a36f20 [label="Share"];
    op_0x563e48a36f70 [label="Share"];
    op_0x563e48a36fc0 [label="Share"];
    op_0x563e4b7d9258 [label="Expand"];
    // Dimension's.
    op_0x563e4b7d9258 -> op_0x563e48a36e80 [label="C_out"];
    interface_0_in_0x563e48a36eb8 -> op_0x563e48a36e80 [label="C_out"];
    interface_0_in_0x563e48a36ef0 -> op_0x563e48a36ed0 [label="k_1"];
    interface_0_in_0x563e48a36f08 -> op_0x563e48a36ed0 [label="k_1"];
    interface_0_in_0x563e48a36f40 -> op_0x563e48a36f20 [label="k_1"];
    interface_0_in_0x563e48a36f58 -> op_0x563e48a36f20 [label="k_1"];
    interface_0_in_0x563e48a36f90 -> op_0x563e48a36f70 [label="g"];
    interface_0_in_0x563e48a36fa8 -> op_0x563e48a36f70 [label="g"];
    interface_0_in_0x563e48a36fe0 -> op_0x563e48a36fc0 [label="g^-1*s^-1*C_out"];
    interface_0_in_0x563e48a36ff8 -> op_0x563e48a36fc0 [label="g^-1*s^-1*C_out"];
    interface_0_in_0x563e48b9d610 -> interface_0_out_0x563e48b9d610 [label="N"];
    interface_0_in_0x563e4b7c4510 -> interface_0_out_0x563e4b7c4510 [label="H"];
    interface_0_in_0x563e4b7d4f10 -> interface_0_out_0x563e4b7d4f10 [label="H"];
    op_0x563e48a36ed0 -> reduce_0x563e4b853ee0 [label="k_1"];
    op_0x563e48a36f20 -> reduce_0x563e4b853ef8 [label="k_1"];
    op_0x563e48a36f70 -> reduce_0x563e4b853f98 [label="g"];
    op_0x563e48a36fc0 -> reduce_0x563e4b854050 [label="g^-1*s^-1*C_out"];
    op_0x563e48a36e80 -> interface_0_out_0x563e4b856690 [label="C_out"];
}

// Stage tensor.
subgraph cluster_subgraph_1 {
    label = "Subgraph 1";
    // Reductions.
    // Output.
    subgraph cluster_subgraph_1_out {
        label = "";
        interface_1_out_0x563e48b9d610 [label="N", shape=none];
        interface_1_out_0x563e48a36f90 [label="g", shape=none];
        interface_1_out_0x563e48a36ef0 [label="k_1", shape=none];
        interface_1_out_0x563e4b7d4f10 [label="H", shape=none];
        interface_1_out_0x563e48a36f40 [label="k_1", shape=none];
        interface_1_out_0x563e4b7c4510 [label="H", shape=none];
        interface_1_out_0x563e48a36fe0 [label="g^-1*s^-1*C_out", shape=none];
    }
    {
        rank = same;
        interface_1_out_0x563e48b9d610;
        interface_1_out_0x563e48a36f90;
        interface_1_out_0x563e48a36ef0;
        interface_1_out_0x563e4b7d4f10;
        interface_1_out_0x563e48a36f40;
        interface_1_out_0x563e4b7c4510;
        interface_1_out_0x563e48a36fe0;
    }
    // Input 0.
    subgraph cluster_subgraph_1_in_0 {
        label = "";
        interface_1_in_0x563e48b9d610 [label="N", shape=none];
        interface_1_in_0x563e48a36f90 [label="g", shape=none];
        interface_1_in_0x563e48a37c28 [label="H", shape=none];
        interface_1_in_0x563e48a36f40 [label="k_1", shape=none];
        interface_1_in_0x563e4b7c4510 [label="H", shape=none];
        interface_1_in_0x563e48a36fe0 [label="g^-1*s^-1*C_out", shape=none];
    }
    {
        rank = same;
        interface_1_in_0x563e48b9d610;
        interface_1_in_0x563e48a36f90;
        interface_1_in_0x563e48a37c28;
        interface_1_in_0x563e48a36f40;
        interface_1_in_0x563e4b7c4510;
        interface_1_in_0x563e48a36fe0;
    }
    // Op's.
    op_0x563e48a37c00 [label="Unfold"];
    // Dimension's.
    op_0x563e48a37c00 -> interface_1_out_0x563e48a36ef0 [label="k_1"];
    interface_1_in_0x563e48a36f40 -> interface_1_out_0x563e48a36f40 [label="k_1"];
    interface_1_in_0x563e48a36f90 -> interface_1_out_0x563e48a36f90 [label="g"];
    interface_1_in_0x563e48a36fe0 -> interface_1_out_0x563e48a36fe0 [label="g^-1*s^-1*C_out"];
    interface_1_in_0x563e48a37c28 -> op_0x563e48a37c00 [label="H"];
    interface_1_in_0x563e48b9d610 -> interface_1_out_0x563e48b9d610 [label="N"];
    interface_1_in_0x563e4b7c4510 -> interface_1_out_0x563e4b7c4510 [label="H"];
    op_0x563e48a37c00 -> interface_1_out_0x563e4b7d4f10 [label="H"];
}

// Stage tensor.
subgraph cluster_subgraph_2 {
    label = "Subgraph 2";
    // Reductions.
    reduce_0x563e4b853e28 [label="Sum", shape=box];
    // Output.
    subgraph cluster_subgraph_2_out {
        label = "";
        interface_2_out_0x563e48b9d610 [label="N", shape=none];
        interface_2_out_0x563e48a36f90 [label="g", shape=none];
        interface_2_out_0x563e48a37c28 [label="H", shape=none];
        interface_2_out_0x563e48a36f40 [label="k_1", shape=none];
        interface_2_out_0x563e4b7c4510 [label="H", shape=none];
        interface_2_out_0x563e48a36fe0 [label="g^-1*s^-1*C_out", shape=none];
    }
    {
        rank = same;
        reduce_0x563e4b853e28;
        interface_2_out_0x563e48b9d610;
        interface_2_out_0x563e48a36f90;
        interface_2_out_0x563e48a37c28;
        interface_2_out_0x563e48a36f40;
        interface_2_out_0x563e4b7c4510;
        interface_2_out_0x563e48a36fe0;
    }
    // Input 0.
    subgraph cluster_subgraph_2_in_0 {
        label = "";
        interface_2_in_0x563e48b9d610 [label="N", shape=none];
        interface_2_in_0x563e4b7d46c0 [label="C_in", shape=none];
        interface_2_in_0x563e48a37c28 [label="H", shape=none];
        interface_2_in_0x563e48a36f40 [label="k_1", shape=none];
        interface_2_in_0x563e4b7c4510 [label="H", shape=none];
        interface_2_in_0x563e48a36fe0 [label="g^-1*s^-1*C_out", shape=none];
    }
    {
        rank = same;
        interface_2_in_0x563e48b9d610;
        interface_2_in_0x563e4b7d46c0;
        interface_2_in_0x563e48a37c28;
        interface_2_in_0x563e48a36f40;
        interface_2_in_0x563e4b7c4510;
        interface_2_in_0x563e48a36fe0;
    }
    // Op's.
    op_0x563e4b7d4680 [label="Split"];
    // Dimension's.
    interface_2_in_0x563e48a36f40 -> interface_2_out_0x563e48a36f40 [label="k_1"];
    op_0x563e4b7d4680 -> interface_2_out_0x563e48a36f90 [label="g"];
    interface_2_in_0x563e48a36fe0 -> interface_2_out_0x563e48a36fe0 [label="g^-1*s^-1*C_out"];
    interface_2_in_0x563e48a37c28 -> interface_2_out_0x563e48a37c28 [label="H"];
    interface_2_in_0x563e48b9d610 -> interface_2_out_0x563e48b9d610 [label="N"];
    interface_2_in_0x563e4b7c4510 -> interface_2_out_0x563e4b7c4510 [label="H"];
    interface_2_in_0x563e4b7d46c0 -> op_0x563e4b7d4680 [label="C_in"];
    op_0x563e4b7d4680 -> reduce_0x563e4b853e28 [label="g^-1*C_in"];
}

// Stage tensor.
subgraph cluster_subgraph_3 {
    label = "Subgraph 3";
    // Reductions.
    // Output.
    subgraph cluster_subgraph_3_out {
        label = "";
        interface_3_out_0x563e48b9d610 [label="N", shape=none];
        interface_3_out_0x563e4b7d46c0 [label="C_in", shape=none];
        interface_3_out_0x563e48a37c28 [label="H", shape=none];
        interface_3_out_0x563e48a36f40 [label="k_1", shape=none];
        interface_3_out_0x563e4b7c4510 [label="H", shape=none];
        interface_3_out_0x563e48a36fe0 [label="g^-1*s^-1*C_out", shape=none];
    }
    {
        rank = same;
        interface_3_out_0x563e48b9d610;
        interface_3_out_0x563e4b7d46c0;
        interface_3_out_0x563e48a37c28;
        interface_3_out_0x563e48a36f40;
        interface_3_out_0x563e4b7c4510;
        interface_3_out_0x563e48a36fe0;
    }
    // Input 0.
    subgraph cluster_subgraph_3_in_0 {
        label = "";
        interface_3_in_0x563e48b9d610 [label="N", shape=none];
        interface_3_in_0x563e48a37080 [label="C_in", shape=none];
        interface_3_in_0x563e48a37c28 [label="H", shape=none];
        interface_3_in_0x563e48a37030 [label="k_1", shape=none];
        interface_3_in_0x563e4b7c4510 [label="H", shape=none];
    }
    // Input 1.
    subgraph cluster_subgraph_3_in_1 {
        label = "";
        interface_3_in_0x563e48a37098 [label="C_in", shape=none];
        interface_3_in_0x563e48a37048 [label="k_1", shape=none];
        interface_3_in_0x563e48a370e8 [label="g^-1*s^-1*C_out", shape=none];
    }
    {
        rank = same;
        interface_3_in_0x563e48b9d610;
        interface_3_in_0x563e48a37080;
        interface_3_in_0x563e48a37c28;
        interface_3_in_0x563e48a37030;
        interface_3_in_0x563e4b7c4510;
        interface_3_in_0x563e48a37098;
        interface_3_in_0x563e48a37048;
        interface_3_in_0x563e48a370e8;
    }
    // Op's.
    op_0x563e48a37010 [label="Share"];
    op_0x563e48a37060 [label="Share"];
    op_0x563e48a370b0 [label="Share"];
    op_0x563e4b7d9278 [label="Expand"];
    // Dimension's.
    op_0x563e48a37010 -> interface_3_out_0x563e48a36f40 [label="k_1"];
    op_0x563e48a370b0 -> interface_3_out_0x563e48a36fe0 [label="g^-1*s^-1*C_out"];
    interface_3_in_0x563e48a37030 -> op_0x563e48a37010 [label="k_1"];
    interface_3_in_0x563e48a37048 -> op_0x563e48a37010 [label="k_1"];
    interface_3_in_0x563e48a37080 -> op_0x563e48a37060 [label="C_in"];
    interface_3_in_0x563e48a37098 -> op_0x563e48a37060 [label="C_in"];
    op_0x563e4b7d9278 -> op_0x563e48a370b0 [label="g^-1*s^-1*C_out"];
    interface_3_in_0x563e48a370e8 -> op_0x563e48a370b0 [label="g^-1*s^-1*C_out"];
    interface_3_in_0x563e48a37c28 -> interface_3_out_0x563e48a37c28 [label="H"];
    interface_3_in_0x563e48b9d610 -> interface_3_out_0x563e48b9d610 [label="N"];
    interface_3_in_0x563e4b7c4510 -> interface_3_out_0x563e4b7c4510 [label="H"];
    op_0x563e48a37060 -> interface_3_out_0x563e4b7d46c0 [label="C_in"];
}

// Stage tensor.
subgraph cluster_subgraph_4 {
    label = "Subgraph 4";
    // Reductions.
    // Output.
    subgraph cluster_subgraph_4_out {
        label = "";
        interface_4_out_0x563e48b9d610 [label="N", shape=none];
        interface_4_out_0x563e48a37080 [label="C_in", shape=none];
        interface_4_out_0x563e48a37c28 [label="H", shape=none];
        interface_4_out_0x563e48a37030 [label="k_1", shape=none];
        interface_4_out_0x563e4b7c4510 [label="H", shape=none];
    }
    {
        rank = same;
        interface_4_out_0x563e48b9d610;
        interface_4_out_0x563e48a37080;
        interface_4_out_0x563e48a37c28;
        interface_4_out_0x563e48a37030;
        interface_4_out_0x563e4b7c4510;
    }
    // Input 0.
    subgraph cluster_subgraph_4_in_0 {
        label = "";
        interface_4_in_0x563e48b9d610 [label="N", shape=none];
        interface_4_in_0x563e48a37080 [label="C_in", shape=none];
        interface_4_in_0x563e48a37c28 [label="H", shape=none];
        interface_4_in_0x563e48a37c68 [label="H", shape=none];
    }
    {
        rank = same;
        interface_4_in_0x563e48b9d610;
        interface_4_in_0x563e48a37080;
        interface_4_in_0x563e48a37c28;
        interface_4_in_0x563e48a37c68;
    }
    // Op's.
    op_0x563e48a37c40 [label="Unfold"];
    // Dimension's.
    op_0x563e48a37c40 -> interface_4_out_0x563e48a37030 [label="k_1"];
    interface_4_in_0x563e48a37080 -> interface_4_out_0x563e48a37080 [label="C_in"];
    interface_4_in_0x563e48a37c28 -> interface_4_out_0x563e48a37c28 [label="H"];
    interface_4_in_0x563e48a37c68 -> op_0x563e48a37c40 [label="H"];
    interface_4_in_0x563e48b9d610 -> interface_4_out_0x563e48b9d610 [label="N"];
    op_0x563e48a37c40 -> interface_4_out_0x563e4b7c4510 [label="H"];
}

// Input tensor.
subgraph cluster_subgraph_5 {
    label = "Input 0";
    interface_5_out_0x563e48b9d610 [label="N", shape=none];
    interface_5_out_0x563e48a37080 [label="C_in", shape=none];
    interface_5_out_0x563e48a37c28 [label="H", shape=none];
    interface_5_out_0x563e48a37c68 [label="H", shape=none];
}

interface_5_out_0x563e48b9d610 -> interface_4_in_0x563e48b9d610;
interface_5_out_0x563e48a37080 -> interface_4_in_0x563e48a37080;
interface_5_out_0x563e48a37c28 -> interface_4_in_0x563e48a37c28;
interface_5_out_0x563e48a37c68 -> interface_4_in_0x563e48a37c68;

interface_4_out_0x563e48b9d610 -> interface_3_in_0x563e48b9d610;
interface_4_out_0x563e48a37080 -> interface_3_in_0x563e48a37080;
interface_4_out_0x563e48a37c28 -> interface_3_in_0x563e48a37c28;
interface_4_out_0x563e48a37030 -> interface_3_in_0x563e48a37030;
interface_4_out_0x563e4b7c4510 -> interface_3_in_0x563e4b7c4510;

// Input tensor.
subgraph cluster_subgraph_6 {
    label = "Input 2";
    interface_6_out_0x563e48a37098 [label="C_in", shape=none];
    interface_6_out_0x563e48a37048 [label="k_1", shape=none];
    interface_6_out_0x563e48a370e8 [label="g^-1*s^-1*C_out", shape=none];
}

interface_6_out_0x563e48a37098 -> interface_3_in_0x563e48a37098;
interface_6_out_0x563e48a37048 -> interface_3_in_0x563e48a37048;
interface_6_out_0x563e48a370e8 -> interface_3_in_0x563e48a370e8;

interface_3_out_0x563e48b9d610 -> interface_2_in_0x563e48b9d610;
interface_3_out_0x563e4b7d46c0 -> interface_2_in_0x563e4b7d46c0;
interface_3_out_0x563e48a37c28 -> interface_2_in_0x563e48a37c28;
interface_3_out_0x563e48a36f40 -> interface_2_in_0x563e48a36f40;
interface_3_out_0x563e4b7c4510 -> interface_2_in_0x563e4b7c4510;
interface_3_out_0x563e48a36fe0 -> interface_2_in_0x563e48a36fe0;

interface_2_out_0x563e48b9d610 -> interface_1_in_0x563e48b9d610;
interface_2_out_0x563e48a36f90 -> interface_1_in_0x563e48a36f90;
interface_2_out_0x563e48a37c28 -> interface_1_in_0x563e48a37c28;
interface_2_out_0x563e48a36f40 -> interface_1_in_0x563e48a36f40;
interface_2_out_0x563e4b7c4510 -> interface_1_in_0x563e4b7c4510;
interface_2_out_0x563e48a36fe0 -> interface_1_in_0x563e48a36fe0;

interface_1_out_0x563e48b9d610 -> interface_0_in_0x563e48b9d610;
interface_1_out_0x563e48a36f90 -> interface_0_in_0x563e48a36f90;
interface_1_out_0x563e48a36ef0 -> interface_0_in_0x563e48a36ef0;
interface_1_out_0x563e4b7d4f10 -> interface_0_in_0x563e4b7d4f10;
interface_1_out_0x563e48a36f40 -> interface_0_in_0x563e48a36f40;
interface_1_out_0x563e4b7c4510 -> interface_0_in_0x563e4b7c4510;
interface_1_out_0x563e48a36fe0 -> interface_0_in_0x563e48a36fe0;

// Input tensor.
subgraph cluster_subgraph_7 {
    label = "Input 1";
    interface_7_out_0x563e48a36eb8 [label="C_out", shape=none];
    interface_7_out_0x563e48a36fa8 [label="g", shape=none];
    interface_7_out_0x563e48a36f08 [label="k_1", shape=none];
    interface_7_out_0x563e48a36f58 [label="k_1", shape=none];
    interface_7_out_0x563e48a36ff8 [label="g^-1*s^-1*C_out", shape=none];
}

interface_7_out_0x563e48a36eb8 -> interface_0_in_0x563e48a36eb8;
interface_7_out_0x563e48a36fa8 -> interface_0_in_0x563e48a36fa8;
interface_7_out_0x563e48a36f08 -> interface_0_in_0x563e48a36f08;
interface_7_out_0x563e48a36f58 -> interface_0_in_0x563e48a36f58;
interface_7_out_0x563e48a36ff8 -> interface_0_in_0x563e48a36ff8;

{
    rank = same;
    interface_5_out_0x563e48b9d610;
    interface_5_out_0x563e48a37080;
    interface_5_out_0x563e48a37c28;
    interface_5_out_0x563e48a37c68;
    interface_7_out_0x563e48a36eb8;
    interface_7_out_0x563e48a36fa8;
    interface_7_out_0x563e48a36f08;
    interface_7_out_0x563e48a36f58;
    interface_7_out_0x563e48a36ff8;
    interface_6_out_0x563e48a37098;
    interface_6_out_0x563e48a37048;
    interface_6_out_0x563e48a370e8;
}
subgraph cluster_subgraph_output {
    label = "Output";
    interface_8_in_0x563e48b9d610 [label="N", shape=none];
    interface_8_in_0x563e4b856690 [label="C_out", shape=none];
    interface_8_in_0x563e4b7d4f10 [label="H", shape=none];
    interface_8_in_0x563e4b7c4510 [label="H", shape=none];
}
interface_0_out_0x563e48b9d610 -> interface_8_in_0x563e48b9d610;
interface_0_out_0x563e4b856690 -> interface_8_in_0x563e4b856690;
interface_0_out_0x563e4b7d4f10 -> interface_8_in_0x563e4b7d4f10;
interface_0_out_0x563e4b7c4510 -> interface_8_in_0x563e4b7c4510;

}

"""
class kernel_manual_0(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([64, 32, 3, 3, 1]),
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
		t_3 = torch.reshape(t_3, (1, 3584, 56, 1, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (1, 64, 56, 3, 56, ))

		# Perform contraction.
		t_4 = torch.einsum("mjlin, jik -> mjlink", t_3, in_2)

		# No contraction needed.
		t_5 = t_4

		# [C_in]@Splitc2d52f3525ba6cc4 -> [g]@Sharec7a8ce455b828537, [g^-1*C_in]@Reduceef9903cafc29eea1
		t_5 = torch.reshape(t_5, (1, 32, 2, 56, 3, 56, 1, ))

		# [g^-1*C_in]@Reduce
		t_5 = torch.sum(t_5, dim=(2, ))

		# No contraction needed.
		t_6 = t_5

		# [H]@Unfold4d77c1e3da5bca44 -> [H]@Iterator96123ba3184da39c, [k_1]@Share26cfa48d169008e4
		t_6 = torch.reshape(t_6, (1, 32, 56, 168, ))
		t_6 = torch.nn.functional.unfold(t_6, (3, 1, ), padding=(1, 0, ))
		t_6 = torch.reshape(t_6, (1, 32, 3, 56, 3, 56, 1, ))

		# Perform contraction.
		t_7 = torch.einsum("nljpkom, iljkm -> nipo", t_6, in_1)

		# No need to crop the output tensor.
		y = t_7

		return y

class kernel_manual_1(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([128, 32, 3, 3, 2]),
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
		t_3 = torch.reshape(t_3, (1, 1792, 28, 1, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (1, 64, 28, 3, 28, ))

		# Perform contraction.
		t_4 = torch.einsum("mjlin, jik -> mjlink", t_3, in_2)

		# No contraction needed.
		t_5 = t_4

		# [C_in]@Splitc2d52f3525ba6cc4 -> [g]@Sharec7a8ce455b828537, [g^-1*C_in]@Reduceef9903cafc29eea1
		t_5 = torch.reshape(t_5, (1, 32, 2, 28, 3, 28, 2, ))

		# [g^-1*C_in]@Reduce
		t_5 = torch.sum(t_5, dim=(2, ))

		# No contraction needed.
		t_6 = t_5

		# [H]@Unfold4d77c1e3da5bca44 -> [H]@Iterator96123ba3184da39c, [k_1]@Share26cfa48d169008e4
		t_6 = torch.reshape(t_6, (1, 32, 28, 168, ))
		t_6 = torch.nn.functional.unfold(t_6, (3, 1, ), padding=(1, 0, ))
		t_6 = torch.reshape(t_6, (1, 32, 3, 28, 3, 28, 2, ))

		# Perform contraction.
		t_7 = torch.einsum("nljpkom, iljkm -> nipo", t_6, in_1)

		# No need to crop the output tensor.
		y = t_7

		return y

class kernel_manual_2(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([128, 32, 3, 3, 2]),
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
		t_3 = torch.reshape(t_3, (1, 3584, 28, 1, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (1, 128, 28, 3, 28, ))

		# Perform contraction.
		t_4 = torch.einsum("mjlin, jik -> mjlink", t_3, in_2)

		# No contraction needed.
		t_5 = t_4

		# [C_in]@Splitc2d52f3525ba6cc4 -> [g]@Sharec7a8ce455b828537, [g^-1*C_in]@Reduceef9903cafc29eea1
		t_5 = torch.reshape(t_5, (1, 32, 4, 28, 3, 28, 2, ))

		# [g^-1*C_in]@Reduce
		t_5 = torch.sum(t_5, dim=(2, ))

		# No contraction needed.
		t_6 = t_5

		# [H]@Unfold4d77c1e3da5bca44 -> [H]@Iterator96123ba3184da39c, [k_1]@Share26cfa48d169008e4
		t_6 = torch.reshape(t_6, (1, 32, 28, 168, ))
		t_6 = torch.nn.functional.unfold(t_6, (3, 1, ), padding=(1, 0, ))
		t_6 = torch.reshape(t_6, (1, 32, 3, 28, 3, 28, 2, ))

		# Perform contraction.
		t_7 = torch.einsum("nljpkom, iljkm -> nipo", t_6, in_1)

		# No need to crop the output tensor.
		y = t_7

		return y

class kernel_manual_3(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([256, 32, 3, 3, 4]),
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
		t_3 = torch.reshape(t_3, (1, 1792, 14, 1, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (1, 128, 14, 3, 14, ))

		# Perform contraction.
		t_4 = torch.einsum("mjlin, jik -> mjlink", t_3, in_2)

		# No contraction needed.
		t_5 = t_4

		# [C_in]@Splitc2d52f3525ba6cc4 -> [g]@Sharec7a8ce455b828537, [g^-1*C_in]@Reduceef9903cafc29eea1
		t_5 = torch.reshape(t_5, (1, 32, 4, 14, 3, 14, 4, ))

		# [g^-1*C_in]@Reduce
		t_5 = torch.sum(t_5, dim=(2, ))

		# No contraction needed.
		t_6 = t_5

		# [H]@Unfold4d77c1e3da5bca44 -> [H]@Iterator96123ba3184da39c, [k_1]@Share26cfa48d169008e4
		t_6 = torch.reshape(t_6, (1, 32, 14, 168, ))
		t_6 = torch.nn.functional.unfold(t_6, (3, 1, ), padding=(1, 0, ))
		t_6 = torch.reshape(t_6, (1, 32, 3, 14, 3, 14, 4, ))

		# Perform contraction.
		t_7 = torch.einsum("nljpkom, iljkm -> nipo", t_6, in_1)

		# No need to crop the output tensor.
		y = t_7

		return y

class kernel_manual_4(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([256, 32, 3, 3, 4]),
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
		t_3 = torch.reshape(t_3, (1, 3584, 14, 1, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (1, 256, 14, 3, 14, ))

		# Perform contraction.
		t_4 = torch.einsum("mjlin, jik -> mjlink", t_3, in_2)

		# No contraction needed.
		t_5 = t_4

		# [C_in]@Splitc2d52f3525ba6cc4 -> [g]@Sharec7a8ce455b828537, [g^-1*C_in]@Reduceef9903cafc29eea1
		t_5 = torch.reshape(t_5, (1, 32, 8, 14, 3, 14, 4, ))

		# [g^-1*C_in]@Reduce
		t_5 = torch.sum(t_5, dim=(2, ))

		# No contraction needed.
		t_6 = t_5

		# [H]@Unfold4d77c1e3da5bca44 -> [H]@Iterator96123ba3184da39c, [k_1]@Share26cfa48d169008e4
		t_6 = torch.reshape(t_6, (1, 32, 14, 168, ))
		t_6 = torch.nn.functional.unfold(t_6, (3, 1, ), padding=(1, 0, ))
		t_6 = torch.reshape(t_6, (1, 32, 3, 14, 3, 14, 4, ))

		# Perform contraction.
		t_7 = torch.einsum("nljpkom, iljkm -> nipo", t_6, in_1)

		# No need to crop the output tensor.
		y = t_7

		return y

class kernel_manual_5(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([512, 32, 3, 3, 8]),
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
		t_3 = torch.reshape(t_3, (1, 1792, 7, 1, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (1, 256, 7, 3, 7, ))

		# Perform contraction.
		t_4 = torch.einsum("mjlin, jik -> mjlink", t_3, in_2)

		# No contraction needed.
		t_5 = t_4

		# [C_in]@Splitc2d52f3525ba6cc4 -> [g]@Sharec7a8ce455b828537, [g^-1*C_in]@Reduceef9903cafc29eea1
		t_5 = torch.reshape(t_5, (1, 32, 8, 7, 3, 7, 8, ))

		# [g^-1*C_in]@Reduce
		t_5 = torch.sum(t_5, dim=(2, ))

		# No contraction needed.
		t_6 = t_5

		# [H]@Unfold4d77c1e3da5bca44 -> [H]@Iterator96123ba3184da39c, [k_1]@Share26cfa48d169008e4
		t_6 = torch.reshape(t_6, (1, 32, 7, 168, ))
		t_6 = torch.nn.functional.unfold(t_6, (3, 1, ), padding=(1, 0, ))
		t_6 = torch.reshape(t_6, (1, 32, 3, 7, 3, 7, 8, ))

		# Perform contraction.
		t_7 = torch.einsum("nljpkom, iljkm -> nipo", t_6, in_1)

		# No need to crop the output tensor.
		y = t_7

		return y

class kernel_manual_6(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([512, 32, 3, 3, 8]),
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
		t_3 = torch.reshape(t_3, (1, 3584, 7, 1, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (1, 512, 7, 3, 7, ))

		# Perform contraction.
		t_4 = torch.einsum("mjlin, jik -> mjlink", t_3, in_2)

		# No contraction needed.
		t_5 = t_4

		# [C_in]@Splitc2d52f3525ba6cc4 -> [g]@Sharec7a8ce455b828537, [g^-1*C_in]@Reduceef9903cafc29eea1
		t_5 = torch.reshape(t_5, (1, 32, 16, 7, 3, 7, 8, ))

		# [g^-1*C_in]@Reduce
		t_5 = torch.sum(t_5, dim=(2, ))

		# No contraction needed.
		t_6 = t_5

		# [H]@Unfold4d77c1e3da5bca44 -> [H]@Iterator96123ba3184da39c, [k_1]@Share26cfa48d169008e4
		t_6 = torch.reshape(t_6, (1, 32, 7, 168, ))
		t_6 = torch.nn.functional.unfold(t_6, (3, 1, ), padding=(1, 0, ))
		t_6 = torch.reshape(t_6, (1, 32, 3, 7, 3, 7, 8, ))

		# Perform contraction.
		t_7 = torch.einsum("nljpkom, iljkm -> nipo", t_6, in_1)

		# No need to crop the output tensor.
		y = t_7

		return y

