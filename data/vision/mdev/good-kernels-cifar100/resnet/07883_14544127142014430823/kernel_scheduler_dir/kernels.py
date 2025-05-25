import torch
import random
"""
digraph kernel_preview {
newrank = true;

// Stage tensor.
subgraph cluster_subgraph_0 {
    label = "Subgraph 0";
    // Reductions.
    reduce_0x7f8730001828 [label="Sum", shape=box];
    reduce_0x7f8730001998 [label="Sum", shape=box];
    reduce_0x7f87300019b0 [label="Sum", shape=box];
    reduce_0x7f8730009288 [label="Sum", shape=box];
    // Output.
    subgraph cluster_subgraph_0_out {
        label = "";
        interface_0_out_0x55e70de1f230 [label="N", shape=none];
        interface_0_out_0x55e70de1f258 [label="C_out", shape=none];
        interface_0_out_0x55e70de1f280 [label="H", shape=none];
        interface_0_out_0x55e70de1f2a8 [label="H", shape=none];
    }
    {
        rank = same;
        reduce_0x7f8730001828;
        reduce_0x7f8730001998;
        reduce_0x7f87300019b0;
        reduce_0x7f8730009288;
        interface_0_out_0x55e70de1f230;
        interface_0_out_0x55e70de1f258;
        interface_0_out_0x55e70de1f280;
        interface_0_out_0x55e70de1f2a8;
    }
    // Input 0.
    subgraph cluster_subgraph_0_in_0 {
        label = "";
        interface_0_in_0x55e70de1f230 [label="N", shape=none];
        interface_0_in_0x7f8de8004620 [label="g", shape=none];
        interface_0_in_0x55e70de1f280 [label="H", shape=none];
        interface_0_in_0x7f8e740056d0 [label="k_1", shape=none];
        interface_0_in_0x55e70de1f2a8 [label="H", shape=none];
        interface_0_in_0x7f8e74004820 [label="k_1", shape=none];
        interface_0_in_0x7f8e74004d70 [label="g^-1*s^-1*C_out", shape=none];
    }
    // Input 1.
    subgraph cluster_subgraph_0_in_1 {
        label = "";
        interface_0_in_0x7f8de8004638 [label="g", shape=none];
        interface_0_in_0x7f8e740056e8 [label="k_1", shape=none];
        interface_0_in_0x7f8e74004838 [label="k_1", shape=none];
        interface_0_in_0x7f8ec8004238 [label="C_out", shape=none];
        interface_0_in_0x7f8e74004d88 [label="g^-1*s^-1*C_out", shape=none];
    }
    {
        rank = same;
        interface_0_in_0x55e70de1f230;
        interface_0_in_0x7f8de8004620;
        interface_0_in_0x55e70de1f280;
        interface_0_in_0x7f8e740056d0;
        interface_0_in_0x55e70de1f2a8;
        interface_0_in_0x7f8e74004820;
        interface_0_in_0x7f8e74004d70;
        interface_0_in_0x7f8de8004638;
        interface_0_in_0x7f8e740056e8;
        interface_0_in_0x7f8e74004838;
        interface_0_in_0x7f8ec8004238;
        interface_0_in_0x7f8e74004d88;
    }
    // Op's.
    op_0x7f8de8004600 [label="Share"];
    op_0x7f8e74004800 [label="Share"];
    op_0x7f8e74004d50 [label="Share"];
    op_0x7f8e740056b0 [label="Share"];
    op_0x7f8ec8004200 [label="Share"];
    op_0x7f8ec8004938 [label="Expand"];
    // Dimension's.
    interface_0_in_0x55e70de1f230 -> interface_0_out_0x55e70de1f230 [label="N"];
    op_0x7f8ec8004200 -> interface_0_out_0x55e70de1f258 [label="C_out"];
    interface_0_in_0x55e70de1f280 -> interface_0_out_0x55e70de1f280 [label="H"];
    interface_0_in_0x55e70de1f2a8 -> interface_0_out_0x55e70de1f2a8 [label="H"];
    op_0x7f8de8004600 -> reduce_0x7f8730001828 [label="g"];
    op_0x7f8e74004800 -> reduce_0x7f8730001998 [label="k_1"];
    op_0x7f8e740056b0 -> reduce_0x7f87300019b0 [label="k_1"];
    op_0x7f8e74004d50 -> reduce_0x7f8730009288 [label="g^-1*s^-1*C_out"];
    interface_0_in_0x7f8de8004620 -> op_0x7f8de8004600 [label="g"];
    interface_0_in_0x7f8de8004638 -> op_0x7f8de8004600 [label="g"];
    interface_0_in_0x7f8e74004820 -> op_0x7f8e74004800 [label="k_1"];
    interface_0_in_0x7f8e74004838 -> op_0x7f8e74004800 [label="k_1"];
    interface_0_in_0x7f8e74004d70 -> op_0x7f8e74004d50 [label="g^-1*s^-1*C_out"];
    interface_0_in_0x7f8e74004d88 -> op_0x7f8e74004d50 [label="g^-1*s^-1*C_out"];
    interface_0_in_0x7f8e740056d0 -> op_0x7f8e740056b0 [label="k_1"];
    interface_0_in_0x7f8e740056e8 -> op_0x7f8e740056b0 [label="k_1"];
    op_0x7f8ec8004938 -> op_0x7f8ec8004200 [label="C_out"];
    interface_0_in_0x7f8ec8004238 -> op_0x7f8ec8004200 [label="C_out"];
}

// Stage tensor.
subgraph cluster_subgraph_1 {
    label = "Subgraph 1";
    // Reductions.
    // Output.
    subgraph cluster_subgraph_1_out {
        label = "";
        interface_1_out_0x55e70de1f230 [label="N", shape=none];
        interface_1_out_0x7f8de8004620 [label="g", shape=none];
        interface_1_out_0x55e70de1f280 [label="H", shape=none];
        interface_1_out_0x7f8e740056d0 [label="k_1", shape=none];
        interface_1_out_0x55e70de1f2a8 [label="H", shape=none];
        interface_1_out_0x7f8e74004820 [label="k_1", shape=none];
        interface_1_out_0x7f8e74004d70 [label="g^-1*s^-1*C_out", shape=none];
    }
    {
        rank = same;
        interface_1_out_0x55e70de1f230;
        interface_1_out_0x7f8de8004620;
        interface_1_out_0x55e70de1f280;
        interface_1_out_0x7f8e740056d0;
        interface_1_out_0x55e70de1f2a8;
        interface_1_out_0x7f8e74004820;
        interface_1_out_0x7f8e74004d70;
    }
    // Input 0.
    subgraph cluster_subgraph_1_in_0 {
        label = "";
        interface_1_in_0x55e70de1f230 [label="N", shape=none];
        interface_1_in_0x7f8de8004620 [label="g", shape=none];
        interface_1_in_0x7f88e804a870 [label="H", shape=none];
        interface_1_in_0x55e70de1f2a8 [label="H", shape=none];
        interface_1_in_0x7f8e74004820 [label="k_1", shape=none];
        interface_1_in_0x7f8e74004d70 [label="g^-1*s^-1*C_out", shape=none];
    }
    {
        rank = same;
        interface_1_in_0x55e70de1f230;
        interface_1_in_0x7f8de8004620;
        interface_1_in_0x7f88e804a870;
        interface_1_in_0x55e70de1f2a8;
        interface_1_in_0x7f8e74004820;
        interface_1_in_0x7f8e74004d70;
    }
    // Op's.
    op_0x7f88e804a850 [label="Shift"];
    op_0x7f895400cfc0 [label="Unfold"];
    // Dimension's.
    interface_1_in_0x55e70de1f230 -> interface_1_out_0x55e70de1f230 [label="N"];
    op_0x7f895400cfc0 -> interface_1_out_0x55e70de1f280 [label="H"];
    interface_1_in_0x55e70de1f2a8 -> interface_1_out_0x55e70de1f2a8 [label="H"];
    interface_1_in_0x7f88e804a870 -> op_0x7f88e804a850 [label="H"];
    op_0x7f88e804a850 -> op_0x7f895400cfc0 [label="H"];
    interface_1_in_0x7f8de8004620 -> interface_1_out_0x7f8de8004620 [label="g"];
    interface_1_in_0x7f8e74004820 -> interface_1_out_0x7f8e74004820 [label="k_1"];
    interface_1_in_0x7f8e74004d70 -> interface_1_out_0x7f8e74004d70 [label="g^-1*s^-1*C_out"];
    op_0x7f895400cfc0 -> interface_1_out_0x7f8e740056d0 [label="k_1"];
}

// Stage tensor.
subgraph cluster_subgraph_2 {
    label = "Subgraph 2";
    // Reductions.
    reduce_0x7f8730005b90 [label="Sum", shape=box];
    // Output.
    subgraph cluster_subgraph_2_out {
        label = "";
        interface_2_out_0x55e70de1f230 [label="N", shape=none];
        interface_2_out_0x7f8de8004620 [label="g", shape=none];
        interface_2_out_0x7f88e804a870 [label="H", shape=none];
        interface_2_out_0x55e70de1f2a8 [label="H", shape=none];
        interface_2_out_0x7f8e74004820 [label="k_1", shape=none];
        interface_2_out_0x7f8e74004d70 [label="g^-1*s^-1*C_out", shape=none];
    }
    {
        rank = same;
        reduce_0x7f8730005b90;
        interface_2_out_0x55e70de1f230;
        interface_2_out_0x7f8de8004620;
        interface_2_out_0x7f88e804a870;
        interface_2_out_0x55e70de1f2a8;
        interface_2_out_0x7f8e74004820;
        interface_2_out_0x7f8e74004d70;
    }
    // Input 0.
    subgraph cluster_subgraph_2_in_0 {
        label = "";
        interface_2_in_0x55e70de1f230 [label="N", shape=none];
        interface_2_in_0x7f8eac01f970 [label="C_in", shape=none];
        interface_2_in_0x7f88e804a870 [label="H", shape=none];
        interface_2_in_0x55e70de1f2a8 [label="H", shape=none];
        interface_2_in_0x7f8e74004820 [label="k_1", shape=none];
        interface_2_in_0x7f8e74004d70 [label="g^-1*s^-1*C_out", shape=none];
    }
    {
        rank = same;
        interface_2_in_0x55e70de1f230;
        interface_2_in_0x7f8eac01f970;
        interface_2_in_0x7f88e804a870;
        interface_2_in_0x55e70de1f2a8;
        interface_2_in_0x7f8e74004820;
        interface_2_in_0x7f8e74004d70;
    }
    // Op's.
    op_0x7f8eac01f930 [label="Split"];
    // Dimension's.
    interface_2_in_0x55e70de1f230 -> interface_2_out_0x55e70de1f230 [label="N"];
    interface_2_in_0x55e70de1f2a8 -> interface_2_out_0x55e70de1f2a8 [label="H"];
    op_0x7f8eac01f930 -> reduce_0x7f8730005b90 [label="g^-1*C_in"];
    interface_2_in_0x7f88e804a870 -> interface_2_out_0x7f88e804a870 [label="H"];
    op_0x7f8eac01f930 -> interface_2_out_0x7f8de8004620 [label="g"];
    interface_2_in_0x7f8e74004820 -> interface_2_out_0x7f8e74004820 [label="k_1"];
    interface_2_in_0x7f8e74004d70 -> interface_2_out_0x7f8e74004d70 [label="g^-1*s^-1*C_out"];
    interface_2_in_0x7f8eac01f970 -> op_0x7f8eac01f930 [label="C_in"];
}

// Stage tensor.
subgraph cluster_subgraph_3 {
    label = "Subgraph 3";
    // Reductions.
    // Output.
    subgraph cluster_subgraph_3_out {
        label = "";
        interface_3_out_0x55e70de1f230 [label="N", shape=none];
        interface_3_out_0x7f8eac01f970 [label="C_in", shape=none];
        interface_3_out_0x7f88e804a870 [label="H", shape=none];
        interface_3_out_0x55e70de1f2a8 [label="H", shape=none];
        interface_3_out_0x7f8e74004820 [label="k_1", shape=none];
        interface_3_out_0x7f8e74004d70 [label="g^-1*s^-1*C_out", shape=none];
    }
    {
        rank = same;
        interface_3_out_0x55e70de1f230;
        interface_3_out_0x7f8eac01f970;
        interface_3_out_0x7f88e804a870;
        interface_3_out_0x55e70de1f2a8;
        interface_3_out_0x7f8e74004820;
        interface_3_out_0x7f8e74004d70;
    }
    // Input 0.
    subgraph cluster_subgraph_3_in_0 {
        label = "";
        interface_3_in_0x55e70de1f230 [label="N", shape=none];
        interface_3_in_0x7f8d9409a1d0 [label="C_in", shape=none];
        interface_3_in_0x7f88e804a870 [label="H", shape=none];
        interface_3_in_0x55e70de1f2a8 [label="H", shape=none];
        interface_3_in_0x7f8a5c037e40 [label="k_1", shape=none];
    }
    // Input 1.
    subgraph cluster_subgraph_3_in_1 {
        label = "";
        interface_3_in_0x7f8d9409a1e8 [label="C_in", shape=none];
        interface_3_in_0x7f8a5c037e58 [label="k_1", shape=none];
        interface_3_in_0x7f8b40006648 [label="g^-1*s^-1*C_out", shape=none];
    }
    {
        rank = same;
        interface_3_in_0x55e70de1f230;
        interface_3_in_0x7f8d9409a1d0;
        interface_3_in_0x7f88e804a870;
        interface_3_in_0x55e70de1f2a8;
        interface_3_in_0x7f8a5c037e40;
        interface_3_in_0x7f8d9409a1e8;
        interface_3_in_0x7f8a5c037e58;
        interface_3_in_0x7f8b40006648;
    }
    // Op's.
    op_0x7f8a5c037e20 [label="Share"];
    op_0x7f8b40006610 [label="Share"];
    op_0x7f8d9409a1b0 [label="Share"];
    op_0x7f8ec8004b18 [label="Expand"];
    // Dimension's.
    interface_3_in_0x55e70de1f230 -> interface_3_out_0x55e70de1f230 [label="N"];
    interface_3_in_0x55e70de1f2a8 -> interface_3_out_0x55e70de1f2a8 [label="H"];
    interface_3_in_0x7f88e804a870 -> interface_3_out_0x7f88e804a870 [label="H"];
    interface_3_in_0x7f8a5c037e40 -> op_0x7f8a5c037e20 [label="k_1"];
    interface_3_in_0x7f8a5c037e58 -> op_0x7f8a5c037e20 [label="k_1"];
    op_0x7f8ec8004b18 -> op_0x7f8b40006610 [label="g^-1*s^-1*C_out"];
    interface_3_in_0x7f8b40006648 -> op_0x7f8b40006610 [label="g^-1*s^-1*C_out"];
    interface_3_in_0x7f8d9409a1d0 -> op_0x7f8d9409a1b0 [label="C_in"];
    interface_3_in_0x7f8d9409a1e8 -> op_0x7f8d9409a1b0 [label="C_in"];
    op_0x7f8a5c037e20 -> interface_3_out_0x7f8e74004820 [label="k_1"];
    op_0x7f8b40006610 -> interface_3_out_0x7f8e74004d70 [label="g^-1*s^-1*C_out"];
    op_0x7f8d9409a1b0 -> interface_3_out_0x7f8eac01f970 [label="C_in"];
}

// Stage tensor.
subgraph cluster_subgraph_4 {
    label = "Subgraph 4";
    // Reductions.
    // Output.
    subgraph cluster_subgraph_4_out {
        label = "";
        interface_4_out_0x55e70de1f230 [label="N", shape=none];
        interface_4_out_0x7f8d9409a1d0 [label="C_in", shape=none];
        interface_4_out_0x7f88e804a870 [label="H", shape=none];
        interface_4_out_0x55e70de1f2a8 [label="H", shape=none];
        interface_4_out_0x7f8a5c037e40 [label="k_1", shape=none];
    }
    {
        rank = same;
        interface_4_out_0x55e70de1f230;
        interface_4_out_0x7f8d9409a1d0;
        interface_4_out_0x7f88e804a870;
        interface_4_out_0x55e70de1f2a8;
        interface_4_out_0x7f8a5c037e40;
    }
    // Input 0.
    subgraph cluster_subgraph_4_in_0 {
        label = "";
        interface_4_in_0x55e70de1f230 [label="N", shape=none];
        interface_4_in_0x7f8d9409a1d0 [label="C_in", shape=none];
        interface_4_in_0x7f88e804a870 [label="H", shape=none];
        interface_4_in_0x7f8e8c08b9e8 [label="H", shape=none];
    }
    {
        rank = same;
        interface_4_in_0x55e70de1f230;
        interface_4_in_0x7f8d9409a1d0;
        interface_4_in_0x7f88e804a870;
        interface_4_in_0x7f8e8c08b9e8;
    }
    // Op's.
    op_0x7f8e8c08b9c0 [label="Unfold"];
    // Dimension's.
    interface_4_in_0x55e70de1f230 -> interface_4_out_0x55e70de1f230 [label="N"];
    op_0x7f8e8c08b9c0 -> interface_4_out_0x55e70de1f2a8 [label="H"];
    interface_4_in_0x7f88e804a870 -> interface_4_out_0x7f88e804a870 [label="H"];
    op_0x7f8e8c08b9c0 -> interface_4_out_0x7f8a5c037e40 [label="k_1"];
    interface_4_in_0x7f8d9409a1d0 -> interface_4_out_0x7f8d9409a1d0 [label="C_in"];
    interface_4_in_0x7f8e8c08b9e8 -> op_0x7f8e8c08b9c0 [label="H"];
}

// Input tensor.
subgraph cluster_subgraph_5 {
    label = "Input 0";
    interface_5_out_0x55e70de1f230 [label="N", shape=none];
    interface_5_out_0x7f8d9409a1d0 [label="C_in", shape=none];
    interface_5_out_0x7f88e804a870 [label="H", shape=none];
    interface_5_out_0x7f8e8c08b9e8 [label="H", shape=none];
}

interface_5_out_0x55e70de1f230 -> interface_4_in_0x55e70de1f230;
interface_5_out_0x7f8d9409a1d0 -> interface_4_in_0x7f8d9409a1d0;
interface_5_out_0x7f88e804a870 -> interface_4_in_0x7f88e804a870;
interface_5_out_0x7f8e8c08b9e8 -> interface_4_in_0x7f8e8c08b9e8;

interface_4_out_0x55e70de1f230 -> interface_3_in_0x55e70de1f230;
interface_4_out_0x7f8d9409a1d0 -> interface_3_in_0x7f8d9409a1d0;
interface_4_out_0x7f88e804a870 -> interface_3_in_0x7f88e804a870;
interface_4_out_0x55e70de1f2a8 -> interface_3_in_0x55e70de1f2a8;
interface_4_out_0x7f8a5c037e40 -> interface_3_in_0x7f8a5c037e40;

// Input tensor.
subgraph cluster_subgraph_6 {
    label = "Input 2";
    interface_6_out_0x7f8d9409a1e8 [label="C_in", shape=none];
    interface_6_out_0x7f8a5c037e58 [label="k_1", shape=none];
    interface_6_out_0x7f8b40006648 [label="g^-1*s^-1*C_out", shape=none];
}

interface_6_out_0x7f8d9409a1e8 -> interface_3_in_0x7f8d9409a1e8;
interface_6_out_0x7f8a5c037e58 -> interface_3_in_0x7f8a5c037e58;
interface_6_out_0x7f8b40006648 -> interface_3_in_0x7f8b40006648;

interface_3_out_0x55e70de1f230 -> interface_2_in_0x55e70de1f230;
interface_3_out_0x7f8eac01f970 -> interface_2_in_0x7f8eac01f970;
interface_3_out_0x7f88e804a870 -> interface_2_in_0x7f88e804a870;
interface_3_out_0x55e70de1f2a8 -> interface_2_in_0x55e70de1f2a8;
interface_3_out_0x7f8e74004820 -> interface_2_in_0x7f8e74004820;
interface_3_out_0x7f8e74004d70 -> interface_2_in_0x7f8e74004d70;

interface_2_out_0x55e70de1f230 -> interface_1_in_0x55e70de1f230;
interface_2_out_0x7f8de8004620 -> interface_1_in_0x7f8de8004620;
interface_2_out_0x7f88e804a870 -> interface_1_in_0x7f88e804a870;
interface_2_out_0x55e70de1f2a8 -> interface_1_in_0x55e70de1f2a8;
interface_2_out_0x7f8e74004820 -> interface_1_in_0x7f8e74004820;
interface_2_out_0x7f8e74004d70 -> interface_1_in_0x7f8e74004d70;

interface_1_out_0x55e70de1f230 -> interface_0_in_0x55e70de1f230;
interface_1_out_0x7f8de8004620 -> interface_0_in_0x7f8de8004620;
interface_1_out_0x55e70de1f280 -> interface_0_in_0x55e70de1f280;
interface_1_out_0x7f8e740056d0 -> interface_0_in_0x7f8e740056d0;
interface_1_out_0x55e70de1f2a8 -> interface_0_in_0x55e70de1f2a8;
interface_1_out_0x7f8e74004820 -> interface_0_in_0x7f8e74004820;
interface_1_out_0x7f8e74004d70 -> interface_0_in_0x7f8e74004d70;

// Input tensor.
subgraph cluster_subgraph_7 {
    label = "Input 1";
    interface_7_out_0x7f8de8004638 [label="g", shape=none];
    interface_7_out_0x7f8e740056e8 [label="k_1", shape=none];
    interface_7_out_0x7f8e74004838 [label="k_1", shape=none];
    interface_7_out_0x7f8ec8004238 [label="C_out", shape=none];
    interface_7_out_0x7f8e74004d88 [label="g^-1*s^-1*C_out", shape=none];
}

interface_7_out_0x7f8de8004638 -> interface_0_in_0x7f8de8004638;
interface_7_out_0x7f8e740056e8 -> interface_0_in_0x7f8e740056e8;
interface_7_out_0x7f8e74004838 -> interface_0_in_0x7f8e74004838;
interface_7_out_0x7f8ec8004238 -> interface_0_in_0x7f8ec8004238;
interface_7_out_0x7f8e74004d88 -> interface_0_in_0x7f8e74004d88;

{
    rank = same;
    interface_5_out_0x55e70de1f230;
    interface_5_out_0x7f8d9409a1d0;
    interface_5_out_0x7f88e804a870;
    interface_5_out_0x7f8e8c08b9e8;
    interface_7_out_0x7f8de8004638;
    interface_7_out_0x7f8e740056e8;
    interface_7_out_0x7f8e74004838;
    interface_7_out_0x7f8ec8004238;
    interface_7_out_0x7f8e74004d88;
    interface_6_out_0x7f8d9409a1e8;
    interface_6_out_0x7f8a5c037e58;
    interface_6_out_0x7f8b40006648;
}
subgraph cluster_subgraph_output {
    label = "Output";
    interface_8_in_0x55e70de1f230 [label="N", shape=none];
    interface_8_in_0x55e70de1f258 [label="C_out", shape=none];
    interface_8_in_0x55e70de1f280 [label="H", shape=none];
    interface_8_in_0x55e70de1f2a8 [label="H", shape=none];
}
interface_0_out_0x55e70de1f230 -> interface_8_in_0x55e70de1f230;
interface_0_out_0x55e70de1f258 -> interface_8_in_0x55e70de1f258;
interface_0_out_0x55e70de1f280 -> interface_8_in_0x55e70de1f280;
interface_0_out_0x55e70de1f2a8 -> interface_8_in_0x55e70de1f2a8;

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

		# [H]@Unfolde3f17abf629a5707 -> [H]@Iteratorb0a1def4ad5784ec, [k_1]@Shareffd3dd34f2fd42e9
		t_3 = torch.reshape(t_3, (128, 3584, 56, 1, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (128, 64, 56, 3, 56, ))

		# Permute to match the output of this subgraph.
		t_3 = torch.permute(t_3, (0, 1, 2, 4, 3, ))

		# Perform contraction.
		t_4 = torch.einsum("lknmi, kij -> lknmij", t_3, in_2)

		# No contraction needed.
		t_5 = t_4

		# [C_in]@Splitc2d52f3525ba6cc4 -> [g]@Sharec7a8ce455b828537, [g^-1*C_in]@Reduceef9903cafc29eea1
		t_5 = torch.reshape(t_5, (128, 32, 2, 56, 56, 3, 1, ))

		# [g^-1*C_in]@Reduce
		t_5 = torch.sum(t_5, dim=(2, ))

		# No contraction needed.
		t_6 = t_5

		# [H]@Shift50434f3e383b3310 -> [H]@Unfold87ed2fb8f6552d8f
		t_6 = torch.roll(t_6, self.shift_direction, 2)

		# [H]@Unfold87ed2fb8f6552d8f -> [H]@Iterator96123ba3184da39c, [k_1]@Share02da0a485106ab3d
		t_6 = torch.reshape(t_6, (128, 32, 56, 168, ))
		t_6 = torch.nn.functional.unfold(t_6, (3, 1, ), padding=(1, 0, ))
		t_6 = torch.reshape(t_6, (128, 32, 3, 56, 56, 3, 1, ))

		# Permute to match the output of this subgraph.
		t_6 = torch.permute(t_6, (0, 1, 3, 2, 4, 5, 6, ))

		# Perform contraction.
		t_7 = torch.einsum("niolpjk, iljmk -> nopm", t_6, in_1)

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

		# [H]@Unfolde3f17abf629a5707 -> [H]@Iteratorb0a1def4ad5784ec, [k_1]@Shareffd3dd34f2fd42e9
		t_3 = torch.reshape(t_3, (128, 1792, 28, 1, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (128, 64, 28, 3, 28, ))

		# Permute to match the output of this subgraph.
		t_3 = torch.permute(t_3, (0, 1, 2, 4, 3, ))

		# Perform contraction.
		t_4 = torch.einsum("lknmi, kij -> lknmij", t_3, in_2)

		# No contraction needed.
		t_5 = t_4

		# [C_in]@Splitc2d52f3525ba6cc4 -> [g]@Sharec7a8ce455b828537, [g^-1*C_in]@Reduceef9903cafc29eea1
		t_5 = torch.reshape(t_5, (128, 32, 2, 28, 28, 3, 2, ))

		# [g^-1*C_in]@Reduce
		t_5 = torch.sum(t_5, dim=(2, ))

		# No contraction needed.
		t_6 = t_5

		# [H]@Shift50434f3e383b3310 -> [H]@Unfold87ed2fb8f6552d8f
		t_6 = torch.roll(t_6, self.shift_direction, 2)

		# [H]@Unfold87ed2fb8f6552d8f -> [H]@Iterator96123ba3184da39c, [k_1]@Share02da0a485106ab3d
		t_6 = torch.reshape(t_6, (128, 32, 28, 168, ))
		t_6 = torch.nn.functional.unfold(t_6, (3, 1, ), padding=(1, 0, ))
		t_6 = torch.reshape(t_6, (128, 32, 3, 28, 28, 3, 2, ))

		# Permute to match the output of this subgraph.
		t_6 = torch.permute(t_6, (0, 1, 3, 2, 4, 5, 6, ))

		# Perform contraction.
		t_7 = torch.einsum("niolpjk, iljmk -> nopm", t_6, in_1)

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

		# [H]@Unfolde3f17abf629a5707 -> [H]@Iteratorb0a1def4ad5784ec, [k_1]@Shareffd3dd34f2fd42e9
		t_3 = torch.reshape(t_3, (128, 3584, 28, 1, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (128, 128, 28, 3, 28, ))

		# Permute to match the output of this subgraph.
		t_3 = torch.permute(t_3, (0, 1, 2, 4, 3, ))

		# Perform contraction.
		t_4 = torch.einsum("lknmi, kij -> lknmij", t_3, in_2)

		# No contraction needed.
		t_5 = t_4

		# [C_in]@Splitc2d52f3525ba6cc4 -> [g]@Sharec7a8ce455b828537, [g^-1*C_in]@Reduceef9903cafc29eea1
		t_5 = torch.reshape(t_5, (128, 32, 4, 28, 28, 3, 2, ))

		# [g^-1*C_in]@Reduce
		t_5 = torch.sum(t_5, dim=(2, ))

		# No contraction needed.
		t_6 = t_5

		# [H]@Shift50434f3e383b3310 -> [H]@Unfold87ed2fb8f6552d8f
		t_6 = torch.roll(t_6, self.shift_direction, 2)

		# [H]@Unfold87ed2fb8f6552d8f -> [H]@Iterator96123ba3184da39c, [k_1]@Share02da0a485106ab3d
		t_6 = torch.reshape(t_6, (128, 32, 28, 168, ))
		t_6 = torch.nn.functional.unfold(t_6, (3, 1, ), padding=(1, 0, ))
		t_6 = torch.reshape(t_6, (128, 32, 3, 28, 28, 3, 2, ))

		# Permute to match the output of this subgraph.
		t_6 = torch.permute(t_6, (0, 1, 3, 2, 4, 5, 6, ))

		# Perform contraction.
		t_7 = torch.einsum("niolpjk, iljmk -> nopm", t_6, in_1)

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

		# [H]@Unfolde3f17abf629a5707 -> [H]@Iteratorb0a1def4ad5784ec, [k_1]@Shareffd3dd34f2fd42e9
		t_3 = torch.reshape(t_3, (128, 1792, 14, 1, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (128, 128, 14, 3, 14, ))

		# Permute to match the output of this subgraph.
		t_3 = torch.permute(t_3, (0, 1, 2, 4, 3, ))

		# Perform contraction.
		t_4 = torch.einsum("lknmi, kij -> lknmij", t_3, in_2)

		# No contraction needed.
		t_5 = t_4

		# [C_in]@Splitc2d52f3525ba6cc4 -> [g]@Sharec7a8ce455b828537, [g^-1*C_in]@Reduceef9903cafc29eea1
		t_5 = torch.reshape(t_5, (128, 32, 4, 14, 14, 3, 4, ))

		# [g^-1*C_in]@Reduce
		t_5 = torch.sum(t_5, dim=(2, ))

		# No contraction needed.
		t_6 = t_5

		# [H]@Shift50434f3e383b3310 -> [H]@Unfold87ed2fb8f6552d8f
		t_6 = torch.roll(t_6, self.shift_direction, 2)

		# [H]@Unfold87ed2fb8f6552d8f -> [H]@Iterator96123ba3184da39c, [k_1]@Share02da0a485106ab3d
		t_6 = torch.reshape(t_6, (128, 32, 14, 168, ))
		t_6 = torch.nn.functional.unfold(t_6, (3, 1, ), padding=(1, 0, ))
		t_6 = torch.reshape(t_6, (128, 32, 3, 14, 14, 3, 4, ))

		# Permute to match the output of this subgraph.
		t_6 = torch.permute(t_6, (0, 1, 3, 2, 4, 5, 6, ))

		# Perform contraction.
		t_7 = torch.einsum("niolpjk, iljmk -> nopm", t_6, in_1)

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

		# [H]@Unfolde3f17abf629a5707 -> [H]@Iteratorb0a1def4ad5784ec, [k_1]@Shareffd3dd34f2fd42e9
		t_3 = torch.reshape(t_3, (128, 3584, 14, 1, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (128, 256, 14, 3, 14, ))

		# Permute to match the output of this subgraph.
		t_3 = torch.permute(t_3, (0, 1, 2, 4, 3, ))

		# Perform contraction.
		t_4 = torch.einsum("lknmi, kij -> lknmij", t_3, in_2)

		# No contraction needed.
		t_5 = t_4

		# [C_in]@Splitc2d52f3525ba6cc4 -> [g]@Sharec7a8ce455b828537, [g^-1*C_in]@Reduceef9903cafc29eea1
		t_5 = torch.reshape(t_5, (128, 32, 8, 14, 14, 3, 4, ))

		# [g^-1*C_in]@Reduce
		t_5 = torch.sum(t_5, dim=(2, ))

		# No contraction needed.
		t_6 = t_5

		# [H]@Shift50434f3e383b3310 -> [H]@Unfold87ed2fb8f6552d8f
		t_6 = torch.roll(t_6, self.shift_direction, 2)

		# [H]@Unfold87ed2fb8f6552d8f -> [H]@Iterator96123ba3184da39c, [k_1]@Share02da0a485106ab3d
		t_6 = torch.reshape(t_6, (128, 32, 14, 168, ))
		t_6 = torch.nn.functional.unfold(t_6, (3, 1, ), padding=(1, 0, ))
		t_6 = torch.reshape(t_6, (128, 32, 3, 14, 14, 3, 4, ))

		# Permute to match the output of this subgraph.
		t_6 = torch.permute(t_6, (0, 1, 3, 2, 4, 5, 6, ))

		# Perform contraction.
		t_7 = torch.einsum("niolpjk, iljmk -> nopm", t_6, in_1)

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

		# [H]@Unfolde3f17abf629a5707 -> [H]@Iteratorb0a1def4ad5784ec, [k_1]@Shareffd3dd34f2fd42e9
		t_3 = torch.reshape(t_3, (128, 1792, 7, 1, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (128, 256, 7, 3, 7, ))

		# Permute to match the output of this subgraph.
		t_3 = torch.permute(t_3, (0, 1, 2, 4, 3, ))

		# Perform contraction.
		t_4 = torch.einsum("lknmi, kij -> lknmij", t_3, in_2)

		# No contraction needed.
		t_5 = t_4

		# [C_in]@Splitc2d52f3525ba6cc4 -> [g]@Sharec7a8ce455b828537, [g^-1*C_in]@Reduceef9903cafc29eea1
		t_5 = torch.reshape(t_5, (128, 32, 8, 7, 7, 3, 8, ))

		# [g^-1*C_in]@Reduce
		t_5 = torch.sum(t_5, dim=(2, ))

		# No contraction needed.
		t_6 = t_5

		# [H]@Shift50434f3e383b3310 -> [H]@Unfold87ed2fb8f6552d8f
		t_6 = torch.roll(t_6, self.shift_direction, 2)

		# [H]@Unfold87ed2fb8f6552d8f -> [H]@Iterator96123ba3184da39c, [k_1]@Share02da0a485106ab3d
		t_6 = torch.reshape(t_6, (128, 32, 7, 168, ))
		t_6 = torch.nn.functional.unfold(t_6, (3, 1, ), padding=(1, 0, ))
		t_6 = torch.reshape(t_6, (128, 32, 3, 7, 7, 3, 8, ))

		# Permute to match the output of this subgraph.
		t_6 = torch.permute(t_6, (0, 1, 3, 2, 4, 5, 6, ))

		# Perform contraction.
		t_7 = torch.einsum("niolpjk, iljmk -> nopm", t_6, in_1)

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

		# [H]@Unfolde3f17abf629a5707 -> [H]@Iteratorb0a1def4ad5784ec, [k_1]@Shareffd3dd34f2fd42e9
		t_3 = torch.reshape(t_3, (128, 3584, 7, 1, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (128, 512, 7, 3, 7, ))

		# Permute to match the output of this subgraph.
		t_3 = torch.permute(t_3, (0, 1, 2, 4, 3, ))

		# Perform contraction.
		t_4 = torch.einsum("lknmi, kij -> lknmij", t_3, in_2)

		# No contraction needed.
		t_5 = t_4

		# [C_in]@Splitc2d52f3525ba6cc4 -> [g]@Sharec7a8ce455b828537, [g^-1*C_in]@Reduceef9903cafc29eea1
		t_5 = torch.reshape(t_5, (128, 32, 16, 7, 7, 3, 8, ))

		# [g^-1*C_in]@Reduce
		t_5 = torch.sum(t_5, dim=(2, ))

		# No contraction needed.
		t_6 = t_5

		# [H]@Shift50434f3e383b3310 -> [H]@Unfold87ed2fb8f6552d8f
		t_6 = torch.roll(t_6, self.shift_direction, 2)

		# [H]@Unfold87ed2fb8f6552d8f -> [H]@Iterator96123ba3184da39c, [k_1]@Share02da0a485106ab3d
		t_6 = torch.reshape(t_6, (128, 32, 7, 168, ))
		t_6 = torch.nn.functional.unfold(t_6, (3, 1, ), padding=(1, 0, ))
		t_6 = torch.reshape(t_6, (128, 32, 3, 7, 7, 3, 8, ))

		# Permute to match the output of this subgraph.
		t_6 = torch.permute(t_6, (0, 1, 3, 2, 4, 5, 6, ))

		# Perform contraction.
		t_7 = torch.einsum("niolpjk, iljmk -> nopm", t_6, in_1)

		# Permute to match the output of this subgraph.
		t_7 = torch.permute(t_7, (0, 3, 1, 2, ))

		# No need to crop the output tensor.
		y = t_7

		return y

