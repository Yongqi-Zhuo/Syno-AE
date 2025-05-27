import torch
import random
"""
digraph kernel_preview {
newrank = true;

// Stage tensor.
subgraph cluster_subgraph_0 {
    label = "Subgraph 0";
    // Reductions.
    reduce_0x7f51b0001928 [label="Sum", shape=box];
    reduce_0x7f51b0001ab0 [label="Sum", shape=box];
    reduce_0x7f51b0001a98 [label="Sum", shape=box];
    reduce_0x7f51b0009088 [label="Sum", shape=box];
    // Output.
    subgraph cluster_subgraph_0_out {
        label = "";
        interface_0_out_0x5590c9c880c0 [label="N", shape=none];
        interface_0_out_0x5590c9c880e8 [label="C_out", shape=none];
        interface_0_out_0x5590c9c88110 [label="H", shape=none];
        interface_0_out_0x5590c9c88138 [label="H", shape=none];
    }
    {
        rank = same;
        reduce_0x7f51b0001928;
        reduce_0x7f51b0001ab0;
        reduce_0x7f51b0001a98;
        reduce_0x7f51b0009088;
        interface_0_out_0x5590c9c880c0;
        interface_0_out_0x5590c9c880e8;
        interface_0_out_0x5590c9c88110;
        interface_0_out_0x5590c9c88138;
    }
    // Input 0.
    subgraph cluster_subgraph_0_in_0 {
        label = "";
        interface_0_in_0x5590c9c880c0 [label="N", shape=none];
        interface_0_in_0x5590da8a77c0 [label="g", shape=none];
        interface_0_in_0x5590da8a7860 [label="k_1", shape=none];
        interface_0_in_0x5590c9c88110 [label="H", shape=none];
        interface_0_in_0x5590da8a7590 [label="k_1", shape=none];
        interface_0_in_0x5590c9c88138 [label="H", shape=none];
        interface_0_in_0x5590da8a7810 [label="g^-1*s^-1*C_out", shape=none];
    }
    // Input 1.
    subgraph cluster_subgraph_0_in_1 {
        label = "";
        interface_0_in_0x5590da8a74b8 [label="C_out", shape=none];
        interface_0_in_0x5590da8a77d8 [label="g", shape=none];
        interface_0_in_0x5590da8a7878 [label="k_1", shape=none];
        interface_0_in_0x5590da8a75a8 [label="k_1", shape=none];
        interface_0_in_0x5590da8a7828 [label="g^-1*s^-1*C_out", shape=none];
    }
    {
        rank = same;
        interface_0_in_0x5590c9c880c0;
        interface_0_in_0x5590da8a77c0;
        interface_0_in_0x5590da8a7860;
        interface_0_in_0x5590c9c88110;
        interface_0_in_0x5590da8a7590;
        interface_0_in_0x5590c9c88138;
        interface_0_in_0x5590da8a7810;
        interface_0_in_0x5590da8a74b8;
        interface_0_in_0x5590da8a77d8;
        interface_0_in_0x5590da8a7878;
        interface_0_in_0x5590da8a75a8;
        interface_0_in_0x5590da8a7828;
    }
    // Op's.
    op_0x5590da8a7480 [label="Share"];
    op_0x5590da8a7570 [label="Share"];
    op_0x5590da8a77a0 [label="Share"];
    op_0x5590da8a77f0 [label="Share"];
    op_0x5590da8a7840 [label="Share"];
    op_0x5590da8a7a38 [label="Expand"];
    // Dimension's.
    interface_0_in_0x5590c9c880c0 -> interface_0_out_0x5590c9c880c0 [label="N"];
    op_0x5590da8a7480 -> interface_0_out_0x5590c9c880e8 [label="C_out"];
    interface_0_in_0x5590c9c88110 -> interface_0_out_0x5590c9c88110 [label="H"];
    interface_0_in_0x5590c9c88138 -> interface_0_out_0x5590c9c88138 [label="H"];
    op_0x5590da8a7a38 -> op_0x5590da8a7480 [label="C_out"];
    interface_0_in_0x5590da8a74b8 -> op_0x5590da8a7480 [label="C_out"];
    interface_0_in_0x5590da8a7590 -> op_0x5590da8a7570 [label="k_1"];
    interface_0_in_0x5590da8a75a8 -> op_0x5590da8a7570 [label="k_1"];
    interface_0_in_0x5590da8a77c0 -> op_0x5590da8a77a0 [label="g"];
    interface_0_in_0x5590da8a77d8 -> op_0x5590da8a77a0 [label="g"];
    interface_0_in_0x5590da8a7810 -> op_0x5590da8a77f0 [label="g^-1*s^-1*C_out"];
    interface_0_in_0x5590da8a7828 -> op_0x5590da8a77f0 [label="g^-1*s^-1*C_out"];
    interface_0_in_0x5590da8a7860 -> op_0x5590da8a7840 [label="k_1"];
    interface_0_in_0x5590da8a7878 -> op_0x5590da8a7840 [label="k_1"];
    op_0x5590da8a77a0 -> reduce_0x7f51b0001928 [label="g"];
    op_0x5590da8a7570 -> reduce_0x7f51b0001a98 [label="k_1"];
    op_0x5590da8a7840 -> reduce_0x7f51b0001ab0 [label="k_1"];
    op_0x5590da8a77f0 -> reduce_0x7f51b0009088 [label="g^-1*s^-1*C_out"];
}

// Stage tensor.
subgraph cluster_subgraph_1 {
    label = "Subgraph 1";
    // Reductions.
    // Output.
    subgraph cluster_subgraph_1_out {
        label = "";
        interface_1_out_0x5590c9c880c0 [label="N", shape=none];
        interface_1_out_0x5590da8a77c0 [label="g", shape=none];
        interface_1_out_0x5590da8a7860 [label="k_1", shape=none];
        interface_1_out_0x5590c9c88110 [label="H", shape=none];
        interface_1_out_0x5590da8a7590 [label="k_1", shape=none];
        interface_1_out_0x5590c9c88138 [label="H", shape=none];
        interface_1_out_0x5590da8a7810 [label="g^-1*s^-1*C_out", shape=none];
    }
    {
        rank = same;
        interface_1_out_0x5590c9c880c0;
        interface_1_out_0x5590da8a77c0;
        interface_1_out_0x5590da8a7860;
        interface_1_out_0x5590c9c88110;
        interface_1_out_0x5590da8a7590;
        interface_1_out_0x5590c9c88138;
        interface_1_out_0x5590da8a7810;
    }
    // Input 0.
    subgraph cluster_subgraph_1_in_0 {
        label = "";
        interface_1_in_0x5590c9c880c0 [label="N", shape=none];
        interface_1_in_0x5590da8a77c0 [label="g", shape=none];
        interface_1_in_0x5590da8a7860 [label="k_1", shape=none];
        interface_1_in_0x5590c9c88110 [label="H", shape=none];
        interface_1_in_0x5590da8a9760 [label="H", shape=none];
        interface_1_in_0x5590da8a7810 [label="g^-1*s^-1*C_out", shape=none];
    }
    {
        rank = same;
        interface_1_in_0x5590c9c880c0;
        interface_1_in_0x5590da8a77c0;
        interface_1_in_0x5590da8a7860;
        interface_1_in_0x5590c9c88110;
        interface_1_in_0x5590da8a9760;
        interface_1_in_0x5590da8a7810;
    }
    // Op's.
    op_0x5590da8a9740 [label="Shift"];
    op_0x5590da8bf000 [label="Unfold"];
    // Dimension's.
    interface_1_in_0x5590c9c880c0 -> interface_1_out_0x5590c9c880c0 [label="N"];
    interface_1_in_0x5590c9c88110 -> interface_1_out_0x5590c9c88110 [label="H"];
    op_0x5590da8bf000 -> interface_1_out_0x5590c9c88138 [label="H"];
    op_0x5590da8bf000 -> interface_1_out_0x5590da8a7590 [label="k_1"];
    interface_1_in_0x5590da8a77c0 -> interface_1_out_0x5590da8a77c0 [label="g"];
    interface_1_in_0x5590da8a7810 -> interface_1_out_0x5590da8a7810 [label="g^-1*s^-1*C_out"];
    interface_1_in_0x5590da8a7860 -> interface_1_out_0x5590da8a7860 [label="k_1"];
    interface_1_in_0x5590da8a9760 -> op_0x5590da8a9740 [label="H"];
    op_0x5590da8a9740 -> op_0x5590da8bf000 [label="H"];
}

// Stage tensor.
subgraph cluster_subgraph_2 {
    label = "Subgraph 2";
    // Reductions.
    reduce_0x7f51b0005990 [label="Sum", shape=box];
    // Output.
    subgraph cluster_subgraph_2_out {
        label = "";
        interface_2_out_0x5590c9c880c0 [label="N", shape=none];
        interface_2_out_0x5590da8a77c0 [label="g", shape=none];
        interface_2_out_0x5590da8a7860 [label="k_1", shape=none];
        interface_2_out_0x5590c9c88110 [label="H", shape=none];
        interface_2_out_0x5590da8a9760 [label="H", shape=none];
        interface_2_out_0x5590da8a7810 [label="g^-1*s^-1*C_out", shape=none];
    }
    {
        rank = same;
        reduce_0x7f51b0005990;
        interface_2_out_0x5590c9c880c0;
        interface_2_out_0x5590da8a77c0;
        interface_2_out_0x5590da8a7860;
        interface_2_out_0x5590c9c88110;
        interface_2_out_0x5590da8a9760;
        interface_2_out_0x5590da8a7810;
    }
    // Input 0.
    subgraph cluster_subgraph_2_in_0 {
        label = "";
        interface_2_in_0x5590c9c880c0 [label="N", shape=none];
        interface_2_in_0x5590da8d35d0 [label="C_in", shape=none];
        interface_2_in_0x5590da8a7860 [label="k_1", shape=none];
        interface_2_in_0x5590c9c88110 [label="H", shape=none];
        interface_2_in_0x5590da8a9760 [label="H", shape=none];
        interface_2_in_0x5590da8a7810 [label="g^-1*s^-1*C_out", shape=none];
    }
    {
        rank = same;
        interface_2_in_0x5590c9c880c0;
        interface_2_in_0x5590da8d35d0;
        interface_2_in_0x5590da8a7860;
        interface_2_in_0x5590c9c88110;
        interface_2_in_0x5590da8a9760;
        interface_2_in_0x5590da8a7810;
    }
    // Op's.
    op_0x5590da8d3590 [label="Split"];
    // Dimension's.
    interface_2_in_0x5590c9c880c0 -> interface_2_out_0x5590c9c880c0 [label="N"];
    interface_2_in_0x5590c9c88110 -> interface_2_out_0x5590c9c88110 [label="H"];
    op_0x5590da8d3590 -> interface_2_out_0x5590da8a77c0 [label="g"];
    interface_2_in_0x5590da8a7810 -> interface_2_out_0x5590da8a7810 [label="g^-1*s^-1*C_out"];
    interface_2_in_0x5590da8a7860 -> interface_2_out_0x5590da8a7860 [label="k_1"];
    interface_2_in_0x5590da8a9760 -> interface_2_out_0x5590da8a9760 [label="H"];
    interface_2_in_0x5590da8d35d0 -> op_0x5590da8d3590 [label="C_in"];
    op_0x5590da8d3590 -> reduce_0x7f51b0005990 [label="g^-1*C_in"];
}

// Stage tensor.
subgraph cluster_subgraph_3 {
    label = "Subgraph 3";
    // Reductions.
    // Output.
    subgraph cluster_subgraph_3_out {
        label = "";
        interface_3_out_0x5590c9c880c0 [label="N", shape=none];
        interface_3_out_0x5590da8d35d0 [label="C_in", shape=none];
        interface_3_out_0x5590da8a7860 [label="k_1", shape=none];
        interface_3_out_0x5590c9c88110 [label="H", shape=none];
        interface_3_out_0x5590da8a9760 [label="H", shape=none];
        interface_3_out_0x5590da8a7810 [label="g^-1*s^-1*C_out", shape=none];
    }
    {
        rank = same;
        interface_3_out_0x5590c9c880c0;
        interface_3_out_0x5590da8d35d0;
        interface_3_out_0x5590da8a7860;
        interface_3_out_0x5590c9c88110;
        interface_3_out_0x5590da8a9760;
        interface_3_out_0x5590da8a7810;
    }
    // Input 0.
    subgraph cluster_subgraph_3_in_0 {
        label = "";
        interface_3_in_0x5590c9c880c0 [label="N", shape=none];
        interface_3_in_0x5590da8f9c10 [label="C_in", shape=none];
        interface_3_in_0x5590da8f9c60 [label="k_1", shape=none];
        interface_3_in_0x5590c9c88110 [label="H", shape=none];
        interface_3_in_0x5590da8a9760 [label="H", shape=none];
    }
    // Input 1.
    subgraph cluster_subgraph_3_in_1 {
        label = "";
        interface_3_in_0x5590da8f9c28 [label="C_in", shape=none];
        interface_3_in_0x5590da8f9c78 [label="k_1", shape=none];
        interface_3_in_0x5590da8a78c8 [label="g^-1*s^-1*C_out", shape=none];
    }
    {
        rank = same;
        interface_3_in_0x5590c9c880c0;
        interface_3_in_0x5590da8f9c10;
        interface_3_in_0x5590da8f9c60;
        interface_3_in_0x5590c9c88110;
        interface_3_in_0x5590da8a9760;
        interface_3_in_0x5590da8f9c28;
        interface_3_in_0x5590da8f9c78;
        interface_3_in_0x5590da8a78c8;
    }
    // Op's.
    op_0x5590da8a7890 [label="Share"];
    op_0x5590da8a7ab8 [label="Expand"];
    op_0x5590da8f9bf0 [label="Share"];
    op_0x5590da8f9c40 [label="Share"];
    // Dimension's.
    interface_3_in_0x5590c9c880c0 -> interface_3_out_0x5590c9c880c0 [label="N"];
    interface_3_in_0x5590c9c88110 -> interface_3_out_0x5590c9c88110 [label="H"];
    op_0x5590da8a7890 -> interface_3_out_0x5590da8a7810 [label="g^-1*s^-1*C_out"];
    op_0x5590da8f9c40 -> interface_3_out_0x5590da8a7860 [label="k_1"];
    op_0x5590da8a7ab8 -> op_0x5590da8a7890 [label="g^-1*s^-1*C_out"];
    interface_3_in_0x5590da8a78c8 -> op_0x5590da8a7890 [label="g^-1*s^-1*C_out"];
    interface_3_in_0x5590da8a9760 -> interface_3_out_0x5590da8a9760 [label="H"];
    op_0x5590da8f9bf0 -> interface_3_out_0x5590da8d35d0 [label="C_in"];
    interface_3_in_0x5590da8f9c10 -> op_0x5590da8f9bf0 [label="C_in"];
    interface_3_in_0x5590da8f9c28 -> op_0x5590da8f9bf0 [label="C_in"];
    interface_3_in_0x5590da8f9c60 -> op_0x5590da8f9c40 [label="k_1"];
    interface_3_in_0x5590da8f9c78 -> op_0x5590da8f9c40 [label="k_1"];
}

// Stage tensor.
subgraph cluster_subgraph_4 {
    label = "Subgraph 4";
    // Reductions.
    // Output.
    subgraph cluster_subgraph_4_out {
        label = "";
        interface_4_out_0x5590c9c880c0 [label="N", shape=none];
        interface_4_out_0x5590da8f9c10 [label="C_in", shape=none];
        interface_4_out_0x5590da8f9c60 [label="k_1", shape=none];
        interface_4_out_0x5590c9c88110 [label="H", shape=none];
        interface_4_out_0x5590da8a9760 [label="H", shape=none];
    }
    {
        rank = same;
        interface_4_out_0x5590c9c880c0;
        interface_4_out_0x5590da8f9c10;
        interface_4_out_0x5590da8f9c60;
        interface_4_out_0x5590c9c88110;
        interface_4_out_0x5590da8a9760;
    }
    // Input 0.
    subgraph cluster_subgraph_4_in_0 {
        label = "";
        interface_4_in_0x5590c9c880c0 [label="N", shape=none];
        interface_4_in_0x5590da8f9c10 [label="C_in", shape=none];
        interface_4_in_0x5590da8a9790 [label="H", shape=none];
        interface_4_in_0x5590da8a9760 [label="H", shape=none];
    }
    {
        rank = same;
        interface_4_in_0x5590c9c880c0;
        interface_4_in_0x5590da8f9c10;
        interface_4_in_0x5590da8a9790;
        interface_4_in_0x5590da8a9760;
    }
    // Op's.
    op_0x5590da8a9770 [label="Shift"];
    op_0x5590da8bf200 [label="Unfold"];
    // Dimension's.
    interface_4_in_0x5590c9c880c0 -> interface_4_out_0x5590c9c880c0 [label="N"];
    op_0x5590da8bf200 -> interface_4_out_0x5590c9c88110 [label="H"];
    interface_4_in_0x5590da8a9760 -> interface_4_out_0x5590da8a9760 [label="H"];
    interface_4_in_0x5590da8a9790 -> op_0x5590da8a9770 [label="H"];
    op_0x5590da8a9770 -> op_0x5590da8bf200 [label="H"];
    interface_4_in_0x5590da8f9c10 -> interface_4_out_0x5590da8f9c10 [label="C_in"];
    op_0x5590da8bf200 -> interface_4_out_0x5590da8f9c60 [label="k_1"];
}

// Input tensor.
subgraph cluster_subgraph_5 {
    label = "Input 0";
    interface_5_out_0x5590c9c880c0 [label="N", shape=none];
    interface_5_out_0x5590da8f9c10 [label="C_in", shape=none];
    interface_5_out_0x5590da8a9790 [label="H", shape=none];
    interface_5_out_0x5590da8a9760 [label="H", shape=none];
}

interface_5_out_0x5590c9c880c0 -> interface_4_in_0x5590c9c880c0;
interface_5_out_0x5590da8f9c10 -> interface_4_in_0x5590da8f9c10;
interface_5_out_0x5590da8a9790 -> interface_4_in_0x5590da8a9790;
interface_5_out_0x5590da8a9760 -> interface_4_in_0x5590da8a9760;

interface_4_out_0x5590c9c880c0 -> interface_3_in_0x5590c9c880c0;
interface_4_out_0x5590da8f9c10 -> interface_3_in_0x5590da8f9c10;
interface_4_out_0x5590da8f9c60 -> interface_3_in_0x5590da8f9c60;
interface_4_out_0x5590c9c88110 -> interface_3_in_0x5590c9c88110;
interface_4_out_0x5590da8a9760 -> interface_3_in_0x5590da8a9760;

// Input tensor.
subgraph cluster_subgraph_6 {
    label = "Input 2";
    interface_6_out_0x5590da8f9c28 [label="C_in", shape=none];
    interface_6_out_0x5590da8f9c78 [label="k_1", shape=none];
    interface_6_out_0x5590da8a78c8 [label="g^-1*s^-1*C_out", shape=none];
}

interface_6_out_0x5590da8f9c28 -> interface_3_in_0x5590da8f9c28;
interface_6_out_0x5590da8f9c78 -> interface_3_in_0x5590da8f9c78;
interface_6_out_0x5590da8a78c8 -> interface_3_in_0x5590da8a78c8;

interface_3_out_0x5590c9c880c0 -> interface_2_in_0x5590c9c880c0;
interface_3_out_0x5590da8d35d0 -> interface_2_in_0x5590da8d35d0;
interface_3_out_0x5590da8a7860 -> interface_2_in_0x5590da8a7860;
interface_3_out_0x5590c9c88110 -> interface_2_in_0x5590c9c88110;
interface_3_out_0x5590da8a9760 -> interface_2_in_0x5590da8a9760;
interface_3_out_0x5590da8a7810 -> interface_2_in_0x5590da8a7810;

interface_2_out_0x5590c9c880c0 -> interface_1_in_0x5590c9c880c0;
interface_2_out_0x5590da8a77c0 -> interface_1_in_0x5590da8a77c0;
interface_2_out_0x5590da8a7860 -> interface_1_in_0x5590da8a7860;
interface_2_out_0x5590c9c88110 -> interface_1_in_0x5590c9c88110;
interface_2_out_0x5590da8a9760 -> interface_1_in_0x5590da8a9760;
interface_2_out_0x5590da8a7810 -> interface_1_in_0x5590da8a7810;

interface_1_out_0x5590c9c880c0 -> interface_0_in_0x5590c9c880c0;
interface_1_out_0x5590da8a77c0 -> interface_0_in_0x5590da8a77c0;
interface_1_out_0x5590da8a7860 -> interface_0_in_0x5590da8a7860;
interface_1_out_0x5590c9c88110 -> interface_0_in_0x5590c9c88110;
interface_1_out_0x5590da8a7590 -> interface_0_in_0x5590da8a7590;
interface_1_out_0x5590c9c88138 -> interface_0_in_0x5590c9c88138;
interface_1_out_0x5590da8a7810 -> interface_0_in_0x5590da8a7810;

// Input tensor.
subgraph cluster_subgraph_7 {
    label = "Input 1";
    interface_7_out_0x5590da8a74b8 [label="C_out", shape=none];
    interface_7_out_0x5590da8a77d8 [label="g", shape=none];
    interface_7_out_0x5590da8a7878 [label="k_1", shape=none];
    interface_7_out_0x5590da8a75a8 [label="k_1", shape=none];
    interface_7_out_0x5590da8a7828 [label="g^-1*s^-1*C_out", shape=none];
}

interface_7_out_0x5590da8a74b8 -> interface_0_in_0x5590da8a74b8;
interface_7_out_0x5590da8a77d8 -> interface_0_in_0x5590da8a77d8;
interface_7_out_0x5590da8a7878 -> interface_0_in_0x5590da8a7878;
interface_7_out_0x5590da8a75a8 -> interface_0_in_0x5590da8a75a8;
interface_7_out_0x5590da8a7828 -> interface_0_in_0x5590da8a7828;

{
    rank = same;
    interface_5_out_0x5590c9c880c0;
    interface_5_out_0x5590da8f9c10;
    interface_5_out_0x5590da8a9790;
    interface_5_out_0x5590da8a9760;
    interface_7_out_0x5590da8a74b8;
    interface_7_out_0x5590da8a77d8;
    interface_7_out_0x5590da8a7878;
    interface_7_out_0x5590da8a75a8;
    interface_7_out_0x5590da8a7828;
    interface_6_out_0x5590da8f9c28;
    interface_6_out_0x5590da8f9c78;
    interface_6_out_0x5590da8a78c8;
}
subgraph cluster_subgraph_output {
    label = "Output";
    interface_8_in_0x5590c9c880c0 [label="N", shape=none];
    interface_8_in_0x5590c9c880e8 [label="C_out", shape=none];
    interface_8_in_0x5590c9c88110 [label="H", shape=none];
    interface_8_in_0x5590c9c88138 [label="H", shape=none];
}
interface_0_out_0x5590c9c880c0 -> interface_8_in_0x5590c9c880c0;
interface_0_out_0x5590c9c880e8 -> interface_8_in_0x5590c9c880e8;
interface_0_out_0x5590c9c88110 -> interface_8_in_0x5590c9c88110;
interface_0_out_0x5590c9c88138 -> interface_8_in_0x5590c9c88138;

}

"""
class kernel_generated_0(torch.nn.Module):
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

		# [H]@Shift05348c1f59ed8f45 -> [H]@Unfoldd282eed81682d1c4
		t_3 = torch.roll(t_3, self.shift_direction, 2)

		# [H]@Unfoldd282eed81682d1c4 -> [H]@Iterator96123ba3184da39c, [k_1]@Share63a88e0da5dce9dc
		t_3 = torch.reshape(t_3, (1, 64, 56, 56, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (1, 64, 3, 56, 56, ))

		# Perform contraction.
		t_4 = torch.einsum("ljkmn, jki -> ljkmni", t_3, in_2)

		# No contraction needed.
		t_5 = t_4

		# [C_in]@Splitc2d52f3525ba6cc4 -> [g]@Sharec7a8ce455b828537, [g^-1*C_in]@Reduceef9903cafc29eea1
		t_5 = torch.reshape(t_5, (1, 32, 2, 3, 56, 56, 1, ))

		# [g^-1*C_in]@Reduce
		t_5 = torch.sum(t_5, dim=(2, ))

		# No contraction needed.
		t_6 = t_5

		# [H]@Shiftdbd5b2e652804221 -> [H]@Unfold0063bc810b9e1e60
		t_6 = torch.roll(t_6, self.shift_direction, 4)

		# [H]@Unfold0063bc810b9e1e60 -> [H]@Iteratorb0a1def4ad5784ec, [k_1]@Share26cfa48d169008e4
		t_6 = torch.reshape(t_6, (1, 5376, 56, 1, ))
		t_6 = torch.nn.functional.unfold(t_6, (3, 1, ), padding=(1, 0, ))
		t_6 = torch.reshape(t_6, (1, 32, 3, 56, 3, 56, 1, ))

		# Perform contraction.
		t_7 = torch.einsum("nkmojpl, ikmjl -> niop", t_6, in_1)

		# No need to crop the output tensor.
		y = t_7

		return y

class kernel_generated_1(torch.nn.Module):
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

		# [H]@Shift05348c1f59ed8f45 -> [H]@Unfoldd282eed81682d1c4
		t_3 = torch.roll(t_3, self.shift_direction, 2)

		# [H]@Unfoldd282eed81682d1c4 -> [H]@Iterator96123ba3184da39c, [k_1]@Share63a88e0da5dce9dc
		t_3 = torch.reshape(t_3, (1, 64, 28, 28, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (1, 64, 3, 28, 28, ))

		# Perform contraction.
		t_4 = torch.einsum("ljkmn, jki -> ljkmni", t_3, in_2)

		# No contraction needed.
		t_5 = t_4

		# [C_in]@Splitc2d52f3525ba6cc4 -> [g]@Sharec7a8ce455b828537, [g^-1*C_in]@Reduceef9903cafc29eea1
		t_5 = torch.reshape(t_5, (1, 32, 2, 3, 28, 28, 2, ))

		# [g^-1*C_in]@Reduce
		t_5 = torch.sum(t_5, dim=(2, ))

		# No contraction needed.
		t_6 = t_5

		# [H]@Shiftdbd5b2e652804221 -> [H]@Unfold0063bc810b9e1e60
		t_6 = torch.roll(t_6, self.shift_direction, 4)

		# [H]@Unfold0063bc810b9e1e60 -> [H]@Iteratorb0a1def4ad5784ec, [k_1]@Share26cfa48d169008e4
		t_6 = torch.reshape(t_6, (1, 2688, 28, 2, ))
		t_6 = torch.nn.functional.unfold(t_6, (3, 1, ), padding=(1, 0, ))
		t_6 = torch.reshape(t_6, (1, 32, 3, 28, 3, 28, 2, ))

		# Perform contraction.
		t_7 = torch.einsum("nkmojpl, ikmjl -> niop", t_6, in_1)

		# No need to crop the output tensor.
		y = t_7

		return y

class kernel_generated_2(torch.nn.Module):
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

		# [H]@Shift05348c1f59ed8f45 -> [H]@Unfoldd282eed81682d1c4
		t_3 = torch.roll(t_3, self.shift_direction, 2)

		# [H]@Unfoldd282eed81682d1c4 -> [H]@Iterator96123ba3184da39c, [k_1]@Share63a88e0da5dce9dc
		t_3 = torch.reshape(t_3, (1, 128, 28, 28, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (1, 128, 3, 28, 28, ))

		# Perform contraction.
		t_4 = torch.einsum("ljkmn, jki -> ljkmni", t_3, in_2)

		# No contraction needed.
		t_5 = t_4

		# [C_in]@Splitc2d52f3525ba6cc4 -> [g]@Sharec7a8ce455b828537, [g^-1*C_in]@Reduceef9903cafc29eea1
		t_5 = torch.reshape(t_5, (1, 32, 4, 3, 28, 28, 2, ))

		# [g^-1*C_in]@Reduce
		t_5 = torch.sum(t_5, dim=(2, ))

		# No contraction needed.
		t_6 = t_5

		# [H]@Shiftdbd5b2e652804221 -> [H]@Unfold0063bc810b9e1e60
		t_6 = torch.roll(t_6, self.shift_direction, 4)

		# [H]@Unfold0063bc810b9e1e60 -> [H]@Iteratorb0a1def4ad5784ec, [k_1]@Share26cfa48d169008e4
		t_6 = torch.reshape(t_6, (1, 2688, 28, 2, ))
		t_6 = torch.nn.functional.unfold(t_6, (3, 1, ), padding=(1, 0, ))
		t_6 = torch.reshape(t_6, (1, 32, 3, 28, 3, 28, 2, ))

		# Perform contraction.
		t_7 = torch.einsum("nkmojpl, ikmjl -> niop", t_6, in_1)

		# No need to crop the output tensor.
		y = t_7

		return y

class kernel_generated_3(torch.nn.Module):
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

		# [H]@Shift05348c1f59ed8f45 -> [H]@Unfoldd282eed81682d1c4
		t_3 = torch.roll(t_3, self.shift_direction, 2)

		# [H]@Unfoldd282eed81682d1c4 -> [H]@Iterator96123ba3184da39c, [k_1]@Share63a88e0da5dce9dc
		t_3 = torch.reshape(t_3, (1, 128, 14, 14, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (1, 128, 3, 14, 14, ))

		# Perform contraction.
		t_4 = torch.einsum("ljkmn, jki -> ljkmni", t_3, in_2)

		# No contraction needed.
		t_5 = t_4

		# [C_in]@Splitc2d52f3525ba6cc4 -> [g]@Sharec7a8ce455b828537, [g^-1*C_in]@Reduceef9903cafc29eea1
		t_5 = torch.reshape(t_5, (1, 32, 4, 3, 14, 14, 4, ))

		# [g^-1*C_in]@Reduce
		t_5 = torch.sum(t_5, dim=(2, ))

		# No contraction needed.
		t_6 = t_5

		# [H]@Shiftdbd5b2e652804221 -> [H]@Unfold0063bc810b9e1e60
		t_6 = torch.roll(t_6, self.shift_direction, 4)

		# [H]@Unfold0063bc810b9e1e60 -> [H]@Iteratorb0a1def4ad5784ec, [k_1]@Share26cfa48d169008e4
		t_6 = torch.reshape(t_6, (1, 1344, 14, 4, ))
		t_6 = torch.nn.functional.unfold(t_6, (3, 1, ), padding=(1, 0, ))
		t_6 = torch.reshape(t_6, (1, 32, 3, 14, 3, 14, 4, ))

		# Perform contraction.
		t_7 = torch.einsum("nkmojpl, ikmjl -> niop", t_6, in_1)

		# No need to crop the output tensor.
		y = t_7

		return y

class kernel_generated_4(torch.nn.Module):
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

		# [H]@Shift05348c1f59ed8f45 -> [H]@Unfoldd282eed81682d1c4
		t_3 = torch.roll(t_3, self.shift_direction, 2)

		# [H]@Unfoldd282eed81682d1c4 -> [H]@Iterator96123ba3184da39c, [k_1]@Share63a88e0da5dce9dc
		t_3 = torch.reshape(t_3, (1, 256, 14, 14, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (1, 256, 3, 14, 14, ))

		# Perform contraction.
		t_4 = torch.einsum("ljkmn, jki -> ljkmni", t_3, in_2)

		# No contraction needed.
		t_5 = t_4

		# [C_in]@Splitc2d52f3525ba6cc4 -> [g]@Sharec7a8ce455b828537, [g^-1*C_in]@Reduceef9903cafc29eea1
		t_5 = torch.reshape(t_5, (1, 32, 8, 3, 14, 14, 4, ))

		# [g^-1*C_in]@Reduce
		t_5 = torch.sum(t_5, dim=(2, ))

		# No contraction needed.
		t_6 = t_5

		# [H]@Shiftdbd5b2e652804221 -> [H]@Unfold0063bc810b9e1e60
		t_6 = torch.roll(t_6, self.shift_direction, 4)

		# [H]@Unfold0063bc810b9e1e60 -> [H]@Iteratorb0a1def4ad5784ec, [k_1]@Share26cfa48d169008e4
		t_6 = torch.reshape(t_6, (1, 1344, 14, 4, ))
		t_6 = torch.nn.functional.unfold(t_6, (3, 1, ), padding=(1, 0, ))
		t_6 = torch.reshape(t_6, (1, 32, 3, 14, 3, 14, 4, ))

		# Perform contraction.
		t_7 = torch.einsum("nkmojpl, ikmjl -> niop", t_6, in_1)

		# No need to crop the output tensor.
		y = t_7

		return y

class kernel_generated_5(torch.nn.Module):
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

		# [H]@Shift05348c1f59ed8f45 -> [H]@Unfoldd282eed81682d1c4
		t_3 = torch.roll(t_3, self.shift_direction, 2)

		# [H]@Unfoldd282eed81682d1c4 -> [H]@Iterator96123ba3184da39c, [k_1]@Share63a88e0da5dce9dc
		t_3 = torch.reshape(t_3, (1, 256, 7, 7, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (1, 256, 3, 7, 7, ))

		# Perform contraction.
		t_4 = torch.einsum("ljkmn, jki -> ljkmni", t_3, in_2)

		# No contraction needed.
		t_5 = t_4

		# [C_in]@Splitc2d52f3525ba6cc4 -> [g]@Sharec7a8ce455b828537, [g^-1*C_in]@Reduceef9903cafc29eea1
		t_5 = torch.reshape(t_5, (1, 32, 8, 3, 7, 7, 8, ))

		# [g^-1*C_in]@Reduce
		t_5 = torch.sum(t_5, dim=(2, ))

		# No contraction needed.
		t_6 = t_5

		# [H]@Shiftdbd5b2e652804221 -> [H]@Unfold0063bc810b9e1e60
		t_6 = torch.roll(t_6, self.shift_direction, 4)

		# [H]@Unfold0063bc810b9e1e60 -> [H]@Iteratorb0a1def4ad5784ec, [k_1]@Share26cfa48d169008e4
		t_6 = torch.reshape(t_6, (1, 672, 7, 8, ))
		t_6 = torch.nn.functional.unfold(t_6, (3, 1, ), padding=(1, 0, ))
		t_6 = torch.reshape(t_6, (1, 32, 3, 7, 3, 7, 8, ))

		# Perform contraction.
		t_7 = torch.einsum("nkmojpl, ikmjl -> niop", t_6, in_1)

		# No need to crop the output tensor.
		y = t_7

		return y

class kernel_generated_6(torch.nn.Module):
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

		# [H]@Shift05348c1f59ed8f45 -> [H]@Unfoldd282eed81682d1c4
		t_3 = torch.roll(t_3, self.shift_direction, 2)

		# [H]@Unfoldd282eed81682d1c4 -> [H]@Iterator96123ba3184da39c, [k_1]@Share63a88e0da5dce9dc
		t_3 = torch.reshape(t_3, (1, 512, 7, 7, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (1, 512, 3, 7, 7, ))

		# Perform contraction.
		t_4 = torch.einsum("ljkmn, jki -> ljkmni", t_3, in_2)

		# No contraction needed.
		t_5 = t_4

		# [C_in]@Splitc2d52f3525ba6cc4 -> [g]@Sharec7a8ce455b828537, [g^-1*C_in]@Reduceef9903cafc29eea1
		t_5 = torch.reshape(t_5, (1, 32, 16, 3, 7, 7, 8, ))

		# [g^-1*C_in]@Reduce
		t_5 = torch.sum(t_5, dim=(2, ))

		# No contraction needed.
		t_6 = t_5

		# [H]@Shiftdbd5b2e652804221 -> [H]@Unfold0063bc810b9e1e60
		t_6 = torch.roll(t_6, self.shift_direction, 4)

		# [H]@Unfold0063bc810b9e1e60 -> [H]@Iteratorb0a1def4ad5784ec, [k_1]@Share26cfa48d169008e4
		t_6 = torch.reshape(t_6, (1, 672, 7, 8, ))
		t_6 = torch.nn.functional.unfold(t_6, (3, 1, ), padding=(1, 0, ))
		t_6 = torch.reshape(t_6, (1, 32, 3, 7, 3, 7, 8, ))

		# Perform contraction.
		t_7 = torch.einsum("nkmojpl, ikmjl -> niop", t_6, in_1)

		# No need to crop the output tensor.
		y = t_7

		return y

