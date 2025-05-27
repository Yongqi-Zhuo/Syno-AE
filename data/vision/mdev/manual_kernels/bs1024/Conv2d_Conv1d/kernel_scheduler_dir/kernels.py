import torch
import random
"""
digraph kernel_preview {
newrank = true;

// Stage tensor.
subgraph cluster_subgraph_0 {
    label = "Subgraph 0";
    // Reductions.
    reduce_0x55646e5fe898 [label="Sum", shape=box];
    reduce_0x55646e5fe7f8 [label="Sum", shape=box];
    reduce_0x55646e5fe810 [label="Sum", shape=box];
    reduce_0x55646e5fe950 [label="Sum", shape=box];
    // Output.
    subgraph cluster_subgraph_0_out {
        label = "";
        interface_0_out_0x7fda74000b60 [label="N", shape=none];
        interface_0_out_0x7fda38000b60 [label="C_out", shape=none];
        interface_0_out_0x7fda48000b60 [label="H", shape=none];
        interface_0_out_0x7fda40000b60 [label="H", shape=none];
    }
    {
        rank = same;
        reduce_0x55646e5fe898;
        reduce_0x55646e5fe7f8;
        reduce_0x55646e5fe810;
        reduce_0x55646e5fe950;
        interface_0_out_0x7fda74000b60;
        interface_0_out_0x7fda38000b60;
        interface_0_out_0x7fda48000b60;
        interface_0_out_0x7fda40000b60;
    }
    // Input 0.
    subgraph cluster_subgraph_0_in_0 {
        label = "";
        interface_0_in_0x7fda74000b60 [label="N", shape=none];
        interface_0_in_0x55646e5ff390 [label="g", shape=none];
        interface_0_in_0x55646e5ff2f0 [label="k_1", shape=none];
        interface_0_in_0x7fda48000b60 [label="H", shape=none];
        interface_0_in_0x55646e5ff340 [label="k_1", shape=none];
        interface_0_in_0x7fda40000b60 [label="H", shape=none];
        interface_0_in_0x55646e5ff3e0 [label="g^-1*s^-1*C_out", shape=none];
    }
    // Input 1.
    subgraph cluster_subgraph_0_in_1 {
        label = "";
        interface_0_in_0x55646e5ff2b8 [label="C_out", shape=none];
        interface_0_in_0x55646e5ff3a8 [label="g", shape=none];
        interface_0_in_0x55646e5ff308 [label="k_1", shape=none];
        interface_0_in_0x55646e5ff358 [label="k_1", shape=none];
        interface_0_in_0x55646e5ff3f8 [label="g^-1*s^-1*C_out", shape=none];
    }
    {
        rank = same;
        interface_0_in_0x7fda74000b60;
        interface_0_in_0x55646e5ff390;
        interface_0_in_0x55646e5ff2f0;
        interface_0_in_0x7fda48000b60;
        interface_0_in_0x55646e5ff340;
        interface_0_in_0x7fda40000b60;
        interface_0_in_0x55646e5ff3e0;
        interface_0_in_0x55646e5ff2b8;
        interface_0_in_0x55646e5ff3a8;
        interface_0_in_0x55646e5ff308;
        interface_0_in_0x55646e5ff358;
        interface_0_in_0x55646e5ff3f8;
    }
    // Op's.
    op_0x55646e5ff280 [label="Share"];
    op_0x55646e5ff2d0 [label="Share"];
    op_0x55646e5ff320 [label="Share"];
    op_0x55646e5ff370 [label="Share"];
    op_0x55646e5ff3c0 [label="Share"];
    op_0x55646e5ff7f8 [label="Expand"];
    // Dimension's.
    op_0x55646e5ff2d0 -> reduce_0x55646e5fe7f8 [label="k_1"];
    op_0x55646e5ff320 -> reduce_0x55646e5fe810 [label="k_1"];
    op_0x55646e5ff370 -> reduce_0x55646e5fe898 [label="g"];
    op_0x55646e5ff3c0 -> reduce_0x55646e5fe950 [label="g^-1*s^-1*C_out"];
    op_0x55646e5ff7f8 -> op_0x55646e5ff280 [label="C_out"];
    interface_0_in_0x55646e5ff2b8 -> op_0x55646e5ff280 [label="C_out"];
    interface_0_in_0x55646e5ff2f0 -> op_0x55646e5ff2d0 [label="k_1"];
    interface_0_in_0x55646e5ff308 -> op_0x55646e5ff2d0 [label="k_1"];
    interface_0_in_0x55646e5ff340 -> op_0x55646e5ff320 [label="k_1"];
    interface_0_in_0x55646e5ff358 -> op_0x55646e5ff320 [label="k_1"];
    interface_0_in_0x55646e5ff390 -> op_0x55646e5ff370 [label="g"];
    interface_0_in_0x55646e5ff3a8 -> op_0x55646e5ff370 [label="g"];
    interface_0_in_0x55646e5ff3e0 -> op_0x55646e5ff3c0 [label="g^-1*s^-1*C_out"];
    interface_0_in_0x55646e5ff3f8 -> op_0x55646e5ff3c0 [label="g^-1*s^-1*C_out"];
    op_0x55646e5ff280 -> interface_0_out_0x7fda38000b60 [label="C_out"];
    interface_0_in_0x7fda40000b60 -> interface_0_out_0x7fda40000b60 [label="H"];
    interface_0_in_0x7fda48000b60 -> interface_0_out_0x7fda48000b60 [label="H"];
    interface_0_in_0x7fda74000b60 -> interface_0_out_0x7fda74000b60 [label="N"];
}

// Stage tensor.
subgraph cluster_subgraph_1 {
    label = "Subgraph 1";
    // Reductions.
    // Output.
    subgraph cluster_subgraph_1_out {
        label = "";
        interface_1_out_0x7fda74000b60 [label="N", shape=none];
        interface_1_out_0x55646e5ff390 [label="g", shape=none];
        interface_1_out_0x55646e5ff2f0 [label="k_1", shape=none];
        interface_1_out_0x7fda48000b60 [label="H", shape=none];
        interface_1_out_0x55646e5ff340 [label="k_1", shape=none];
        interface_1_out_0x7fda40000b60 [label="H", shape=none];
        interface_1_out_0x55646e5ff3e0 [label="g^-1*s^-1*C_out", shape=none];
    }
    {
        rank = same;
        interface_1_out_0x7fda74000b60;
        interface_1_out_0x55646e5ff390;
        interface_1_out_0x55646e5ff2f0;
        interface_1_out_0x7fda48000b60;
        interface_1_out_0x55646e5ff340;
        interface_1_out_0x7fda40000b60;
        interface_1_out_0x55646e5ff3e0;
    }
    // Input 0.
    subgraph cluster_subgraph_1_in_0 {
        label = "";
        interface_1_in_0x7fda74000b60 [label="N", shape=none];
        interface_1_in_0x55646e5ff390 [label="g", shape=none];
        interface_1_in_0x55646e5ffc68 [label="H", shape=none];
        interface_1_in_0x55646e5ffca8 [label="H", shape=none];
        interface_1_in_0x55646e5ff3e0 [label="g^-1*s^-1*C_out", shape=none];
    }
    {
        rank = same;
        interface_1_in_0x7fda74000b60;
        interface_1_in_0x55646e5ff390;
        interface_1_in_0x55646e5ffc68;
        interface_1_in_0x55646e5ffca8;
        interface_1_in_0x55646e5ff3e0;
    }
    // Op's.
    op_0x55646e5ffc40 [label="Unfold"];
    op_0x55646e5ffc80 [label="Unfold"];
    // Dimension's.
    op_0x55646e5ffc40 -> interface_1_out_0x55646e5ff2f0 [label="k_1"];
    op_0x55646e5ffc80 -> interface_1_out_0x55646e5ff340 [label="k_1"];
    interface_1_in_0x55646e5ff390 -> interface_1_out_0x55646e5ff390 [label="g"];
    interface_1_in_0x55646e5ff3e0 -> interface_1_out_0x55646e5ff3e0 [label="g^-1*s^-1*C_out"];
    interface_1_in_0x55646e5ffc68 -> op_0x55646e5ffc40 [label="H"];
    interface_1_in_0x55646e5ffca8 -> op_0x55646e5ffc80 [label="H"];
    op_0x55646e5ffc80 -> interface_1_out_0x7fda40000b60 [label="H"];
    op_0x55646e5ffc40 -> interface_1_out_0x7fda48000b60 [label="H"];
    interface_1_in_0x7fda74000b60 -> interface_1_out_0x7fda74000b60 [label="N"];
}

// Stage tensor.
subgraph cluster_subgraph_2 {
    label = "Subgraph 2";
    // Reductions.
    reduce_0x55646e5fe728 [label="Sum", shape=box];
    // Output.
    subgraph cluster_subgraph_2_out {
        label = "";
        interface_2_out_0x7fda74000b60 [label="N", shape=none];
        interface_2_out_0x55646e5ff390 [label="g", shape=none];
        interface_2_out_0x55646e5ffc68 [label="H", shape=none];
        interface_2_out_0x55646e5ffca8 [label="H", shape=none];
        interface_2_out_0x55646e5ff3e0 [label="g^-1*s^-1*C_out", shape=none];
    }
    {
        rank = same;
        reduce_0x55646e5fe728;
        interface_2_out_0x7fda74000b60;
        interface_2_out_0x55646e5ff390;
        interface_2_out_0x55646e5ffc68;
        interface_2_out_0x55646e5ffca8;
        interface_2_out_0x55646e5ff3e0;
    }
    // Input 0.
    subgraph cluster_subgraph_2_in_0 {
        label = "";
        interface_2_in_0x7fda74000b60 [label="N", shape=none];
        interface_2_in_0x55646e6000c0 [label="C_in", shape=none];
        interface_2_in_0x55646e5ffc68 [label="H", shape=none];
        interface_2_in_0x55646e5ffca8 [label="H", shape=none];
        interface_2_in_0x55646e5ff3e0 [label="g^-1*s^-1*C_out", shape=none];
    }
    {
        rank = same;
        interface_2_in_0x7fda74000b60;
        interface_2_in_0x55646e6000c0;
        interface_2_in_0x55646e5ffc68;
        interface_2_in_0x55646e5ffca8;
        interface_2_in_0x55646e5ff3e0;
    }
    // Op's.
    op_0x55646e600080 [label="Split"];
    // Dimension's.
    op_0x55646e600080 -> reduce_0x55646e5fe728 [label="g^-1*C_in"];
    op_0x55646e600080 -> interface_2_out_0x55646e5ff390 [label="g"];
    interface_2_in_0x55646e5ff3e0 -> interface_2_out_0x55646e5ff3e0 [label="g^-1*s^-1*C_out"];
    interface_2_in_0x55646e5ffc68 -> interface_2_out_0x55646e5ffc68 [label="H"];
    interface_2_in_0x55646e5ffca8 -> interface_2_out_0x55646e5ffca8 [label="H"];
    interface_2_in_0x55646e6000c0 -> op_0x55646e600080 [label="C_in"];
    interface_2_in_0x7fda74000b60 -> interface_2_out_0x7fda74000b60 [label="N"];
}

// Stage tensor.
subgraph cluster_subgraph_3 {
    label = "Subgraph 3";
    // Reductions.
    reduce_0x55646e5fe7e0 [label="Sum", shape=box];
    // Output.
    subgraph cluster_subgraph_3_out {
        label = "";
        interface_3_out_0x7fda74000b60 [label="N", shape=none];
        interface_3_out_0x55646e6000c0 [label="C_in", shape=none];
        interface_3_out_0x55646e5ffc68 [label="H", shape=none];
        interface_3_out_0x55646e5ffca8 [label="H", shape=none];
        interface_3_out_0x55646e5ff3e0 [label="g^-1*s^-1*C_out", shape=none];
    }
    {
        rank = same;
        reduce_0x55646e5fe7e0;
        interface_3_out_0x7fda74000b60;
        interface_3_out_0x55646e6000c0;
        interface_3_out_0x55646e5ffc68;
        interface_3_out_0x55646e5ffca8;
        interface_3_out_0x55646e5ff3e0;
    }
    // Input 0.
    subgraph cluster_subgraph_3_in_0 {
        label = "";
        interface_3_in_0x7fda74000b60 [label="N", shape=none];
        interface_3_in_0x55646e5ff480 [label="C_in", shape=none];
        interface_3_in_0x55646e5ffc68 [label="H", shape=none];
        interface_3_in_0x55646e5ff430 [label="k_1", shape=none];
        interface_3_in_0x55646e5ffca8 [label="H", shape=none];
    }
    // Input 1.
    subgraph cluster_subgraph_3_in_1 {
        label = "";
        interface_3_in_0x55646e5ff498 [label="C_in", shape=none];
        interface_3_in_0x55646e5ff448 [label="k_1", shape=none];
        interface_3_in_0x55646e5ff4e8 [label="g^-1*s^-1*C_out", shape=none];
    }
    {
        rank = same;
        interface_3_in_0x7fda74000b60;
        interface_3_in_0x55646e5ff480;
        interface_3_in_0x55646e5ffc68;
        interface_3_in_0x55646e5ff430;
        interface_3_in_0x55646e5ffca8;
        interface_3_in_0x55646e5ff498;
        interface_3_in_0x55646e5ff448;
        interface_3_in_0x55646e5ff4e8;
    }
    // Op's.
    op_0x55646e5ff410 [label="Share"];
    op_0x55646e5ff460 [label="Share"];
    op_0x55646e5ff4b0 [label="Share"];
    op_0x55646e5ff818 [label="Expand"];
    // Dimension's.
    op_0x55646e5ff410 -> reduce_0x55646e5fe7e0 [label="k_1"];
    op_0x55646e5ff4b0 -> interface_3_out_0x55646e5ff3e0 [label="g^-1*s^-1*C_out"];
    interface_3_in_0x55646e5ff430 -> op_0x55646e5ff410 [label="k_1"];
    interface_3_in_0x55646e5ff448 -> op_0x55646e5ff410 [label="k_1"];
    interface_3_in_0x55646e5ff480 -> op_0x55646e5ff460 [label="C_in"];
    interface_3_in_0x55646e5ff498 -> op_0x55646e5ff460 [label="C_in"];
    op_0x55646e5ff818 -> op_0x55646e5ff4b0 [label="g^-1*s^-1*C_out"];
    interface_3_in_0x55646e5ff4e8 -> op_0x55646e5ff4b0 [label="g^-1*s^-1*C_out"];
    interface_3_in_0x55646e5ffc68 -> interface_3_out_0x55646e5ffc68 [label="H"];
    interface_3_in_0x55646e5ffca8 -> interface_3_out_0x55646e5ffca8 [label="H"];
    op_0x55646e5ff460 -> interface_3_out_0x55646e6000c0 [label="C_in"];
    interface_3_in_0x7fda74000b60 -> interface_3_out_0x7fda74000b60 [label="N"];
}

// Stage tensor.
subgraph cluster_subgraph_4 {
    label = "Subgraph 4";
    // Reductions.
    // Output.
    subgraph cluster_subgraph_4_out {
        label = "";
        interface_4_out_0x7fda74000b60 [label="N", shape=none];
        interface_4_out_0x55646e5ff480 [label="C_in", shape=none];
        interface_4_out_0x55646e5ffc68 [label="H", shape=none];
        interface_4_out_0x55646e5ff430 [label="k_1", shape=none];
        interface_4_out_0x55646e5ffca8 [label="H", shape=none];
    }
    {
        rank = same;
        interface_4_out_0x7fda74000b60;
        interface_4_out_0x55646e5ff480;
        interface_4_out_0x55646e5ffc68;
        interface_4_out_0x55646e5ff430;
        interface_4_out_0x55646e5ffca8;
    }
    // Input 0.
    subgraph cluster_subgraph_4_in_0 {
        label = "";
        interface_4_in_0x7fda74000b60 [label="N", shape=none];
        interface_4_in_0x55646e5ff480 [label="C_in", shape=none];
        interface_4_in_0x55646e5ffc68 [label="H", shape=none];
        interface_4_in_0x55646e5ffce8 [label="H", shape=none];
    }
    {
        rank = same;
        interface_4_in_0x7fda74000b60;
        interface_4_in_0x55646e5ff480;
        interface_4_in_0x55646e5ffc68;
        interface_4_in_0x55646e5ffce8;
    }
    // Op's.
    op_0x55646e5ffcc0 [label="Unfold"];
    // Dimension's.
    op_0x55646e5ffcc0 -> interface_4_out_0x55646e5ff430 [label="k_1"];
    interface_4_in_0x55646e5ff480 -> interface_4_out_0x55646e5ff480 [label="C_in"];
    interface_4_in_0x55646e5ffc68 -> interface_4_out_0x55646e5ffc68 [label="H"];
    op_0x55646e5ffcc0 -> interface_4_out_0x55646e5ffca8 [label="H"];
    interface_4_in_0x55646e5ffce8 -> op_0x55646e5ffcc0 [label="H"];
    interface_4_in_0x7fda74000b60 -> interface_4_out_0x7fda74000b60 [label="N"];
}

// Input tensor.
subgraph cluster_subgraph_5 {
    label = "Input 0";
    interface_5_out_0x7fda74000b60 [label="N", shape=none];
    interface_5_out_0x55646e5ff480 [label="C_in", shape=none];
    interface_5_out_0x55646e5ffc68 [label="H", shape=none];
    interface_5_out_0x55646e5ffce8 [label="H", shape=none];
}

interface_5_out_0x7fda74000b60 -> interface_4_in_0x7fda74000b60;
interface_5_out_0x55646e5ff480 -> interface_4_in_0x55646e5ff480;
interface_5_out_0x55646e5ffc68 -> interface_4_in_0x55646e5ffc68;
interface_5_out_0x55646e5ffce8 -> interface_4_in_0x55646e5ffce8;

interface_4_out_0x7fda74000b60 -> interface_3_in_0x7fda74000b60;
interface_4_out_0x55646e5ff480 -> interface_3_in_0x55646e5ff480;
interface_4_out_0x55646e5ffc68 -> interface_3_in_0x55646e5ffc68;
interface_4_out_0x55646e5ff430 -> interface_3_in_0x55646e5ff430;
interface_4_out_0x55646e5ffca8 -> interface_3_in_0x55646e5ffca8;

// Input tensor.
subgraph cluster_subgraph_6 {
    label = "Input 2";
    interface_6_out_0x55646e5ff498 [label="C_in", shape=none];
    interface_6_out_0x55646e5ff448 [label="k_1", shape=none];
    interface_6_out_0x55646e5ff4e8 [label="g^-1*s^-1*C_out", shape=none];
}

interface_6_out_0x55646e5ff498 -> interface_3_in_0x55646e5ff498;
interface_6_out_0x55646e5ff448 -> interface_3_in_0x55646e5ff448;
interface_6_out_0x55646e5ff4e8 -> interface_3_in_0x55646e5ff4e8;

interface_3_out_0x7fda74000b60 -> interface_2_in_0x7fda74000b60;
interface_3_out_0x55646e6000c0 -> interface_2_in_0x55646e6000c0;
interface_3_out_0x55646e5ffc68 -> interface_2_in_0x55646e5ffc68;
interface_3_out_0x55646e5ffca8 -> interface_2_in_0x55646e5ffca8;
interface_3_out_0x55646e5ff3e0 -> interface_2_in_0x55646e5ff3e0;

interface_2_out_0x7fda74000b60 -> interface_1_in_0x7fda74000b60;
interface_2_out_0x55646e5ff390 -> interface_1_in_0x55646e5ff390;
interface_2_out_0x55646e5ffc68 -> interface_1_in_0x55646e5ffc68;
interface_2_out_0x55646e5ffca8 -> interface_1_in_0x55646e5ffca8;
interface_2_out_0x55646e5ff3e0 -> interface_1_in_0x55646e5ff3e0;

interface_1_out_0x7fda74000b60 -> interface_0_in_0x7fda74000b60;
interface_1_out_0x55646e5ff390 -> interface_0_in_0x55646e5ff390;
interface_1_out_0x55646e5ff2f0 -> interface_0_in_0x55646e5ff2f0;
interface_1_out_0x7fda48000b60 -> interface_0_in_0x7fda48000b60;
interface_1_out_0x55646e5ff340 -> interface_0_in_0x55646e5ff340;
interface_1_out_0x7fda40000b60 -> interface_0_in_0x7fda40000b60;
interface_1_out_0x55646e5ff3e0 -> interface_0_in_0x55646e5ff3e0;

// Input tensor.
subgraph cluster_subgraph_7 {
    label = "Input 1";
    interface_7_out_0x55646e5ff2b8 [label="C_out", shape=none];
    interface_7_out_0x55646e5ff3a8 [label="g", shape=none];
    interface_7_out_0x55646e5ff308 [label="k_1", shape=none];
    interface_7_out_0x55646e5ff358 [label="k_1", shape=none];
    interface_7_out_0x55646e5ff3f8 [label="g^-1*s^-1*C_out", shape=none];
}

interface_7_out_0x55646e5ff2b8 -> interface_0_in_0x55646e5ff2b8;
interface_7_out_0x55646e5ff3a8 -> interface_0_in_0x55646e5ff3a8;
interface_7_out_0x55646e5ff308 -> interface_0_in_0x55646e5ff308;
interface_7_out_0x55646e5ff358 -> interface_0_in_0x55646e5ff358;
interface_7_out_0x55646e5ff3f8 -> interface_0_in_0x55646e5ff3f8;

{
    rank = same;
    interface_5_out_0x7fda74000b60;
    interface_5_out_0x55646e5ff480;
    interface_5_out_0x55646e5ffc68;
    interface_5_out_0x55646e5ffce8;
    interface_7_out_0x55646e5ff2b8;
    interface_7_out_0x55646e5ff3a8;
    interface_7_out_0x55646e5ff308;
    interface_7_out_0x55646e5ff358;
    interface_7_out_0x55646e5ff3f8;
    interface_6_out_0x55646e5ff498;
    interface_6_out_0x55646e5ff448;
    interface_6_out_0x55646e5ff4e8;
}
subgraph cluster_subgraph_output {
    label = "Output";
    interface_8_in_0x7fda74000b60 [label="N", shape=none];
    interface_8_in_0x7fda38000b60 [label="C_out", shape=none];
    interface_8_in_0x7fda48000b60 [label="H", shape=none];
    interface_8_in_0x7fda40000b60 [label="H", shape=none];
}
interface_0_out_0x7fda74000b60 -> interface_8_in_0x7fda74000b60;
interface_0_out_0x7fda38000b60 -> interface_8_in_0x7fda38000b60;
interface_0_out_0x7fda48000b60 -> interface_8_in_0x7fda48000b60;
interface_0_out_0x7fda40000b60 -> interface_8_in_0x7fda40000b60;

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

		# [H]@Unfold22f5584eb7a8b416 -> [H]@Unfolde73c9e24012bc66d, [k_1]@Shared4e0659d169008e4
		t_3 = torch.reshape(t_3, (1024, 3584, 56, 1, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (1024, 64, 56, 3, 56, ))

		# Perform contraction.
		t_4 = torch.einsum("njlim, jik -> njlmk", t_3, in_2)

		# No contraction needed.
		t_5 = t_4

		# [C_in]@Splitc2d52f3525ba6cc4 -> [g]@Sharec7a8ce455b828537, [g^-1*C_in]@Reduceef9903cafc29eea1
		t_5 = torch.reshape(t_5, (1024, 32, 2, 56, 56, 1, ))

		# [g^-1*C_in]@Reduce
		t_5 = torch.sum(t_5, dim=(2, ))

		# No contraction needed.
		t_6 = t_5

		# [H]@Unfold87ed2fb8f6552d8f -> [H]@Iterator96123ba3184da39c, [k_1]@Share02da0a485106ab3d
		t_6 = torch.reshape(t_6, (1024, 32, 56, 56, ))
		t_6 = torch.nn.functional.unfold(t_6, (3, 1, ), padding=(1, 0, ))
		t_6 = torch.reshape(t_6, (1024, 32, 3, 56, 56, 1, ))

		# [H]@Unfolde73c9e24012bc66d -> [H]@Iteratorb0a1def4ad5784ec, [k_1]@Share20826c8af74ae67f
		t_6 = torch.reshape(t_6, (1024, 5376, 56, 1, ))
		t_6 = torch.nn.functional.unfold(t_6, (3, 1, ), padding=(1, 0, ))
		t_6 = torch.reshape(t_6, (1024, 32, 3, 56, 3, 56, 1, ))

		# Perform contraction.
		t_7 = torch.einsum("pljoknm, iljkm -> pion", t_6, in_1)

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

		# [H]@Unfold22f5584eb7a8b416 -> [H]@Unfolde73c9e24012bc66d, [k_1]@Shared4e0659d169008e4
		t_3 = torch.reshape(t_3, (1024, 1792, 28, 1, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (1024, 64, 28, 3, 28, ))

		# Perform contraction.
		t_4 = torch.einsum("njlim, jik -> njlmk", t_3, in_2)

		# No contraction needed.
		t_5 = t_4

		# [C_in]@Splitc2d52f3525ba6cc4 -> [g]@Sharec7a8ce455b828537, [g^-1*C_in]@Reduceef9903cafc29eea1
		t_5 = torch.reshape(t_5, (1024, 32, 2, 28, 28, 2, ))

		# [g^-1*C_in]@Reduce
		t_5 = torch.sum(t_5, dim=(2, ))

		# No contraction needed.
		t_6 = t_5

		# [H]@Unfold87ed2fb8f6552d8f -> [H]@Iterator96123ba3184da39c, [k_1]@Share02da0a485106ab3d
		t_6 = torch.reshape(t_6, (1024, 32, 28, 56, ))
		t_6 = torch.nn.functional.unfold(t_6, (3, 1, ), padding=(1, 0, ))
		t_6 = torch.reshape(t_6, (1024, 32, 3, 28, 28, 2, ))

		# [H]@Unfolde73c9e24012bc66d -> [H]@Iteratorb0a1def4ad5784ec, [k_1]@Share20826c8af74ae67f
		t_6 = torch.reshape(t_6, (1024, 2688, 28, 2, ))
		t_6 = torch.nn.functional.unfold(t_6, (3, 1, ), padding=(1, 0, ))
		t_6 = torch.reshape(t_6, (1024, 32, 3, 28, 3, 28, 2, ))

		# Perform contraction.
		t_7 = torch.einsum("pljoknm, iljkm -> pion", t_6, in_1)

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

		# [H]@Unfold22f5584eb7a8b416 -> [H]@Unfolde73c9e24012bc66d, [k_1]@Shared4e0659d169008e4
		t_3 = torch.reshape(t_3, (1024, 3584, 28, 1, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (1024, 128, 28, 3, 28, ))

		# Perform contraction.
		t_4 = torch.einsum("njlim, jik -> njlmk", t_3, in_2)

		# No contraction needed.
		t_5 = t_4

		# [C_in]@Splitc2d52f3525ba6cc4 -> [g]@Sharec7a8ce455b828537, [g^-1*C_in]@Reduceef9903cafc29eea1
		t_5 = torch.reshape(t_5, (1024, 32, 4, 28, 28, 2, ))

		# [g^-1*C_in]@Reduce
		t_5 = torch.sum(t_5, dim=(2, ))

		# No contraction needed.
		t_6 = t_5

		# [H]@Unfold87ed2fb8f6552d8f -> [H]@Iterator96123ba3184da39c, [k_1]@Share02da0a485106ab3d
		t_6 = torch.reshape(t_6, (1024, 32, 28, 56, ))
		t_6 = torch.nn.functional.unfold(t_6, (3, 1, ), padding=(1, 0, ))
		t_6 = torch.reshape(t_6, (1024, 32, 3, 28, 28, 2, ))

		# [H]@Unfolde73c9e24012bc66d -> [H]@Iteratorb0a1def4ad5784ec, [k_1]@Share20826c8af74ae67f
		t_6 = torch.reshape(t_6, (1024, 2688, 28, 2, ))
		t_6 = torch.nn.functional.unfold(t_6, (3, 1, ), padding=(1, 0, ))
		t_6 = torch.reshape(t_6, (1024, 32, 3, 28, 3, 28, 2, ))

		# Perform contraction.
		t_7 = torch.einsum("pljoknm, iljkm -> pion", t_6, in_1)

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

		# [H]@Unfold22f5584eb7a8b416 -> [H]@Unfolde73c9e24012bc66d, [k_1]@Shared4e0659d169008e4
		t_3 = torch.reshape(t_3, (1024, 1792, 14, 1, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (1024, 128, 14, 3, 14, ))

		# Perform contraction.
		t_4 = torch.einsum("njlim, jik -> njlmk", t_3, in_2)

		# No contraction needed.
		t_5 = t_4

		# [C_in]@Splitc2d52f3525ba6cc4 -> [g]@Sharec7a8ce455b828537, [g^-1*C_in]@Reduceef9903cafc29eea1
		t_5 = torch.reshape(t_5, (1024, 32, 4, 14, 14, 4, ))

		# [g^-1*C_in]@Reduce
		t_5 = torch.sum(t_5, dim=(2, ))

		# No contraction needed.
		t_6 = t_5

		# [H]@Unfold87ed2fb8f6552d8f -> [H]@Iterator96123ba3184da39c, [k_1]@Share02da0a485106ab3d
		t_6 = torch.reshape(t_6, (1024, 32, 14, 56, ))
		t_6 = torch.nn.functional.unfold(t_6, (3, 1, ), padding=(1, 0, ))
		t_6 = torch.reshape(t_6, (1024, 32, 3, 14, 14, 4, ))

		# [H]@Unfolde73c9e24012bc66d -> [H]@Iteratorb0a1def4ad5784ec, [k_1]@Share20826c8af74ae67f
		t_6 = torch.reshape(t_6, (1024, 1344, 14, 4, ))
		t_6 = torch.nn.functional.unfold(t_6, (3, 1, ), padding=(1, 0, ))
		t_6 = torch.reshape(t_6, (1024, 32, 3, 14, 3, 14, 4, ))

		# Perform contraction.
		t_7 = torch.einsum("pljoknm, iljkm -> pion", t_6, in_1)

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

		# [H]@Unfold22f5584eb7a8b416 -> [H]@Unfolde73c9e24012bc66d, [k_1]@Shared4e0659d169008e4
		t_3 = torch.reshape(t_3, (1024, 3584, 14, 1, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (1024, 256, 14, 3, 14, ))

		# Perform contraction.
		t_4 = torch.einsum("njlim, jik -> njlmk", t_3, in_2)

		# No contraction needed.
		t_5 = t_4

		# [C_in]@Splitc2d52f3525ba6cc4 -> [g]@Sharec7a8ce455b828537, [g^-1*C_in]@Reduceef9903cafc29eea1
		t_5 = torch.reshape(t_5, (1024, 32, 8, 14, 14, 4, ))

		# [g^-1*C_in]@Reduce
		t_5 = torch.sum(t_5, dim=(2, ))

		# No contraction needed.
		t_6 = t_5

		# [H]@Unfold87ed2fb8f6552d8f -> [H]@Iterator96123ba3184da39c, [k_1]@Share02da0a485106ab3d
		t_6 = torch.reshape(t_6, (1024, 32, 14, 56, ))
		t_6 = torch.nn.functional.unfold(t_6, (3, 1, ), padding=(1, 0, ))
		t_6 = torch.reshape(t_6, (1024, 32, 3, 14, 14, 4, ))

		# [H]@Unfolde73c9e24012bc66d -> [H]@Iteratorb0a1def4ad5784ec, [k_1]@Share20826c8af74ae67f
		t_6 = torch.reshape(t_6, (1024, 1344, 14, 4, ))
		t_6 = torch.nn.functional.unfold(t_6, (3, 1, ), padding=(1, 0, ))
		t_6 = torch.reshape(t_6, (1024, 32, 3, 14, 3, 14, 4, ))

		# Perform contraction.
		t_7 = torch.einsum("pljoknm, iljkm -> pion", t_6, in_1)

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

		# [H]@Unfold22f5584eb7a8b416 -> [H]@Unfolde73c9e24012bc66d, [k_1]@Shared4e0659d169008e4
		t_3 = torch.reshape(t_3, (1024, 1792, 7, 1, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (1024, 256, 7, 3, 7, ))

		# Perform contraction.
		t_4 = torch.einsum("njlim, jik -> njlmk", t_3, in_2)

		# No contraction needed.
		t_5 = t_4

		# [C_in]@Splitc2d52f3525ba6cc4 -> [g]@Sharec7a8ce455b828537, [g^-1*C_in]@Reduceef9903cafc29eea1
		t_5 = torch.reshape(t_5, (1024, 32, 8, 7, 7, 8, ))

		# [g^-1*C_in]@Reduce
		t_5 = torch.sum(t_5, dim=(2, ))

		# No contraction needed.
		t_6 = t_5

		# [H]@Unfold87ed2fb8f6552d8f -> [H]@Iterator96123ba3184da39c, [k_1]@Share02da0a485106ab3d
		t_6 = torch.reshape(t_6, (1024, 32, 7, 56, ))
		t_6 = torch.nn.functional.unfold(t_6, (3, 1, ), padding=(1, 0, ))
		t_6 = torch.reshape(t_6, (1024, 32, 3, 7, 7, 8, ))

		# [H]@Unfolde73c9e24012bc66d -> [H]@Iteratorb0a1def4ad5784ec, [k_1]@Share20826c8af74ae67f
		t_6 = torch.reshape(t_6, (1024, 672, 7, 8, ))
		t_6 = torch.nn.functional.unfold(t_6, (3, 1, ), padding=(1, 0, ))
		t_6 = torch.reshape(t_6, (1024, 32, 3, 7, 3, 7, 8, ))

		# Perform contraction.
		t_7 = torch.einsum("pljoknm, iljkm -> pion", t_6, in_1)

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

		# [H]@Unfold22f5584eb7a8b416 -> [H]@Unfolde73c9e24012bc66d, [k_1]@Shared4e0659d169008e4
		t_3 = torch.reshape(t_3, (1024, 3584, 7, 1, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (1024, 512, 7, 3, 7, ))

		# Perform contraction.
		t_4 = torch.einsum("njlim, jik -> njlmk", t_3, in_2)

		# No contraction needed.
		t_5 = t_4

		# [C_in]@Splitc2d52f3525ba6cc4 -> [g]@Sharec7a8ce455b828537, [g^-1*C_in]@Reduceef9903cafc29eea1
		t_5 = torch.reshape(t_5, (1024, 32, 16, 7, 7, 8, ))

		# [g^-1*C_in]@Reduce
		t_5 = torch.sum(t_5, dim=(2, ))

		# No contraction needed.
		t_6 = t_5

		# [H]@Unfold87ed2fb8f6552d8f -> [H]@Iterator96123ba3184da39c, [k_1]@Share02da0a485106ab3d
		t_6 = torch.reshape(t_6, (1024, 32, 7, 56, ))
		t_6 = torch.nn.functional.unfold(t_6, (3, 1, ), padding=(1, 0, ))
		t_6 = torch.reshape(t_6, (1024, 32, 3, 7, 7, 8, ))

		# [H]@Unfolde73c9e24012bc66d -> [H]@Iteratorb0a1def4ad5784ec, [k_1]@Share20826c8af74ae67f
		t_6 = torch.reshape(t_6, (1024, 672, 7, 8, ))
		t_6 = torch.nn.functional.unfold(t_6, (3, 1, ), padding=(1, 0, ))
		t_6 = torch.reshape(t_6, (1024, 32, 3, 7, 3, 7, 8, ))

		# Perform contraction.
		t_7 = torch.einsum("pljoknm, iljkm -> pion", t_6, in_1)

		# No need to crop the output tensor.
		y = t_7

		return y

