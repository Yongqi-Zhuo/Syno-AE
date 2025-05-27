import torch
import random
"""
digraph kernel_preview {
newrank = true;

// Stage tensor.
subgraph cluster_subgraph_0 {
    label = "Subgraph 0";
    // Reductions.
    reduce_0x7f3cd0003928 [label="Sum", shape=box];
    reduce_0x7f3cd0003ab0 [label="Sum", shape=box];
    reduce_0x7f3cd0003a98 [label="Sum", shape=box];
    reduce_0x7f3cd000ae88 [label="Sum", shape=box];
    // Output.
    subgraph cluster_subgraph_0_out {
        label = "";
        interface_0_out_0x560f6c4cbed0 [label="N", shape=none];
        interface_0_out_0x560f6c4cbef8 [label="C_out", shape=none];
        interface_0_out_0x560f6c4cbf20 [label="H", shape=none];
        interface_0_out_0x560f6c4cbf48 [label="H", shape=none];
    }
    {
        rank = same;
        reduce_0x7f3cd0003928;
        reduce_0x7f3cd0003ab0;
        reduce_0x7f3cd0003a98;
        reduce_0x7f3cd000ae88;
        interface_0_out_0x560f6c4cbed0;
        interface_0_out_0x560f6c4cbef8;
        interface_0_out_0x560f6c4cbf20;
        interface_0_out_0x560f6c4cbf48;
    }
    // Input 0.
    subgraph cluster_subgraph_0_in_0 {
        label = "";
        interface_0_in_0x560f6c4cbed0 [label="N", shape=none];
        interface_0_in_0x560f70f803d0 [label="g", shape=none];
        interface_0_in_0x560f70f802e0 [label="k_1", shape=none];
        interface_0_in_0x560f6c4cbf20 [label="H", shape=none];
        interface_0_in_0x560f70f80290 [label="k_1", shape=none];
        interface_0_in_0x560f6c4cbf48 [label="H", shape=none];
        interface_0_in_0x560f70f80420 [label="g^-1*s^-1*C_out", shape=none];
    }
    // Input 1.
    subgraph cluster_subgraph_0_in_1 {
        label = "";
        interface_0_in_0x560f70f801b8 [label="C_out", shape=none];
        interface_0_in_0x560f70f803e8 [label="g", shape=none];
        interface_0_in_0x560f70f802f8 [label="k_1", shape=none];
        interface_0_in_0x560f70f802a8 [label="k_1", shape=none];
        interface_0_in_0x560f70f80438 [label="g^-1*s^-1*C_out", shape=none];
    }
    {
        rank = same;
        interface_0_in_0x560f6c4cbed0;
        interface_0_in_0x560f70f803d0;
        interface_0_in_0x560f70f802e0;
        interface_0_in_0x560f6c4cbf20;
        interface_0_in_0x560f70f80290;
        interface_0_in_0x560f6c4cbf48;
        interface_0_in_0x560f70f80420;
        interface_0_in_0x560f70f801b8;
        interface_0_in_0x560f70f803e8;
        interface_0_in_0x560f70f802f8;
        interface_0_in_0x560f70f802a8;
        interface_0_in_0x560f70f80438;
    }
    // Op's.
    op_0x560f70f80180 [label="Share"];
    op_0x560f70f80270 [label="Share"];
    op_0x560f70f802c0 [label="Share"];
    op_0x560f70f803b0 [label="Share"];
    op_0x560f70f80400 [label="Share"];
    op_0x560f70f80658 [label="Expand"];
    // Dimension's.
    interface_0_in_0x560f6c4cbed0 -> interface_0_out_0x560f6c4cbed0 [label="N"];
    op_0x560f70f80180 -> interface_0_out_0x560f6c4cbef8 [label="C_out"];
    interface_0_in_0x560f6c4cbf20 -> interface_0_out_0x560f6c4cbf20 [label="H"];
    interface_0_in_0x560f6c4cbf48 -> interface_0_out_0x560f6c4cbf48 [label="H"];
    op_0x560f70f80658 -> op_0x560f70f80180 [label="C_out"];
    interface_0_in_0x560f70f801b8 -> op_0x560f70f80180 [label="C_out"];
    interface_0_in_0x560f70f80290 -> op_0x560f70f80270 [label="k_1"];
    interface_0_in_0x560f70f802a8 -> op_0x560f70f80270 [label="k_1"];
    interface_0_in_0x560f70f802e0 -> op_0x560f70f802c0 [label="k_1"];
    interface_0_in_0x560f70f802f8 -> op_0x560f70f802c0 [label="k_1"];
    interface_0_in_0x560f70f803d0 -> op_0x560f70f803b0 [label="g"];
    interface_0_in_0x560f70f803e8 -> op_0x560f70f803b0 [label="g"];
    interface_0_in_0x560f70f80420 -> op_0x560f70f80400 [label="g^-1*s^-1*C_out"];
    interface_0_in_0x560f70f80438 -> op_0x560f70f80400 [label="g^-1*s^-1*C_out"];
    op_0x560f70f803b0 -> reduce_0x7f3cd0003928 [label="g"];
    op_0x560f70f80270 -> reduce_0x7f3cd0003a98 [label="k_1"];
    op_0x560f70f802c0 -> reduce_0x7f3cd0003ab0 [label="k_1"];
    op_0x560f70f80400 -> reduce_0x7f3cd000ae88 [label="g^-1*s^-1*C_out"];
}

// Stage tensor.
subgraph cluster_subgraph_1 {
    label = "Subgraph 1";
    // Reductions.
    // Output.
    subgraph cluster_subgraph_1_out {
        label = "";
        interface_1_out_0x560f6c4cbed0 [label="N", shape=none];
        interface_1_out_0x560f70f803d0 [label="g", shape=none];
        interface_1_out_0x560f70f802e0 [label="k_1", shape=none];
        interface_1_out_0x560f6c4cbf20 [label="H", shape=none];
        interface_1_out_0x560f70f80290 [label="k_1", shape=none];
        interface_1_out_0x560f6c4cbf48 [label="H", shape=none];
        interface_1_out_0x560f70f80420 [label="g^-1*s^-1*C_out", shape=none];
    }
    {
        rank = same;
        interface_1_out_0x560f6c4cbed0;
        interface_1_out_0x560f70f803d0;
        interface_1_out_0x560f70f802e0;
        interface_1_out_0x560f6c4cbf20;
        interface_1_out_0x560f70f80290;
        interface_1_out_0x560f6c4cbf48;
        interface_1_out_0x560f70f80420;
    }
    // Input 0.
    subgraph cluster_subgraph_1_in_0 {
        label = "";
        interface_1_in_0x560f6c4cbed0 [label="N", shape=none];
        interface_1_in_0x560f70f803d0 [label="g", shape=none];
        interface_1_in_0x560f70f802e0 [label="k_1", shape=none];
        interface_1_in_0x560f6c4cbf20 [label="H", shape=none];
        interface_1_in_0x560f70f81020 [label="H", shape=none];
        interface_1_in_0x560f70f80420 [label="g^-1*s^-1*C_out", shape=none];
    }
    {
        rank = same;
        interface_1_in_0x560f6c4cbed0;
        interface_1_in_0x560f70f803d0;
        interface_1_in_0x560f70f802e0;
        interface_1_in_0x560f6c4cbf20;
        interface_1_in_0x560f70f81020;
        interface_1_in_0x560f70f80420;
    }
    // Op's.
    op_0x560f70f81000 [label="Shift"];
    op_0x560f70f92e00 [label="Unfold"];
    // Dimension's.
    interface_1_in_0x560f6c4cbed0 -> interface_1_out_0x560f6c4cbed0 [label="N"];
    interface_1_in_0x560f6c4cbf20 -> interface_1_out_0x560f6c4cbf20 [label="H"];
    op_0x560f70f92e00 -> interface_1_out_0x560f6c4cbf48 [label="H"];
    op_0x560f70f92e00 -> interface_1_out_0x560f70f80290 [label="k_1"];
    interface_1_in_0x560f70f802e0 -> interface_1_out_0x560f70f802e0 [label="k_1"];
    interface_1_in_0x560f70f803d0 -> interface_1_out_0x560f70f803d0 [label="g"];
    interface_1_in_0x560f70f80420 -> interface_1_out_0x560f70f80420 [label="g^-1*s^-1*C_out"];
    interface_1_in_0x560f70f81020 -> op_0x560f70f81000 [label="H"];
    op_0x560f70f81000 -> op_0x560f70f92e00 [label="H"];
}

// Stage tensor.
subgraph cluster_subgraph_2 {
    label = "Subgraph 2";
    // Reductions.
    reduce_0x7f3cd0007890 [label="Sum", shape=box];
    // Output.
    subgraph cluster_subgraph_2_out {
        label = "";
        interface_2_out_0x560f6c4cbed0 [label="N", shape=none];
        interface_2_out_0x560f70f803d0 [label="g", shape=none];
        interface_2_out_0x560f70f802e0 [label="k_1", shape=none];
        interface_2_out_0x560f6c4cbf20 [label="H", shape=none];
        interface_2_out_0x560f70f81020 [label="H", shape=none];
        interface_2_out_0x560f70f80420 [label="g^-1*s^-1*C_out", shape=none];
    }
    {
        rank = same;
        reduce_0x7f3cd0007890;
        interface_2_out_0x560f6c4cbed0;
        interface_2_out_0x560f70f803d0;
        interface_2_out_0x560f70f802e0;
        interface_2_out_0x560f6c4cbf20;
        interface_2_out_0x560f70f81020;
        interface_2_out_0x560f70f80420;
    }
    // Input 0.
    subgraph cluster_subgraph_2_in_0 {
        label = "";
        interface_2_in_0x560f6c4cbed0 [label="N", shape=none];
        interface_2_in_0x560f70f97a60 [label="C_in", shape=none];
        interface_2_in_0x560f70f802e0 [label="k_1", shape=none];
        interface_2_in_0x560f6c4cbf20 [label="H", shape=none];
        interface_2_in_0x560f70f81020 [label="H", shape=none];
        interface_2_in_0x560f70f80420 [label="g^-1*s^-1*C_out", shape=none];
    }
    {
        rank = same;
        interface_2_in_0x560f6c4cbed0;
        interface_2_in_0x560f70f97a60;
        interface_2_in_0x560f70f802e0;
        interface_2_in_0x560f6c4cbf20;
        interface_2_in_0x560f70f81020;
        interface_2_in_0x560f70f80420;
    }
    // Op's.
    op_0x560f70f97a20 [label="Split"];
    // Dimension's.
    interface_2_in_0x560f6c4cbed0 -> interface_2_out_0x560f6c4cbed0 [label="N"];
    interface_2_in_0x560f6c4cbf20 -> interface_2_out_0x560f6c4cbf20 [label="H"];
    interface_2_in_0x560f70f802e0 -> interface_2_out_0x560f70f802e0 [label="k_1"];
    op_0x560f70f97a20 -> interface_2_out_0x560f70f803d0 [label="g"];
    interface_2_in_0x560f70f80420 -> interface_2_out_0x560f70f80420 [label="g^-1*s^-1*C_out"];
    interface_2_in_0x560f70f81020 -> interface_2_out_0x560f70f81020 [label="H"];
    interface_2_in_0x560f70f97a60 -> op_0x560f70f97a20 [label="C_in"];
    op_0x560f70f97a20 -> reduce_0x7f3cd0007890 [label="g^-1*C_in"];
}

// Stage tensor.
subgraph cluster_subgraph_3 {
    label = "Subgraph 3";
    // Reductions.
    // Output.
    subgraph cluster_subgraph_3_out {
        label = "";
        interface_3_out_0x560f6c4cbed0 [label="N", shape=none];
        interface_3_out_0x560f70f97a60 [label="C_in", shape=none];
        interface_3_out_0x560f70f802e0 [label="k_1", shape=none];
        interface_3_out_0x560f6c4cbf20 [label="H", shape=none];
        interface_3_out_0x560f70f81020 [label="H", shape=none];
        interface_3_out_0x560f70f80420 [label="g^-1*s^-1*C_out", shape=none];
    }
    {
        rank = same;
        interface_3_out_0x560f6c4cbed0;
        interface_3_out_0x560f70f97a60;
        interface_3_out_0x560f70f802e0;
        interface_3_out_0x560f6c4cbf20;
        interface_3_out_0x560f70f81020;
        interface_3_out_0x560f70f80420;
    }
    // Input 0.
    subgraph cluster_subgraph_3_in_0 {
        label = "";
        interface_3_in_0x560f6c4cbed0 [label="N", shape=none];
        interface_3_in_0x560f70f80600 [label="C_in", shape=none];
        interface_3_in_0x560f70facc20 [label="k_1", shape=none];
        interface_3_in_0x560f6c4cbf20 [label="H", shape=none];
        interface_3_in_0x560f70f81020 [label="H", shape=none];
    }
    // Input 1.
    subgraph cluster_subgraph_3_in_1 {
        label = "";
        interface_3_in_0x560f70f80618 [label="C_in", shape=none];
        interface_3_in_0x560f70facc38 [label="k_1", shape=none];
        interface_3_in_0x560f70f80488 [label="g^-1*s^-1*C_out", shape=none];
    }
    {
        rank = same;
        interface_3_in_0x560f6c4cbed0;
        interface_3_in_0x560f70f80600;
        interface_3_in_0x560f70facc20;
        interface_3_in_0x560f6c4cbf20;
        interface_3_in_0x560f70f81020;
        interface_3_in_0x560f70f80618;
        interface_3_in_0x560f70facc38;
        interface_3_in_0x560f70f80488;
    }
    // Op's.
    op_0x560f70f80450 [label="Share"];
    op_0x560f70f805e0 [label="Share"];
    op_0x560f70f80698 [label="Expand"];
    op_0x560f70facc00 [label="Share"];
    // Dimension's.
    interface_3_in_0x560f6c4cbed0 -> interface_3_out_0x560f6c4cbed0 [label="N"];
    interface_3_in_0x560f6c4cbf20 -> interface_3_out_0x560f6c4cbf20 [label="H"];
    op_0x560f70facc00 -> interface_3_out_0x560f70f802e0 [label="k_1"];
    op_0x560f70f80450 -> interface_3_out_0x560f70f80420 [label="g^-1*s^-1*C_out"];
    op_0x560f70f80698 -> op_0x560f70f80450 [label="g^-1*s^-1*C_out"];
    interface_3_in_0x560f70f80488 -> op_0x560f70f80450 [label="g^-1*s^-1*C_out"];
    interface_3_in_0x560f70f80600 -> op_0x560f70f805e0 [label="C_in"];
    interface_3_in_0x560f70f80618 -> op_0x560f70f805e0 [label="C_in"];
    interface_3_in_0x560f70f81020 -> interface_3_out_0x560f70f81020 [label="H"];
    op_0x560f70f805e0 -> interface_3_out_0x560f70f97a60 [label="C_in"];
    interface_3_in_0x560f70facc20 -> op_0x560f70facc00 [label="k_1"];
    interface_3_in_0x560f70facc38 -> op_0x560f70facc00 [label="k_1"];
}

// Stage tensor.
subgraph cluster_subgraph_4 {
    label = "Subgraph 4";
    // Reductions.
    // Output.
    subgraph cluster_subgraph_4_out {
        label = "";
        interface_4_out_0x560f6c4cbed0 [label="N", shape=none];
        interface_4_out_0x560f70f80600 [label="C_in", shape=none];
        interface_4_out_0x560f70facc20 [label="k_1", shape=none];
        interface_4_out_0x560f6c4cbf20 [label="H", shape=none];
        interface_4_out_0x560f70f81020 [label="H", shape=none];
    }
    {
        rank = same;
        interface_4_out_0x560f6c4cbed0;
        interface_4_out_0x560f70f80600;
        interface_4_out_0x560f70facc20;
        interface_4_out_0x560f6c4cbf20;
        interface_4_out_0x560f70f81020;
    }
    // Input 0.
    subgraph cluster_subgraph_4_in_0 {
        label = "";
        interface_4_in_0x560f6c4cbed0 [label="N", shape=none];
        interface_4_in_0x560f70f80600 [label="C_in", shape=none];
        interface_4_in_0x560f70f81050 [label="H", shape=none];
        interface_4_in_0x560f70f81020 [label="H", shape=none];
    }
    {
        rank = same;
        interface_4_in_0x560f6c4cbed0;
        interface_4_in_0x560f70f80600;
        interface_4_in_0x560f70f81050;
        interface_4_in_0x560f70f81020;
    }
    // Op's.
    op_0x560f70f81030 [label="Shift"];
    op_0x560f70f92f80 [label="Unfold"];
    // Dimension's.
    interface_4_in_0x560f6c4cbed0 -> interface_4_out_0x560f6c4cbed0 [label="N"];
    op_0x560f70f92f80 -> interface_4_out_0x560f6c4cbf20 [label="H"];
    interface_4_in_0x560f70f80600 -> interface_4_out_0x560f70f80600 [label="C_in"];
    interface_4_in_0x560f70f81020 -> interface_4_out_0x560f70f81020 [label="H"];
    interface_4_in_0x560f70f81050 -> op_0x560f70f81030 [label="H"];
    op_0x560f70f81030 -> op_0x560f70f92f80 [label="H"];
    op_0x560f70f92f80 -> interface_4_out_0x560f70facc20 [label="k_1"];
}

// Input tensor.
subgraph cluster_subgraph_5 {
    label = "Input 0";
    interface_5_out_0x560f6c4cbed0 [label="N", shape=none];
    interface_5_out_0x560f70f80600 [label="C_in", shape=none];
    interface_5_out_0x560f70f81050 [label="H", shape=none];
    interface_5_out_0x560f70f81020 [label="H", shape=none];
}

interface_5_out_0x560f6c4cbed0 -> interface_4_in_0x560f6c4cbed0;
interface_5_out_0x560f70f80600 -> interface_4_in_0x560f70f80600;
interface_5_out_0x560f70f81050 -> interface_4_in_0x560f70f81050;
interface_5_out_0x560f70f81020 -> interface_4_in_0x560f70f81020;

interface_4_out_0x560f6c4cbed0 -> interface_3_in_0x560f6c4cbed0;
interface_4_out_0x560f70f80600 -> interface_3_in_0x560f70f80600;
interface_4_out_0x560f70facc20 -> interface_3_in_0x560f70facc20;
interface_4_out_0x560f6c4cbf20 -> interface_3_in_0x560f6c4cbf20;
interface_4_out_0x560f70f81020 -> interface_3_in_0x560f70f81020;

// Input tensor.
subgraph cluster_subgraph_6 {
    label = "Input 2";
    interface_6_out_0x560f70f80618 [label="C_in", shape=none];
    interface_6_out_0x560f70facc38 [label="k_1", shape=none];
    interface_6_out_0x560f70f80488 [label="g^-1*s^-1*C_out", shape=none];
}

interface_6_out_0x560f70f80618 -> interface_3_in_0x560f70f80618;
interface_6_out_0x560f70facc38 -> interface_3_in_0x560f70facc38;
interface_6_out_0x560f70f80488 -> interface_3_in_0x560f70f80488;

interface_3_out_0x560f6c4cbed0 -> interface_2_in_0x560f6c4cbed0;
interface_3_out_0x560f70f97a60 -> interface_2_in_0x560f70f97a60;
interface_3_out_0x560f70f802e0 -> interface_2_in_0x560f70f802e0;
interface_3_out_0x560f6c4cbf20 -> interface_2_in_0x560f6c4cbf20;
interface_3_out_0x560f70f81020 -> interface_2_in_0x560f70f81020;
interface_3_out_0x560f70f80420 -> interface_2_in_0x560f70f80420;

interface_2_out_0x560f6c4cbed0 -> interface_1_in_0x560f6c4cbed0;
interface_2_out_0x560f70f803d0 -> interface_1_in_0x560f70f803d0;
interface_2_out_0x560f70f802e0 -> interface_1_in_0x560f70f802e0;
interface_2_out_0x560f6c4cbf20 -> interface_1_in_0x560f6c4cbf20;
interface_2_out_0x560f70f81020 -> interface_1_in_0x560f70f81020;
interface_2_out_0x560f70f80420 -> interface_1_in_0x560f70f80420;

interface_1_out_0x560f6c4cbed0 -> interface_0_in_0x560f6c4cbed0;
interface_1_out_0x560f70f803d0 -> interface_0_in_0x560f70f803d0;
interface_1_out_0x560f70f802e0 -> interface_0_in_0x560f70f802e0;
interface_1_out_0x560f6c4cbf20 -> interface_0_in_0x560f6c4cbf20;
interface_1_out_0x560f70f80290 -> interface_0_in_0x560f70f80290;
interface_1_out_0x560f6c4cbf48 -> interface_0_in_0x560f6c4cbf48;
interface_1_out_0x560f70f80420 -> interface_0_in_0x560f70f80420;

// Input tensor.
subgraph cluster_subgraph_7 {
    label = "Input 1";
    interface_7_out_0x560f70f801b8 [label="C_out", shape=none];
    interface_7_out_0x560f70f803e8 [label="g", shape=none];
    interface_7_out_0x560f70f802f8 [label="k_1", shape=none];
    interface_7_out_0x560f70f802a8 [label="k_1", shape=none];
    interface_7_out_0x560f70f80438 [label="g^-1*s^-1*C_out", shape=none];
}

interface_7_out_0x560f70f801b8 -> interface_0_in_0x560f70f801b8;
interface_7_out_0x560f70f803e8 -> interface_0_in_0x560f70f803e8;
interface_7_out_0x560f70f802f8 -> interface_0_in_0x560f70f802f8;
interface_7_out_0x560f70f802a8 -> interface_0_in_0x560f70f802a8;
interface_7_out_0x560f70f80438 -> interface_0_in_0x560f70f80438;

{
    rank = same;
    interface_5_out_0x560f6c4cbed0;
    interface_5_out_0x560f70f80600;
    interface_5_out_0x560f70f81050;
    interface_5_out_0x560f70f81020;
    interface_7_out_0x560f70f801b8;
    interface_7_out_0x560f70f803e8;
    interface_7_out_0x560f70f802f8;
    interface_7_out_0x560f70f802a8;
    interface_7_out_0x560f70f80438;
    interface_6_out_0x560f70f80618;
    interface_6_out_0x560f70facc38;
    interface_6_out_0x560f70f80488;
}
subgraph cluster_subgraph_output {
    label = "Output";
    interface_8_in_0x560f6c4cbed0 [label="N", shape=none];
    interface_8_in_0x560f6c4cbef8 [label="C_out", shape=none];
    interface_8_in_0x560f6c4cbf20 [label="H", shape=none];
    interface_8_in_0x560f6c4cbf48 [label="H", shape=none];
}
interface_0_out_0x560f6c4cbed0 -> interface_8_in_0x560f6c4cbed0;
interface_0_out_0x560f6c4cbef8 -> interface_8_in_0x560f6c4cbef8;
interface_0_out_0x560f6c4cbf20 -> interface_8_in_0x560f6c4cbf20;
interface_0_out_0x560f6c4cbf48 -> interface_8_in_0x560f6c4cbf48;

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
		t_7 = torch.einsum("nlkojpm, ilkjm -> niop", t_6, in_1)

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
		t_7 = torch.einsum("nlkojpm, ilkjm -> niop", t_6, in_1)

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
		t_7 = torch.einsum("nlkojpm, ilkjm -> niop", t_6, in_1)

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
		t_7 = torch.einsum("nlkojpm, ilkjm -> niop", t_6, in_1)

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
		t_7 = torch.einsum("nlkojpm, ilkjm -> niop", t_6, in_1)

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
		t_7 = torch.einsum("nlkojpm, ilkjm -> niop", t_6, in_1)

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
		t_7 = torch.einsum("nlkojpm, ilkjm -> niop", t_6, in_1)

		# No need to crop the output tensor.
		y = t_7

		return y

