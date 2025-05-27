import torch
import random
"""
digraph kernel_preview {
newrank = true;

// Stage tensor.
subgraph cluster_subgraph_0 {
    label = "Subgraph 0";
    // Reductions.
    // Output.
    subgraph cluster_subgraph_0_out {
        label = "";
        interface_0_out_0x55ef9e30f530 [label="N", shape=none];
        interface_0_out_0x55ef9e30f558 [label="C_out", shape=none];
        interface_0_out_0x55ef9e30f580 [label="H", shape=none];
        interface_0_out_0x55ef9e30f5a8 [label="H", shape=none];
    }
    {
        rank = same;
        interface_0_out_0x55ef9e30f530;
        interface_0_out_0x55ef9e30f558;
        interface_0_out_0x55ef9e30f580;
        interface_0_out_0x55ef9e30f5a8;
    }
    // Input 0.
    subgraph cluster_subgraph_0_in_0 {
        label = "";
        interface_0_in_0x55ef9e30f530 [label="N", shape=none];
        interface_0_in_0x55efa1d46860 [label="g", shape=none];
        interface_0_in_0x55efa1d46878 [label="g^-1*C_out", shape=none];
        interface_0_in_0x55ef9e30f580 [label="H", shape=none];
        interface_0_in_0x55ef9e30f5a8 [label="H", shape=none];
    }
    {
        rank = same;
        interface_0_in_0x55ef9e30f530;
        interface_0_in_0x55efa1d46860;
        interface_0_in_0x55efa1d46878;
        interface_0_in_0x55ef9e30f580;
        interface_0_in_0x55ef9e30f5a8;
    }
    // Op's.
    op_0x55efa1d46820 [label="Merge"];
    // Dimension's.
    interface_0_in_0x55ef9e30f530 -> interface_0_out_0x55ef9e30f530 [label="N"];
    op_0x55efa1d46820 -> interface_0_out_0x55ef9e30f558 [label="C_out"];
    interface_0_in_0x55ef9e30f580 -> interface_0_out_0x55ef9e30f580 [label="H"];
    interface_0_in_0x55ef9e30f5a8 -> interface_0_out_0x55ef9e30f5a8 [label="H"];
    interface_0_in_0x55efa1d46860 -> op_0x55efa1d46820 [label="g"];
    interface_0_in_0x55efa1d46878 -> op_0x55efa1d46820 [label="g^-1*C_out"];
}

// Stage tensor.
subgraph cluster_subgraph_1 {
    label = "Subgraph 1";
    // Reductions.
    reduce_0x7f3dcc005820 [label="Sum", shape=box];
    reduce_0x7f3dcc001a98 [label="Sum", shape=box];
    reduce_0x7f3dcc001ab0 [label="Sum", shape=box];
    // Output.
    subgraph cluster_subgraph_1_out {
        label = "";
        interface_1_out_0x55ef9e30f530 [label="N", shape=none];
        interface_1_out_0x55efa1d46860 [label="g", shape=none];
        interface_1_out_0x55efa1d46878 [label="g^-1*C_out", shape=none];
        interface_1_out_0x55ef9e30f580 [label="H", shape=none];
        interface_1_out_0x55ef9e30f5a8 [label="H", shape=none];
    }
    {
        rank = same;
        reduce_0x7f3dcc005820;
        reduce_0x7f3dcc001a98;
        reduce_0x7f3dcc001ab0;
        interface_1_out_0x55ef9e30f530;
        interface_1_out_0x55efa1d46860;
        interface_1_out_0x55efa1d46878;
        interface_1_out_0x55ef9e30f580;
        interface_1_out_0x55ef9e30f5a8;
    }
    // Input 0.
    subgraph cluster_subgraph_1_in_0 {
        label = "";
        interface_1_in_0x55ef9e30f530 [label="N", shape=none];
        interface_1_in_0x55efa1d46878 [label="g^-1*C_out", shape=none];
        interface_1_in_0x55efa1d445b0 [label="g^-1*s^-1*C_in", shape=none];
        interface_1_in_0x55efa1d444c0 [label="k_1", shape=none];
        interface_1_in_0x55ef9e30f580 [label="H", shape=none];
        interface_1_in_0x55efa1d44650 [label="k_1", shape=none];
        interface_1_in_0x55ef9e30f5a8 [label="H", shape=none];
    }
    // Input 1.
    subgraph cluster_subgraph_1_in_1 {
        label = "";
        interface_1_in_0x55efa1d446b8 [label="g", shape=none];
        interface_1_in_0x55efa1d445c8 [label="g^-1*s^-1*C_in", shape=none];
        interface_1_in_0x55efa1d444d8 [label="k_1", shape=none];
        interface_1_in_0x55efa1d44668 [label="k_1", shape=none];
    }
    {
        rank = same;
        interface_1_in_0x55ef9e30f530;
        interface_1_in_0x55efa1d46878;
        interface_1_in_0x55efa1d445b0;
        interface_1_in_0x55efa1d444c0;
        interface_1_in_0x55ef9e30f580;
        interface_1_in_0x55efa1d44650;
        interface_1_in_0x55ef9e30f5a8;
        interface_1_in_0x55efa1d446b8;
        interface_1_in_0x55efa1d445c8;
        interface_1_in_0x55efa1d444d8;
        interface_1_in_0x55efa1d44668;
    }
    // Op's.
    op_0x55efa1d444a0 [label="Share"];
    op_0x55efa1d44590 [label="Share"];
    op_0x55efa1d44630 [label="Share"];
    op_0x55efa1d44680 [label="Share"];
    op_0x55efa1d449b8 [label="Expand"];
    // Dimension's.
    interface_1_in_0x55ef9e30f530 -> interface_1_out_0x55ef9e30f530 [label="N"];
    interface_1_in_0x55ef9e30f580 -> interface_1_out_0x55ef9e30f580 [label="H"];
    interface_1_in_0x55ef9e30f5a8 -> interface_1_out_0x55ef9e30f5a8 [label="H"];
    interface_1_in_0x55efa1d444c0 -> op_0x55efa1d444a0 [label="k_1"];
    interface_1_in_0x55efa1d444d8 -> op_0x55efa1d444a0 [label="k_1"];
    interface_1_in_0x55efa1d445b0 -> op_0x55efa1d44590 [label="g^-1*s^-1*C_in"];
    interface_1_in_0x55efa1d445c8 -> op_0x55efa1d44590 [label="g^-1*s^-1*C_in"];
    interface_1_in_0x55efa1d44650 -> op_0x55efa1d44630 [label="k_1"];
    interface_1_in_0x55efa1d44668 -> op_0x55efa1d44630 [label="k_1"];
    op_0x55efa1d449b8 -> op_0x55efa1d44680 [label="g"];
    interface_1_in_0x55efa1d446b8 -> op_0x55efa1d44680 [label="g"];
    op_0x55efa1d44680 -> interface_1_out_0x55efa1d46860 [label="g"];
    interface_1_in_0x55efa1d46878 -> interface_1_out_0x55efa1d46878 [label="g^-1*C_out"];
    op_0x55efa1d444a0 -> reduce_0x7f3dcc001a98 [label="k_1"];
    op_0x55efa1d44630 -> reduce_0x7f3dcc001ab0 [label="k_1"];
    op_0x55efa1d44590 -> reduce_0x7f3dcc005820 [label="g^-1*s^-1*C_in"];
}

// Stage tensor.
subgraph cluster_subgraph_2 {
    label = "Subgraph 2";
    // Reductions.
    // Output.
    subgraph cluster_subgraph_2_out {
        label = "";
        interface_2_out_0x55ef9e30f530 [label="N", shape=none];
        interface_2_out_0x55efa1d46878 [label="g^-1*C_out", shape=none];
        interface_2_out_0x55efa1d445b0 [label="g^-1*s^-1*C_in", shape=none];
        interface_2_out_0x55efa1d444c0 [label="k_1", shape=none];
        interface_2_out_0x55ef9e30f580 [label="H", shape=none];
        interface_2_out_0x55efa1d44650 [label="k_1", shape=none];
        interface_2_out_0x55ef9e30f5a8 [label="H", shape=none];
    }
    {
        rank = same;
        interface_2_out_0x55ef9e30f530;
        interface_2_out_0x55efa1d46878;
        interface_2_out_0x55efa1d445b0;
        interface_2_out_0x55efa1d444c0;
        interface_2_out_0x55ef9e30f580;
        interface_2_out_0x55efa1d44650;
        interface_2_out_0x55ef9e30f5a8;
    }
    // Input 0.
    subgraph cluster_subgraph_2_in_0 {
        label = "";
        interface_2_in_0x55ef9e30f530 [label="N", shape=none];
        interface_2_in_0x55efa1d46878 [label="g^-1*C_out", shape=none];
        interface_2_in_0x55efa1d445b0 [label="g^-1*s^-1*C_in", shape=none];
        interface_2_in_0x55efa1d54aa8 [label="H", shape=none];
        interface_2_in_0x55efa1d44650 [label="k_1", shape=none];
        interface_2_in_0x55ef9e30f5a8 [label="H", shape=none];
    }
    {
        rank = same;
        interface_2_in_0x55ef9e30f530;
        interface_2_in_0x55efa1d46878;
        interface_2_in_0x55efa1d445b0;
        interface_2_in_0x55efa1d54aa8;
        interface_2_in_0x55efa1d44650;
        interface_2_in_0x55ef9e30f5a8;
    }
    // Op's.
    op_0x55efa1d54a80 [label="Unfold"];
    // Dimension's.
    interface_2_in_0x55ef9e30f530 -> interface_2_out_0x55ef9e30f530 [label="N"];
    op_0x55efa1d54a80 -> interface_2_out_0x55ef9e30f580 [label="H"];
    interface_2_in_0x55ef9e30f5a8 -> interface_2_out_0x55ef9e30f5a8 [label="H"];
    op_0x55efa1d54a80 -> interface_2_out_0x55efa1d444c0 [label="k_1"];
    interface_2_in_0x55efa1d445b0 -> interface_2_out_0x55efa1d445b0 [label="g^-1*s^-1*C_in"];
    interface_2_in_0x55efa1d44650 -> interface_2_out_0x55efa1d44650 [label="k_1"];
    interface_2_in_0x55efa1d46878 -> interface_2_out_0x55efa1d46878 [label="g^-1*C_out"];
    interface_2_in_0x55efa1d54aa8 -> op_0x55efa1d54a80 [label="H"];
}

// Stage tensor.
subgraph cluster_subgraph_3 {
    label = "Subgraph 3";
    // Reductions.
    reduce_0x7f3dcc002f10 [label="Sum", shape=box];
    // Output.
    subgraph cluster_subgraph_3_out {
        label = "";
        interface_3_out_0x55ef9e30f530 [label="N", shape=none];
        interface_3_out_0x55efa1d46878 [label="g^-1*C_out", shape=none];
        interface_3_out_0x55efa1d445b0 [label="g^-1*s^-1*C_in", shape=none];
        interface_3_out_0x55efa1d54aa8 [label="H", shape=none];
        interface_3_out_0x55efa1d44650 [label="k_1", shape=none];
        interface_3_out_0x55ef9e30f5a8 [label="H", shape=none];
    }
    {
        rank = same;
        reduce_0x7f3dcc002f10;
        interface_3_out_0x55ef9e30f530;
        interface_3_out_0x55efa1d46878;
        interface_3_out_0x55efa1d445b0;
        interface_3_out_0x55efa1d54aa8;
        interface_3_out_0x55efa1d44650;
        interface_3_out_0x55ef9e30f5a8;
    }
    // Input 0.
    subgraph cluster_subgraph_3_in_0 {
        label = "";
        interface_3_in_0x55ef9e30f530 [label="N", shape=none];
        interface_3_in_0x55efa1d44790 [label="g*s", shape=none];
        interface_3_in_0x55efa1d445b0 [label="g^-1*s^-1*C_in", shape=none];
        interface_3_in_0x55efa1d54aa8 [label="H", shape=none];
        interface_3_in_0x55efa1d44830 [label="k_1", shape=none];
        interface_3_in_0x55ef9e30f5a8 [label="H", shape=none];
    }
    // Input 1.
    subgraph cluster_subgraph_3_in_1 {
        label = "";
        interface_3_in_0x55efa1d44758 [label="g^-1*C_out", shape=none];
        interface_3_in_0x55efa1d447a8 [label="g*s", shape=none];
        interface_3_in_0x55efa1d44848 [label="k_1", shape=none];
    }
    {
        rank = same;
        interface_3_in_0x55ef9e30f530;
        interface_3_in_0x55efa1d44790;
        interface_3_in_0x55efa1d445b0;
        interface_3_in_0x55efa1d54aa8;
        interface_3_in_0x55efa1d44830;
        interface_3_in_0x55ef9e30f5a8;
        interface_3_in_0x55efa1d44758;
        interface_3_in_0x55efa1d447a8;
        interface_3_in_0x55efa1d44848;
    }
    // Op's.
    op_0x55efa1d44720 [label="Share"];
    op_0x55efa1d44770 [label="Share"];
    op_0x55efa1d44810 [label="Share"];
    op_0x55efa1d449f8 [label="Expand"];
    // Dimension's.
    interface_3_in_0x55ef9e30f530 -> interface_3_out_0x55ef9e30f530 [label="N"];
    interface_3_in_0x55ef9e30f5a8 -> interface_3_out_0x55ef9e30f5a8 [label="H"];
    interface_3_in_0x55efa1d445b0 -> interface_3_out_0x55efa1d445b0 [label="g^-1*s^-1*C_in"];
    op_0x55efa1d44810 -> interface_3_out_0x55efa1d44650 [label="k_1"];
    op_0x55efa1d449f8 -> op_0x55efa1d44720 [label="g^-1*C_out"];
    interface_3_in_0x55efa1d44758 -> op_0x55efa1d44720 [label="g^-1*C_out"];
    interface_3_in_0x55efa1d44790 -> op_0x55efa1d44770 [label="g*s"];
    interface_3_in_0x55efa1d447a8 -> op_0x55efa1d44770 [label="g*s"];
    interface_3_in_0x55efa1d44830 -> op_0x55efa1d44810 [label="k_1"];
    interface_3_in_0x55efa1d44848 -> op_0x55efa1d44810 [label="k_1"];
    op_0x55efa1d44720 -> interface_3_out_0x55efa1d46878 [label="g^-1*C_out"];
    interface_3_in_0x55efa1d54aa8 -> interface_3_out_0x55efa1d54aa8 [label="H"];
    op_0x55efa1d44770 -> reduce_0x7f3dcc002f10 [label="g*s"];
}

// Stage tensor.
subgraph cluster_subgraph_4 {
    label = "Subgraph 4";
    // Reductions.
    // Output.
    subgraph cluster_subgraph_4_out {
        label = "";
        interface_4_out_0x55ef9e30f530 [label="N", shape=none];
        interface_4_out_0x55efa1d44790 [label="g*s", shape=none];
        interface_4_out_0x55efa1d445b0 [label="g^-1*s^-1*C_in", shape=none];
        interface_4_out_0x55efa1d54aa8 [label="H", shape=none];
        interface_4_out_0x55efa1d44830 [label="k_1", shape=none];
        interface_4_out_0x55ef9e30f5a8 [label="H", shape=none];
    }
    {
        rank = same;
        interface_4_out_0x55ef9e30f530;
        interface_4_out_0x55efa1d44790;
        interface_4_out_0x55efa1d445b0;
        interface_4_out_0x55efa1d54aa8;
        interface_4_out_0x55efa1d44830;
        interface_4_out_0x55ef9e30f5a8;
    }
    // Input 0.
    subgraph cluster_subgraph_4_in_0 {
        label = "";
        interface_4_in_0x55ef9e30f530 [label="N", shape=none];
        interface_4_in_0x55efa1d81f90 [label="C_in", shape=none];
        interface_4_in_0x55efa1d54aa8 [label="H", shape=none];
        interface_4_in_0x55efa1d54b28 [label="H", shape=none];
    }
    {
        rank = same;
        interface_4_in_0x55ef9e30f530;
        interface_4_in_0x55efa1d81f90;
        interface_4_in_0x55efa1d54aa8;
        interface_4_in_0x55efa1d54b28;
    }
    // Op's.
    op_0x55efa1d54b00 [label="Unfold"];
    op_0x55efa1d81f50 [label="Split"];
    // Dimension's.
    interface_4_in_0x55ef9e30f530 -> interface_4_out_0x55ef9e30f530 [label="N"];
    op_0x55efa1d54b00 -> interface_4_out_0x55ef9e30f5a8 [label="H"];
    op_0x55efa1d81f50 -> interface_4_out_0x55efa1d445b0 [label="g^-1*s^-1*C_in"];
    op_0x55efa1d81f50 -> interface_4_out_0x55efa1d44790 [label="g*s"];
    op_0x55efa1d54b00 -> interface_4_out_0x55efa1d44830 [label="k_1"];
    interface_4_in_0x55efa1d54aa8 -> interface_4_out_0x55efa1d54aa8 [label="H"];
    interface_4_in_0x55efa1d54b28 -> op_0x55efa1d54b00 [label="H"];
    interface_4_in_0x55efa1d81f90 -> op_0x55efa1d81f50 [label="C_in"];
}

// Input tensor.
subgraph cluster_subgraph_5 {
    label = "Input 0";
    interface_5_out_0x55ef9e30f530 [label="N", shape=none];
    interface_5_out_0x55efa1d81f90 [label="C_in", shape=none];
    interface_5_out_0x55efa1d54aa8 [label="H", shape=none];
    interface_5_out_0x55efa1d54b28 [label="H", shape=none];
}

interface_5_out_0x55ef9e30f530 -> interface_4_in_0x55ef9e30f530;
interface_5_out_0x55efa1d81f90 -> interface_4_in_0x55efa1d81f90;
interface_5_out_0x55efa1d54aa8 -> interface_4_in_0x55efa1d54aa8;
interface_5_out_0x55efa1d54b28 -> interface_4_in_0x55efa1d54b28;

interface_4_out_0x55ef9e30f530 -> interface_3_in_0x55ef9e30f530;
interface_4_out_0x55efa1d44790 -> interface_3_in_0x55efa1d44790;
interface_4_out_0x55efa1d445b0 -> interface_3_in_0x55efa1d445b0;
interface_4_out_0x55efa1d54aa8 -> interface_3_in_0x55efa1d54aa8;
interface_4_out_0x55efa1d44830 -> interface_3_in_0x55efa1d44830;
interface_4_out_0x55ef9e30f5a8 -> interface_3_in_0x55ef9e30f5a8;

// Input tensor.
subgraph cluster_subgraph_6 {
    label = "Input 2";
    interface_6_out_0x55efa1d44758 [label="g^-1*C_out", shape=none];
    interface_6_out_0x55efa1d447a8 [label="g*s", shape=none];
    interface_6_out_0x55efa1d44848 [label="k_1", shape=none];
}

interface_6_out_0x55efa1d44758 -> interface_3_in_0x55efa1d44758;
interface_6_out_0x55efa1d447a8 -> interface_3_in_0x55efa1d447a8;
interface_6_out_0x55efa1d44848 -> interface_3_in_0x55efa1d44848;

interface_3_out_0x55ef9e30f530 -> interface_2_in_0x55ef9e30f530;
interface_3_out_0x55efa1d46878 -> interface_2_in_0x55efa1d46878;
interface_3_out_0x55efa1d445b0 -> interface_2_in_0x55efa1d445b0;
interface_3_out_0x55efa1d54aa8 -> interface_2_in_0x55efa1d54aa8;
interface_3_out_0x55efa1d44650 -> interface_2_in_0x55efa1d44650;
interface_3_out_0x55ef9e30f5a8 -> interface_2_in_0x55ef9e30f5a8;

interface_2_out_0x55ef9e30f530 -> interface_1_in_0x55ef9e30f530;
interface_2_out_0x55efa1d46878 -> interface_1_in_0x55efa1d46878;
interface_2_out_0x55efa1d445b0 -> interface_1_in_0x55efa1d445b0;
interface_2_out_0x55efa1d444c0 -> interface_1_in_0x55efa1d444c0;
interface_2_out_0x55ef9e30f580 -> interface_1_in_0x55ef9e30f580;
interface_2_out_0x55efa1d44650 -> interface_1_in_0x55efa1d44650;
interface_2_out_0x55ef9e30f5a8 -> interface_1_in_0x55ef9e30f5a8;

// Input tensor.
subgraph cluster_subgraph_7 {
    label = "Input 1";
    interface_7_out_0x55efa1d446b8 [label="g", shape=none];
    interface_7_out_0x55efa1d445c8 [label="g^-1*s^-1*C_in", shape=none];
    interface_7_out_0x55efa1d444d8 [label="k_1", shape=none];
    interface_7_out_0x55efa1d44668 [label="k_1", shape=none];
}

interface_7_out_0x55efa1d446b8 -> interface_1_in_0x55efa1d446b8;
interface_7_out_0x55efa1d445c8 -> interface_1_in_0x55efa1d445c8;
interface_7_out_0x55efa1d444d8 -> interface_1_in_0x55efa1d444d8;
interface_7_out_0x55efa1d44668 -> interface_1_in_0x55efa1d44668;

interface_1_out_0x55ef9e30f530 -> interface_0_in_0x55ef9e30f530;
interface_1_out_0x55efa1d46860 -> interface_0_in_0x55efa1d46860;
interface_1_out_0x55efa1d46878 -> interface_0_in_0x55efa1d46878;
interface_1_out_0x55ef9e30f580 -> interface_0_in_0x55ef9e30f580;
interface_1_out_0x55ef9e30f5a8 -> interface_0_in_0x55ef9e30f5a8;

{
    rank = same;
    interface_5_out_0x55ef9e30f530;
    interface_5_out_0x55efa1d81f90;
    interface_5_out_0x55efa1d54aa8;
    interface_5_out_0x55efa1d54b28;
    interface_7_out_0x55efa1d446b8;
    interface_7_out_0x55efa1d445c8;
    interface_7_out_0x55efa1d444d8;
    interface_7_out_0x55efa1d44668;
    interface_6_out_0x55efa1d44758;
    interface_6_out_0x55efa1d447a8;
    interface_6_out_0x55efa1d44848;
}
subgraph cluster_subgraph_output {
    label = "Output";
    interface_8_in_0x55ef9e30f530 [label="N", shape=none];
    interface_8_in_0x55ef9e30f558 [label="C_out", shape=none];
    interface_8_in_0x55ef9e30f580 [label="H", shape=none];
    interface_8_in_0x55ef9e30f5a8 [label="H", shape=none];
}
interface_0_out_0x55ef9e30f530 -> interface_8_in_0x55ef9e30f530;
interface_0_out_0x55ef9e30f558 -> interface_8_in_0x55ef9e30f558;
interface_0_out_0x55ef9e30f580 -> interface_8_in_0x55ef9e30f580;
interface_0_out_0x55ef9e30f5a8 -> interface_8_in_0x55ef9e30f5a8;

}

"""
class kernel_generated_0(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([32, 2, 3, 3]),
			torch.randn([4, 64, 3]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]
		in_2 = self.weights[1]

		# No contraction needed.
		t_3 = in_0

		# [C_in]@Split7156f2737a83a060 -> [g*s]@Sharedc15ce1c9326f917, [g^-1*s^-1*C_in]@Share77b21cfebfb4fc10
		t_3 = torch.reshape(t_3, (1, 64, 2, 56, 56, ))

		# [H]@Unfold90ae9d8acef524e0 -> [H]@Iteratorb0a1def4ad5784ec, [k_1]@Share63a88e0da5dce9dc
		t_3 = torch.reshape(t_3, (1, 7168, 56, 1, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (1, 64, 2, 56, 3, 56, ))

		# Perform contraction.
		t_4 = torch.einsum("ljnokm, ijk -> linokm", t_3, in_2)

		# No contraction needed.
		t_5 = t_4

		# [H]@Unfold4d77c1e3da5bca44 -> [H]@Iterator96123ba3184da39c, [k_1]@Share26cfa48d169008e4
		t_5 = torch.reshape(t_5, (1, 8, 56, 168, ))
		t_5 = torch.nn.functional.unfold(t_5, (3, 1, ), padding=(1, 0, ))
		t_5 = torch.reshape(t_5, (1, 4, 2, 3, 56, 3, 56, ))

		# Perform contraction.
		t_6 = torch.einsum("mpjinko, ljik -> mlpno", t_5, in_1)

		# No contraction needed.
		t_7 = t_6

		# [g]@Merge402ce7fe20a0a5fb, [g^-1*C_out]@Merge402ce7fe20a0a5f8 -> [C_out]@Iteratorc7f8eb87a5a0a9e0
		t_7 = torch.reshape(t_7, (1, 128, 56, 56, ))

		# No need to crop the output tensor.
		y = t_7

		return y

class kernel_generated_1(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([32, 4, 3, 3]),
			torch.randn([8, 64, 3]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]
		in_2 = self.weights[1]

		# No contraction needed.
		t_3 = in_0

		# [C_in]@Split7156f2737a83a060 -> [g*s]@Sharedc15ce1c9326f917, [g^-1*s^-1*C_in]@Share77b21cfebfb4fc10
		t_3 = torch.reshape(t_3, (1, 64, 4, 28, 28, ))

		# [H]@Unfold90ae9d8acef524e0 -> [H]@Iteratorb0a1def4ad5784ec, [k_1]@Share63a88e0da5dce9dc
		t_3 = torch.reshape(t_3, (1, 7168, 28, 1, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (1, 64, 4, 28, 3, 28, ))

		# Perform contraction.
		t_4 = torch.einsum("ljnokm, ijk -> linokm", t_3, in_2)

		# No contraction needed.
		t_5 = t_4

		# [H]@Unfold4d77c1e3da5bca44 -> [H]@Iterator96123ba3184da39c, [k_1]@Share26cfa48d169008e4
		t_5 = torch.reshape(t_5, (1, 32, 28, 84, ))
		t_5 = torch.nn.functional.unfold(t_5, (3, 1, ), padding=(1, 0, ))
		t_5 = torch.reshape(t_5, (1, 8, 4, 3, 28, 3, 28, ))

		# Perform contraction.
		t_6 = torch.einsum("mpjinko, ljik -> mlpno", t_5, in_1)

		# No contraction needed.
		t_7 = t_6

		# [g]@Merge402ce7fe20a0a5fb, [g^-1*C_out]@Merge402ce7fe20a0a5f8 -> [C_out]@Iteratorc7f8eb87a5a0a9e0
		t_7 = torch.reshape(t_7, (1, 256, 28, 28, ))

		# No need to crop the output tensor.
		y = t_7

		return y

class kernel_generated_2(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([32, 8, 3, 3]),
			torch.randn([16, 64, 3]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]
		in_2 = self.weights[1]

		# No contraction needed.
		t_3 = in_0

		# [C_in]@Split7156f2737a83a060 -> [g*s]@Sharedc15ce1c9326f917, [g^-1*s^-1*C_in]@Share77b21cfebfb4fc10
		t_3 = torch.reshape(t_3, (1, 64, 8, 14, 14, ))

		# [H]@Unfold90ae9d8acef524e0 -> [H]@Iteratorb0a1def4ad5784ec, [k_1]@Share63a88e0da5dce9dc
		t_3 = torch.reshape(t_3, (1, 7168, 14, 1, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (1, 64, 8, 14, 3, 14, ))

		# Perform contraction.
		t_4 = torch.einsum("ljnokm, ijk -> linokm", t_3, in_2)

		# No contraction needed.
		t_5 = t_4

		# [H]@Unfold4d77c1e3da5bca44 -> [H]@Iterator96123ba3184da39c, [k_1]@Share26cfa48d169008e4
		t_5 = torch.reshape(t_5, (1, 128, 14, 42, ))
		t_5 = torch.nn.functional.unfold(t_5, (3, 1, ), padding=(1, 0, ))
		t_5 = torch.reshape(t_5, (1, 16, 8, 3, 14, 3, 14, ))

		# Perform contraction.
		t_6 = torch.einsum("mpjinko, ljik -> mlpno", t_5, in_1)

		# No contraction needed.
		t_7 = t_6

		# [g]@Merge402ce7fe20a0a5fb, [g^-1*C_out]@Merge402ce7fe20a0a5f8 -> [C_out]@Iteratorc7f8eb87a5a0a9e0
		t_7 = torch.reshape(t_7, (1, 512, 14, 14, ))

		# No need to crop the output tensor.
		y = t_7

		return y

class kernel_generated_3(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([32, 16, 3, 3]),
			torch.randn([32, 64, 3]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]
		in_2 = self.weights[1]

		# No contraction needed.
		t_3 = in_0

		# [C_in]@Split7156f2737a83a060 -> [g*s]@Sharedc15ce1c9326f917, [g^-1*s^-1*C_in]@Share77b21cfebfb4fc10
		t_3 = torch.reshape(t_3, (1, 64, 16, 7, 7, ))

		# [H]@Unfold90ae9d8acef524e0 -> [H]@Iteratorb0a1def4ad5784ec, [k_1]@Share63a88e0da5dce9dc
		t_3 = torch.reshape(t_3, (1, 7168, 7, 1, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (1, 64, 16, 7, 3, 7, ))

		# Perform contraction.
		t_4 = torch.einsum("ljnokm, ijk -> linokm", t_3, in_2)

		# No contraction needed.
		t_5 = t_4

		# [H]@Unfold4d77c1e3da5bca44 -> [H]@Iterator96123ba3184da39c, [k_1]@Share26cfa48d169008e4
		t_5 = torch.reshape(t_5, (1, 512, 7, 21, ))
		t_5 = torch.nn.functional.unfold(t_5, (3, 1, ), padding=(1, 0, ))
		t_5 = torch.reshape(t_5, (1, 32, 16, 3, 7, 3, 7, ))

		# Perform contraction.
		t_6 = torch.einsum("mpjinko, ljik -> mlpno", t_5, in_1)

		# No contraction needed.
		t_7 = t_6

		# [g]@Merge402ce7fe20a0a5fb, [g^-1*C_out]@Merge402ce7fe20a0a5f8 -> [C_out]@Iteratorc7f8eb87a5a0a9e0
		t_7 = torch.reshape(t_7, (1, 1024, 7, 7, ))

		# No need to crop the output tensor.
		y = t_7

		return y

