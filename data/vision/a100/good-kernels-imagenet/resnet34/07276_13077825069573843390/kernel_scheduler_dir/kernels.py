import torch
import random
"""
digraph kernel_preview {
newrank = true;

// Stage tensor.
subgraph cluster_subgraph_0 {
    label = "Subgraph 0";
    // Reductions.
    reduce_0x7f5708001928 [label="Sum", shape=box];
    reduce_0x7f5708001ab0 [label="Sum", shape=box];
    reduce_0x7f5708001a98 [label="Sum", shape=box];
    reduce_0x7f5708009288 [label="Sum", shape=box];
    // Output.
    subgraph cluster_subgraph_0_out {
        label = "";
        interface_0_out_0x5573688f8610 [label="N", shape=none];
        interface_0_out_0x5573688f8638 [label="C_out", shape=none];
        interface_0_out_0x5573688f8660 [label="H", shape=none];
        interface_0_out_0x5573688f8688 [label="H", shape=none];
    }
    {
        rank = same;
        reduce_0x7f5708001928;
        reduce_0x7f5708001ab0;
        reduce_0x7f5708001a98;
        reduce_0x7f5708009288;
        interface_0_out_0x5573688f8610;
        interface_0_out_0x5573688f8638;
        interface_0_out_0x5573688f8660;
        interface_0_out_0x5573688f8688;
    }
    // Input 0.
    subgraph cluster_subgraph_0_in_0 {
        label = "";
        interface_0_in_0x5573688f8610 [label="N", shape=none];
        interface_0_in_0x5573682b5c40 [label="g", shape=none];
        interface_0_in_0x5573682b5d30 [label="k_1", shape=none];
        interface_0_in_0x5573688f8660 [label="H", shape=none];
        interface_0_in_0x5573682b5c90 [label="k_1", shape=none];
        interface_0_in_0x5573688f8688 [label="H", shape=none];
        interface_0_in_0x5573682b5ce0 [label="g^-1*s^-1*C_out", shape=none];
    }
    // Input 1.
    subgraph cluster_subgraph_0_in_1 {
        label = "";
        interface_0_in_0x5573682b5bb8 [label="C_out", shape=none];
        interface_0_in_0x5573682b5c58 [label="g", shape=none];
        interface_0_in_0x5573682b5d48 [label="k_1", shape=none];
        interface_0_in_0x5573682b5ca8 [label="k_1", shape=none];
        interface_0_in_0x5573682b5cf8 [label="g^-1*s^-1*C_out", shape=none];
    }
    {
        rank = same;
        interface_0_in_0x5573688f8610;
        interface_0_in_0x5573682b5c40;
        interface_0_in_0x5573682b5d30;
        interface_0_in_0x5573688f8660;
        interface_0_in_0x5573682b5c90;
        interface_0_in_0x5573688f8688;
        interface_0_in_0x5573682b5ce0;
        interface_0_in_0x5573682b5bb8;
        interface_0_in_0x5573682b5c58;
        interface_0_in_0x5573682b5d48;
        interface_0_in_0x5573682b5ca8;
        interface_0_in_0x5573682b5cf8;
    }
    // Op's.
    op_0x557366936818 [label="Expand"];
    op_0x5573682b5b80 [label="Share"];
    op_0x5573682b5c20 [label="Share"];
    op_0x5573682b5c70 [label="Share"];
    op_0x5573682b5cc0 [label="Share"];
    op_0x5573682b5d10 [label="Share"];
    // Dimension's.
    op_0x557366936818 -> op_0x5573682b5b80 [label="C_out"];
    interface_0_in_0x5573682b5bb8 -> op_0x5573682b5b80 [label="C_out"];
    interface_0_in_0x5573682b5c40 -> op_0x5573682b5c20 [label="g"];
    interface_0_in_0x5573682b5c58 -> op_0x5573682b5c20 [label="g"];
    interface_0_in_0x5573682b5c90 -> op_0x5573682b5c70 [label="k_1"];
    interface_0_in_0x5573682b5ca8 -> op_0x5573682b5c70 [label="k_1"];
    interface_0_in_0x5573682b5ce0 -> op_0x5573682b5cc0 [label="g^-1*s^-1*C_out"];
    interface_0_in_0x5573682b5cf8 -> op_0x5573682b5cc0 [label="g^-1*s^-1*C_out"];
    interface_0_in_0x5573682b5d30 -> op_0x5573682b5d10 [label="k_1"];
    interface_0_in_0x5573682b5d48 -> op_0x5573682b5d10 [label="k_1"];
    interface_0_in_0x5573688f8610 -> interface_0_out_0x5573688f8610 [label="N"];
    op_0x5573682b5b80 -> interface_0_out_0x5573688f8638 [label="C_out"];
    interface_0_in_0x5573688f8660 -> interface_0_out_0x5573688f8660 [label="H"];
    interface_0_in_0x5573688f8688 -> interface_0_out_0x5573688f8688 [label="H"];
    op_0x5573682b5c20 -> reduce_0x7f5708001928 [label="g"];
    op_0x5573682b5c70 -> reduce_0x7f5708001a98 [label="k_1"];
    op_0x5573682b5d10 -> reduce_0x7f5708001ab0 [label="k_1"];
    op_0x5573682b5cc0 -> reduce_0x7f5708009288 [label="g^-1*s^-1*C_out"];
}

// Stage tensor.
subgraph cluster_subgraph_1 {
    label = "Subgraph 1";
    // Reductions.
    // Output.
    subgraph cluster_subgraph_1_out {
        label = "";
        interface_1_out_0x5573688f8610 [label="N", shape=none];
        interface_1_out_0x5573682b5c40 [label="g", shape=none];
        interface_1_out_0x5573682b5d30 [label="k_1", shape=none];
        interface_1_out_0x5573688f8660 [label="H", shape=none];
        interface_1_out_0x5573682b5c90 [label="k_1", shape=none];
        interface_1_out_0x5573688f8688 [label="H", shape=none];
        interface_1_out_0x5573682b5ce0 [label="g^-1*s^-1*C_out", shape=none];
    }
    {
        rank = same;
        interface_1_out_0x5573688f8610;
        interface_1_out_0x5573682b5c40;
        interface_1_out_0x5573682b5d30;
        interface_1_out_0x5573688f8660;
        interface_1_out_0x5573682b5c90;
        interface_1_out_0x5573688f8688;
        interface_1_out_0x5573682b5ce0;
    }
    // Input 0.
    subgraph cluster_subgraph_1_in_0 {
        label = "";
        interface_1_in_0x5573688f8610 [label="N", shape=none];
        interface_1_in_0x5573682b5c40 [label="g", shape=none];
        interface_1_in_0x5573682b5d30 [label="k_1", shape=none];
        interface_1_in_0x5573688f8660 [label="H", shape=none];
        interface_1_in_0x5573688fb8c0 [label="H", shape=none];
        interface_1_in_0x5573682b5ce0 [label="g^-1*s^-1*C_out", shape=none];
    }
    {
        rank = same;
        interface_1_in_0x5573688f8610;
        interface_1_in_0x5573682b5c40;
        interface_1_in_0x5573682b5d30;
        interface_1_in_0x5573688f8660;
        interface_1_in_0x5573688fb8c0;
        interface_1_in_0x5573682b5ce0;
    }
    // Op's.
    op_0x5573682a8880 [label="Unfold"];
    op_0x5573688fb8a0 [label="Shift"];
    // Dimension's.
    op_0x5573688fb8a0 -> op_0x5573682a8880 [label="H"];
    interface_1_in_0x5573682b5c40 -> interface_1_out_0x5573682b5c40 [label="g"];
    op_0x5573682a8880 -> interface_1_out_0x5573682b5c90 [label="k_1"];
    interface_1_in_0x5573682b5ce0 -> interface_1_out_0x5573682b5ce0 [label="g^-1*s^-1*C_out"];
    interface_1_in_0x5573682b5d30 -> interface_1_out_0x5573682b5d30 [label="k_1"];
    interface_1_in_0x5573688f8610 -> interface_1_out_0x5573688f8610 [label="N"];
    interface_1_in_0x5573688f8660 -> interface_1_out_0x5573688f8660 [label="H"];
    op_0x5573682a8880 -> interface_1_out_0x5573688f8688 [label="H"];
    interface_1_in_0x5573688fb8c0 -> op_0x5573688fb8a0 [label="H"];
}

// Stage tensor.
subgraph cluster_subgraph_2 {
    label = "Subgraph 2";
    // Reductions.
    reduce_0x7f5708005a90 [label="Sum", shape=box];
    // Output.
    subgraph cluster_subgraph_2_out {
        label = "";
        interface_2_out_0x5573688f8610 [label="N", shape=none];
        interface_2_out_0x5573682b5c40 [label="g", shape=none];
        interface_2_out_0x5573682b5d30 [label="k_1", shape=none];
        interface_2_out_0x5573688f8660 [label="H", shape=none];
        interface_2_out_0x5573688fb8c0 [label="H", shape=none];
        interface_2_out_0x5573682b5ce0 [label="g^-1*s^-1*C_out", shape=none];
    }
    {
        rank = same;
        reduce_0x7f5708005a90;
        interface_2_out_0x5573688f8610;
        interface_2_out_0x5573682b5c40;
        interface_2_out_0x5573682b5d30;
        interface_2_out_0x5573688f8660;
        interface_2_out_0x5573688fb8c0;
        interface_2_out_0x5573682b5ce0;
    }
    // Input 0.
    subgraph cluster_subgraph_2_in_0 {
        label = "";
        interface_2_in_0x5573688f8610 [label="N", shape=none];
        interface_2_in_0x5573670a1f90 [label="C_in", shape=none];
        interface_2_in_0x5573682b5d30 [label="k_1", shape=none];
        interface_2_in_0x5573688f8660 [label="H", shape=none];
        interface_2_in_0x5573688fb8c0 [label="H", shape=none];
        interface_2_in_0x5573682b5ce0 [label="g^-1*s^-1*C_out", shape=none];
    }
    {
        rank = same;
        interface_2_in_0x5573688f8610;
        interface_2_in_0x5573670a1f90;
        interface_2_in_0x5573682b5d30;
        interface_2_in_0x5573688f8660;
        interface_2_in_0x5573688fb8c0;
        interface_2_in_0x5573682b5ce0;
    }
    // Op's.
    op_0x5573670a1f50 [label="Split"];
    // Dimension's.
    interface_2_in_0x5573670a1f90 -> op_0x5573670a1f50 [label="C_in"];
    op_0x5573670a1f50 -> interface_2_out_0x5573682b5c40 [label="g"];
    interface_2_in_0x5573682b5ce0 -> interface_2_out_0x5573682b5ce0 [label="g^-1*s^-1*C_out"];
    interface_2_in_0x5573682b5d30 -> interface_2_out_0x5573682b5d30 [label="k_1"];
    interface_2_in_0x5573688f8610 -> interface_2_out_0x5573688f8610 [label="N"];
    interface_2_in_0x5573688f8660 -> interface_2_out_0x5573688f8660 [label="H"];
    interface_2_in_0x5573688fb8c0 -> interface_2_out_0x5573688fb8c0 [label="H"];
    op_0x5573670a1f50 -> reduce_0x7f5708005a90 [label="g^-1*C_in"];
}

// Stage tensor.
subgraph cluster_subgraph_3 {
    label = "Subgraph 3";
    // Reductions.
    // Output.
    subgraph cluster_subgraph_3_out {
        label = "";
        interface_3_out_0x5573688f8610 [label="N", shape=none];
        interface_3_out_0x5573670a1f90 [label="C_in", shape=none];
        interface_3_out_0x5573682b5d30 [label="k_1", shape=none];
        interface_3_out_0x5573688f8660 [label="H", shape=none];
        interface_3_out_0x5573688fb8c0 [label="H", shape=none];
        interface_3_out_0x5573682b5ce0 [label="g^-1*s^-1*C_out", shape=none];
    }
    {
        rank = same;
        interface_3_out_0x5573688f8610;
        interface_3_out_0x5573670a1f90;
        interface_3_out_0x5573682b5d30;
        interface_3_out_0x5573688f8660;
        interface_3_out_0x5573688fb8c0;
        interface_3_out_0x5573682b5ce0;
    }
    // Input 0.
    subgraph cluster_subgraph_3_in_0 {
        label = "";
        interface_3_in_0x5573688f8610 [label="N", shape=none];
        interface_3_in_0x5573682b5f10 [label="C_in", shape=none];
        interface_3_in_0x5573682b5ec0 [label="k_1", shape=none];
        interface_3_in_0x5573688f8660 [label="H", shape=none];
        interface_3_in_0x5573688fb8c0 [label="H", shape=none];
    }
    // Input 1.
    subgraph cluster_subgraph_3_in_1 {
        label = "";
        interface_3_in_0x5573682b5f28 [label="C_in", shape=none];
        interface_3_in_0x5573682b5ed8 [label="k_1", shape=none];
        interface_3_in_0x5573682b5d98 [label="g^-1*s^-1*C_out", shape=none];
    }
    {
        rank = same;
        interface_3_in_0x5573688f8610;
        interface_3_in_0x5573682b5f10;
        interface_3_in_0x5573682b5ec0;
        interface_3_in_0x5573688f8660;
        interface_3_in_0x5573688fb8c0;
        interface_3_in_0x5573682b5f28;
        interface_3_in_0x5573682b5ed8;
        interface_3_in_0x5573682b5d98;
    }
    // Op's.
    op_0x557366936838 [label="Expand"];
    op_0x5573682b5d60 [label="Share"];
    op_0x5573682b5ea0 [label="Share"];
    op_0x5573682b5ef0 [label="Share"];
    // Dimension's.
    op_0x5573682b5ef0 -> interface_3_out_0x5573670a1f90 [label="C_in"];
    op_0x5573682b5d60 -> interface_3_out_0x5573682b5ce0 [label="g^-1*s^-1*C_out"];
    op_0x5573682b5ea0 -> interface_3_out_0x5573682b5d30 [label="k_1"];
    op_0x557366936838 -> op_0x5573682b5d60 [label="g^-1*s^-1*C_out"];
    interface_3_in_0x5573682b5d98 -> op_0x5573682b5d60 [label="g^-1*s^-1*C_out"];
    interface_3_in_0x5573682b5ec0 -> op_0x5573682b5ea0 [label="k_1"];
    interface_3_in_0x5573682b5ed8 -> op_0x5573682b5ea0 [label="k_1"];
    interface_3_in_0x5573682b5f10 -> op_0x5573682b5ef0 [label="C_in"];
    interface_3_in_0x5573682b5f28 -> op_0x5573682b5ef0 [label="C_in"];
    interface_3_in_0x5573688f8610 -> interface_3_out_0x5573688f8610 [label="N"];
    interface_3_in_0x5573688f8660 -> interface_3_out_0x5573688f8660 [label="H"];
    interface_3_in_0x5573688fb8c0 -> interface_3_out_0x5573688fb8c0 [label="H"];
}

// Stage tensor.
subgraph cluster_subgraph_4 {
    label = "Subgraph 4";
    // Reductions.
    // Output.
    subgraph cluster_subgraph_4_out {
        label = "";
        interface_4_out_0x5573688f8610 [label="N", shape=none];
        interface_4_out_0x5573682b5f10 [label="C_in", shape=none];
        interface_4_out_0x5573682b5ec0 [label="k_1", shape=none];
        interface_4_out_0x5573688f8660 [label="H", shape=none];
        interface_4_out_0x5573688fb8c0 [label="H", shape=none];
    }
    {
        rank = same;
        interface_4_out_0x5573688f8610;
        interface_4_out_0x5573682b5f10;
        interface_4_out_0x5573682b5ec0;
        interface_4_out_0x5573688f8660;
        interface_4_out_0x5573688fb8c0;
    }
    // Input 0.
    subgraph cluster_subgraph_4_in_0 {
        label = "";
        interface_4_in_0x5573688f8610 [label="N", shape=none];
        interface_4_in_0x5573682b5f10 [label="C_in", shape=none];
        interface_4_in_0x5573688fb8f0 [label="H", shape=none];
        interface_4_in_0x5573688fb8c0 [label="H", shape=none];
    }
    {
        rank = same;
        interface_4_in_0x5573688f8610;
        interface_4_in_0x5573682b5f10;
        interface_4_in_0x5573688fb8f0;
        interface_4_in_0x5573688fb8c0;
    }
    // Op's.
    op_0x5573682a8900 [label="Unfold"];
    op_0x5573688fb8d0 [label="Shift"];
    // Dimension's.
    op_0x5573688fb8d0 -> op_0x5573682a8900 [label="H"];
    op_0x5573682a8900 -> interface_4_out_0x5573682b5ec0 [label="k_1"];
    interface_4_in_0x5573682b5f10 -> interface_4_out_0x5573682b5f10 [label="C_in"];
    interface_4_in_0x5573688f8610 -> interface_4_out_0x5573688f8610 [label="N"];
    op_0x5573682a8900 -> interface_4_out_0x5573688f8660 [label="H"];
    interface_4_in_0x5573688fb8c0 -> interface_4_out_0x5573688fb8c0 [label="H"];
    interface_4_in_0x5573688fb8f0 -> op_0x5573688fb8d0 [label="H"];
}

// Input tensor.
subgraph cluster_subgraph_5 {
    label = "Input 0";
    interface_5_out_0x5573688f8610 [label="N", shape=none];
    interface_5_out_0x5573682b5f10 [label="C_in", shape=none];
    interface_5_out_0x5573688fb8f0 [label="H", shape=none];
    interface_5_out_0x5573688fb8c0 [label="H", shape=none];
}

interface_5_out_0x5573688f8610 -> interface_4_in_0x5573688f8610;
interface_5_out_0x5573682b5f10 -> interface_4_in_0x5573682b5f10;
interface_5_out_0x5573688fb8f0 -> interface_4_in_0x5573688fb8f0;
interface_5_out_0x5573688fb8c0 -> interface_4_in_0x5573688fb8c0;

interface_4_out_0x5573688f8610 -> interface_3_in_0x5573688f8610;
interface_4_out_0x5573682b5f10 -> interface_3_in_0x5573682b5f10;
interface_4_out_0x5573682b5ec0 -> interface_3_in_0x5573682b5ec0;
interface_4_out_0x5573688f8660 -> interface_3_in_0x5573688f8660;
interface_4_out_0x5573688fb8c0 -> interface_3_in_0x5573688fb8c0;

// Input tensor.
subgraph cluster_subgraph_6 {
    label = "Input 2";
    interface_6_out_0x5573682b5f28 [label="C_in", shape=none];
    interface_6_out_0x5573682b5ed8 [label="k_1", shape=none];
    interface_6_out_0x5573682b5d98 [label="g^-1*s^-1*C_out", shape=none];
}

interface_6_out_0x5573682b5f28 -> interface_3_in_0x5573682b5f28;
interface_6_out_0x5573682b5ed8 -> interface_3_in_0x5573682b5ed8;
interface_6_out_0x5573682b5d98 -> interface_3_in_0x5573682b5d98;

interface_3_out_0x5573688f8610 -> interface_2_in_0x5573688f8610;
interface_3_out_0x5573670a1f90 -> interface_2_in_0x5573670a1f90;
interface_3_out_0x5573682b5d30 -> interface_2_in_0x5573682b5d30;
interface_3_out_0x5573688f8660 -> interface_2_in_0x5573688f8660;
interface_3_out_0x5573688fb8c0 -> interface_2_in_0x5573688fb8c0;
interface_3_out_0x5573682b5ce0 -> interface_2_in_0x5573682b5ce0;

interface_2_out_0x5573688f8610 -> interface_1_in_0x5573688f8610;
interface_2_out_0x5573682b5c40 -> interface_1_in_0x5573682b5c40;
interface_2_out_0x5573682b5d30 -> interface_1_in_0x5573682b5d30;
interface_2_out_0x5573688f8660 -> interface_1_in_0x5573688f8660;
interface_2_out_0x5573688fb8c0 -> interface_1_in_0x5573688fb8c0;
interface_2_out_0x5573682b5ce0 -> interface_1_in_0x5573682b5ce0;

interface_1_out_0x5573688f8610 -> interface_0_in_0x5573688f8610;
interface_1_out_0x5573682b5c40 -> interface_0_in_0x5573682b5c40;
interface_1_out_0x5573682b5d30 -> interface_0_in_0x5573682b5d30;
interface_1_out_0x5573688f8660 -> interface_0_in_0x5573688f8660;
interface_1_out_0x5573682b5c90 -> interface_0_in_0x5573682b5c90;
interface_1_out_0x5573688f8688 -> interface_0_in_0x5573688f8688;
interface_1_out_0x5573682b5ce0 -> interface_0_in_0x5573682b5ce0;

// Input tensor.
subgraph cluster_subgraph_7 {
    label = "Input 1";
    interface_7_out_0x5573682b5bb8 [label="C_out", shape=none];
    interface_7_out_0x5573682b5c58 [label="g", shape=none];
    interface_7_out_0x5573682b5d48 [label="k_1", shape=none];
    interface_7_out_0x5573682b5ca8 [label="k_1", shape=none];
    interface_7_out_0x5573682b5cf8 [label="g^-1*s^-1*C_out", shape=none];
}

interface_7_out_0x5573682b5bb8 -> interface_0_in_0x5573682b5bb8;
interface_7_out_0x5573682b5c58 -> interface_0_in_0x5573682b5c58;
interface_7_out_0x5573682b5d48 -> interface_0_in_0x5573682b5d48;
interface_7_out_0x5573682b5ca8 -> interface_0_in_0x5573682b5ca8;
interface_7_out_0x5573682b5cf8 -> interface_0_in_0x5573682b5cf8;

{
    rank = same;
    interface_5_out_0x5573688f8610;
    interface_5_out_0x5573682b5f10;
    interface_5_out_0x5573688fb8f0;
    interface_5_out_0x5573688fb8c0;
    interface_7_out_0x5573682b5bb8;
    interface_7_out_0x5573682b5c58;
    interface_7_out_0x5573682b5d48;
    interface_7_out_0x5573682b5ca8;
    interface_7_out_0x5573682b5cf8;
    interface_6_out_0x5573682b5f28;
    interface_6_out_0x5573682b5ed8;
    interface_6_out_0x5573682b5d98;
}
subgraph cluster_subgraph_output {
    label = "Output";
    interface_8_in_0x5573688f8610 [label="N", shape=none];
    interface_8_in_0x5573688f8638 [label="C_out", shape=none];
    interface_8_in_0x5573688f8660 [label="H", shape=none];
    interface_8_in_0x5573688f8688 [label="H", shape=none];
}
interface_0_out_0x5573688f8610 -> interface_8_in_0x5573688f8610;
interface_0_out_0x5573688f8638 -> interface_8_in_0x5573688f8638;
interface_0_out_0x5573688f8660 -> interface_8_in_0x5573688f8660;
interface_0_out_0x5573688f8688 -> interface_8_in_0x5573688f8688;

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
		t_3 = torch.reshape(t_3, (1024, 64, 56, 56, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (1024, 64, 3, 56, 56, ))

		# Perform contraction.
		t_4 = torch.einsum("lkjmn, kji -> lkjmni", t_3, in_2)

		# No contraction needed.
		t_5 = t_4

		# [C_in]@Splitc2d52f3525ba6cc4 -> [g]@Sharec7a8ce455b828537, [g^-1*C_in]@Reduceef9903cafc29eea1
		t_5 = torch.reshape(t_5, (1024, 32, 2, 3, 56, 56, 1, ))

		# [g^-1*C_in]@Reduce
		t_5 = torch.sum(t_5, dim=(2, ))

		# No contraction needed.
		t_6 = t_5

		# [H]@Shiftdbd5b2e652804221 -> [H]@Unfold0063bc810b9e1e60
		t_6 = torch.roll(t_6, self.shift_direction, 4)

		# [H]@Unfold0063bc810b9e1e60 -> [H]@Iteratorb0a1def4ad5784ec, [k_1]@Share26cfa48d169008e4
		t_6 = torch.reshape(t_6, (1024, 5376, 56, 1, ))
		t_6 = torch.nn.functional.unfold(t_6, (3, 1, ), padding=(1, 0, ))
		t_6 = torch.reshape(t_6, (1024, 32, 3, 56, 3, 56, 1, ))

		# Perform contraction.
		t_7 = torch.einsum("njmokpl, ijmkl -> niop", t_6, in_1)

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
		t_3 = torch.reshape(t_3, (1024, 64, 28, 28, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (1024, 64, 3, 28, 28, ))

		# Perform contraction.
		t_4 = torch.einsum("lkjmn, kji -> lkjmni", t_3, in_2)

		# No contraction needed.
		t_5 = t_4

		# [C_in]@Splitc2d52f3525ba6cc4 -> [g]@Sharec7a8ce455b828537, [g^-1*C_in]@Reduceef9903cafc29eea1
		t_5 = torch.reshape(t_5, (1024, 32, 2, 3, 28, 28, 2, ))

		# [g^-1*C_in]@Reduce
		t_5 = torch.sum(t_5, dim=(2, ))

		# No contraction needed.
		t_6 = t_5

		# [H]@Shiftdbd5b2e652804221 -> [H]@Unfold0063bc810b9e1e60
		t_6 = torch.roll(t_6, self.shift_direction, 4)

		# [H]@Unfold0063bc810b9e1e60 -> [H]@Iteratorb0a1def4ad5784ec, [k_1]@Share26cfa48d169008e4
		t_6 = torch.reshape(t_6, (1024, 2688, 28, 2, ))
		t_6 = torch.nn.functional.unfold(t_6, (3, 1, ), padding=(1, 0, ))
		t_6 = torch.reshape(t_6, (1024, 32, 3, 28, 3, 28, 2, ))

		# Perform contraction.
		t_7 = torch.einsum("njmokpl, ijmkl -> niop", t_6, in_1)

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
		t_3 = torch.reshape(t_3, (1024, 128, 28, 28, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (1024, 128, 3, 28, 28, ))

		# Perform contraction.
		t_4 = torch.einsum("lkjmn, kji -> lkjmni", t_3, in_2)

		# No contraction needed.
		t_5 = t_4

		# [C_in]@Splitc2d52f3525ba6cc4 -> [g]@Sharec7a8ce455b828537, [g^-1*C_in]@Reduceef9903cafc29eea1
		t_5 = torch.reshape(t_5, (1024, 32, 4, 3, 28, 28, 2, ))

		# [g^-1*C_in]@Reduce
		t_5 = torch.sum(t_5, dim=(2, ))

		# No contraction needed.
		t_6 = t_5

		# [H]@Shiftdbd5b2e652804221 -> [H]@Unfold0063bc810b9e1e60
		t_6 = torch.roll(t_6, self.shift_direction, 4)

		# [H]@Unfold0063bc810b9e1e60 -> [H]@Iteratorb0a1def4ad5784ec, [k_1]@Share26cfa48d169008e4
		t_6 = torch.reshape(t_6, (1024, 2688, 28, 2, ))
		t_6 = torch.nn.functional.unfold(t_6, (3, 1, ), padding=(1, 0, ))
		t_6 = torch.reshape(t_6, (1024, 32, 3, 28, 3, 28, 2, ))

		# Perform contraction.
		t_7 = torch.einsum("njmokpl, ijmkl -> niop", t_6, in_1)

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
		t_3 = torch.reshape(t_3, (1024, 128, 14, 14, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (1024, 128, 3, 14, 14, ))

		# Perform contraction.
		t_4 = torch.einsum("lkjmn, kji -> lkjmni", t_3, in_2)

		# No contraction needed.
		t_5 = t_4

		# [C_in]@Splitc2d52f3525ba6cc4 -> [g]@Sharec7a8ce455b828537, [g^-1*C_in]@Reduceef9903cafc29eea1
		t_5 = torch.reshape(t_5, (1024, 32, 4, 3, 14, 14, 4, ))

		# [g^-1*C_in]@Reduce
		t_5 = torch.sum(t_5, dim=(2, ))

		# No contraction needed.
		t_6 = t_5

		# [H]@Shiftdbd5b2e652804221 -> [H]@Unfold0063bc810b9e1e60
		t_6 = torch.roll(t_6, self.shift_direction, 4)

		# [H]@Unfold0063bc810b9e1e60 -> [H]@Iteratorb0a1def4ad5784ec, [k_1]@Share26cfa48d169008e4
		t_6 = torch.reshape(t_6, (1024, 1344, 14, 4, ))
		t_6 = torch.nn.functional.unfold(t_6, (3, 1, ), padding=(1, 0, ))
		t_6 = torch.reshape(t_6, (1024, 32, 3, 14, 3, 14, 4, ))

		# Perform contraction.
		t_7 = torch.einsum("njmokpl, ijmkl -> niop", t_6, in_1)

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
		t_3 = torch.reshape(t_3, (1024, 256, 14, 14, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (1024, 256, 3, 14, 14, ))

		# Perform contraction.
		t_4 = torch.einsum("lkjmn, kji -> lkjmni", t_3, in_2)

		# No contraction needed.
		t_5 = t_4

		# [C_in]@Splitc2d52f3525ba6cc4 -> [g]@Sharec7a8ce455b828537, [g^-1*C_in]@Reduceef9903cafc29eea1
		t_5 = torch.reshape(t_5, (1024, 32, 8, 3, 14, 14, 4, ))

		# [g^-1*C_in]@Reduce
		t_5 = torch.sum(t_5, dim=(2, ))

		# No contraction needed.
		t_6 = t_5

		# [H]@Shiftdbd5b2e652804221 -> [H]@Unfold0063bc810b9e1e60
		t_6 = torch.roll(t_6, self.shift_direction, 4)

		# [H]@Unfold0063bc810b9e1e60 -> [H]@Iteratorb0a1def4ad5784ec, [k_1]@Share26cfa48d169008e4
		t_6 = torch.reshape(t_6, (1024, 1344, 14, 4, ))
		t_6 = torch.nn.functional.unfold(t_6, (3, 1, ), padding=(1, 0, ))
		t_6 = torch.reshape(t_6, (1024, 32, 3, 14, 3, 14, 4, ))

		# Perform contraction.
		t_7 = torch.einsum("njmokpl, ijmkl -> niop", t_6, in_1)

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
		t_3 = torch.reshape(t_3, (1024, 256, 7, 7, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (1024, 256, 3, 7, 7, ))

		# Perform contraction.
		t_4 = torch.einsum("lkjmn, kji -> lkjmni", t_3, in_2)

		# No contraction needed.
		t_5 = t_4

		# [C_in]@Splitc2d52f3525ba6cc4 -> [g]@Sharec7a8ce455b828537, [g^-1*C_in]@Reduceef9903cafc29eea1
		t_5 = torch.reshape(t_5, (1024, 32, 8, 3, 7, 7, 8, ))

		# [g^-1*C_in]@Reduce
		t_5 = torch.sum(t_5, dim=(2, ))

		# No contraction needed.
		t_6 = t_5

		# [H]@Shiftdbd5b2e652804221 -> [H]@Unfold0063bc810b9e1e60
		t_6 = torch.roll(t_6, self.shift_direction, 4)

		# [H]@Unfold0063bc810b9e1e60 -> [H]@Iteratorb0a1def4ad5784ec, [k_1]@Share26cfa48d169008e4
		t_6 = torch.reshape(t_6, (1024, 672, 7, 8, ))
		t_6 = torch.nn.functional.unfold(t_6, (3, 1, ), padding=(1, 0, ))
		t_6 = torch.reshape(t_6, (1024, 32, 3, 7, 3, 7, 8, ))

		# Perform contraction.
		t_7 = torch.einsum("njmokpl, ijmkl -> niop", t_6, in_1)

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
		t_3 = torch.reshape(t_3, (1024, 512, 7, 7, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (1024, 512, 3, 7, 7, ))

		# Perform contraction.
		t_4 = torch.einsum("lkjmn, kji -> lkjmni", t_3, in_2)

		# No contraction needed.
		t_5 = t_4

		# [C_in]@Splitc2d52f3525ba6cc4 -> [g]@Sharec7a8ce455b828537, [g^-1*C_in]@Reduceef9903cafc29eea1
		t_5 = torch.reshape(t_5, (1024, 32, 16, 3, 7, 7, 8, ))

		# [g^-1*C_in]@Reduce
		t_5 = torch.sum(t_5, dim=(2, ))

		# No contraction needed.
		t_6 = t_5

		# [H]@Shiftdbd5b2e652804221 -> [H]@Unfold0063bc810b9e1e60
		t_6 = torch.roll(t_6, self.shift_direction, 4)

		# [H]@Unfold0063bc810b9e1e60 -> [H]@Iteratorb0a1def4ad5784ec, [k_1]@Share26cfa48d169008e4
		t_6 = torch.reshape(t_6, (1024, 672, 7, 8, ))
		t_6 = torch.nn.functional.unfold(t_6, (3, 1, ), padding=(1, 0, ))
		t_6 = torch.reshape(t_6, (1024, 32, 3, 7, 3, 7, 8, ))

		# Perform contraction.
		t_7 = torch.einsum("njmokpl, ijmkl -> niop", t_6, in_1)

		# No need to crop the output tensor.
		y = t_7

		return y

