import torch
import random
"""
digraph kernel_preview {
newrank = true;

// Stage tensor.
subgraph cluster_subgraph_0 {
    label = "Subgraph 0";
    // Reductions.
    reduce_0x7ef2c8001928 [label="Sum", shape=box];
    reduce_0x7ef2c8001a98 [label="Sum", shape=box];
    reduce_0x7ef2c8001ab0 [label="Sum", shape=box];
    reduce_0x7ef2c8009088 [label="Sum", shape=box];
    // Output.
    subgraph cluster_subgraph_0_out {
        label = "";
        interface_0_out_0x55acfaae6490 [label="N", shape=none];
        interface_0_out_0x55acfaae64b8 [label="C_out", shape=none];
        interface_0_out_0x55acfaae64e0 [label="H", shape=none];
        interface_0_out_0x55acfaae6508 [label="H", shape=none];
    }
    {
        rank = same;
        reduce_0x7ef2c8001928;
        reduce_0x7ef2c8001a98;
        reduce_0x7ef2c8001ab0;
        reduce_0x7ef2c8009088;
        interface_0_out_0x55acfaae6490;
        interface_0_out_0x55acfaae64b8;
        interface_0_out_0x55acfaae64e0;
        interface_0_out_0x55acfaae6508;
    }
    // Input 0.
    subgraph cluster_subgraph_0_in_0 {
        label = "";
        interface_0_in_0x55acfaae6490 [label="N", shape=none];
        interface_0_in_0x55ad0b705f40 [label="g", shape=none];
        interface_0_in_0x55ad0b705d10 [label="k_1", shape=none];
        interface_0_in_0x55acfaae64e0 [label="H", shape=none];
        interface_0_in_0x55ad0b705fe0 [label="k_1", shape=none];
        interface_0_in_0x55acfaae6508 [label="H", shape=none];
        interface_0_in_0x55ad0b705f90 [label="g^-1*s^-1*C_out", shape=none];
    }
    // Input 1.
    subgraph cluster_subgraph_0_in_1 {
        label = "";
        interface_0_in_0x55ad0b705c38 [label="C_out", shape=none];
        interface_0_in_0x55ad0b705f58 [label="g", shape=none];
        interface_0_in_0x55ad0b705d28 [label="k_1", shape=none];
        interface_0_in_0x55ad0b705ff8 [label="k_1", shape=none];
        interface_0_in_0x55ad0b705fa8 [label="g^-1*s^-1*C_out", shape=none];
    }
    {
        rank = same;
        interface_0_in_0x55acfaae6490;
        interface_0_in_0x55ad0b705f40;
        interface_0_in_0x55ad0b705d10;
        interface_0_in_0x55acfaae64e0;
        interface_0_in_0x55ad0b705fe0;
        interface_0_in_0x55acfaae6508;
        interface_0_in_0x55ad0b705f90;
        interface_0_in_0x55ad0b705c38;
        interface_0_in_0x55ad0b705f58;
        interface_0_in_0x55ad0b705d28;
        interface_0_in_0x55ad0b705ff8;
        interface_0_in_0x55ad0b705fa8;
    }
    // Op's.
    op_0x55ad0b705c00 [label="Share"];
    op_0x55ad0b705cf0 [label="Share"];
    op_0x55ad0b705f20 [label="Share"];
    op_0x55ad0b705f70 [label="Share"];
    op_0x55ad0b705fc0 [label="Share"];
    op_0x55ad0b706138 [label="Expand"];
    // Dimension's.
    interface_0_in_0x55acfaae6490 -> interface_0_out_0x55acfaae6490 [label="N"];
    op_0x55ad0b705c00 -> interface_0_out_0x55acfaae64b8 [label="C_out"];
    interface_0_in_0x55acfaae64e0 -> interface_0_out_0x55acfaae64e0 [label="H"];
    interface_0_in_0x55acfaae6508 -> interface_0_out_0x55acfaae6508 [label="H"];
    op_0x55ad0b706138 -> op_0x55ad0b705c00 [label="C_out"];
    interface_0_in_0x55ad0b705c38 -> op_0x55ad0b705c00 [label="C_out"];
    interface_0_in_0x55ad0b705d10 -> op_0x55ad0b705cf0 [label="k_1"];
    interface_0_in_0x55ad0b705d28 -> op_0x55ad0b705cf0 [label="k_1"];
    interface_0_in_0x55ad0b705f40 -> op_0x55ad0b705f20 [label="g"];
    interface_0_in_0x55ad0b705f58 -> op_0x55ad0b705f20 [label="g"];
    interface_0_in_0x55ad0b705f90 -> op_0x55ad0b705f70 [label="g^-1*s^-1*C_out"];
    interface_0_in_0x55ad0b705fa8 -> op_0x55ad0b705f70 [label="g^-1*s^-1*C_out"];
    interface_0_in_0x55ad0b705fe0 -> op_0x55ad0b705fc0 [label="k_1"];
    interface_0_in_0x55ad0b705ff8 -> op_0x55ad0b705fc0 [label="k_1"];
    op_0x55ad0b705f20 -> reduce_0x7ef2c8001928 [label="g"];
    op_0x55ad0b705cf0 -> reduce_0x7ef2c8001a98 [label="k_1"];
    op_0x55ad0b705fc0 -> reduce_0x7ef2c8001ab0 [label="k_1"];
    op_0x55ad0b705f70 -> reduce_0x7ef2c8009088 [label="g^-1*s^-1*C_out"];
}

// Stage tensor.
subgraph cluster_subgraph_1 {
    label = "Subgraph 1";
    // Reductions.
    // Output.
    subgraph cluster_subgraph_1_out {
        label = "";
        interface_1_out_0x55acfaae6490 [label="N", shape=none];
        interface_1_out_0x55ad0b705f40 [label="g", shape=none];
        interface_1_out_0x55ad0b705d10 [label="k_1", shape=none];
        interface_1_out_0x55acfaae64e0 [label="H", shape=none];
        interface_1_out_0x55ad0b705fe0 [label="k_1", shape=none];
        interface_1_out_0x55acfaae6508 [label="H", shape=none];
        interface_1_out_0x55ad0b705f90 [label="g^-1*s^-1*C_out", shape=none];
    }
    {
        rank = same;
        interface_1_out_0x55acfaae6490;
        interface_1_out_0x55ad0b705f40;
        interface_1_out_0x55ad0b705d10;
        interface_1_out_0x55acfaae64e0;
        interface_1_out_0x55ad0b705fe0;
        interface_1_out_0x55acfaae6508;
        interface_1_out_0x55ad0b705f90;
    }
    // Input 0.
    subgraph cluster_subgraph_1_in_0 {
        label = "";
        interface_1_in_0x55acfaae6490 [label="N", shape=none];
        interface_1_in_0x55ad0b705f40 [label="g", shape=none];
        interface_1_in_0x55ad0b71c528 [label="H", shape=none];
        interface_1_in_0x55ad0b705fe0 [label="k_1", shape=none];
        interface_1_in_0x55acfaae6508 [label="H", shape=none];
        interface_1_in_0x55ad0b705f90 [label="g^-1*s^-1*C_out", shape=none];
    }
    {
        rank = same;
        interface_1_in_0x55acfaae6490;
        interface_1_in_0x55ad0b705f40;
        interface_1_in_0x55ad0b71c528;
        interface_1_in_0x55ad0b705fe0;
        interface_1_in_0x55acfaae6508;
        interface_1_in_0x55ad0b705f90;
    }
    // Op's.
    op_0x55ad0b71c500 [label="Unfold"];
    // Dimension's.
    interface_1_in_0x55acfaae6490 -> interface_1_out_0x55acfaae6490 [label="N"];
    op_0x55ad0b71c500 -> interface_1_out_0x55acfaae64e0 [label="H"];
    interface_1_in_0x55acfaae6508 -> interface_1_out_0x55acfaae6508 [label="H"];
    op_0x55ad0b71c500 -> interface_1_out_0x55ad0b705d10 [label="k_1"];
    interface_1_in_0x55ad0b705f40 -> interface_1_out_0x55ad0b705f40 [label="g"];
    interface_1_in_0x55ad0b705f90 -> interface_1_out_0x55ad0b705f90 [label="g^-1*s^-1*C_out"];
    interface_1_in_0x55ad0b705fe0 -> interface_1_out_0x55ad0b705fe0 [label="k_1"];
    interface_1_in_0x55ad0b71c528 -> op_0x55ad0b71c500 [label="H"];
}

// Stage tensor.
subgraph cluster_subgraph_2 {
    label = "Subgraph 2";
    // Reductions.
    reduce_0x7ef2c8005990 [label="Sum", shape=box];
    // Output.
    subgraph cluster_subgraph_2_out {
        label = "";
        interface_2_out_0x55acfaae6490 [label="N", shape=none];
        interface_2_out_0x55ad0b705f40 [label="g", shape=none];
        interface_2_out_0x55ad0b71c528 [label="H", shape=none];
        interface_2_out_0x55ad0b705fe0 [label="k_1", shape=none];
        interface_2_out_0x55acfaae6508 [label="H", shape=none];
        interface_2_out_0x55ad0b705f90 [label="g^-1*s^-1*C_out", shape=none];
    }
    {
        rank = same;
        reduce_0x7ef2c8005990;
        interface_2_out_0x55acfaae6490;
        interface_2_out_0x55ad0b705f40;
        interface_2_out_0x55ad0b71c528;
        interface_2_out_0x55ad0b705fe0;
        interface_2_out_0x55acfaae6508;
        interface_2_out_0x55ad0b705f90;
    }
    // Input 0.
    subgraph cluster_subgraph_2_in_0 {
        label = "";
        interface_2_in_0x55acfaae6490 [label="N", shape=none];
        interface_2_in_0x55ad0b731650 [label="C_in", shape=none];
        interface_2_in_0x55ad0b71c528 [label="H", shape=none];
        interface_2_in_0x55ad0b705fe0 [label="k_1", shape=none];
        interface_2_in_0x55acfaae6508 [label="H", shape=none];
        interface_2_in_0x55ad0b705f90 [label="g^-1*s^-1*C_out", shape=none];
    }
    {
        rank = same;
        interface_2_in_0x55acfaae6490;
        interface_2_in_0x55ad0b731650;
        interface_2_in_0x55ad0b71c528;
        interface_2_in_0x55ad0b705fe0;
        interface_2_in_0x55acfaae6508;
        interface_2_in_0x55ad0b705f90;
    }
    // Op's.
    op_0x55ad0b731610 [label="Split"];
    // Dimension's.
    interface_2_in_0x55acfaae6490 -> interface_2_out_0x55acfaae6490 [label="N"];
    interface_2_in_0x55acfaae6508 -> interface_2_out_0x55acfaae6508 [label="H"];
    op_0x55ad0b731610 -> interface_2_out_0x55ad0b705f40 [label="g"];
    interface_2_in_0x55ad0b705f90 -> interface_2_out_0x55ad0b705f90 [label="g^-1*s^-1*C_out"];
    interface_2_in_0x55ad0b705fe0 -> interface_2_out_0x55ad0b705fe0 [label="k_1"];
    interface_2_in_0x55ad0b71c528 -> interface_2_out_0x55ad0b71c528 [label="H"];
    interface_2_in_0x55ad0b731650 -> op_0x55ad0b731610 [label="C_in"];
    op_0x55ad0b731610 -> reduce_0x7ef2c8005990 [label="g^-1*C_in"];
}

// Stage tensor.
subgraph cluster_subgraph_3 {
    label = "Subgraph 3";
    // Reductions.
    // Output.
    subgraph cluster_subgraph_3_out {
        label = "";
        interface_3_out_0x55acfaae6490 [label="N", shape=none];
        interface_3_out_0x55ad0b731650 [label="C_in", shape=none];
        interface_3_out_0x55ad0b71c528 [label="H", shape=none];
        interface_3_out_0x55ad0b705fe0 [label="k_1", shape=none];
        interface_3_out_0x55acfaae6508 [label="H", shape=none];
        interface_3_out_0x55ad0b705f90 [label="g^-1*s^-1*C_out", shape=none];
    }
    {
        rank = same;
        interface_3_out_0x55acfaae6490;
        interface_3_out_0x55ad0b731650;
        interface_3_out_0x55ad0b71c528;
        interface_3_out_0x55ad0b705fe0;
        interface_3_out_0x55acfaae6508;
        interface_3_out_0x55ad0b705f90;
    }
    // Input 0.
    subgraph cluster_subgraph_3_in_0 {
        label = "";
        interface_3_in_0x55acfaae6490 [label="N", shape=none];
        interface_3_in_0x55ad0b757290 [label="C_in", shape=none];
        interface_3_in_0x55ad0b71c528 [label="H", shape=none];
        interface_3_in_0x55ad0b7572e0 [label="k_1", shape=none];
        interface_3_in_0x55acfaae6508 [label="H", shape=none];
    }
    // Input 1.
    subgraph cluster_subgraph_3_in_1 {
        label = "";
        interface_3_in_0x55ad0b7572a8 [label="C_in", shape=none];
        interface_3_in_0x55ad0b7572f8 [label="k_1", shape=none];
        interface_3_in_0x55ad0b706048 [label="g^-1*s^-1*C_out", shape=none];
    }
    {
        rank = same;
        interface_3_in_0x55acfaae6490;
        interface_3_in_0x55ad0b757290;
        interface_3_in_0x55ad0b71c528;
        interface_3_in_0x55ad0b7572e0;
        interface_3_in_0x55acfaae6508;
        interface_3_in_0x55ad0b7572a8;
        interface_3_in_0x55ad0b7572f8;
        interface_3_in_0x55ad0b706048;
    }
    // Op's.
    op_0x55ad0b706010 [label="Share"];
    op_0x55ad0b7061b8 [label="Expand"];
    op_0x55ad0b757270 [label="Share"];
    op_0x55ad0b7572c0 [label="Share"];
    // Dimension's.
    interface_3_in_0x55acfaae6490 -> interface_3_out_0x55acfaae6490 [label="N"];
    interface_3_in_0x55acfaae6508 -> interface_3_out_0x55acfaae6508 [label="H"];
    op_0x55ad0b706010 -> interface_3_out_0x55ad0b705f90 [label="g^-1*s^-1*C_out"];
    op_0x55ad0b7572c0 -> interface_3_out_0x55ad0b705fe0 [label="k_1"];
    op_0x55ad0b7061b8 -> op_0x55ad0b706010 [label="g^-1*s^-1*C_out"];
    interface_3_in_0x55ad0b706048 -> op_0x55ad0b706010 [label="g^-1*s^-1*C_out"];
    interface_3_in_0x55ad0b71c528 -> interface_3_out_0x55ad0b71c528 [label="H"];
    op_0x55ad0b757270 -> interface_3_out_0x55ad0b731650 [label="C_in"];
    interface_3_in_0x55ad0b757290 -> op_0x55ad0b757270 [label="C_in"];
    interface_3_in_0x55ad0b7572a8 -> op_0x55ad0b757270 [label="C_in"];
    interface_3_in_0x55ad0b7572e0 -> op_0x55ad0b7572c0 [label="k_1"];
    interface_3_in_0x55ad0b7572f8 -> op_0x55ad0b7572c0 [label="k_1"];
}

// Stage tensor.
subgraph cluster_subgraph_4 {
    label = "Subgraph 4";
    // Reductions.
    // Output.
    subgraph cluster_subgraph_4_out {
        label = "";
        interface_4_out_0x55acfaae6490 [label="N", shape=none];
        interface_4_out_0x55ad0b757290 [label="C_in", shape=none];
        interface_4_out_0x55ad0b71c528 [label="H", shape=none];
        interface_4_out_0x55ad0b7572e0 [label="k_1", shape=none];
        interface_4_out_0x55acfaae6508 [label="H", shape=none];
    }
    {
        rank = same;
        interface_4_out_0x55acfaae6490;
        interface_4_out_0x55ad0b757290;
        interface_4_out_0x55ad0b71c528;
        interface_4_out_0x55ad0b7572e0;
        interface_4_out_0x55acfaae6508;
    }
    // Input 0.
    subgraph cluster_subgraph_4_in_0 {
        label = "";
        interface_4_in_0x55acfaae6490 [label="N", shape=none];
        interface_4_in_0x55ad0b757290 [label="C_in", shape=none];
        interface_4_in_0x55ad0b71c528 [label="H", shape=none];
        interface_4_in_0x55ad0b71c668 [label="H", shape=none];
    }
    {
        rank = same;
        interface_4_in_0x55acfaae6490;
        interface_4_in_0x55ad0b757290;
        interface_4_in_0x55ad0b71c528;
        interface_4_in_0x55ad0b71c668;
    }
    // Op's.
    op_0x55ad0b71c640 [label="Unfold"];
    // Dimension's.
    interface_4_in_0x55acfaae6490 -> interface_4_out_0x55acfaae6490 [label="N"];
    op_0x55ad0b71c640 -> interface_4_out_0x55acfaae6508 [label="H"];
    interface_4_in_0x55ad0b71c528 -> interface_4_out_0x55ad0b71c528 [label="H"];
    interface_4_in_0x55ad0b71c668 -> op_0x55ad0b71c640 [label="H"];
    interface_4_in_0x55ad0b757290 -> interface_4_out_0x55ad0b757290 [label="C_in"];
    op_0x55ad0b71c640 -> interface_4_out_0x55ad0b7572e0 [label="k_1"];
}

// Input tensor.
subgraph cluster_subgraph_5 {
    label = "Input 0";
    interface_5_out_0x55acfaae6490 [label="N", shape=none];
    interface_5_out_0x55ad0b757290 [label="C_in", shape=none];
    interface_5_out_0x55ad0b71c528 [label="H", shape=none];
    interface_5_out_0x55ad0b71c668 [label="H", shape=none];
}

interface_5_out_0x55acfaae6490 -> interface_4_in_0x55acfaae6490;
interface_5_out_0x55ad0b757290 -> interface_4_in_0x55ad0b757290;
interface_5_out_0x55ad0b71c528 -> interface_4_in_0x55ad0b71c528;
interface_5_out_0x55ad0b71c668 -> interface_4_in_0x55ad0b71c668;

interface_4_out_0x55acfaae6490 -> interface_3_in_0x55acfaae6490;
interface_4_out_0x55ad0b757290 -> interface_3_in_0x55ad0b757290;
interface_4_out_0x55ad0b71c528 -> interface_3_in_0x55ad0b71c528;
interface_4_out_0x55ad0b7572e0 -> interface_3_in_0x55ad0b7572e0;
interface_4_out_0x55acfaae6508 -> interface_3_in_0x55acfaae6508;

// Input tensor.
subgraph cluster_subgraph_6 {
    label = "Input 2";
    interface_6_out_0x55ad0b7572a8 [label="C_in", shape=none];
    interface_6_out_0x55ad0b7572f8 [label="k_1", shape=none];
    interface_6_out_0x55ad0b706048 [label="g^-1*s^-1*C_out", shape=none];
}

interface_6_out_0x55ad0b7572a8 -> interface_3_in_0x55ad0b7572a8;
interface_6_out_0x55ad0b7572f8 -> interface_3_in_0x55ad0b7572f8;
interface_6_out_0x55ad0b706048 -> interface_3_in_0x55ad0b706048;

interface_3_out_0x55acfaae6490 -> interface_2_in_0x55acfaae6490;
interface_3_out_0x55ad0b731650 -> interface_2_in_0x55ad0b731650;
interface_3_out_0x55ad0b71c528 -> interface_2_in_0x55ad0b71c528;
interface_3_out_0x55ad0b705fe0 -> interface_2_in_0x55ad0b705fe0;
interface_3_out_0x55acfaae6508 -> interface_2_in_0x55acfaae6508;
interface_3_out_0x55ad0b705f90 -> interface_2_in_0x55ad0b705f90;

interface_2_out_0x55acfaae6490 -> interface_1_in_0x55acfaae6490;
interface_2_out_0x55ad0b705f40 -> interface_1_in_0x55ad0b705f40;
interface_2_out_0x55ad0b71c528 -> interface_1_in_0x55ad0b71c528;
interface_2_out_0x55ad0b705fe0 -> interface_1_in_0x55ad0b705fe0;
interface_2_out_0x55acfaae6508 -> interface_1_in_0x55acfaae6508;
interface_2_out_0x55ad0b705f90 -> interface_1_in_0x55ad0b705f90;

interface_1_out_0x55acfaae6490 -> interface_0_in_0x55acfaae6490;
interface_1_out_0x55ad0b705f40 -> interface_0_in_0x55ad0b705f40;
interface_1_out_0x55ad0b705d10 -> interface_0_in_0x55ad0b705d10;
interface_1_out_0x55acfaae64e0 -> interface_0_in_0x55acfaae64e0;
interface_1_out_0x55ad0b705fe0 -> interface_0_in_0x55ad0b705fe0;
interface_1_out_0x55acfaae6508 -> interface_0_in_0x55acfaae6508;
interface_1_out_0x55ad0b705f90 -> interface_0_in_0x55ad0b705f90;

// Input tensor.
subgraph cluster_subgraph_7 {
    label = "Input 1";
    interface_7_out_0x55ad0b705c38 [label="C_out", shape=none];
    interface_7_out_0x55ad0b705f58 [label="g", shape=none];
    interface_7_out_0x55ad0b705d28 [label="k_1", shape=none];
    interface_7_out_0x55ad0b705ff8 [label="k_1", shape=none];
    interface_7_out_0x55ad0b705fa8 [label="g^-1*s^-1*C_out", shape=none];
}

interface_7_out_0x55ad0b705c38 -> interface_0_in_0x55ad0b705c38;
interface_7_out_0x55ad0b705f58 -> interface_0_in_0x55ad0b705f58;
interface_7_out_0x55ad0b705d28 -> interface_0_in_0x55ad0b705d28;
interface_7_out_0x55ad0b705ff8 -> interface_0_in_0x55ad0b705ff8;
interface_7_out_0x55ad0b705fa8 -> interface_0_in_0x55ad0b705fa8;

{
    rank = same;
    interface_5_out_0x55acfaae6490;
    interface_5_out_0x55ad0b757290;
    interface_5_out_0x55ad0b71c528;
    interface_5_out_0x55ad0b71c668;
    interface_7_out_0x55ad0b705c38;
    interface_7_out_0x55ad0b705f58;
    interface_7_out_0x55ad0b705d28;
    interface_7_out_0x55ad0b705ff8;
    interface_7_out_0x55ad0b705fa8;
    interface_6_out_0x55ad0b7572a8;
    interface_6_out_0x55ad0b7572f8;
    interface_6_out_0x55ad0b706048;
}
subgraph cluster_subgraph_output {
    label = "Output";
    interface_8_in_0x55acfaae6490 [label="N", shape=none];
    interface_8_in_0x55acfaae64b8 [label="C_out", shape=none];
    interface_8_in_0x55acfaae64e0 [label="H", shape=none];
    interface_8_in_0x55acfaae6508 [label="H", shape=none];
}
interface_0_out_0x55acfaae6490 -> interface_8_in_0x55acfaae6490;
interface_0_out_0x55acfaae64b8 -> interface_8_in_0x55acfaae64b8;
interface_0_out_0x55acfaae64e0 -> interface_8_in_0x55acfaae64e0;
interface_0_out_0x55acfaae6508 -> interface_8_in_0x55acfaae6508;

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

		# [H]@Unfold90ae9d8acef524e0 -> [H]@Iteratorb0a1def4ad5784ec, [k_1]@Share63a88e0da5dce9dc
		t_3 = torch.reshape(t_3, (1, 3584, 56, 1, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (1, 64, 56, 3, 56, ))

		# Perform contraction.
		t_4 = torch.einsum("ljnkm, jki -> ljnkmi", t_3, in_2)

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
		t_7 = torch.einsum("nkjompl, ikjml -> niop", t_6, in_1)

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

		# [H]@Unfold90ae9d8acef524e0 -> [H]@Iteratorb0a1def4ad5784ec, [k_1]@Share63a88e0da5dce9dc
		t_3 = torch.reshape(t_3, (1, 1792, 28, 1, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (1, 64, 28, 3, 28, ))

		# Perform contraction.
		t_4 = torch.einsum("ljnkm, jki -> ljnkmi", t_3, in_2)

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
		t_7 = torch.einsum("nkjompl, ikjml -> niop", t_6, in_1)

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

		# [H]@Unfold90ae9d8acef524e0 -> [H]@Iteratorb0a1def4ad5784ec, [k_1]@Share63a88e0da5dce9dc
		t_3 = torch.reshape(t_3, (1, 3584, 28, 1, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (1, 128, 28, 3, 28, ))

		# Perform contraction.
		t_4 = torch.einsum("ljnkm, jki -> ljnkmi", t_3, in_2)

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
		t_7 = torch.einsum("nkjompl, ikjml -> niop", t_6, in_1)

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

		# [H]@Unfold90ae9d8acef524e0 -> [H]@Iteratorb0a1def4ad5784ec, [k_1]@Share63a88e0da5dce9dc
		t_3 = torch.reshape(t_3, (1, 1792, 14, 1, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (1, 128, 14, 3, 14, ))

		# Perform contraction.
		t_4 = torch.einsum("ljnkm, jki -> ljnkmi", t_3, in_2)

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
		t_7 = torch.einsum("nkjompl, ikjml -> niop", t_6, in_1)

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

		# [H]@Unfold90ae9d8acef524e0 -> [H]@Iteratorb0a1def4ad5784ec, [k_1]@Share63a88e0da5dce9dc
		t_3 = torch.reshape(t_3, (1, 3584, 14, 1, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (1, 256, 14, 3, 14, ))

		# Perform contraction.
		t_4 = torch.einsum("ljnkm, jki -> ljnkmi", t_3, in_2)

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
		t_7 = torch.einsum("nkjompl, ikjml -> niop", t_6, in_1)

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

		# [H]@Unfold90ae9d8acef524e0 -> [H]@Iteratorb0a1def4ad5784ec, [k_1]@Share63a88e0da5dce9dc
		t_3 = torch.reshape(t_3, (1, 1792, 7, 1, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (1, 256, 7, 3, 7, ))

		# Perform contraction.
		t_4 = torch.einsum("ljnkm, jki -> ljnkmi", t_3, in_2)

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
		t_7 = torch.einsum("nkjompl, ikjml -> niop", t_6, in_1)

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

		# [H]@Unfold90ae9d8acef524e0 -> [H]@Iteratorb0a1def4ad5784ec, [k_1]@Share63a88e0da5dce9dc
		t_3 = torch.reshape(t_3, (1, 3584, 7, 1, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (1, 512, 7, 3, 7, ))

		# Perform contraction.
		t_4 = torch.einsum("ljnkm, jki -> ljnkmi", t_3, in_2)

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
		t_7 = torch.einsum("nkjompl, ikjml -> niop", t_6, in_1)

		# No need to crop the output tensor.
		y = t_7

		return y

