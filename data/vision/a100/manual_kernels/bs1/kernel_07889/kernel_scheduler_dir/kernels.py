import torch
import random
"""
digraph kernel_preview {
newrank = true;

// Stage tensor.
subgraph cluster_subgraph_0 {
    label = "Subgraph 0";
    // Reductions.
    reduce_0x561f594ee198 [label="Sum", shape=box];
    reduce_0x561f594ee0e0 [label="Sum", shape=box];
    reduce_0x561f594ee0f8 [label="Sum", shape=box];
    reduce_0x561f594ee250 [label="Sum", shape=box];
    // Output.
    subgraph cluster_subgraph_0_out {
        label = "";
        interface_0_out_0x561f59514e90 [label="N", shape=none];
        interface_0_out_0x561f5c3acc90 [label="C_out", shape=none];
        interface_0_out_0x561f5c32f210 [label="H", shape=none];
        interface_0_out_0x561f5c3a9a10 [label="H", shape=none];
    }
    {
        rank = same;
        reduce_0x561f594ee198;
        reduce_0x561f594ee0e0;
        reduce_0x561f594ee0f8;
        reduce_0x561f594ee250;
        interface_0_out_0x561f59514e90;
        interface_0_out_0x561f5c3acc90;
        interface_0_out_0x561f5c32f210;
        interface_0_out_0x561f5c3a9a10;
    }
    // Input 0.
    subgraph cluster_subgraph_0_in_0 {
        label = "";
        interface_0_in_0x561f59514e90 [label="N", shape=none];
        interface_0_in_0x561f594f0e90 [label="g", shape=none];
        interface_0_in_0x561f594f0df0 [label="k_1", shape=none];
        interface_0_in_0x561f5c32f210 [label="H", shape=none];
        interface_0_in_0x561f594f0e40 [label="k_1", shape=none];
        interface_0_in_0x561f5c3a9a10 [label="H", shape=none];
        interface_0_in_0x561f594f0ee0 [label="g^-1*s^-1*C_out", shape=none];
    }
    // Input 1.
    subgraph cluster_subgraph_0_in_1 {
        label = "";
        interface_0_in_0x561f594f0db8 [label="C_out", shape=none];
        interface_0_in_0x561f594f0ea8 [label="g", shape=none];
        interface_0_in_0x561f594f0e08 [label="k_1", shape=none];
        interface_0_in_0x561f594f0e58 [label="k_1", shape=none];
        interface_0_in_0x561f594f0ef8 [label="g^-1*s^-1*C_out", shape=none];
    }
    {
        rank = same;
        interface_0_in_0x561f59514e90;
        interface_0_in_0x561f594f0e90;
        interface_0_in_0x561f594f0df0;
        interface_0_in_0x561f5c32f210;
        interface_0_in_0x561f594f0e40;
        interface_0_in_0x561f5c3a9a10;
        interface_0_in_0x561f594f0ee0;
        interface_0_in_0x561f594f0db8;
        interface_0_in_0x561f594f0ea8;
        interface_0_in_0x561f594f0e08;
        interface_0_in_0x561f594f0e58;
        interface_0_in_0x561f594f0ef8;
    }
    // Op's.
    op_0x561f594f0d80 [label="Share"];
    op_0x561f594f0dd0 [label="Share"];
    op_0x561f594f0e20 [label="Share"];
    op_0x561f594f0e70 [label="Share"];
    op_0x561f594f0ec0 [label="Share"];
    op_0x561f5c3acf18 [label="Expand"];
    // Dimension's.
    op_0x561f594f0dd0 -> reduce_0x561f594ee0e0 [label="k_1"];
    op_0x561f594f0e20 -> reduce_0x561f594ee0f8 [label="k_1"];
    op_0x561f594f0e70 -> reduce_0x561f594ee198 [label="g"];
    op_0x561f594f0ec0 -> reduce_0x561f594ee250 [label="g^-1*s^-1*C_out"];
    op_0x561f5c3acf18 -> op_0x561f594f0d80 [label="C_out"];
    interface_0_in_0x561f594f0db8 -> op_0x561f594f0d80 [label="C_out"];
    interface_0_in_0x561f594f0df0 -> op_0x561f594f0dd0 [label="k_1"];
    interface_0_in_0x561f594f0e08 -> op_0x561f594f0dd0 [label="k_1"];
    interface_0_in_0x561f594f0e40 -> op_0x561f594f0e20 [label="k_1"];
    interface_0_in_0x561f594f0e58 -> op_0x561f594f0e20 [label="k_1"];
    interface_0_in_0x561f594f0e90 -> op_0x561f594f0e70 [label="g"];
    interface_0_in_0x561f594f0ea8 -> op_0x561f594f0e70 [label="g"];
    interface_0_in_0x561f594f0ee0 -> op_0x561f594f0ec0 [label="g^-1*s^-1*C_out"];
    interface_0_in_0x561f594f0ef8 -> op_0x561f594f0ec0 [label="g^-1*s^-1*C_out"];
    interface_0_in_0x561f59514e90 -> interface_0_out_0x561f59514e90 [label="N"];
    interface_0_in_0x561f5c32f210 -> interface_0_out_0x561f5c32f210 [label="H"];
    interface_0_in_0x561f5c3a9a10 -> interface_0_out_0x561f5c3a9a10 [label="H"];
    op_0x561f594f0d80 -> interface_0_out_0x561f5c3acc90 [label="C_out"];
}

// Stage tensor.
subgraph cluster_subgraph_1 {
    label = "Subgraph 1";
    // Reductions.
    // Output.
    subgraph cluster_subgraph_1_out {
        label = "";
        interface_1_out_0x561f59514e90 [label="N", shape=none];
        interface_1_out_0x561f594f0e90 [label="g", shape=none];
        interface_1_out_0x561f594f0df0 [label="k_1", shape=none];
        interface_1_out_0x561f5c32f210 [label="H", shape=none];
        interface_1_out_0x561f594f0e40 [label="k_1", shape=none];
        interface_1_out_0x561f5c3a9a10 [label="H", shape=none];
        interface_1_out_0x561f594f0ee0 [label="g^-1*s^-1*C_out", shape=none];
    }
    {
        rank = same;
        interface_1_out_0x561f59514e90;
        interface_1_out_0x561f594f0e90;
        interface_1_out_0x561f594f0df0;
        interface_1_out_0x561f5c32f210;
        interface_1_out_0x561f594f0e40;
        interface_1_out_0x561f5c3a9a10;
        interface_1_out_0x561f594f0ee0;
    }
    // Input 0.
    subgraph cluster_subgraph_1_in_0 {
        label = "";
        interface_1_in_0x561f59514e90 [label="N", shape=none];
        interface_1_in_0x561f594f0e90 [label="g", shape=none];
        interface_1_in_0x561f594ef968 [label="H", shape=none];
        interface_1_in_0x561f594f0e40 [label="k_1", shape=none];
        interface_1_in_0x561f5c3a9a10 [label="H", shape=none];
        interface_1_in_0x561f594f0ee0 [label="g^-1*s^-1*C_out", shape=none];
    }
    {
        rank = same;
        interface_1_in_0x561f59514e90;
        interface_1_in_0x561f594f0e90;
        interface_1_in_0x561f594ef968;
        interface_1_in_0x561f594f0e40;
        interface_1_in_0x561f5c3a9a10;
        interface_1_in_0x561f594f0ee0;
    }
    // Op's.
    op_0x561f594ef940 [label="Unfold"];
    // Dimension's.
    interface_1_in_0x561f594ef968 -> op_0x561f594ef940 [label="H"];
    op_0x561f594ef940 -> interface_1_out_0x561f594f0df0 [label="k_1"];
    interface_1_in_0x561f594f0e40 -> interface_1_out_0x561f594f0e40 [label="k_1"];
    interface_1_in_0x561f594f0e90 -> interface_1_out_0x561f594f0e90 [label="g"];
    interface_1_in_0x561f594f0ee0 -> interface_1_out_0x561f594f0ee0 [label="g^-1*s^-1*C_out"];
    interface_1_in_0x561f59514e90 -> interface_1_out_0x561f59514e90 [label="N"];
    op_0x561f594ef940 -> interface_1_out_0x561f5c32f210 [label="H"];
    interface_1_in_0x561f5c3a9a10 -> interface_1_out_0x561f5c3a9a10 [label="H"];
}

// Stage tensor.
subgraph cluster_subgraph_2 {
    label = "Subgraph 2";
    // Reductions.
    reduce_0x561f594ee028 [label="Sum", shape=box];
    // Output.
    subgraph cluster_subgraph_2_out {
        label = "";
        interface_2_out_0x561f59514e90 [label="N", shape=none];
        interface_2_out_0x561f594f0e90 [label="g", shape=none];
        interface_2_out_0x561f594ef968 [label="H", shape=none];
        interface_2_out_0x561f594f0e40 [label="k_1", shape=none];
        interface_2_out_0x561f5c3a9a10 [label="H", shape=none];
        interface_2_out_0x561f594f0ee0 [label="g^-1*s^-1*C_out", shape=none];
    }
    {
        rank = same;
        reduce_0x561f594ee028;
        interface_2_out_0x561f59514e90;
        interface_2_out_0x561f594f0e90;
        interface_2_out_0x561f594ef968;
        interface_2_out_0x561f594f0e40;
        interface_2_out_0x561f5c3a9a10;
        interface_2_out_0x561f594f0ee0;
    }
    // Input 0.
    subgraph cluster_subgraph_2_in_0 {
        label = "";
        interface_2_in_0x561f59514e90 [label="N", shape=none];
        interface_2_in_0x561f5c3ab540 [label="C_in", shape=none];
        interface_2_in_0x561f594ef968 [label="H", shape=none];
        interface_2_in_0x561f594f0e40 [label="k_1", shape=none];
        interface_2_in_0x561f5c3a9a10 [label="H", shape=none];
        interface_2_in_0x561f594f0ee0 [label="g^-1*s^-1*C_out", shape=none];
    }
    {
        rank = same;
        interface_2_in_0x561f59514e90;
        interface_2_in_0x561f5c3ab540;
        interface_2_in_0x561f594ef968;
        interface_2_in_0x561f594f0e40;
        interface_2_in_0x561f5c3a9a10;
        interface_2_in_0x561f594f0ee0;
    }
    // Op's.
    op_0x561f5c3ab500 [label="Split"];
    // Dimension's.
    op_0x561f5c3ab500 -> reduce_0x561f594ee028 [label="g^-1*C_in"];
    interface_2_in_0x561f594ef968 -> interface_2_out_0x561f594ef968 [label="H"];
    interface_2_in_0x561f594f0e40 -> interface_2_out_0x561f594f0e40 [label="k_1"];
    op_0x561f5c3ab500 -> interface_2_out_0x561f594f0e90 [label="g"];
    interface_2_in_0x561f594f0ee0 -> interface_2_out_0x561f594f0ee0 [label="g^-1*s^-1*C_out"];
    interface_2_in_0x561f59514e90 -> interface_2_out_0x561f59514e90 [label="N"];
    interface_2_in_0x561f5c3a9a10 -> interface_2_out_0x561f5c3a9a10 [label="H"];
    interface_2_in_0x561f5c3ab540 -> op_0x561f5c3ab500 [label="C_in"];
}

// Stage tensor.
subgraph cluster_subgraph_3 {
    label = "Subgraph 3";
    // Reductions.
    // Output.
    subgraph cluster_subgraph_3_out {
        label = "";
        interface_3_out_0x561f59514e90 [label="N", shape=none];
        interface_3_out_0x561f5c3ab540 [label="C_in", shape=none];
        interface_3_out_0x561f594ef968 [label="H", shape=none];
        interface_3_out_0x561f594f0e40 [label="k_1", shape=none];
        interface_3_out_0x561f5c3a9a10 [label="H", shape=none];
        interface_3_out_0x561f594f0ee0 [label="g^-1*s^-1*C_out", shape=none];
    }
    {
        rank = same;
        interface_3_out_0x561f59514e90;
        interface_3_out_0x561f5c3ab540;
        interface_3_out_0x561f594ef968;
        interface_3_out_0x561f594f0e40;
        interface_3_out_0x561f5c3a9a10;
        interface_3_out_0x561f594f0ee0;
    }
    // Input 0.
    subgraph cluster_subgraph_3_in_0 {
        label = "";
        interface_3_in_0x561f59514e90 [label="N", shape=none];
        interface_3_in_0x561f594f0f80 [label="C_in", shape=none];
        interface_3_in_0x561f594ef968 [label="H", shape=none];
        interface_3_in_0x561f594f0f30 [label="k_1", shape=none];
        interface_3_in_0x561f5c3a9a10 [label="H", shape=none];
    }
    // Input 1.
    subgraph cluster_subgraph_3_in_1 {
        label = "";
        interface_3_in_0x561f594f0f98 [label="C_in", shape=none];
        interface_3_in_0x561f594f0f48 [label="k_1", shape=none];
        interface_3_in_0x561f594f0fe8 [label="g^-1*s^-1*C_out", shape=none];
    }
    {
        rank = same;
        interface_3_in_0x561f59514e90;
        interface_3_in_0x561f594f0f80;
        interface_3_in_0x561f594ef968;
        interface_3_in_0x561f594f0f30;
        interface_3_in_0x561f5c3a9a10;
        interface_3_in_0x561f594f0f98;
        interface_3_in_0x561f594f0f48;
        interface_3_in_0x561f594f0fe8;
    }
    // Op's.
    op_0x561f594f0f10 [label="Share"];
    op_0x561f594f0f60 [label="Share"];
    op_0x561f594f0fb0 [label="Share"];
    op_0x561f5c3acf38 [label="Expand"];
    // Dimension's.
    interface_3_in_0x561f594ef968 -> interface_3_out_0x561f594ef968 [label="H"];
    op_0x561f594f0f10 -> interface_3_out_0x561f594f0e40 [label="k_1"];
    op_0x561f594f0fb0 -> interface_3_out_0x561f594f0ee0 [label="g^-1*s^-1*C_out"];
    interface_3_in_0x561f594f0f30 -> op_0x561f594f0f10 [label="k_1"];
    interface_3_in_0x561f594f0f48 -> op_0x561f594f0f10 [label="k_1"];
    interface_3_in_0x561f594f0f80 -> op_0x561f594f0f60 [label="C_in"];
    interface_3_in_0x561f594f0f98 -> op_0x561f594f0f60 [label="C_in"];
    op_0x561f5c3acf38 -> op_0x561f594f0fb0 [label="g^-1*s^-1*C_out"];
    interface_3_in_0x561f594f0fe8 -> op_0x561f594f0fb0 [label="g^-1*s^-1*C_out"];
    interface_3_in_0x561f59514e90 -> interface_3_out_0x561f59514e90 [label="N"];
    interface_3_in_0x561f5c3a9a10 -> interface_3_out_0x561f5c3a9a10 [label="H"];
    op_0x561f594f0f60 -> interface_3_out_0x561f5c3ab540 [label="C_in"];
}

// Stage tensor.
subgraph cluster_subgraph_4 {
    label = "Subgraph 4";
    // Reductions.
    // Output.
    subgraph cluster_subgraph_4_out {
        label = "";
        interface_4_out_0x561f59514e90 [label="N", shape=none];
        interface_4_out_0x561f594f0f80 [label="C_in", shape=none];
        interface_4_out_0x561f594ef968 [label="H", shape=none];
        interface_4_out_0x561f594f0f30 [label="k_1", shape=none];
        interface_4_out_0x561f5c3a9a10 [label="H", shape=none];
    }
    {
        rank = same;
        interface_4_out_0x561f59514e90;
        interface_4_out_0x561f594f0f80;
        interface_4_out_0x561f594ef968;
        interface_4_out_0x561f594f0f30;
        interface_4_out_0x561f5c3a9a10;
    }
    // Input 0.
    subgraph cluster_subgraph_4_in_0 {
        label = "";
        interface_4_in_0x561f59514e90 [label="N", shape=none];
        interface_4_in_0x561f594f0f80 [label="C_in", shape=none];
        interface_4_in_0x561f594ef968 [label="H", shape=none];
        interface_4_in_0x561f594ef9a8 [label="H", shape=none];
    }
    {
        rank = same;
        interface_4_in_0x561f59514e90;
        interface_4_in_0x561f594f0f80;
        interface_4_in_0x561f594ef968;
        interface_4_in_0x561f594ef9a8;
    }
    // Op's.
    op_0x561f594ef980 [label="Unfold"];
    // Dimension's.
    interface_4_in_0x561f594ef968 -> interface_4_out_0x561f594ef968 [label="H"];
    interface_4_in_0x561f594ef9a8 -> op_0x561f594ef980 [label="H"];
    op_0x561f594ef980 -> interface_4_out_0x561f594f0f30 [label="k_1"];
    interface_4_in_0x561f594f0f80 -> interface_4_out_0x561f594f0f80 [label="C_in"];
    interface_4_in_0x561f59514e90 -> interface_4_out_0x561f59514e90 [label="N"];
    op_0x561f594ef980 -> interface_4_out_0x561f5c3a9a10 [label="H"];
}

// Input tensor.
subgraph cluster_subgraph_5 {
    label = "Input 0";
    interface_5_out_0x561f59514e90 [label="N", shape=none];
    interface_5_out_0x561f594f0f80 [label="C_in", shape=none];
    interface_5_out_0x561f594ef968 [label="H", shape=none];
    interface_5_out_0x561f594ef9a8 [label="H", shape=none];
}

interface_5_out_0x561f59514e90 -> interface_4_in_0x561f59514e90;
interface_5_out_0x561f594f0f80 -> interface_4_in_0x561f594f0f80;
interface_5_out_0x561f594ef968 -> interface_4_in_0x561f594ef968;
interface_5_out_0x561f594ef9a8 -> interface_4_in_0x561f594ef9a8;

interface_4_out_0x561f59514e90 -> interface_3_in_0x561f59514e90;
interface_4_out_0x561f594f0f80 -> interface_3_in_0x561f594f0f80;
interface_4_out_0x561f594ef968 -> interface_3_in_0x561f594ef968;
interface_4_out_0x561f594f0f30 -> interface_3_in_0x561f594f0f30;
interface_4_out_0x561f5c3a9a10 -> interface_3_in_0x561f5c3a9a10;

// Input tensor.
subgraph cluster_subgraph_6 {
    label = "Input 2";
    interface_6_out_0x561f594f0f98 [label="C_in", shape=none];
    interface_6_out_0x561f594f0f48 [label="k_1", shape=none];
    interface_6_out_0x561f594f0fe8 [label="g^-1*s^-1*C_out", shape=none];
}

interface_6_out_0x561f594f0f98 -> interface_3_in_0x561f594f0f98;
interface_6_out_0x561f594f0f48 -> interface_3_in_0x561f594f0f48;
interface_6_out_0x561f594f0fe8 -> interface_3_in_0x561f594f0fe8;

interface_3_out_0x561f59514e90 -> interface_2_in_0x561f59514e90;
interface_3_out_0x561f5c3ab540 -> interface_2_in_0x561f5c3ab540;
interface_3_out_0x561f594ef968 -> interface_2_in_0x561f594ef968;
interface_3_out_0x561f594f0e40 -> interface_2_in_0x561f594f0e40;
interface_3_out_0x561f5c3a9a10 -> interface_2_in_0x561f5c3a9a10;
interface_3_out_0x561f594f0ee0 -> interface_2_in_0x561f594f0ee0;

interface_2_out_0x561f59514e90 -> interface_1_in_0x561f59514e90;
interface_2_out_0x561f594f0e90 -> interface_1_in_0x561f594f0e90;
interface_2_out_0x561f594ef968 -> interface_1_in_0x561f594ef968;
interface_2_out_0x561f594f0e40 -> interface_1_in_0x561f594f0e40;
interface_2_out_0x561f5c3a9a10 -> interface_1_in_0x561f5c3a9a10;
interface_2_out_0x561f594f0ee0 -> interface_1_in_0x561f594f0ee0;

interface_1_out_0x561f59514e90 -> interface_0_in_0x561f59514e90;
interface_1_out_0x561f594f0e90 -> interface_0_in_0x561f594f0e90;
interface_1_out_0x561f594f0df0 -> interface_0_in_0x561f594f0df0;
interface_1_out_0x561f5c32f210 -> interface_0_in_0x561f5c32f210;
interface_1_out_0x561f594f0e40 -> interface_0_in_0x561f594f0e40;
interface_1_out_0x561f5c3a9a10 -> interface_0_in_0x561f5c3a9a10;
interface_1_out_0x561f594f0ee0 -> interface_0_in_0x561f594f0ee0;

// Input tensor.
subgraph cluster_subgraph_7 {
    label = "Input 1";
    interface_7_out_0x561f594f0db8 [label="C_out", shape=none];
    interface_7_out_0x561f594f0ea8 [label="g", shape=none];
    interface_7_out_0x561f594f0e08 [label="k_1", shape=none];
    interface_7_out_0x561f594f0e58 [label="k_1", shape=none];
    interface_7_out_0x561f594f0ef8 [label="g^-1*s^-1*C_out", shape=none];
}

interface_7_out_0x561f594f0db8 -> interface_0_in_0x561f594f0db8;
interface_7_out_0x561f594f0ea8 -> interface_0_in_0x561f594f0ea8;
interface_7_out_0x561f594f0e08 -> interface_0_in_0x561f594f0e08;
interface_7_out_0x561f594f0e58 -> interface_0_in_0x561f594f0e58;
interface_7_out_0x561f594f0ef8 -> interface_0_in_0x561f594f0ef8;

{
    rank = same;
    interface_5_out_0x561f59514e90;
    interface_5_out_0x561f594f0f80;
    interface_5_out_0x561f594ef968;
    interface_5_out_0x561f594ef9a8;
    interface_7_out_0x561f594f0db8;
    interface_7_out_0x561f594f0ea8;
    interface_7_out_0x561f594f0e08;
    interface_7_out_0x561f594f0e58;
    interface_7_out_0x561f594f0ef8;
    interface_6_out_0x561f594f0f98;
    interface_6_out_0x561f594f0f48;
    interface_6_out_0x561f594f0fe8;
}
subgraph cluster_subgraph_output {
    label = "Output";
    interface_8_in_0x561f59514e90 [label="N", shape=none];
    interface_8_in_0x561f5c3acc90 [label="C_out", shape=none];
    interface_8_in_0x561f5c32f210 [label="H", shape=none];
    interface_8_in_0x561f5c3a9a10 [label="H", shape=none];
}
interface_0_out_0x561f59514e90 -> interface_8_in_0x561f59514e90;
interface_0_out_0x561f5c3acc90 -> interface_8_in_0x561f5c3acc90;
interface_0_out_0x561f5c32f210 -> interface_8_in_0x561f5c32f210;
interface_0_out_0x561f5c3a9a10 -> interface_8_in_0x561f5c3a9a10;

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
		t_7 = torch.einsum("nljokpm, iljkm -> niop", t_6, in_1)

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
		t_7 = torch.einsum("nljokpm, iljkm -> niop", t_6, in_1)

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
		t_7 = torch.einsum("nljokpm, iljkm -> niop", t_6, in_1)

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
		t_7 = torch.einsum("nljokpm, iljkm -> niop", t_6, in_1)

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
		t_7 = torch.einsum("nljokpm, iljkm -> niop", t_6, in_1)

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
		t_7 = torch.einsum("nljokpm, iljkm -> niop", t_6, in_1)

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
		t_7 = torch.einsum("nljokpm, iljkm -> niop", t_6, in_1)

		# No need to crop the output tensor.
		y = t_7

		return y

