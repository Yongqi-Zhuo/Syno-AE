import torch
import random
"""
digraph kernel_preview {
newrank = true;

// Stage tensor.
subgraph cluster_subgraph_0 {
    label = "Subgraph 0";
    // Reductions.
    reduce_0x7f8ea8001828 [label="Sum", shape=box];
    reduce_0x7f8ea8001998 [label="Sum", shape=box];
    reduce_0x7f8ea80019b0 [label="Sum", shape=box];
    reduce_0x7f8ea8009288 [label="Sum", shape=box];
    // Output.
    subgraph cluster_subgraph_0_out {
        label = "";
        interface_0_out_0x5560e507fd50 [label="N", shape=none];
        interface_0_out_0x5560e507fd78 [label="C_out", shape=none];
        interface_0_out_0x5560e507fda0 [label="H", shape=none];
        interface_0_out_0x5560e507fdc8 [label="H", shape=none];
    }
    {
        rank = same;
        reduce_0x7f8ea8001828;
        reduce_0x7f8ea8001998;
        reduce_0x7f8ea80019b0;
        reduce_0x7f8ea8009288;
        interface_0_out_0x5560e507fd50;
        interface_0_out_0x5560e507fd78;
        interface_0_out_0x5560e507fda0;
        interface_0_out_0x5560e507fdc8;
    }
    // Input 0.
    subgraph cluster_subgraph_0_in_0 {
        label = "";
        interface_0_in_0x5560e507fd50 [label="N", shape=none];
        interface_0_in_0x5560e51979d0 [label="g", shape=none];
        interface_0_in_0x5560e507fda0 [label="H", shape=none];
        interface_0_in_0x7f934c0040b0 [label="k_1", shape=none];
        interface_0_in_0x5560e507fdc8 [label="H", shape=none];
        interface_0_in_0x5560e50b32d0 [label="k_1", shape=none];
        interface_0_in_0x5560e50b31e0 [label="g^-1*s^-1*C_out", shape=none];
    }
    // Input 1.
    subgraph cluster_subgraph_0_in_1 {
        label = "";
        interface_0_in_0x5560e51979e8 [label="g", shape=none];
        interface_0_in_0x7f934c0040c8 [label="k_1", shape=none];
        interface_0_in_0x5560e50b32e8 [label="k_1", shape=none];
        interface_0_in_0x5560e5187c38 [label="C_out", shape=none];
        interface_0_in_0x5560e50b31f8 [label="g^-1*s^-1*C_out", shape=none];
    }
    {
        rank = same;
        interface_0_in_0x5560e507fd50;
        interface_0_in_0x5560e51979d0;
        interface_0_in_0x5560e507fda0;
        interface_0_in_0x7f934c0040b0;
        interface_0_in_0x5560e507fdc8;
        interface_0_in_0x5560e50b32d0;
        interface_0_in_0x5560e50b31e0;
        interface_0_in_0x5560e51979e8;
        interface_0_in_0x7f934c0040c8;
        interface_0_in_0x5560e50b32e8;
        interface_0_in_0x5560e5187c38;
        interface_0_in_0x5560e50b31f8;
    }
    // Op's.
    op_0x5560e4e3c778 [label="Expand"];
    op_0x5560e50b31c0 [label="Share"];
    op_0x5560e50b32b0 [label="Share"];
    op_0x5560e5187c00 [label="Share"];
    op_0x5560e51979b0 [label="Share"];
    op_0x7f934c004090 [label="Share"];
    // Dimension's.
    interface_0_in_0x5560e507fd50 -> interface_0_out_0x5560e507fd50 [label="N"];
    op_0x5560e5187c00 -> interface_0_out_0x5560e507fd78 [label="C_out"];
    interface_0_in_0x5560e507fda0 -> interface_0_out_0x5560e507fda0 [label="H"];
    interface_0_in_0x5560e507fdc8 -> interface_0_out_0x5560e507fdc8 [label="H"];
    interface_0_in_0x5560e50b31e0 -> op_0x5560e50b31c0 [label="g^-1*s^-1*C_out"];
    interface_0_in_0x5560e50b31f8 -> op_0x5560e50b31c0 [label="g^-1*s^-1*C_out"];
    interface_0_in_0x5560e50b32d0 -> op_0x5560e50b32b0 [label="k_1"];
    interface_0_in_0x5560e50b32e8 -> op_0x5560e50b32b0 [label="k_1"];
    op_0x5560e4e3c778 -> op_0x5560e5187c00 [label="C_out"];
    interface_0_in_0x5560e5187c38 -> op_0x5560e5187c00 [label="C_out"];
    interface_0_in_0x5560e51979d0 -> op_0x5560e51979b0 [label="g"];
    interface_0_in_0x5560e51979e8 -> op_0x5560e51979b0 [label="g"];
    op_0x5560e51979b0 -> reduce_0x7f8ea8001828 [label="g"];
    op_0x5560e50b32b0 -> reduce_0x7f8ea8001998 [label="k_1"];
    op_0x7f934c004090 -> reduce_0x7f8ea80019b0 [label="k_1"];
    op_0x5560e50b31c0 -> reduce_0x7f8ea8009288 [label="g^-1*s^-1*C_out"];
    interface_0_in_0x7f934c0040b0 -> op_0x7f934c004090 [label="k_1"];
    interface_0_in_0x7f934c0040c8 -> op_0x7f934c004090 [label="k_1"];
}

// Stage tensor.
subgraph cluster_subgraph_1 {
    label = "Subgraph 1";
    // Reductions.
    // Output.
    subgraph cluster_subgraph_1_out {
        label = "";
        interface_1_out_0x5560e507fd50 [label="N", shape=none];
        interface_1_out_0x5560e51979d0 [label="g", shape=none];
        interface_1_out_0x5560e507fda0 [label="H", shape=none];
        interface_1_out_0x7f934c0040b0 [label="k_1", shape=none];
        interface_1_out_0x5560e507fdc8 [label="H", shape=none];
        interface_1_out_0x5560e50b32d0 [label="k_1", shape=none];
        interface_1_out_0x5560e50b31e0 [label="g^-1*s^-1*C_out", shape=none];
    }
    {
        rank = same;
        interface_1_out_0x5560e507fd50;
        interface_1_out_0x5560e51979d0;
        interface_1_out_0x5560e507fda0;
        interface_1_out_0x7f934c0040b0;
        interface_1_out_0x5560e507fdc8;
        interface_1_out_0x5560e50b32d0;
        interface_1_out_0x5560e50b31e0;
    }
    // Input 0.
    subgraph cluster_subgraph_1_in_0 {
        label = "";
        interface_1_in_0x5560e507fd50 [label="N", shape=none];
        interface_1_in_0x5560e51979d0 [label="g", shape=none];
        interface_1_in_0x5560e507fda0 [label="H", shape=none];
        interface_1_in_0x7f934c0040b0 [label="k_1", shape=none];
        interface_1_in_0x5560e5aca580 [label="H", shape=none];
        interface_1_in_0x5560e50b31e0 [label="g^-1*s^-1*C_out", shape=none];
    }
    {
        rank = same;
        interface_1_in_0x5560e507fd50;
        interface_1_in_0x5560e51979d0;
        interface_1_in_0x5560e507fda0;
        interface_1_in_0x7f934c0040b0;
        interface_1_in_0x5560e5aca580;
        interface_1_in_0x5560e50b31e0;
    }
    // Op's.
    op_0x5560e5aca560 [label="Shift"];
    op_0x5560e5bbdec0 [label="Unfold"];
    // Dimension's.
    interface_1_in_0x5560e507fd50 -> interface_1_out_0x5560e507fd50 [label="N"];
    interface_1_in_0x5560e507fda0 -> interface_1_out_0x5560e507fda0 [label="H"];
    op_0x5560e5bbdec0 -> interface_1_out_0x5560e507fdc8 [label="H"];
    interface_1_in_0x5560e50b31e0 -> interface_1_out_0x5560e50b31e0 [label="g^-1*s^-1*C_out"];
    op_0x5560e5bbdec0 -> interface_1_out_0x5560e50b32d0 [label="k_1"];
    interface_1_in_0x5560e51979d0 -> interface_1_out_0x5560e51979d0 [label="g"];
    interface_1_in_0x5560e5aca580 -> op_0x5560e5aca560 [label="H"];
    op_0x5560e5aca560 -> op_0x5560e5bbdec0 [label="H"];
    interface_1_in_0x7f934c0040b0 -> interface_1_out_0x7f934c0040b0 [label="k_1"];
}

// Stage tensor.
subgraph cluster_subgraph_2 {
    label = "Subgraph 2";
    // Reductions.
    reduce_0x7f8ea8005b90 [label="Sum", shape=box];
    // Output.
    subgraph cluster_subgraph_2_out {
        label = "";
        interface_2_out_0x5560e507fd50 [label="N", shape=none];
        interface_2_out_0x5560e51979d0 [label="g", shape=none];
        interface_2_out_0x5560e507fda0 [label="H", shape=none];
        interface_2_out_0x7f934c0040b0 [label="k_1", shape=none];
        interface_2_out_0x5560e5aca580 [label="H", shape=none];
        interface_2_out_0x5560e50b31e0 [label="g^-1*s^-1*C_out", shape=none];
    }
    {
        rank = same;
        reduce_0x7f8ea8005b90;
        interface_2_out_0x5560e507fd50;
        interface_2_out_0x5560e51979d0;
        interface_2_out_0x5560e507fda0;
        interface_2_out_0x7f934c0040b0;
        interface_2_out_0x5560e5aca580;
        interface_2_out_0x5560e50b31e0;
    }
    // Input 0.
    subgraph cluster_subgraph_2_in_0 {
        label = "";
        interface_2_in_0x5560e507fd50 [label="N", shape=none];
        interface_2_in_0x5560e5b19bf0 [label="C_in", shape=none];
        interface_2_in_0x5560e507fda0 [label="H", shape=none];
        interface_2_in_0x7f934c0040b0 [label="k_1", shape=none];
        interface_2_in_0x5560e5aca580 [label="H", shape=none];
        interface_2_in_0x5560e50b31e0 [label="g^-1*s^-1*C_out", shape=none];
    }
    {
        rank = same;
        interface_2_in_0x5560e507fd50;
        interface_2_in_0x5560e5b19bf0;
        interface_2_in_0x5560e507fda0;
        interface_2_in_0x7f934c0040b0;
        interface_2_in_0x5560e5aca580;
        interface_2_in_0x5560e50b31e0;
    }
    // Op's.
    op_0x5560e5b19bb0 [label="Split"];
    // Dimension's.
    interface_2_in_0x5560e507fd50 -> interface_2_out_0x5560e507fd50 [label="N"];
    interface_2_in_0x5560e507fda0 -> interface_2_out_0x5560e507fda0 [label="H"];
    interface_2_in_0x5560e50b31e0 -> interface_2_out_0x5560e50b31e0 [label="g^-1*s^-1*C_out"];
    op_0x5560e5b19bb0 -> interface_2_out_0x5560e51979d0 [label="g"];
    interface_2_in_0x5560e5aca580 -> interface_2_out_0x5560e5aca580 [label="H"];
    interface_2_in_0x5560e5b19bf0 -> op_0x5560e5b19bb0 [label="C_in"];
    op_0x5560e5b19bb0 -> reduce_0x7f8ea8005b90 [label="g^-1*C_in"];
    interface_2_in_0x7f934c0040b0 -> interface_2_out_0x7f934c0040b0 [label="k_1"];
}

// Stage tensor.
subgraph cluster_subgraph_3 {
    label = "Subgraph 3";
    // Reductions.
    // Output.
    subgraph cluster_subgraph_3_out {
        label = "";
        interface_3_out_0x5560e507fd50 [label="N", shape=none];
        interface_3_out_0x5560e5b19bf0 [label="C_in", shape=none];
        interface_3_out_0x5560e507fda0 [label="H", shape=none];
        interface_3_out_0x7f934c0040b0 [label="k_1", shape=none];
        interface_3_out_0x5560e5aca580 [label="H", shape=none];
        interface_3_out_0x5560e50b31e0 [label="g^-1*s^-1*C_out", shape=none];
    }
    {
        rank = same;
        interface_3_out_0x5560e507fd50;
        interface_3_out_0x5560e5b19bf0;
        interface_3_out_0x5560e507fda0;
        interface_3_out_0x7f934c0040b0;
        interface_3_out_0x5560e5aca580;
        interface_3_out_0x5560e50b31e0;
    }
    // Input 0.
    subgraph cluster_subgraph_3_in_0 {
        label = "";
        interface_3_in_0x5560e507fd50 [label="N", shape=none];
        interface_3_in_0x7f94f4019f90 [label="C_in", shape=none];
        interface_3_in_0x5560e507fda0 [label="H", shape=none];
        interface_3_in_0x7f94f401b660 [label="k_1", shape=none];
        interface_3_in_0x5560e5aca580 [label="H", shape=none];
    }
    // Input 1.
    subgraph cluster_subgraph_3_in_1 {
        label = "";
        interface_3_in_0x7f94f4019fa8 [label="C_in", shape=none];
        interface_3_in_0x7f94f401b678 [label="k_1", shape=none];
        interface_3_in_0x7f934c005658 [label="g^-1*s^-1*C_out", shape=none];
    }
    {
        rank = same;
        interface_3_in_0x5560e507fd50;
        interface_3_in_0x7f94f4019f90;
        interface_3_in_0x5560e507fda0;
        interface_3_in_0x7f94f401b660;
        interface_3_in_0x5560e5aca580;
        interface_3_in_0x7f94f4019fa8;
        interface_3_in_0x7f94f401b678;
        interface_3_in_0x7f934c005658;
    }
    // Op's.
    op_0x5560e6569138 [label="Expand"];
    op_0x7f934c005620 [label="Share"];
    op_0x7f94f4019f70 [label="Share"];
    op_0x7f94f401b640 [label="Share"];
    // Dimension's.
    interface_3_in_0x5560e507fd50 -> interface_3_out_0x5560e507fd50 [label="N"];
    interface_3_in_0x5560e507fda0 -> interface_3_out_0x5560e507fda0 [label="H"];
    op_0x7f934c005620 -> interface_3_out_0x5560e50b31e0 [label="g^-1*s^-1*C_out"];
    interface_3_in_0x5560e5aca580 -> interface_3_out_0x5560e5aca580 [label="H"];
    op_0x7f94f4019f70 -> interface_3_out_0x5560e5b19bf0 [label="C_in"];
    op_0x7f94f401b640 -> interface_3_out_0x7f934c0040b0 [label="k_1"];
    op_0x5560e6569138 -> op_0x7f934c005620 [label="g^-1*s^-1*C_out"];
    interface_3_in_0x7f934c005658 -> op_0x7f934c005620 [label="g^-1*s^-1*C_out"];
    interface_3_in_0x7f94f4019f90 -> op_0x7f94f4019f70 [label="C_in"];
    interface_3_in_0x7f94f4019fa8 -> op_0x7f94f4019f70 [label="C_in"];
    interface_3_in_0x7f94f401b660 -> op_0x7f94f401b640 [label="k_1"];
    interface_3_in_0x7f94f401b678 -> op_0x7f94f401b640 [label="k_1"];
}

// Stage tensor.
subgraph cluster_subgraph_4 {
    label = "Subgraph 4";
    // Reductions.
    // Output.
    subgraph cluster_subgraph_4_out {
        label = "";
        interface_4_out_0x5560e507fd50 [label="N", shape=none];
        interface_4_out_0x7f94f4019f90 [label="C_in", shape=none];
        interface_4_out_0x5560e507fda0 [label="H", shape=none];
        interface_4_out_0x7f94f401b660 [label="k_1", shape=none];
        interface_4_out_0x5560e5aca580 [label="H", shape=none];
    }
    {
        rank = same;
        interface_4_out_0x5560e507fd50;
        interface_4_out_0x7f94f4019f90;
        interface_4_out_0x5560e507fda0;
        interface_4_out_0x7f94f401b660;
        interface_4_out_0x5560e5aca580;
    }
    // Input 0.
    subgraph cluster_subgraph_4_in_0 {
        label = "";
        interface_4_in_0x5560e507fd50 [label="N", shape=none];
        interface_4_in_0x7f94f4019f90 [label="C_in", shape=none];
        interface_4_in_0x5560e7466a90 [label="H", shape=none];
        interface_4_in_0x5560e5aca580 [label="H", shape=none];
    }
    {
        rank = same;
        interface_4_in_0x5560e507fd50;
        interface_4_in_0x7f94f4019f90;
        interface_4_in_0x5560e7466a90;
        interface_4_in_0x5560e5aca580;
    }
    // Op's.
    op_0x5560e7466a70 [label="Shift"];
    op_0x7f91c40253c0 [label="Unfold"];
    // Dimension's.
    interface_4_in_0x5560e507fd50 -> interface_4_out_0x5560e507fd50 [label="N"];
    op_0x7f91c40253c0 -> interface_4_out_0x5560e507fda0 [label="H"];
    interface_4_in_0x5560e5aca580 -> interface_4_out_0x5560e5aca580 [label="H"];
    interface_4_in_0x5560e7466a90 -> op_0x5560e7466a70 [label="H"];
    op_0x5560e7466a70 -> op_0x7f91c40253c0 [label="H"];
    interface_4_in_0x7f94f4019f90 -> interface_4_out_0x7f94f4019f90 [label="C_in"];
    op_0x7f91c40253c0 -> interface_4_out_0x7f94f401b660 [label="k_1"];
}

// Input tensor.
subgraph cluster_subgraph_5 {
    label = "Input 0";
    interface_5_out_0x5560e507fd50 [label="N", shape=none];
    interface_5_out_0x7f94f4019f90 [label="C_in", shape=none];
    interface_5_out_0x5560e7466a90 [label="H", shape=none];
    interface_5_out_0x5560e5aca580 [label="H", shape=none];
}

interface_5_out_0x5560e507fd50 -> interface_4_in_0x5560e507fd50;
interface_5_out_0x7f94f4019f90 -> interface_4_in_0x7f94f4019f90;
interface_5_out_0x5560e7466a90 -> interface_4_in_0x5560e7466a90;
interface_5_out_0x5560e5aca580 -> interface_4_in_0x5560e5aca580;

interface_4_out_0x5560e507fd50 -> interface_3_in_0x5560e507fd50;
interface_4_out_0x7f94f4019f90 -> interface_3_in_0x7f94f4019f90;
interface_4_out_0x5560e507fda0 -> interface_3_in_0x5560e507fda0;
interface_4_out_0x7f94f401b660 -> interface_3_in_0x7f94f401b660;
interface_4_out_0x5560e5aca580 -> interface_3_in_0x5560e5aca580;

// Input tensor.
subgraph cluster_subgraph_6 {
    label = "Input 2";
    interface_6_out_0x7f94f4019fa8 [label="C_in", shape=none];
    interface_6_out_0x7f94f401b678 [label="k_1", shape=none];
    interface_6_out_0x7f934c005658 [label="g^-1*s^-1*C_out", shape=none];
}

interface_6_out_0x7f94f4019fa8 -> interface_3_in_0x7f94f4019fa8;
interface_6_out_0x7f94f401b678 -> interface_3_in_0x7f94f401b678;
interface_6_out_0x7f934c005658 -> interface_3_in_0x7f934c005658;

interface_3_out_0x5560e507fd50 -> interface_2_in_0x5560e507fd50;
interface_3_out_0x5560e5b19bf0 -> interface_2_in_0x5560e5b19bf0;
interface_3_out_0x5560e507fda0 -> interface_2_in_0x5560e507fda0;
interface_3_out_0x7f934c0040b0 -> interface_2_in_0x7f934c0040b0;
interface_3_out_0x5560e5aca580 -> interface_2_in_0x5560e5aca580;
interface_3_out_0x5560e50b31e0 -> interface_2_in_0x5560e50b31e0;

interface_2_out_0x5560e507fd50 -> interface_1_in_0x5560e507fd50;
interface_2_out_0x5560e51979d0 -> interface_1_in_0x5560e51979d0;
interface_2_out_0x5560e507fda0 -> interface_1_in_0x5560e507fda0;
interface_2_out_0x7f934c0040b0 -> interface_1_in_0x7f934c0040b0;
interface_2_out_0x5560e5aca580 -> interface_1_in_0x5560e5aca580;
interface_2_out_0x5560e50b31e0 -> interface_1_in_0x5560e50b31e0;

interface_1_out_0x5560e507fd50 -> interface_0_in_0x5560e507fd50;
interface_1_out_0x5560e51979d0 -> interface_0_in_0x5560e51979d0;
interface_1_out_0x5560e507fda0 -> interface_0_in_0x5560e507fda0;
interface_1_out_0x7f934c0040b0 -> interface_0_in_0x7f934c0040b0;
interface_1_out_0x5560e507fdc8 -> interface_0_in_0x5560e507fdc8;
interface_1_out_0x5560e50b32d0 -> interface_0_in_0x5560e50b32d0;
interface_1_out_0x5560e50b31e0 -> interface_0_in_0x5560e50b31e0;

// Input tensor.
subgraph cluster_subgraph_7 {
    label = "Input 1";
    interface_7_out_0x5560e51979e8 [label="g", shape=none];
    interface_7_out_0x7f934c0040c8 [label="k_1", shape=none];
    interface_7_out_0x5560e50b32e8 [label="k_1", shape=none];
    interface_7_out_0x5560e5187c38 [label="C_out", shape=none];
    interface_7_out_0x5560e50b31f8 [label="g^-1*s^-1*C_out", shape=none];
}

interface_7_out_0x5560e51979e8 -> interface_0_in_0x5560e51979e8;
interface_7_out_0x7f934c0040c8 -> interface_0_in_0x7f934c0040c8;
interface_7_out_0x5560e50b32e8 -> interface_0_in_0x5560e50b32e8;
interface_7_out_0x5560e5187c38 -> interface_0_in_0x5560e5187c38;
interface_7_out_0x5560e50b31f8 -> interface_0_in_0x5560e50b31f8;

{
    rank = same;
    interface_5_out_0x5560e507fd50;
    interface_5_out_0x7f94f4019f90;
    interface_5_out_0x5560e7466a90;
    interface_5_out_0x5560e5aca580;
    interface_7_out_0x5560e51979e8;
    interface_7_out_0x7f934c0040c8;
    interface_7_out_0x5560e50b32e8;
    interface_7_out_0x5560e5187c38;
    interface_7_out_0x5560e50b31f8;
    interface_6_out_0x7f94f4019fa8;
    interface_6_out_0x7f94f401b678;
    interface_6_out_0x7f934c005658;
}
subgraph cluster_subgraph_output {
    label = "Output";
    interface_8_in_0x5560e507fd50 [label="N", shape=none];
    interface_8_in_0x5560e507fd78 [label="C_out", shape=none];
    interface_8_in_0x5560e507fda0 [label="H", shape=none];
    interface_8_in_0x5560e507fdc8 [label="H", shape=none];
}
interface_0_out_0x5560e507fd50 -> interface_8_in_0x5560e507fd50;
interface_0_out_0x5560e507fd78 -> interface_8_in_0x5560e507fd78;
interface_0_out_0x5560e507fda0 -> interface_8_in_0x5560e507fda0;
interface_0_out_0x5560e507fdc8 -> interface_8_in_0x5560e507fdc8;

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

		# [H]@Shift05348c1f59ed8f45 -> [H]@Unfoldd282eed81682d1c4
		t_3 = torch.roll(t_3, self.shift_direction, 2)

		# [H]@Unfoldd282eed81682d1c4 -> [H]@Iterator96123ba3184da39c, [k_1]@Share63a88e0da5dce9dc
		t_3 = torch.reshape(t_3, (128, 64, 56, 56, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (128, 64, 3, 56, 56, ))

		# Permute to match the output of this subgraph.
		t_3 = torch.permute(t_3, (0, 1, 3, 2, 4, ))

		# Perform contraction.
		t_4 = torch.einsum("ljmkn, jki -> ljmkni", t_3, in_2)

		# No contraction needed.
		t_5 = t_4

		# [C_in]@Splitc2d52f3525ba6cc4 -> [g]@Sharec7a8ce455b828537, [g^-1*C_in]@Reduceef9903cafc29eea1
		t_5 = torch.reshape(t_5, (128, 32, 2, 56, 3, 56, 1, ))

		# [g^-1*C_in]@Reduce
		t_5 = torch.sum(t_5, dim=(2, ))

		# No contraction needed.
		t_6 = t_5

		# [H]@Shiftdbd5b2e652804221 -> [H]@Unfold0063bc810b9e1e60
		t_6 = torch.roll(t_6, self.shift_direction, 4)

		# [H]@Unfold0063bc810b9e1e60 -> [H]@Iteratorb0a1def4ad5784ec, [k_1]@Share26cfa48d169008e4
		t_6 = torch.reshape(t_6, (128, 5376, 56, 1, ))
		t_6 = torch.nn.functional.unfold(t_6, (3, 1, ), padding=(1, 0, ))
		t_6 = torch.reshape(t_6, (128, 32, 56, 3, 3, 56, 1, ))

		# Permute to match the output of this subgraph.
		t_6 = torch.permute(t_6, (0, 1, 2, 3, 5, 4, 6, ))

		# Perform contraction.
		t_7 = torch.einsum("nlompji, lmjki -> nopk", t_6, in_1)

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

		# [H]@Shift05348c1f59ed8f45 -> [H]@Unfoldd282eed81682d1c4
		t_3 = torch.roll(t_3, self.shift_direction, 2)

		# [H]@Unfoldd282eed81682d1c4 -> [H]@Iterator96123ba3184da39c, [k_1]@Share63a88e0da5dce9dc
		t_3 = torch.reshape(t_3, (128, 64, 28, 28, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (128, 64, 3, 28, 28, ))

		# Permute to match the output of this subgraph.
		t_3 = torch.permute(t_3, (0, 1, 3, 2, 4, ))

		# Perform contraction.
		t_4 = torch.einsum("ljmkn, jki -> ljmkni", t_3, in_2)

		# No contraction needed.
		t_5 = t_4

		# [C_in]@Splitc2d52f3525ba6cc4 -> [g]@Sharec7a8ce455b828537, [g^-1*C_in]@Reduceef9903cafc29eea1
		t_5 = torch.reshape(t_5, (128, 32, 2, 28, 3, 28, 2, ))

		# [g^-1*C_in]@Reduce
		t_5 = torch.sum(t_5, dim=(2, ))

		# No contraction needed.
		t_6 = t_5

		# [H]@Shiftdbd5b2e652804221 -> [H]@Unfold0063bc810b9e1e60
		t_6 = torch.roll(t_6, self.shift_direction, 4)

		# [H]@Unfold0063bc810b9e1e60 -> [H]@Iteratorb0a1def4ad5784ec, [k_1]@Share26cfa48d169008e4
		t_6 = torch.reshape(t_6, (128, 2688, 28, 2, ))
		t_6 = torch.nn.functional.unfold(t_6, (3, 1, ), padding=(1, 0, ))
		t_6 = torch.reshape(t_6, (128, 32, 28, 3, 3, 28, 2, ))

		# Permute to match the output of this subgraph.
		t_6 = torch.permute(t_6, (0, 1, 2, 3, 5, 4, 6, ))

		# Perform contraction.
		t_7 = torch.einsum("nlompji, lmjki -> nopk", t_6, in_1)

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

		# [H]@Shift05348c1f59ed8f45 -> [H]@Unfoldd282eed81682d1c4
		t_3 = torch.roll(t_3, self.shift_direction, 2)

		# [H]@Unfoldd282eed81682d1c4 -> [H]@Iterator96123ba3184da39c, [k_1]@Share63a88e0da5dce9dc
		t_3 = torch.reshape(t_3, (128, 128, 28, 28, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (128, 128, 3, 28, 28, ))

		# Permute to match the output of this subgraph.
		t_3 = torch.permute(t_3, (0, 1, 3, 2, 4, ))

		# Perform contraction.
		t_4 = torch.einsum("ljmkn, jki -> ljmkni", t_3, in_2)

		# No contraction needed.
		t_5 = t_4

		# [C_in]@Splitc2d52f3525ba6cc4 -> [g]@Sharec7a8ce455b828537, [g^-1*C_in]@Reduceef9903cafc29eea1
		t_5 = torch.reshape(t_5, (128, 32, 4, 28, 3, 28, 2, ))

		# [g^-1*C_in]@Reduce
		t_5 = torch.sum(t_5, dim=(2, ))

		# No contraction needed.
		t_6 = t_5

		# [H]@Shiftdbd5b2e652804221 -> [H]@Unfold0063bc810b9e1e60
		t_6 = torch.roll(t_6, self.shift_direction, 4)

		# [H]@Unfold0063bc810b9e1e60 -> [H]@Iteratorb0a1def4ad5784ec, [k_1]@Share26cfa48d169008e4
		t_6 = torch.reshape(t_6, (128, 2688, 28, 2, ))
		t_6 = torch.nn.functional.unfold(t_6, (3, 1, ), padding=(1, 0, ))
		t_6 = torch.reshape(t_6, (128, 32, 28, 3, 3, 28, 2, ))

		# Permute to match the output of this subgraph.
		t_6 = torch.permute(t_6, (0, 1, 2, 3, 5, 4, 6, ))

		# Perform contraction.
		t_7 = torch.einsum("nlompji, lmjki -> nopk", t_6, in_1)

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

		# [H]@Shift05348c1f59ed8f45 -> [H]@Unfoldd282eed81682d1c4
		t_3 = torch.roll(t_3, self.shift_direction, 2)

		# [H]@Unfoldd282eed81682d1c4 -> [H]@Iterator96123ba3184da39c, [k_1]@Share63a88e0da5dce9dc
		t_3 = torch.reshape(t_3, (128, 128, 14, 14, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (128, 128, 3, 14, 14, ))

		# Permute to match the output of this subgraph.
		t_3 = torch.permute(t_3, (0, 1, 3, 2, 4, ))

		# Perform contraction.
		t_4 = torch.einsum("ljmkn, jki -> ljmkni", t_3, in_2)

		# No contraction needed.
		t_5 = t_4

		# [C_in]@Splitc2d52f3525ba6cc4 -> [g]@Sharec7a8ce455b828537, [g^-1*C_in]@Reduceef9903cafc29eea1
		t_5 = torch.reshape(t_5, (128, 32, 4, 14, 3, 14, 4, ))

		# [g^-1*C_in]@Reduce
		t_5 = torch.sum(t_5, dim=(2, ))

		# No contraction needed.
		t_6 = t_5

		# [H]@Shiftdbd5b2e652804221 -> [H]@Unfold0063bc810b9e1e60
		t_6 = torch.roll(t_6, self.shift_direction, 4)

		# [H]@Unfold0063bc810b9e1e60 -> [H]@Iteratorb0a1def4ad5784ec, [k_1]@Share26cfa48d169008e4
		t_6 = torch.reshape(t_6, (128, 1344, 14, 4, ))
		t_6 = torch.nn.functional.unfold(t_6, (3, 1, ), padding=(1, 0, ))
		t_6 = torch.reshape(t_6, (128, 32, 14, 3, 3, 14, 4, ))

		# Permute to match the output of this subgraph.
		t_6 = torch.permute(t_6, (0, 1, 2, 3, 5, 4, 6, ))

		# Perform contraction.
		t_7 = torch.einsum("nlompji, lmjki -> nopk", t_6, in_1)

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

		# [H]@Shift05348c1f59ed8f45 -> [H]@Unfoldd282eed81682d1c4
		t_3 = torch.roll(t_3, self.shift_direction, 2)

		# [H]@Unfoldd282eed81682d1c4 -> [H]@Iterator96123ba3184da39c, [k_1]@Share63a88e0da5dce9dc
		t_3 = torch.reshape(t_3, (128, 256, 14, 14, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (128, 256, 3, 14, 14, ))

		# Permute to match the output of this subgraph.
		t_3 = torch.permute(t_3, (0, 1, 3, 2, 4, ))

		# Perform contraction.
		t_4 = torch.einsum("ljmkn, jki -> ljmkni", t_3, in_2)

		# No contraction needed.
		t_5 = t_4

		# [C_in]@Splitc2d52f3525ba6cc4 -> [g]@Sharec7a8ce455b828537, [g^-1*C_in]@Reduceef9903cafc29eea1
		t_5 = torch.reshape(t_5, (128, 32, 8, 14, 3, 14, 4, ))

		# [g^-1*C_in]@Reduce
		t_5 = torch.sum(t_5, dim=(2, ))

		# No contraction needed.
		t_6 = t_5

		# [H]@Shiftdbd5b2e652804221 -> [H]@Unfold0063bc810b9e1e60
		t_6 = torch.roll(t_6, self.shift_direction, 4)

		# [H]@Unfold0063bc810b9e1e60 -> [H]@Iteratorb0a1def4ad5784ec, [k_1]@Share26cfa48d169008e4
		t_6 = torch.reshape(t_6, (128, 1344, 14, 4, ))
		t_6 = torch.nn.functional.unfold(t_6, (3, 1, ), padding=(1, 0, ))
		t_6 = torch.reshape(t_6, (128, 32, 14, 3, 3, 14, 4, ))

		# Permute to match the output of this subgraph.
		t_6 = torch.permute(t_6, (0, 1, 2, 3, 5, 4, 6, ))

		# Perform contraction.
		t_7 = torch.einsum("nlompji, lmjki -> nopk", t_6, in_1)

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

		# [H]@Shift05348c1f59ed8f45 -> [H]@Unfoldd282eed81682d1c4
		t_3 = torch.roll(t_3, self.shift_direction, 2)

		# [H]@Unfoldd282eed81682d1c4 -> [H]@Iterator96123ba3184da39c, [k_1]@Share63a88e0da5dce9dc
		t_3 = torch.reshape(t_3, (128, 256, 7, 7, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (128, 256, 3, 7, 7, ))

		# Permute to match the output of this subgraph.
		t_3 = torch.permute(t_3, (0, 1, 3, 2, 4, ))

		# Perform contraction.
		t_4 = torch.einsum("ljmkn, jki -> ljmkni", t_3, in_2)

		# No contraction needed.
		t_5 = t_4

		# [C_in]@Splitc2d52f3525ba6cc4 -> [g]@Sharec7a8ce455b828537, [g^-1*C_in]@Reduceef9903cafc29eea1
		t_5 = torch.reshape(t_5, (128, 32, 8, 7, 3, 7, 8, ))

		# [g^-1*C_in]@Reduce
		t_5 = torch.sum(t_5, dim=(2, ))

		# No contraction needed.
		t_6 = t_5

		# [H]@Shiftdbd5b2e652804221 -> [H]@Unfold0063bc810b9e1e60
		t_6 = torch.roll(t_6, self.shift_direction, 4)

		# [H]@Unfold0063bc810b9e1e60 -> [H]@Iteratorb0a1def4ad5784ec, [k_1]@Share26cfa48d169008e4
		t_6 = torch.reshape(t_6, (128, 672, 7, 8, ))
		t_6 = torch.nn.functional.unfold(t_6, (3, 1, ), padding=(1, 0, ))
		t_6 = torch.reshape(t_6, (128, 32, 7, 3, 3, 7, 8, ))

		# Permute to match the output of this subgraph.
		t_6 = torch.permute(t_6, (0, 1, 2, 3, 5, 4, 6, ))

		# Perform contraction.
		t_7 = torch.einsum("nlompji, lmjki -> nopk", t_6, in_1)

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

		# [H]@Shift05348c1f59ed8f45 -> [H]@Unfoldd282eed81682d1c4
		t_3 = torch.roll(t_3, self.shift_direction, 2)

		# [H]@Unfoldd282eed81682d1c4 -> [H]@Iterator96123ba3184da39c, [k_1]@Share63a88e0da5dce9dc
		t_3 = torch.reshape(t_3, (128, 512, 7, 7, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (128, 512, 3, 7, 7, ))

		# Permute to match the output of this subgraph.
		t_3 = torch.permute(t_3, (0, 1, 3, 2, 4, ))

		# Perform contraction.
		t_4 = torch.einsum("ljmkn, jki -> ljmkni", t_3, in_2)

		# No contraction needed.
		t_5 = t_4

		# [C_in]@Splitc2d52f3525ba6cc4 -> [g]@Sharec7a8ce455b828537, [g^-1*C_in]@Reduceef9903cafc29eea1
		t_5 = torch.reshape(t_5, (128, 32, 16, 7, 3, 7, 8, ))

		# [g^-1*C_in]@Reduce
		t_5 = torch.sum(t_5, dim=(2, ))

		# No contraction needed.
		t_6 = t_5

		# [H]@Shiftdbd5b2e652804221 -> [H]@Unfold0063bc810b9e1e60
		t_6 = torch.roll(t_6, self.shift_direction, 4)

		# [H]@Unfold0063bc810b9e1e60 -> [H]@Iteratorb0a1def4ad5784ec, [k_1]@Share26cfa48d169008e4
		t_6 = torch.reshape(t_6, (128, 672, 7, 8, ))
		t_6 = torch.nn.functional.unfold(t_6, (3, 1, ), padding=(1, 0, ))
		t_6 = torch.reshape(t_6, (128, 32, 7, 3, 3, 7, 8, ))

		# Permute to match the output of this subgraph.
		t_6 = torch.permute(t_6, (0, 1, 2, 3, 5, 4, 6, ))

		# Perform contraction.
		t_7 = torch.einsum("nlompji, lmjki -> nopk", t_6, in_1)

		# Permute to match the output of this subgraph.
		t_7 = torch.permute(t_7, (0, 3, 1, 2, ))

		# No need to crop the output tensor.
		y = t_7

		return y

