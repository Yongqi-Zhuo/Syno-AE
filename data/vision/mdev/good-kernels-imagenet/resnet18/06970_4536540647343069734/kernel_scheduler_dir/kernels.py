import torch
import random
"""
digraph kernel_preview {
newrank = true;

// Stage tensor.
subgraph cluster_subgraph_0 {
    label = "Subgraph 0";
    // Reductions.
    reduce_0x7f23c0001928 [label="Sum", shape=box];
    reduce_0x7f23c0001a98 [label="Sum", shape=box];
    reduce_0x7f23c0001ab0 [label="Sum", shape=box];
    reduce_0x7f23c0009288 [label="Sum", shape=box];
    // Output.
    subgraph cluster_subgraph_0_out {
        label = "";
        interface_0_out_0x5566a5448560 [label="N", shape=none];
        interface_0_out_0x5566a5448588 [label="C_out", shape=none];
        interface_0_out_0x5566a54485b0 [label="H", shape=none];
        interface_0_out_0x5566a54485d8 [label="H", shape=none];
    }
    {
        rank = same;
        reduce_0x7f23c0001928;
        reduce_0x7f23c0001a98;
        reduce_0x7f23c0001ab0;
        reduce_0x7f23c0009288;
        interface_0_out_0x5566a5448560;
        interface_0_out_0x5566a5448588;
        interface_0_out_0x5566a54485b0;
        interface_0_out_0x5566a54485d8;
    }
    // Input 0.
    subgraph cluster_subgraph_0_in_0 {
        label = "";
        interface_0_in_0x5566a5448560 [label="N", shape=none];
        interface_0_in_0x5566a540e5c0 [label="g", shape=none];
        interface_0_in_0x5566a54485b0 [label="H", shape=none];
        interface_0_in_0x5566a540e6b0 [label="k_1", shape=none];
        interface_0_in_0x5566a54485d8 [label="H", shape=none];
        interface_0_in_0x5566a540e610 [label="k_1", shape=none];
        interface_0_in_0x5566a540e660 [label="g^-1*s^-1*C_out", shape=none];
    }
    // Input 1.
    subgraph cluster_subgraph_0_in_1 {
        label = "";
        interface_0_in_0x5566a540e5d8 [label="g", shape=none];
        interface_0_in_0x5566a540e6c8 [label="k_1", shape=none];
        interface_0_in_0x5566a540e628 [label="k_1", shape=none];
        interface_0_in_0x5566a540e538 [label="C_out", shape=none];
        interface_0_in_0x5566a540e678 [label="g^-1*s^-1*C_out", shape=none];
    }
    {
        rank = same;
        interface_0_in_0x5566a5448560;
        interface_0_in_0x5566a540e5c0;
        interface_0_in_0x5566a54485b0;
        interface_0_in_0x5566a540e6b0;
        interface_0_in_0x5566a54485d8;
        interface_0_in_0x5566a540e610;
        interface_0_in_0x5566a540e660;
        interface_0_in_0x5566a540e5d8;
        interface_0_in_0x5566a540e6c8;
        interface_0_in_0x5566a540e628;
        interface_0_in_0x5566a540e538;
        interface_0_in_0x5566a540e678;
    }
    // Op's.
    op_0x5566a540e500 [label="Share"];
    op_0x5566a540e5a0 [label="Share"];
    op_0x5566a540e5f0 [label="Share"];
    op_0x5566a540e640 [label="Share"];
    op_0x5566a540e690 [label="Share"];
    op_0x5566a540eab8 [label="Expand"];
    // Dimension's.
    op_0x5566a540eab8 -> op_0x5566a540e500 [label="C_out"];
    interface_0_in_0x5566a540e538 -> op_0x5566a540e500 [label="C_out"];
    interface_0_in_0x5566a540e5c0 -> op_0x5566a540e5a0 [label="g"];
    interface_0_in_0x5566a540e5d8 -> op_0x5566a540e5a0 [label="g"];
    interface_0_in_0x5566a540e610 -> op_0x5566a540e5f0 [label="k_1"];
    interface_0_in_0x5566a540e628 -> op_0x5566a540e5f0 [label="k_1"];
    interface_0_in_0x5566a540e660 -> op_0x5566a540e640 [label="g^-1*s^-1*C_out"];
    interface_0_in_0x5566a540e678 -> op_0x5566a540e640 [label="g^-1*s^-1*C_out"];
    interface_0_in_0x5566a540e6b0 -> op_0x5566a540e690 [label="k_1"];
    interface_0_in_0x5566a540e6c8 -> op_0x5566a540e690 [label="k_1"];
    interface_0_in_0x5566a5448560 -> interface_0_out_0x5566a5448560 [label="N"];
    op_0x5566a540e500 -> interface_0_out_0x5566a5448588 [label="C_out"];
    interface_0_in_0x5566a54485b0 -> interface_0_out_0x5566a54485b0 [label="H"];
    interface_0_in_0x5566a54485d8 -> interface_0_out_0x5566a54485d8 [label="H"];
    op_0x5566a540e5a0 -> reduce_0x7f23c0001928 [label="g"];
    op_0x5566a540e5f0 -> reduce_0x7f23c0001a98 [label="k_1"];
    op_0x5566a540e690 -> reduce_0x7f23c0001ab0 [label="k_1"];
    op_0x5566a540e640 -> reduce_0x7f23c0009288 [label="g^-1*s^-1*C_out"];
}

// Stage tensor.
subgraph cluster_subgraph_1 {
    label = "Subgraph 1";
    // Reductions.
    // Output.
    subgraph cluster_subgraph_1_out {
        label = "";
        interface_1_out_0x5566a5448560 [label="N", shape=none];
        interface_1_out_0x5566a540e5c0 [label="g", shape=none];
        interface_1_out_0x5566a54485b0 [label="H", shape=none];
        interface_1_out_0x5566a540e6b0 [label="k_1", shape=none];
        interface_1_out_0x5566a54485d8 [label="H", shape=none];
        interface_1_out_0x5566a540e610 [label="k_1", shape=none];
        interface_1_out_0x5566a540e660 [label="g^-1*s^-1*C_out", shape=none];
    }
    {
        rank = same;
        interface_1_out_0x5566a5448560;
        interface_1_out_0x5566a540e5c0;
        interface_1_out_0x5566a54485b0;
        interface_1_out_0x5566a540e6b0;
        interface_1_out_0x5566a54485d8;
        interface_1_out_0x5566a540e610;
        interface_1_out_0x5566a540e660;
    }
    // Input 0.
    subgraph cluster_subgraph_1_in_0 {
        label = "";
        interface_1_in_0x5566a5448560 [label="N", shape=none];
        interface_1_in_0x5566a540e5c0 [label="g", shape=none];
        interface_1_in_0x5566a54485b0 [label="H", shape=none];
        interface_1_in_0x5566a540e6b0 [label="k_1", shape=none];
        interface_1_in_0x5566a540f520 [label="H", shape=none];
        interface_1_in_0x5566a540e660 [label="g^-1*s^-1*C_out", shape=none];
    }
    {
        rank = same;
        interface_1_in_0x5566a5448560;
        interface_1_in_0x5566a540e5c0;
        interface_1_in_0x5566a54485b0;
        interface_1_in_0x5566a540e6b0;
        interface_1_in_0x5566a540f520;
        interface_1_in_0x5566a540e660;
    }
    // Op's.
    op_0x5566a540f500 [label="Shift"];
    op_0x5566a75445c0 [label="Unfold"];
    // Dimension's.
    interface_1_in_0x5566a540e5c0 -> interface_1_out_0x5566a540e5c0 [label="g"];
    op_0x5566a75445c0 -> interface_1_out_0x5566a540e610 [label="k_1"];
    interface_1_in_0x5566a540e660 -> interface_1_out_0x5566a540e660 [label="g^-1*s^-1*C_out"];
    interface_1_in_0x5566a540e6b0 -> interface_1_out_0x5566a540e6b0 [label="k_1"];
    interface_1_in_0x5566a540f520 -> op_0x5566a540f500 [label="H"];
    interface_1_in_0x5566a5448560 -> interface_1_out_0x5566a5448560 [label="N"];
    interface_1_in_0x5566a54485b0 -> interface_1_out_0x5566a54485b0 [label="H"];
    op_0x5566a75445c0 -> interface_1_out_0x5566a54485d8 [label="H"];
    op_0x5566a540f500 -> op_0x5566a75445c0 [label="H"];
}

// Stage tensor.
subgraph cluster_subgraph_2 {
    label = "Subgraph 2";
    // Reductions.
    reduce_0x7f23c0005a90 [label="Sum", shape=box];
    // Output.
    subgraph cluster_subgraph_2_out {
        label = "";
        interface_2_out_0x5566a5448560 [label="N", shape=none];
        interface_2_out_0x5566a540e5c0 [label="g", shape=none];
        interface_2_out_0x5566a54485b0 [label="H", shape=none];
        interface_2_out_0x5566a540e6b0 [label="k_1", shape=none];
        interface_2_out_0x5566a540f520 [label="H", shape=none];
        interface_2_out_0x5566a540e660 [label="g^-1*s^-1*C_out", shape=none];
    }
    {
        rank = same;
        reduce_0x7f23c0005a90;
        interface_2_out_0x5566a5448560;
        interface_2_out_0x5566a540e5c0;
        interface_2_out_0x5566a54485b0;
        interface_2_out_0x5566a540e6b0;
        interface_2_out_0x5566a540f520;
        interface_2_out_0x5566a540e660;
    }
    // Input 0.
    subgraph cluster_subgraph_2_in_0 {
        label = "";
        interface_2_in_0x5566a5448560 [label="N", shape=none];
        interface_2_in_0x5566a5412fc0 [label="C_in", shape=none];
        interface_2_in_0x5566a54485b0 [label="H", shape=none];
        interface_2_in_0x5566a540e6b0 [label="k_1", shape=none];
        interface_2_in_0x5566a540f520 [label="H", shape=none];
        interface_2_in_0x5566a540e660 [label="g^-1*s^-1*C_out", shape=none];
    }
    {
        rank = same;
        interface_2_in_0x5566a5448560;
        interface_2_in_0x5566a5412fc0;
        interface_2_in_0x5566a54485b0;
        interface_2_in_0x5566a540e6b0;
        interface_2_in_0x5566a540f520;
        interface_2_in_0x5566a540e660;
    }
    // Op's.
    op_0x5566a5412f80 [label="Split"];
    // Dimension's.
    op_0x5566a5412f80 -> interface_2_out_0x5566a540e5c0 [label="g"];
    interface_2_in_0x5566a540e660 -> interface_2_out_0x5566a540e660 [label="g^-1*s^-1*C_out"];
    interface_2_in_0x5566a540e6b0 -> interface_2_out_0x5566a540e6b0 [label="k_1"];
    interface_2_in_0x5566a540f520 -> interface_2_out_0x5566a540f520 [label="H"];
    interface_2_in_0x5566a5412fc0 -> op_0x5566a5412f80 [label="C_in"];
    interface_2_in_0x5566a5448560 -> interface_2_out_0x5566a5448560 [label="N"];
    interface_2_in_0x5566a54485b0 -> interface_2_out_0x5566a54485b0 [label="H"];
    op_0x5566a5412f80 -> reduce_0x7f23c0005a90 [label="g^-1*C_in"];
}

// Stage tensor.
subgraph cluster_subgraph_3 {
    label = "Subgraph 3";
    // Reductions.
    // Output.
    subgraph cluster_subgraph_3_out {
        label = "";
        interface_3_out_0x5566a5448560 [label="N", shape=none];
        interface_3_out_0x5566a5412fc0 [label="C_in", shape=none];
        interface_3_out_0x5566a54485b0 [label="H", shape=none];
        interface_3_out_0x5566a540e6b0 [label="k_1", shape=none];
        interface_3_out_0x5566a540f520 [label="H", shape=none];
        interface_3_out_0x5566a540e660 [label="g^-1*s^-1*C_out", shape=none];
    }
    {
        rank = same;
        interface_3_out_0x5566a5448560;
        interface_3_out_0x5566a5412fc0;
        interface_3_out_0x5566a54485b0;
        interface_3_out_0x5566a540e6b0;
        interface_3_out_0x5566a540f520;
        interface_3_out_0x5566a540e660;
    }
    // Input 0.
    subgraph cluster_subgraph_3_in_0 {
        label = "";
        interface_3_in_0x5566a5448560 [label="N", shape=none];
        interface_3_in_0x5566a540e890 [label="C_in", shape=none];
        interface_3_in_0x5566a54485b0 [label="H", shape=none];
        interface_3_in_0x5566a54cb2b0 [label="k_1", shape=none];
        interface_3_in_0x5566a540f520 [label="H", shape=none];
    }
    // Input 1.
    subgraph cluster_subgraph_3_in_1 {
        label = "";
        interface_3_in_0x5566a540e8a8 [label="C_in", shape=none];
        interface_3_in_0x5566a54cb2c8 [label="k_1", shape=none];
        interface_3_in_0x5566a540e718 [label="g^-1*s^-1*C_out", shape=none];
    }
    {
        rank = same;
        interface_3_in_0x5566a5448560;
        interface_3_in_0x5566a540e890;
        interface_3_in_0x5566a54485b0;
        interface_3_in_0x5566a54cb2b0;
        interface_3_in_0x5566a540f520;
        interface_3_in_0x5566a540e8a8;
        interface_3_in_0x5566a54cb2c8;
        interface_3_in_0x5566a540e718;
    }
    // Op's.
    op_0x5566a540e6e0 [label="Share"];
    op_0x5566a540e870 [label="Share"];
    op_0x5566a540ead8 [label="Expand"];
    op_0x5566a54cb290 [label="Share"];
    // Dimension's.
    op_0x5566a540e6e0 -> interface_3_out_0x5566a540e660 [label="g^-1*s^-1*C_out"];
    op_0x5566a54cb290 -> interface_3_out_0x5566a540e6b0 [label="k_1"];
    op_0x5566a540ead8 -> op_0x5566a540e6e0 [label="g^-1*s^-1*C_out"];
    interface_3_in_0x5566a540e718 -> op_0x5566a540e6e0 [label="g^-1*s^-1*C_out"];
    interface_3_in_0x5566a540e890 -> op_0x5566a540e870 [label="C_in"];
    interface_3_in_0x5566a540e8a8 -> op_0x5566a540e870 [label="C_in"];
    interface_3_in_0x5566a540f520 -> interface_3_out_0x5566a540f520 [label="H"];
    op_0x5566a540e870 -> interface_3_out_0x5566a5412fc0 [label="C_in"];
    interface_3_in_0x5566a5448560 -> interface_3_out_0x5566a5448560 [label="N"];
    interface_3_in_0x5566a54485b0 -> interface_3_out_0x5566a54485b0 [label="H"];
    interface_3_in_0x5566a54cb2b0 -> op_0x5566a54cb290 [label="k_1"];
    interface_3_in_0x5566a54cb2c8 -> op_0x5566a54cb290 [label="k_1"];
}

// Stage tensor.
subgraph cluster_subgraph_4 {
    label = "Subgraph 4";
    // Reductions.
    // Output.
    subgraph cluster_subgraph_4_out {
        label = "";
        interface_4_out_0x5566a5448560 [label="N", shape=none];
        interface_4_out_0x5566a540e890 [label="C_in", shape=none];
        interface_4_out_0x5566a54485b0 [label="H", shape=none];
        interface_4_out_0x5566a54cb2b0 [label="k_1", shape=none];
        interface_4_out_0x5566a540f520 [label="H", shape=none];
    }
    {
        rank = same;
        interface_4_out_0x5566a5448560;
        interface_4_out_0x5566a540e890;
        interface_4_out_0x5566a54485b0;
        interface_4_out_0x5566a54cb2b0;
        interface_4_out_0x5566a540f520;
    }
    // Input 0.
    subgraph cluster_subgraph_4_in_0 {
        label = "";
        interface_4_in_0x5566a5448560 [label="N", shape=none];
        interface_4_in_0x5566a540e890 [label="C_in", shape=none];
        interface_4_in_0x5566a540f6d0 [label="H", shape=none];
        interface_4_in_0x5566a540f520 [label="H", shape=none];
    }
    {
        rank = same;
        interface_4_in_0x5566a5448560;
        interface_4_in_0x5566a540e890;
        interface_4_in_0x5566a540f6d0;
        interface_4_in_0x5566a540f520;
    }
    // Op's.
    op_0x5566a540f6b0 [label="Shift"];
    op_0x5566a754d800 [label="Unfold"];
    // Dimension's.
    interface_4_in_0x5566a540e890 -> interface_4_out_0x5566a540e890 [label="C_in"];
    interface_4_in_0x5566a540f520 -> interface_4_out_0x5566a540f520 [label="H"];
    interface_4_in_0x5566a540f6d0 -> op_0x5566a540f6b0 [label="H"];
    interface_4_in_0x5566a5448560 -> interface_4_out_0x5566a5448560 [label="N"];
    op_0x5566a754d800 -> interface_4_out_0x5566a54485b0 [label="H"];
    op_0x5566a754d800 -> interface_4_out_0x5566a54cb2b0 [label="k_1"];
    op_0x5566a540f6b0 -> op_0x5566a754d800 [label="H"];
}

// Input tensor.
subgraph cluster_subgraph_5 {
    label = "Input 0";
    interface_5_out_0x5566a5448560 [label="N", shape=none];
    interface_5_out_0x5566a540e890 [label="C_in", shape=none];
    interface_5_out_0x5566a540f6d0 [label="H", shape=none];
    interface_5_out_0x5566a540f520 [label="H", shape=none];
}

interface_5_out_0x5566a5448560 -> interface_4_in_0x5566a5448560;
interface_5_out_0x5566a540e890 -> interface_4_in_0x5566a540e890;
interface_5_out_0x5566a540f6d0 -> interface_4_in_0x5566a540f6d0;
interface_5_out_0x5566a540f520 -> interface_4_in_0x5566a540f520;

interface_4_out_0x5566a5448560 -> interface_3_in_0x5566a5448560;
interface_4_out_0x5566a540e890 -> interface_3_in_0x5566a540e890;
interface_4_out_0x5566a54485b0 -> interface_3_in_0x5566a54485b0;
interface_4_out_0x5566a54cb2b0 -> interface_3_in_0x5566a54cb2b0;
interface_4_out_0x5566a540f520 -> interface_3_in_0x5566a540f520;

// Input tensor.
subgraph cluster_subgraph_6 {
    label = "Input 2";
    interface_6_out_0x5566a540e8a8 [label="C_in", shape=none];
    interface_6_out_0x5566a54cb2c8 [label="k_1", shape=none];
    interface_6_out_0x5566a540e718 [label="g^-1*s^-1*C_out", shape=none];
}

interface_6_out_0x5566a540e8a8 -> interface_3_in_0x5566a540e8a8;
interface_6_out_0x5566a54cb2c8 -> interface_3_in_0x5566a54cb2c8;
interface_6_out_0x5566a540e718 -> interface_3_in_0x5566a540e718;

interface_3_out_0x5566a5448560 -> interface_2_in_0x5566a5448560;
interface_3_out_0x5566a5412fc0 -> interface_2_in_0x5566a5412fc0;
interface_3_out_0x5566a54485b0 -> interface_2_in_0x5566a54485b0;
interface_3_out_0x5566a540e6b0 -> interface_2_in_0x5566a540e6b0;
interface_3_out_0x5566a540f520 -> interface_2_in_0x5566a540f520;
interface_3_out_0x5566a540e660 -> interface_2_in_0x5566a540e660;

interface_2_out_0x5566a5448560 -> interface_1_in_0x5566a5448560;
interface_2_out_0x5566a540e5c0 -> interface_1_in_0x5566a540e5c0;
interface_2_out_0x5566a54485b0 -> interface_1_in_0x5566a54485b0;
interface_2_out_0x5566a540e6b0 -> interface_1_in_0x5566a540e6b0;
interface_2_out_0x5566a540f520 -> interface_1_in_0x5566a540f520;
interface_2_out_0x5566a540e660 -> interface_1_in_0x5566a540e660;

interface_1_out_0x5566a5448560 -> interface_0_in_0x5566a5448560;
interface_1_out_0x5566a540e5c0 -> interface_0_in_0x5566a540e5c0;
interface_1_out_0x5566a54485b0 -> interface_0_in_0x5566a54485b0;
interface_1_out_0x5566a540e6b0 -> interface_0_in_0x5566a540e6b0;
interface_1_out_0x5566a54485d8 -> interface_0_in_0x5566a54485d8;
interface_1_out_0x5566a540e610 -> interface_0_in_0x5566a540e610;
interface_1_out_0x5566a540e660 -> interface_0_in_0x5566a540e660;

// Input tensor.
subgraph cluster_subgraph_7 {
    label = "Input 1";
    interface_7_out_0x5566a540e5d8 [label="g", shape=none];
    interface_7_out_0x5566a540e6c8 [label="k_1", shape=none];
    interface_7_out_0x5566a540e628 [label="k_1", shape=none];
    interface_7_out_0x5566a540e538 [label="C_out", shape=none];
    interface_7_out_0x5566a540e678 [label="g^-1*s^-1*C_out", shape=none];
}

interface_7_out_0x5566a540e5d8 -> interface_0_in_0x5566a540e5d8;
interface_7_out_0x5566a540e6c8 -> interface_0_in_0x5566a540e6c8;
interface_7_out_0x5566a540e628 -> interface_0_in_0x5566a540e628;
interface_7_out_0x5566a540e538 -> interface_0_in_0x5566a540e538;
interface_7_out_0x5566a540e678 -> interface_0_in_0x5566a540e678;

{
    rank = same;
    interface_5_out_0x5566a5448560;
    interface_5_out_0x5566a540e890;
    interface_5_out_0x5566a540f6d0;
    interface_5_out_0x5566a540f520;
    interface_7_out_0x5566a540e5d8;
    interface_7_out_0x5566a540e6c8;
    interface_7_out_0x5566a540e628;
    interface_7_out_0x5566a540e538;
    interface_7_out_0x5566a540e678;
    interface_6_out_0x5566a540e8a8;
    interface_6_out_0x5566a54cb2c8;
    interface_6_out_0x5566a540e718;
}
subgraph cluster_subgraph_output {
    label = "Output";
    interface_8_in_0x5566a5448560 [label="N", shape=none];
    interface_8_in_0x5566a5448588 [label="C_out", shape=none];
    interface_8_in_0x5566a54485b0 [label="H", shape=none];
    interface_8_in_0x5566a54485d8 [label="H", shape=none];
}
interface_0_out_0x5566a5448560 -> interface_8_in_0x5566a5448560;
interface_0_out_0x5566a5448588 -> interface_8_in_0x5566a5448588;
interface_0_out_0x5566a54485b0 -> interface_8_in_0x5566a54485b0;
interface_0_out_0x5566a54485d8 -> interface_8_in_0x5566a54485d8;

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
		t_3 = torch.reshape(t_3, (1024, 64, 56, 56, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (1024, 64, 3, 56, 56, ))

		# Permute to match the output of this subgraph.
		t_3 = torch.permute(t_3, (0, 1, 3, 2, 4, ))

		# Perform contraction.
		t_4 = torch.einsum("mjnkl, jki -> mjnkli", t_3, in_2)

		# No contraction needed.
		t_5 = t_4

		# [C_in]@Splitc2d52f3525ba6cc4 -> [g]@Sharec7a8ce455b828537, [g^-1*C_in]@Reduceef9903cafc29eea1
		t_5 = torch.reshape(t_5, (1024, 32, 2, 56, 3, 56, 1, ))

		# [g^-1*C_in]@Reduce
		t_5 = torch.sum(t_5, dim=(2, ))

		# No contraction needed.
		t_6 = t_5

		# [H]@Shiftdbd5b2e652804221 -> [H]@Unfold0063bc810b9e1e60
		t_6 = torch.roll(t_6, self.shift_direction, 4)

		# [H]@Unfold0063bc810b9e1e60 -> [H]@Iteratorb0a1def4ad5784ec, [k_1]@Share26cfa48d169008e4
		t_6 = torch.reshape(t_6, (1024, 5376, 56, 1, ))
		t_6 = torch.nn.functional.unfold(t_6, (3, 1, ), padding=(1, 0, ))
		t_6 = torch.reshape(t_6, (1024, 32, 56, 3, 3, 56, 1, ))

		# Permute to match the output of this subgraph.
		t_6 = torch.permute(t_6, (0, 1, 2, 3, 5, 4, 6, ))

		# Perform contraction.
		t_7 = torch.einsum("njompkl, jmkil -> nopi", t_6, in_1)

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
		t_3 = torch.reshape(t_3, (1024, 64, 28, 28, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (1024, 64, 3, 28, 28, ))

		# Permute to match the output of this subgraph.
		t_3 = torch.permute(t_3, (0, 1, 3, 2, 4, ))

		# Perform contraction.
		t_4 = torch.einsum("mjnkl, jki -> mjnkli", t_3, in_2)

		# No contraction needed.
		t_5 = t_4

		# [C_in]@Splitc2d52f3525ba6cc4 -> [g]@Sharec7a8ce455b828537, [g^-1*C_in]@Reduceef9903cafc29eea1
		t_5 = torch.reshape(t_5, (1024, 32, 2, 28, 3, 28, 2, ))

		# [g^-1*C_in]@Reduce
		t_5 = torch.sum(t_5, dim=(2, ))

		# No contraction needed.
		t_6 = t_5

		# [H]@Shiftdbd5b2e652804221 -> [H]@Unfold0063bc810b9e1e60
		t_6 = torch.roll(t_6, self.shift_direction, 4)

		# [H]@Unfold0063bc810b9e1e60 -> [H]@Iteratorb0a1def4ad5784ec, [k_1]@Share26cfa48d169008e4
		t_6 = torch.reshape(t_6, (1024, 2688, 28, 2, ))
		t_6 = torch.nn.functional.unfold(t_6, (3, 1, ), padding=(1, 0, ))
		t_6 = torch.reshape(t_6, (1024, 32, 28, 3, 3, 28, 2, ))

		# Permute to match the output of this subgraph.
		t_6 = torch.permute(t_6, (0, 1, 2, 3, 5, 4, 6, ))

		# Perform contraction.
		t_7 = torch.einsum("njompkl, jmkil -> nopi", t_6, in_1)

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
		t_3 = torch.reshape(t_3, (1024, 128, 28, 28, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (1024, 128, 3, 28, 28, ))

		# Permute to match the output of this subgraph.
		t_3 = torch.permute(t_3, (0, 1, 3, 2, 4, ))

		# Perform contraction.
		t_4 = torch.einsum("mjnkl, jki -> mjnkli", t_3, in_2)

		# No contraction needed.
		t_5 = t_4

		# [C_in]@Splitc2d52f3525ba6cc4 -> [g]@Sharec7a8ce455b828537, [g^-1*C_in]@Reduceef9903cafc29eea1
		t_5 = torch.reshape(t_5, (1024, 32, 4, 28, 3, 28, 2, ))

		# [g^-1*C_in]@Reduce
		t_5 = torch.sum(t_5, dim=(2, ))

		# No contraction needed.
		t_6 = t_5

		# [H]@Shiftdbd5b2e652804221 -> [H]@Unfold0063bc810b9e1e60
		t_6 = torch.roll(t_6, self.shift_direction, 4)

		# [H]@Unfold0063bc810b9e1e60 -> [H]@Iteratorb0a1def4ad5784ec, [k_1]@Share26cfa48d169008e4
		t_6 = torch.reshape(t_6, (1024, 2688, 28, 2, ))
		t_6 = torch.nn.functional.unfold(t_6, (3, 1, ), padding=(1, 0, ))
		t_6 = torch.reshape(t_6, (1024, 32, 28, 3, 3, 28, 2, ))

		# Permute to match the output of this subgraph.
		t_6 = torch.permute(t_6, (0, 1, 2, 3, 5, 4, 6, ))

		# Perform contraction.
		t_7 = torch.einsum("njompkl, jmkil -> nopi", t_6, in_1)

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
		t_3 = torch.reshape(t_3, (1024, 128, 14, 14, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (1024, 128, 3, 14, 14, ))

		# Permute to match the output of this subgraph.
		t_3 = torch.permute(t_3, (0, 1, 3, 2, 4, ))

		# Perform contraction.
		t_4 = torch.einsum("mjnkl, jki -> mjnkli", t_3, in_2)

		# No contraction needed.
		t_5 = t_4

		# [C_in]@Splitc2d52f3525ba6cc4 -> [g]@Sharec7a8ce455b828537, [g^-1*C_in]@Reduceef9903cafc29eea1
		t_5 = torch.reshape(t_5, (1024, 32, 4, 14, 3, 14, 4, ))

		# [g^-1*C_in]@Reduce
		t_5 = torch.sum(t_5, dim=(2, ))

		# No contraction needed.
		t_6 = t_5

		# [H]@Shiftdbd5b2e652804221 -> [H]@Unfold0063bc810b9e1e60
		t_6 = torch.roll(t_6, self.shift_direction, 4)

		# [H]@Unfold0063bc810b9e1e60 -> [H]@Iteratorb0a1def4ad5784ec, [k_1]@Share26cfa48d169008e4
		t_6 = torch.reshape(t_6, (1024, 1344, 14, 4, ))
		t_6 = torch.nn.functional.unfold(t_6, (3, 1, ), padding=(1, 0, ))
		t_6 = torch.reshape(t_6, (1024, 32, 14, 3, 3, 14, 4, ))

		# Permute to match the output of this subgraph.
		t_6 = torch.permute(t_6, (0, 1, 2, 3, 5, 4, 6, ))

		# Perform contraction.
		t_7 = torch.einsum("njompkl, jmkil -> nopi", t_6, in_1)

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
		t_3 = torch.reshape(t_3, (1024, 256, 14, 14, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (1024, 256, 3, 14, 14, ))

		# Permute to match the output of this subgraph.
		t_3 = torch.permute(t_3, (0, 1, 3, 2, 4, ))

		# Perform contraction.
		t_4 = torch.einsum("mjnkl, jki -> mjnkli", t_3, in_2)

		# No contraction needed.
		t_5 = t_4

		# [C_in]@Splitc2d52f3525ba6cc4 -> [g]@Sharec7a8ce455b828537, [g^-1*C_in]@Reduceef9903cafc29eea1
		t_5 = torch.reshape(t_5, (1024, 32, 8, 14, 3, 14, 4, ))

		# [g^-1*C_in]@Reduce
		t_5 = torch.sum(t_5, dim=(2, ))

		# No contraction needed.
		t_6 = t_5

		# [H]@Shiftdbd5b2e652804221 -> [H]@Unfold0063bc810b9e1e60
		t_6 = torch.roll(t_6, self.shift_direction, 4)

		# [H]@Unfold0063bc810b9e1e60 -> [H]@Iteratorb0a1def4ad5784ec, [k_1]@Share26cfa48d169008e4
		t_6 = torch.reshape(t_6, (1024, 1344, 14, 4, ))
		t_6 = torch.nn.functional.unfold(t_6, (3, 1, ), padding=(1, 0, ))
		t_6 = torch.reshape(t_6, (1024, 32, 14, 3, 3, 14, 4, ))

		# Permute to match the output of this subgraph.
		t_6 = torch.permute(t_6, (0, 1, 2, 3, 5, 4, 6, ))

		# Perform contraction.
		t_7 = torch.einsum("njompkl, jmkil -> nopi", t_6, in_1)

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
		t_3 = torch.reshape(t_3, (1024, 256, 7, 7, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (1024, 256, 3, 7, 7, ))

		# Permute to match the output of this subgraph.
		t_3 = torch.permute(t_3, (0, 1, 3, 2, 4, ))

		# Perform contraction.
		t_4 = torch.einsum("mjnkl, jki -> mjnkli", t_3, in_2)

		# No contraction needed.
		t_5 = t_4

		# [C_in]@Splitc2d52f3525ba6cc4 -> [g]@Sharec7a8ce455b828537, [g^-1*C_in]@Reduceef9903cafc29eea1
		t_5 = torch.reshape(t_5, (1024, 32, 8, 7, 3, 7, 8, ))

		# [g^-1*C_in]@Reduce
		t_5 = torch.sum(t_5, dim=(2, ))

		# No contraction needed.
		t_6 = t_5

		# [H]@Shiftdbd5b2e652804221 -> [H]@Unfold0063bc810b9e1e60
		t_6 = torch.roll(t_6, self.shift_direction, 4)

		# [H]@Unfold0063bc810b9e1e60 -> [H]@Iteratorb0a1def4ad5784ec, [k_1]@Share26cfa48d169008e4
		t_6 = torch.reshape(t_6, (1024, 672, 7, 8, ))
		t_6 = torch.nn.functional.unfold(t_6, (3, 1, ), padding=(1, 0, ))
		t_6 = torch.reshape(t_6, (1024, 32, 7, 3, 3, 7, 8, ))

		# Permute to match the output of this subgraph.
		t_6 = torch.permute(t_6, (0, 1, 2, 3, 5, 4, 6, ))

		# Perform contraction.
		t_7 = torch.einsum("njompkl, jmkil -> nopi", t_6, in_1)

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
		t_3 = torch.reshape(t_3, (1024, 512, 7, 7, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (1024, 512, 3, 7, 7, ))

		# Permute to match the output of this subgraph.
		t_3 = torch.permute(t_3, (0, 1, 3, 2, 4, ))

		# Perform contraction.
		t_4 = torch.einsum("mjnkl, jki -> mjnkli", t_3, in_2)

		# No contraction needed.
		t_5 = t_4

		# [C_in]@Splitc2d52f3525ba6cc4 -> [g]@Sharec7a8ce455b828537, [g^-1*C_in]@Reduceef9903cafc29eea1
		t_5 = torch.reshape(t_5, (1024, 32, 16, 7, 3, 7, 8, ))

		# [g^-1*C_in]@Reduce
		t_5 = torch.sum(t_5, dim=(2, ))

		# No contraction needed.
		t_6 = t_5

		# [H]@Shiftdbd5b2e652804221 -> [H]@Unfold0063bc810b9e1e60
		t_6 = torch.roll(t_6, self.shift_direction, 4)

		# [H]@Unfold0063bc810b9e1e60 -> [H]@Iteratorb0a1def4ad5784ec, [k_1]@Share26cfa48d169008e4
		t_6 = torch.reshape(t_6, (1024, 672, 7, 8, ))
		t_6 = torch.nn.functional.unfold(t_6, (3, 1, ), padding=(1, 0, ))
		t_6 = torch.reshape(t_6, (1024, 32, 7, 3, 3, 7, 8, ))

		# Permute to match the output of this subgraph.
		t_6 = torch.permute(t_6, (0, 1, 2, 3, 5, 4, 6, ))

		# Perform contraction.
		t_7 = torch.einsum("njompkl, jmkil -> nopi", t_6, in_1)

		# Permute to match the output of this subgraph.
		t_7 = torch.permute(t_7, (0, 3, 1, 2, ))

		# No need to crop the output tensor.
		y = t_7

		return y

