import torch
import random
"""
digraph kernel_preview {
newrank = true;

// Stage tensor.
subgraph cluster_subgraph_0 {
    label = "Subgraph 0";
    // Reductions.
    reduce_0x7effd8001928 [label="Sum", shape=box];
    reduce_0x7effd8001a98 [label="Sum", shape=box];
    reduce_0x7effd8001ab0 [label="Sum", shape=box];
    reduce_0x7effd8009288 [label="Sum", shape=box];
    // Output.
    subgraph cluster_subgraph_0_out {
        label = "";
        interface_0_out_0x55a308c0a8f0 [label="N", shape=none];
        interface_0_out_0x55a308c0a918 [label="C_out", shape=none];
        interface_0_out_0x55a308c0a940 [label="H", shape=none];
        interface_0_out_0x55a308c0a968 [label="H", shape=none];
    }
    {
        rank = same;
        reduce_0x7effd8001928;
        reduce_0x7effd8001a98;
        reduce_0x7effd8001ab0;
        reduce_0x7effd8009288;
        interface_0_out_0x55a308c0a8f0;
        interface_0_out_0x55a308c0a918;
        interface_0_out_0x55a308c0a940;
        interface_0_out_0x55a308c0a968;
    }
    // Input 0.
    subgraph cluster_subgraph_0_in_0 {
        label = "";
        interface_0_in_0x55a308c0a8f0 [label="N", shape=none];
        interface_0_in_0x55a3093b87c0 [label="g", shape=none];
        interface_0_in_0x55a308c0a940 [label="H", shape=none];
        interface_0_in_0x55a3093b88b0 [label="k_1", shape=none];
        interface_0_in_0x55a308c0a968 [label="H", shape=none];
        interface_0_in_0x55a3093b8810 [label="k_1", shape=none];
        interface_0_in_0x55a3093b8860 [label="g^-1*s^-1*C_out", shape=none];
    }
    // Input 1.
    subgraph cluster_subgraph_0_in_1 {
        label = "";
        interface_0_in_0x55a3093b87d8 [label="g", shape=none];
        interface_0_in_0x55a3093b88c8 [label="k_1", shape=none];
        interface_0_in_0x55a3093b8828 [label="k_1", shape=none];
        interface_0_in_0x55a3093b8738 [label="C_out", shape=none];
        interface_0_in_0x55a3093b8878 [label="g^-1*s^-1*C_out", shape=none];
    }
    {
        rank = same;
        interface_0_in_0x55a308c0a8f0;
        interface_0_in_0x55a3093b87c0;
        interface_0_in_0x55a308c0a940;
        interface_0_in_0x55a3093b88b0;
        interface_0_in_0x55a308c0a968;
        interface_0_in_0x55a3093b8810;
        interface_0_in_0x55a3093b8860;
        interface_0_in_0x55a3093b87d8;
        interface_0_in_0x55a3093b88c8;
        interface_0_in_0x55a3093b8828;
        interface_0_in_0x55a3093b8738;
        interface_0_in_0x55a3093b8878;
    }
    // Op's.
    op_0x55a3093b8700 [label="Share"];
    op_0x55a3093b87a0 [label="Share"];
    op_0x55a3093b87f0 [label="Share"];
    op_0x55a3093b8840 [label="Share"];
    op_0x55a3093b8890 [label="Share"];
    op_0x55a3093b8c98 [label="Expand"];
    // Dimension's.
    interface_0_in_0x55a308c0a8f0 -> interface_0_out_0x55a308c0a8f0 [label="N"];
    op_0x55a3093b8700 -> interface_0_out_0x55a308c0a918 [label="C_out"];
    interface_0_in_0x55a308c0a940 -> interface_0_out_0x55a308c0a940 [label="H"];
    interface_0_in_0x55a308c0a968 -> interface_0_out_0x55a308c0a968 [label="H"];
    op_0x55a3093b8c98 -> op_0x55a3093b8700 [label="C_out"];
    interface_0_in_0x55a3093b8738 -> op_0x55a3093b8700 [label="C_out"];
    interface_0_in_0x55a3093b87c0 -> op_0x55a3093b87a0 [label="g"];
    interface_0_in_0x55a3093b87d8 -> op_0x55a3093b87a0 [label="g"];
    interface_0_in_0x55a3093b8810 -> op_0x55a3093b87f0 [label="k_1"];
    interface_0_in_0x55a3093b8828 -> op_0x55a3093b87f0 [label="k_1"];
    interface_0_in_0x55a3093b8860 -> op_0x55a3093b8840 [label="g^-1*s^-1*C_out"];
    interface_0_in_0x55a3093b8878 -> op_0x55a3093b8840 [label="g^-1*s^-1*C_out"];
    interface_0_in_0x55a3093b88b0 -> op_0x55a3093b8890 [label="k_1"];
    interface_0_in_0x55a3093b88c8 -> op_0x55a3093b8890 [label="k_1"];
    op_0x55a3093b87a0 -> reduce_0x7effd8001928 [label="g"];
    op_0x55a3093b87f0 -> reduce_0x7effd8001a98 [label="k_1"];
    op_0x55a3093b8890 -> reduce_0x7effd8001ab0 [label="k_1"];
    op_0x55a3093b8840 -> reduce_0x7effd8009288 [label="g^-1*s^-1*C_out"];
}

// Stage tensor.
subgraph cluster_subgraph_1 {
    label = "Subgraph 1";
    // Reductions.
    // Output.
    subgraph cluster_subgraph_1_out {
        label = "";
        interface_1_out_0x55a308c0a8f0 [label="N", shape=none];
        interface_1_out_0x55a3093b87c0 [label="g", shape=none];
        interface_1_out_0x55a308c0a940 [label="H", shape=none];
        interface_1_out_0x55a3093b88b0 [label="k_1", shape=none];
        interface_1_out_0x55a308c0a968 [label="H", shape=none];
        interface_1_out_0x55a3093b8810 [label="k_1", shape=none];
        interface_1_out_0x55a3093b8860 [label="g^-1*s^-1*C_out", shape=none];
    }
    {
        rank = same;
        interface_1_out_0x55a308c0a8f0;
        interface_1_out_0x55a3093b87c0;
        interface_1_out_0x55a308c0a940;
        interface_1_out_0x55a3093b88b0;
        interface_1_out_0x55a308c0a968;
        interface_1_out_0x55a3093b8810;
        interface_1_out_0x55a3093b8860;
    }
    // Input 0.
    subgraph cluster_subgraph_1_in_0 {
        label = "";
        interface_1_in_0x55a308c0a8f0 [label="N", shape=none];
        interface_1_in_0x55a3093b87c0 [label="g", shape=none];
        interface_1_in_0x55a3093b9830 [label="H", shape=none];
        interface_1_in_0x55a308c0a968 [label="H", shape=none];
        interface_1_in_0x55a3093b8810 [label="k_1", shape=none];
        interface_1_in_0x55a3093b8860 [label="g^-1*s^-1*C_out", shape=none];
    }
    {
        rank = same;
        interface_1_in_0x55a308c0a8f0;
        interface_1_in_0x55a3093b87c0;
        interface_1_in_0x55a3093b9830;
        interface_1_in_0x55a308c0a968;
        interface_1_in_0x55a3093b8810;
        interface_1_in_0x55a3093b8860;
    }
    // Op's.
    op_0x55a3093b9810 [label="Shift"];
    op_0x55a3093bba80 [label="Unfold"];
    // Dimension's.
    interface_1_in_0x55a308c0a8f0 -> interface_1_out_0x55a308c0a8f0 [label="N"];
    op_0x55a3093bba80 -> interface_1_out_0x55a308c0a940 [label="H"];
    interface_1_in_0x55a308c0a968 -> interface_1_out_0x55a308c0a968 [label="H"];
    interface_1_in_0x55a3093b87c0 -> interface_1_out_0x55a3093b87c0 [label="g"];
    interface_1_in_0x55a3093b8810 -> interface_1_out_0x55a3093b8810 [label="k_1"];
    interface_1_in_0x55a3093b8860 -> interface_1_out_0x55a3093b8860 [label="g^-1*s^-1*C_out"];
    op_0x55a3093bba80 -> interface_1_out_0x55a3093b88b0 [label="k_1"];
    interface_1_in_0x55a3093b9830 -> op_0x55a3093b9810 [label="H"];
    op_0x55a3093b9810 -> op_0x55a3093bba80 [label="H"];
}

// Stage tensor.
subgraph cluster_subgraph_2 {
    label = "Subgraph 2";
    // Reductions.
    reduce_0x7effd8005a90 [label="Sum", shape=box];
    // Output.
    subgraph cluster_subgraph_2_out {
        label = "";
        interface_2_out_0x55a308c0a8f0 [label="N", shape=none];
        interface_2_out_0x55a3093b87c0 [label="g", shape=none];
        interface_2_out_0x55a3093b9830 [label="H", shape=none];
        interface_2_out_0x55a308c0a968 [label="H", shape=none];
        interface_2_out_0x55a3093b8810 [label="k_1", shape=none];
        interface_2_out_0x55a3093b8860 [label="g^-1*s^-1*C_out", shape=none];
    }
    {
        rank = same;
        reduce_0x7effd8005a90;
        interface_2_out_0x55a308c0a8f0;
        interface_2_out_0x55a3093b87c0;
        interface_2_out_0x55a3093b9830;
        interface_2_out_0x55a308c0a968;
        interface_2_out_0x55a3093b8810;
        interface_2_out_0x55a3093b8860;
    }
    // Input 0.
    subgraph cluster_subgraph_2_in_0 {
        label = "";
        interface_2_in_0x55a308c0a8f0 [label="N", shape=none];
        interface_2_in_0x55a3093bd1c0 [label="C_in", shape=none];
        interface_2_in_0x55a3093b9830 [label="H", shape=none];
        interface_2_in_0x55a308c0a968 [label="H", shape=none];
        interface_2_in_0x55a3093b8810 [label="k_1", shape=none];
        interface_2_in_0x55a3093b8860 [label="g^-1*s^-1*C_out", shape=none];
    }
    {
        rank = same;
        interface_2_in_0x55a308c0a8f0;
        interface_2_in_0x55a3093bd1c0;
        interface_2_in_0x55a3093b9830;
        interface_2_in_0x55a308c0a968;
        interface_2_in_0x55a3093b8810;
        interface_2_in_0x55a3093b8860;
    }
    // Op's.
    op_0x55a3093bd180 [label="Split"];
    // Dimension's.
    interface_2_in_0x55a308c0a8f0 -> interface_2_out_0x55a308c0a8f0 [label="N"];
    interface_2_in_0x55a308c0a968 -> interface_2_out_0x55a308c0a968 [label="H"];
    op_0x55a3093bd180 -> interface_2_out_0x55a3093b87c0 [label="g"];
    interface_2_in_0x55a3093b8810 -> interface_2_out_0x55a3093b8810 [label="k_1"];
    interface_2_in_0x55a3093b8860 -> interface_2_out_0x55a3093b8860 [label="g^-1*s^-1*C_out"];
    interface_2_in_0x55a3093b9830 -> interface_2_out_0x55a3093b9830 [label="H"];
    interface_2_in_0x55a3093bd1c0 -> op_0x55a3093bd180 [label="C_in"];
    op_0x55a3093bd180 -> reduce_0x7effd8005a90 [label="g^-1*C_in"];
}

// Stage tensor.
subgraph cluster_subgraph_3 {
    label = "Subgraph 3";
    // Reductions.
    // Output.
    subgraph cluster_subgraph_3_out {
        label = "";
        interface_3_out_0x55a308c0a8f0 [label="N", shape=none];
        interface_3_out_0x55a3093bd1c0 [label="C_in", shape=none];
        interface_3_out_0x55a3093b9830 [label="H", shape=none];
        interface_3_out_0x55a308c0a968 [label="H", shape=none];
        interface_3_out_0x55a3093b8810 [label="k_1", shape=none];
        interface_3_out_0x55a3093b8860 [label="g^-1*s^-1*C_out", shape=none];
    }
    {
        rank = same;
        interface_3_out_0x55a308c0a8f0;
        interface_3_out_0x55a3093bd1c0;
        interface_3_out_0x55a3093b9830;
        interface_3_out_0x55a308c0a968;
        interface_3_out_0x55a3093b8810;
        interface_3_out_0x55a3093b8860;
    }
    // Input 0.
    subgraph cluster_subgraph_3_in_0 {
        label = "";
        interface_3_in_0x55a308c0a8f0 [label="N", shape=none];
        interface_3_in_0x55a3093b8a90 [label="C_in", shape=none];
        interface_3_in_0x55a3093b9830 [label="H", shape=none];
        interface_3_in_0x55a308c0a968 [label="H", shape=none];
        interface_3_in_0x55a3093b8950 [label="k_1", shape=none];
    }
    // Input 1.
    subgraph cluster_subgraph_3_in_1 {
        label = "";
        interface_3_in_0x55a3093b8aa8 [label="C_in", shape=none];
        interface_3_in_0x55a3093b8968 [label="k_1", shape=none];
        interface_3_in_0x55a3093b8918 [label="g^-1*s^-1*C_out", shape=none];
    }
    {
        rank = same;
        interface_3_in_0x55a308c0a8f0;
        interface_3_in_0x55a3093b8a90;
        interface_3_in_0x55a3093b9830;
        interface_3_in_0x55a308c0a968;
        interface_3_in_0x55a3093b8950;
        interface_3_in_0x55a3093b8aa8;
        interface_3_in_0x55a3093b8968;
        interface_3_in_0x55a3093b8918;
    }
    // Op's.
    op_0x55a3093b88e0 [label="Share"];
    op_0x55a3093b8930 [label="Share"];
    op_0x55a3093b8a70 [label="Share"];
    op_0x55a3093b8cb8 [label="Expand"];
    // Dimension's.
    interface_3_in_0x55a308c0a8f0 -> interface_3_out_0x55a308c0a8f0 [label="N"];
    interface_3_in_0x55a308c0a968 -> interface_3_out_0x55a308c0a968 [label="H"];
    op_0x55a3093b8930 -> interface_3_out_0x55a3093b8810 [label="k_1"];
    op_0x55a3093b88e0 -> interface_3_out_0x55a3093b8860 [label="g^-1*s^-1*C_out"];
    op_0x55a3093b8cb8 -> op_0x55a3093b88e0 [label="g^-1*s^-1*C_out"];
    interface_3_in_0x55a3093b8918 -> op_0x55a3093b88e0 [label="g^-1*s^-1*C_out"];
    interface_3_in_0x55a3093b8950 -> op_0x55a3093b8930 [label="k_1"];
    interface_3_in_0x55a3093b8968 -> op_0x55a3093b8930 [label="k_1"];
    interface_3_in_0x55a3093b8a90 -> op_0x55a3093b8a70 [label="C_in"];
    interface_3_in_0x55a3093b8aa8 -> op_0x55a3093b8a70 [label="C_in"];
    interface_3_in_0x55a3093b9830 -> interface_3_out_0x55a3093b9830 [label="H"];
    op_0x55a3093b8a70 -> interface_3_out_0x55a3093bd1c0 [label="C_in"];
}

// Stage tensor.
subgraph cluster_subgraph_4 {
    label = "Subgraph 4";
    // Reductions.
    // Output.
    subgraph cluster_subgraph_4_out {
        label = "";
        interface_4_out_0x55a308c0a8f0 [label="N", shape=none];
        interface_4_out_0x55a3093b8a90 [label="C_in", shape=none];
        interface_4_out_0x55a3093b9830 [label="H", shape=none];
        interface_4_out_0x55a308c0a968 [label="H", shape=none];
        interface_4_out_0x55a3093b8950 [label="k_1", shape=none];
    }
    {
        rank = same;
        interface_4_out_0x55a308c0a8f0;
        interface_4_out_0x55a3093b8a90;
        interface_4_out_0x55a3093b9830;
        interface_4_out_0x55a308c0a968;
        interface_4_out_0x55a3093b8950;
    }
    // Input 0.
    subgraph cluster_subgraph_4_in_0 {
        label = "";
        interface_4_in_0x55a308c0a8f0 [label="N", shape=none];
        interface_4_in_0x55a3093b8a90 [label="C_in", shape=none];
        interface_4_in_0x55a3093b9830 [label="H", shape=none];
        interface_4_in_0x55a3094118e8 [label="H", shape=none];
    }
    {
        rank = same;
        interface_4_in_0x55a308c0a8f0;
        interface_4_in_0x55a3093b8a90;
        interface_4_in_0x55a3093b9830;
        interface_4_in_0x55a3094118e8;
    }
    // Op's.
    op_0x55a3094118c0 [label="Unfold"];
    // Dimension's.
    interface_4_in_0x55a308c0a8f0 -> interface_4_out_0x55a308c0a8f0 [label="N"];
    op_0x55a3094118c0 -> interface_4_out_0x55a308c0a968 [label="H"];
    op_0x55a3094118c0 -> interface_4_out_0x55a3093b8950 [label="k_1"];
    interface_4_in_0x55a3093b8a90 -> interface_4_out_0x55a3093b8a90 [label="C_in"];
    interface_4_in_0x55a3093b9830 -> interface_4_out_0x55a3093b9830 [label="H"];
    interface_4_in_0x55a3094118e8 -> op_0x55a3094118c0 [label="H"];
}

// Input tensor.
subgraph cluster_subgraph_5 {
    label = "Input 0";
    interface_5_out_0x55a308c0a8f0 [label="N", shape=none];
    interface_5_out_0x55a3093b8a90 [label="C_in", shape=none];
    interface_5_out_0x55a3093b9830 [label="H", shape=none];
    interface_5_out_0x55a3094118e8 [label="H", shape=none];
}

interface_5_out_0x55a308c0a8f0 -> interface_4_in_0x55a308c0a8f0;
interface_5_out_0x55a3093b8a90 -> interface_4_in_0x55a3093b8a90;
interface_5_out_0x55a3093b9830 -> interface_4_in_0x55a3093b9830;
interface_5_out_0x55a3094118e8 -> interface_4_in_0x55a3094118e8;

interface_4_out_0x55a308c0a8f0 -> interface_3_in_0x55a308c0a8f0;
interface_4_out_0x55a3093b8a90 -> interface_3_in_0x55a3093b8a90;
interface_4_out_0x55a3093b9830 -> interface_3_in_0x55a3093b9830;
interface_4_out_0x55a308c0a968 -> interface_3_in_0x55a308c0a968;
interface_4_out_0x55a3093b8950 -> interface_3_in_0x55a3093b8950;

// Input tensor.
subgraph cluster_subgraph_6 {
    label = "Input 2";
    interface_6_out_0x55a3093b8aa8 [label="C_in", shape=none];
    interface_6_out_0x55a3093b8968 [label="k_1", shape=none];
    interface_6_out_0x55a3093b8918 [label="g^-1*s^-1*C_out", shape=none];
}

interface_6_out_0x55a3093b8aa8 -> interface_3_in_0x55a3093b8aa8;
interface_6_out_0x55a3093b8968 -> interface_3_in_0x55a3093b8968;
interface_6_out_0x55a3093b8918 -> interface_3_in_0x55a3093b8918;

interface_3_out_0x55a308c0a8f0 -> interface_2_in_0x55a308c0a8f0;
interface_3_out_0x55a3093bd1c0 -> interface_2_in_0x55a3093bd1c0;
interface_3_out_0x55a3093b9830 -> interface_2_in_0x55a3093b9830;
interface_3_out_0x55a308c0a968 -> interface_2_in_0x55a308c0a968;
interface_3_out_0x55a3093b8810 -> interface_2_in_0x55a3093b8810;
interface_3_out_0x55a3093b8860 -> interface_2_in_0x55a3093b8860;

interface_2_out_0x55a308c0a8f0 -> interface_1_in_0x55a308c0a8f0;
interface_2_out_0x55a3093b87c0 -> interface_1_in_0x55a3093b87c0;
interface_2_out_0x55a3093b9830 -> interface_1_in_0x55a3093b9830;
interface_2_out_0x55a308c0a968 -> interface_1_in_0x55a308c0a968;
interface_2_out_0x55a3093b8810 -> interface_1_in_0x55a3093b8810;
interface_2_out_0x55a3093b8860 -> interface_1_in_0x55a3093b8860;

interface_1_out_0x55a308c0a8f0 -> interface_0_in_0x55a308c0a8f0;
interface_1_out_0x55a3093b87c0 -> interface_0_in_0x55a3093b87c0;
interface_1_out_0x55a308c0a940 -> interface_0_in_0x55a308c0a940;
interface_1_out_0x55a3093b88b0 -> interface_0_in_0x55a3093b88b0;
interface_1_out_0x55a308c0a968 -> interface_0_in_0x55a308c0a968;
interface_1_out_0x55a3093b8810 -> interface_0_in_0x55a3093b8810;
interface_1_out_0x55a3093b8860 -> interface_0_in_0x55a3093b8860;

// Input tensor.
subgraph cluster_subgraph_7 {
    label = "Input 1";
    interface_7_out_0x55a3093b87d8 [label="g", shape=none];
    interface_7_out_0x55a3093b88c8 [label="k_1", shape=none];
    interface_7_out_0x55a3093b8828 [label="k_1", shape=none];
    interface_7_out_0x55a3093b8738 [label="C_out", shape=none];
    interface_7_out_0x55a3093b8878 [label="g^-1*s^-1*C_out", shape=none];
}

interface_7_out_0x55a3093b87d8 -> interface_0_in_0x55a3093b87d8;
interface_7_out_0x55a3093b88c8 -> interface_0_in_0x55a3093b88c8;
interface_7_out_0x55a3093b8828 -> interface_0_in_0x55a3093b8828;
interface_7_out_0x55a3093b8738 -> interface_0_in_0x55a3093b8738;
interface_7_out_0x55a3093b8878 -> interface_0_in_0x55a3093b8878;

{
    rank = same;
    interface_5_out_0x55a308c0a8f0;
    interface_5_out_0x55a3093b8a90;
    interface_5_out_0x55a3093b9830;
    interface_5_out_0x55a3094118e8;
    interface_7_out_0x55a3093b87d8;
    interface_7_out_0x55a3093b88c8;
    interface_7_out_0x55a3093b8828;
    interface_7_out_0x55a3093b8738;
    interface_7_out_0x55a3093b8878;
    interface_6_out_0x55a3093b8aa8;
    interface_6_out_0x55a3093b8968;
    interface_6_out_0x55a3093b8918;
}
subgraph cluster_subgraph_output {
    label = "Output";
    interface_8_in_0x55a308c0a8f0 [label="N", shape=none];
    interface_8_in_0x55a308c0a918 [label="C_out", shape=none];
    interface_8_in_0x55a308c0a940 [label="H", shape=none];
    interface_8_in_0x55a308c0a968 [label="H", shape=none];
}
interface_0_out_0x55a308c0a8f0 -> interface_8_in_0x55a308c0a8f0;
interface_0_out_0x55a308c0a918 -> interface_8_in_0x55a308c0a918;
interface_0_out_0x55a308c0a940 -> interface_8_in_0x55a308c0a940;
interface_0_out_0x55a308c0a968 -> interface_8_in_0x55a308c0a968;

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
		t_3 = torch.reshape(t_3, (1024, 3584, 56, 1, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (1024, 64, 56, 3, 56, ))

		# Permute to match the output of this subgraph.
		t_3 = torch.permute(t_3, (0, 1, 2, 4, 3, ))

		# Perform contraction.
		t_4 = torch.einsum("lknmj, kji -> lknmji", t_3, in_2)

		# No contraction needed.
		t_5 = t_4

		# [C_in]@Splitc2d52f3525ba6cc4 -> [g]@Sharec7a8ce455b828537, [g^-1*C_in]@Reduceef9903cafc29eea1
		t_5 = torch.reshape(t_5, (1024, 32, 2, 56, 56, 3, 1, ))

		# [g^-1*C_in]@Reduce
		t_5 = torch.sum(t_5, dim=(2, ))

		# No contraction needed.
		t_6 = t_5

		# [H]@Shift50434f3e383b3310 -> [H]@Unfold87ed2fb8f6552d8f
		t_6 = torch.roll(t_6, self.shift_direction, 2)

		# [H]@Unfold87ed2fb8f6552d8f -> [H]@Iterator96123ba3184da39c, [k_1]@Share02da0a485106ab3d
		t_6 = torch.reshape(t_6, (1024, 32, 56, 168, ))
		t_6 = torch.nn.functional.unfold(t_6, (3, 1, ), padding=(1, 0, ))
		t_6 = torch.reshape(t_6, (1024, 32, 3, 56, 56, 3, 1, ))

		# Permute to match the output of this subgraph.
		t_6 = torch.permute(t_6, (0, 1, 3, 2, 4, 5, 6, ))

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

		# [H]@Unfolde3f17abf629a5707 -> [H]@Iteratorb0a1def4ad5784ec, [k_1]@Shareffd3dd34f2fd42e9
		t_3 = torch.reshape(t_3, (1024, 1792, 28, 1, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (1024, 64, 28, 3, 28, ))

		# Permute to match the output of this subgraph.
		t_3 = torch.permute(t_3, (0, 1, 2, 4, 3, ))

		# Perform contraction.
		t_4 = torch.einsum("lknmj, kji -> lknmji", t_3, in_2)

		# No contraction needed.
		t_5 = t_4

		# [C_in]@Splitc2d52f3525ba6cc4 -> [g]@Sharec7a8ce455b828537, [g^-1*C_in]@Reduceef9903cafc29eea1
		t_5 = torch.reshape(t_5, (1024, 32, 2, 28, 28, 3, 2, ))

		# [g^-1*C_in]@Reduce
		t_5 = torch.sum(t_5, dim=(2, ))

		# No contraction needed.
		t_6 = t_5

		# [H]@Shift50434f3e383b3310 -> [H]@Unfold87ed2fb8f6552d8f
		t_6 = torch.roll(t_6, self.shift_direction, 2)

		# [H]@Unfold87ed2fb8f6552d8f -> [H]@Iterator96123ba3184da39c, [k_1]@Share02da0a485106ab3d
		t_6 = torch.reshape(t_6, (1024, 32, 28, 168, ))
		t_6 = torch.nn.functional.unfold(t_6, (3, 1, ), padding=(1, 0, ))
		t_6 = torch.reshape(t_6, (1024, 32, 3, 28, 28, 3, 2, ))

		# Permute to match the output of this subgraph.
		t_6 = torch.permute(t_6, (0, 1, 3, 2, 4, 5, 6, ))

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

		# [H]@Unfolde3f17abf629a5707 -> [H]@Iteratorb0a1def4ad5784ec, [k_1]@Shareffd3dd34f2fd42e9
		t_3 = torch.reshape(t_3, (1024, 3584, 28, 1, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (1024, 128, 28, 3, 28, ))

		# Permute to match the output of this subgraph.
		t_3 = torch.permute(t_3, (0, 1, 2, 4, 3, ))

		# Perform contraction.
		t_4 = torch.einsum("lknmj, kji -> lknmji", t_3, in_2)

		# No contraction needed.
		t_5 = t_4

		# [C_in]@Splitc2d52f3525ba6cc4 -> [g]@Sharec7a8ce455b828537, [g^-1*C_in]@Reduceef9903cafc29eea1
		t_5 = torch.reshape(t_5, (1024, 32, 4, 28, 28, 3, 2, ))

		# [g^-1*C_in]@Reduce
		t_5 = torch.sum(t_5, dim=(2, ))

		# No contraction needed.
		t_6 = t_5

		# [H]@Shift50434f3e383b3310 -> [H]@Unfold87ed2fb8f6552d8f
		t_6 = torch.roll(t_6, self.shift_direction, 2)

		# [H]@Unfold87ed2fb8f6552d8f -> [H]@Iterator96123ba3184da39c, [k_1]@Share02da0a485106ab3d
		t_6 = torch.reshape(t_6, (1024, 32, 28, 168, ))
		t_6 = torch.nn.functional.unfold(t_6, (3, 1, ), padding=(1, 0, ))
		t_6 = torch.reshape(t_6, (1024, 32, 3, 28, 28, 3, 2, ))

		# Permute to match the output of this subgraph.
		t_6 = torch.permute(t_6, (0, 1, 3, 2, 4, 5, 6, ))

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

		# [H]@Unfolde3f17abf629a5707 -> [H]@Iteratorb0a1def4ad5784ec, [k_1]@Shareffd3dd34f2fd42e9
		t_3 = torch.reshape(t_3, (1024, 1792, 14, 1, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (1024, 128, 14, 3, 14, ))

		# Permute to match the output of this subgraph.
		t_3 = torch.permute(t_3, (0, 1, 2, 4, 3, ))

		# Perform contraction.
		t_4 = torch.einsum("lknmj, kji -> lknmji", t_3, in_2)

		# No contraction needed.
		t_5 = t_4

		# [C_in]@Splitc2d52f3525ba6cc4 -> [g]@Sharec7a8ce455b828537, [g^-1*C_in]@Reduceef9903cafc29eea1
		t_5 = torch.reshape(t_5, (1024, 32, 4, 14, 14, 3, 4, ))

		# [g^-1*C_in]@Reduce
		t_5 = torch.sum(t_5, dim=(2, ))

		# No contraction needed.
		t_6 = t_5

		# [H]@Shift50434f3e383b3310 -> [H]@Unfold87ed2fb8f6552d8f
		t_6 = torch.roll(t_6, self.shift_direction, 2)

		# [H]@Unfold87ed2fb8f6552d8f -> [H]@Iterator96123ba3184da39c, [k_1]@Share02da0a485106ab3d
		t_6 = torch.reshape(t_6, (1024, 32, 14, 168, ))
		t_6 = torch.nn.functional.unfold(t_6, (3, 1, ), padding=(1, 0, ))
		t_6 = torch.reshape(t_6, (1024, 32, 3, 14, 14, 3, 4, ))

		# Permute to match the output of this subgraph.
		t_6 = torch.permute(t_6, (0, 1, 3, 2, 4, 5, 6, ))

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

		# [H]@Unfolde3f17abf629a5707 -> [H]@Iteratorb0a1def4ad5784ec, [k_1]@Shareffd3dd34f2fd42e9
		t_3 = torch.reshape(t_3, (1024, 3584, 14, 1, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (1024, 256, 14, 3, 14, ))

		# Permute to match the output of this subgraph.
		t_3 = torch.permute(t_3, (0, 1, 2, 4, 3, ))

		# Perform contraction.
		t_4 = torch.einsum("lknmj, kji -> lknmji", t_3, in_2)

		# No contraction needed.
		t_5 = t_4

		# [C_in]@Splitc2d52f3525ba6cc4 -> [g]@Sharec7a8ce455b828537, [g^-1*C_in]@Reduceef9903cafc29eea1
		t_5 = torch.reshape(t_5, (1024, 32, 8, 14, 14, 3, 4, ))

		# [g^-1*C_in]@Reduce
		t_5 = torch.sum(t_5, dim=(2, ))

		# No contraction needed.
		t_6 = t_5

		# [H]@Shift50434f3e383b3310 -> [H]@Unfold87ed2fb8f6552d8f
		t_6 = torch.roll(t_6, self.shift_direction, 2)

		# [H]@Unfold87ed2fb8f6552d8f -> [H]@Iterator96123ba3184da39c, [k_1]@Share02da0a485106ab3d
		t_6 = torch.reshape(t_6, (1024, 32, 14, 168, ))
		t_6 = torch.nn.functional.unfold(t_6, (3, 1, ), padding=(1, 0, ))
		t_6 = torch.reshape(t_6, (1024, 32, 3, 14, 14, 3, 4, ))

		# Permute to match the output of this subgraph.
		t_6 = torch.permute(t_6, (0, 1, 3, 2, 4, 5, 6, ))

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

		# [H]@Unfolde3f17abf629a5707 -> [H]@Iteratorb0a1def4ad5784ec, [k_1]@Shareffd3dd34f2fd42e9
		t_3 = torch.reshape(t_3, (1024, 1792, 7, 1, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (1024, 256, 7, 3, 7, ))

		# Permute to match the output of this subgraph.
		t_3 = torch.permute(t_3, (0, 1, 2, 4, 3, ))

		# Perform contraction.
		t_4 = torch.einsum("lknmj, kji -> lknmji", t_3, in_2)

		# No contraction needed.
		t_5 = t_4

		# [C_in]@Splitc2d52f3525ba6cc4 -> [g]@Sharec7a8ce455b828537, [g^-1*C_in]@Reduceef9903cafc29eea1
		t_5 = torch.reshape(t_5, (1024, 32, 8, 7, 7, 3, 8, ))

		# [g^-1*C_in]@Reduce
		t_5 = torch.sum(t_5, dim=(2, ))

		# No contraction needed.
		t_6 = t_5

		# [H]@Shift50434f3e383b3310 -> [H]@Unfold87ed2fb8f6552d8f
		t_6 = torch.roll(t_6, self.shift_direction, 2)

		# [H]@Unfold87ed2fb8f6552d8f -> [H]@Iterator96123ba3184da39c, [k_1]@Share02da0a485106ab3d
		t_6 = torch.reshape(t_6, (1024, 32, 7, 168, ))
		t_6 = torch.nn.functional.unfold(t_6, (3, 1, ), padding=(1, 0, ))
		t_6 = torch.reshape(t_6, (1024, 32, 3, 7, 7, 3, 8, ))

		# Permute to match the output of this subgraph.
		t_6 = torch.permute(t_6, (0, 1, 3, 2, 4, 5, 6, ))

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

		# [H]@Unfolde3f17abf629a5707 -> [H]@Iteratorb0a1def4ad5784ec, [k_1]@Shareffd3dd34f2fd42e9
		t_3 = torch.reshape(t_3, (1024, 3584, 7, 1, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (1024, 512, 7, 3, 7, ))

		# Permute to match the output of this subgraph.
		t_3 = torch.permute(t_3, (0, 1, 2, 4, 3, ))

		# Perform contraction.
		t_4 = torch.einsum("lknmj, kji -> lknmji", t_3, in_2)

		# No contraction needed.
		t_5 = t_4

		# [C_in]@Splitc2d52f3525ba6cc4 -> [g]@Sharec7a8ce455b828537, [g^-1*C_in]@Reduceef9903cafc29eea1
		t_5 = torch.reshape(t_5, (1024, 32, 16, 7, 7, 3, 8, ))

		# [g^-1*C_in]@Reduce
		t_5 = torch.sum(t_5, dim=(2, ))

		# No contraction needed.
		t_6 = t_5

		# [H]@Shift50434f3e383b3310 -> [H]@Unfold87ed2fb8f6552d8f
		t_6 = torch.roll(t_6, self.shift_direction, 2)

		# [H]@Unfold87ed2fb8f6552d8f -> [H]@Iterator96123ba3184da39c, [k_1]@Share02da0a485106ab3d
		t_6 = torch.reshape(t_6, (1024, 32, 7, 168, ))
		t_6 = torch.nn.functional.unfold(t_6, (3, 1, ), padding=(1, 0, ))
		t_6 = torch.reshape(t_6, (1024, 32, 3, 7, 7, 3, 8, ))

		# Permute to match the output of this subgraph.
		t_6 = torch.permute(t_6, (0, 1, 3, 2, 4, 5, 6, ))

		# Perform contraction.
		t_7 = torch.einsum("njompkl, jmkil -> nopi", t_6, in_1)

		# Permute to match the output of this subgraph.
		t_7 = torch.permute(t_7, (0, 3, 1, 2, ))

		# No need to crop the output tensor.
		y = t_7

		return y

