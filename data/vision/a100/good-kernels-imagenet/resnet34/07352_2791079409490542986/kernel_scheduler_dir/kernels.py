import torch
import random
"""
digraph kernel_preview {
newrank = true;

// Stage tensor.
subgraph cluster_subgraph_0 {
    label = "Subgraph 0";
    // Reductions.
    reduce_0x7f7a20003928 [label="Sum", shape=box];
    reduce_0x7f7a20003a98 [label="Sum", shape=box];
    reduce_0x7f7a20003ab0 [label="Sum", shape=box];
    reduce_0x7f7a2000ae88 [label="Sum", shape=box];
    // Output.
    subgraph cluster_subgraph_0_out {
        label = "";
        interface_0_out_0x5605b0775920 [label="N", shape=none];
        interface_0_out_0x5605b0775948 [label="C_out", shape=none];
        interface_0_out_0x5605b0775970 [label="H", shape=none];
        interface_0_out_0x5605b0775998 [label="H", shape=none];
    }
    {
        rank = same;
        reduce_0x7f7a20003928;
        reduce_0x7f7a20003a98;
        reduce_0x7f7a20003ab0;
        reduce_0x7f7a2000ae88;
        interface_0_out_0x5605b0775920;
        interface_0_out_0x5605b0775948;
        interface_0_out_0x5605b0775970;
        interface_0_out_0x5605b0775998;
    }
    // Input 0.
    subgraph cluster_subgraph_0_in_0 {
        label = "";
        interface_0_in_0x5605b0775920 [label="N", shape=none];
        interface_0_in_0x5605beb88c30 [label="g", shape=none];
        interface_0_in_0x5605beb88910 [label="k_1", shape=none];
        interface_0_in_0x5605b0775970 [label="H", shape=none];
        interface_0_in_0x5605beb88b40 [label="k_1", shape=none];
        interface_0_in_0x5605b0775998 [label="H", shape=none];
        interface_0_in_0x5605beb88c80 [label="g^-1*s^-1*C_out", shape=none];
    }
    // Input 1.
    subgraph cluster_subgraph_0_in_1 {
        label = "";
        interface_0_in_0x5605beb88838 [label="C_out", shape=none];
        interface_0_in_0x5605beb88c48 [label="g", shape=none];
        interface_0_in_0x5605beb88928 [label="k_1", shape=none];
        interface_0_in_0x5605beb88b58 [label="k_1", shape=none];
        interface_0_in_0x5605beb88c98 [label="g^-1*s^-1*C_out", shape=none];
    }
    {
        rank = same;
        interface_0_in_0x5605b0775920;
        interface_0_in_0x5605beb88c30;
        interface_0_in_0x5605beb88910;
        interface_0_in_0x5605b0775970;
        interface_0_in_0x5605beb88b40;
        interface_0_in_0x5605b0775998;
        interface_0_in_0x5605beb88c80;
        interface_0_in_0x5605beb88838;
        interface_0_in_0x5605beb88c48;
        interface_0_in_0x5605beb88928;
        interface_0_in_0x5605beb88b58;
        interface_0_in_0x5605beb88c98;
    }
    // Op's.
    op_0x5605beb88800 [label="Share"];
    op_0x5605beb888f0 [label="Share"];
    op_0x5605beb88b20 [label="Share"];
    op_0x5605beb88c10 [label="Share"];
    op_0x5605beb88c60 [label="Share"];
    op_0x5605beb88cd8 [label="Expand"];
    // Dimension's.
    interface_0_in_0x5605b0775920 -> interface_0_out_0x5605b0775920 [label="N"];
    op_0x5605beb88800 -> interface_0_out_0x5605b0775948 [label="C_out"];
    interface_0_in_0x5605b0775970 -> interface_0_out_0x5605b0775970 [label="H"];
    interface_0_in_0x5605b0775998 -> interface_0_out_0x5605b0775998 [label="H"];
    op_0x5605beb88cd8 -> op_0x5605beb88800 [label="C_out"];
    interface_0_in_0x5605beb88838 -> op_0x5605beb88800 [label="C_out"];
    interface_0_in_0x5605beb88910 -> op_0x5605beb888f0 [label="k_1"];
    interface_0_in_0x5605beb88928 -> op_0x5605beb888f0 [label="k_1"];
    interface_0_in_0x5605beb88b40 -> op_0x5605beb88b20 [label="k_1"];
    interface_0_in_0x5605beb88b58 -> op_0x5605beb88b20 [label="k_1"];
    interface_0_in_0x5605beb88c30 -> op_0x5605beb88c10 [label="g"];
    interface_0_in_0x5605beb88c48 -> op_0x5605beb88c10 [label="g"];
    interface_0_in_0x5605beb88c80 -> op_0x5605beb88c60 [label="g^-1*s^-1*C_out"];
    interface_0_in_0x5605beb88c98 -> op_0x5605beb88c60 [label="g^-1*s^-1*C_out"];
    op_0x5605beb88c10 -> reduce_0x7f7a20003928 [label="g"];
    op_0x5605beb888f0 -> reduce_0x7f7a20003a98 [label="k_1"];
    op_0x5605beb88b20 -> reduce_0x7f7a20003ab0 [label="k_1"];
    op_0x5605beb88c60 -> reduce_0x7f7a2000ae88 [label="g^-1*s^-1*C_out"];
}

// Stage tensor.
subgraph cluster_subgraph_1 {
    label = "Subgraph 1";
    // Reductions.
    // Output.
    subgraph cluster_subgraph_1_out {
        label = "";
        interface_1_out_0x5605b0775920 [label="N", shape=none];
        interface_1_out_0x5605beb88c30 [label="g", shape=none];
        interface_1_out_0x5605beb88910 [label="k_1", shape=none];
        interface_1_out_0x5605b0775970 [label="H", shape=none];
        interface_1_out_0x5605beb88b40 [label="k_1", shape=none];
        interface_1_out_0x5605b0775998 [label="H", shape=none];
        interface_1_out_0x5605beb88c80 [label="g^-1*s^-1*C_out", shape=none];
    }
    {
        rank = same;
        interface_1_out_0x5605b0775920;
        interface_1_out_0x5605beb88c30;
        interface_1_out_0x5605beb88910;
        interface_1_out_0x5605b0775970;
        interface_1_out_0x5605beb88b40;
        interface_1_out_0x5605b0775998;
        interface_1_out_0x5605beb88c80;
    }
    // Input 0.
    subgraph cluster_subgraph_1_in_0 {
        label = "";
        interface_1_in_0x5605b0775920 [label="N", shape=none];
        interface_1_in_0x5605beb88c30 [label="g", shape=none];
        interface_1_in_0x5605beb97a28 [label="H", shape=none];
        interface_1_in_0x5605beb88b40 [label="k_1", shape=none];
        interface_1_in_0x5605b0775998 [label="H", shape=none];
        interface_1_in_0x5605beb88c80 [label="g^-1*s^-1*C_out", shape=none];
    }
    {
        rank = same;
        interface_1_in_0x5605b0775920;
        interface_1_in_0x5605beb88c30;
        interface_1_in_0x5605beb97a28;
        interface_1_in_0x5605beb88b40;
        interface_1_in_0x5605b0775998;
        interface_1_in_0x5605beb88c80;
    }
    // Op's.
    op_0x5605beb97a00 [label="Unfold"];
    // Dimension's.
    interface_1_in_0x5605b0775920 -> interface_1_out_0x5605b0775920 [label="N"];
    op_0x5605beb97a00 -> interface_1_out_0x5605b0775970 [label="H"];
    interface_1_in_0x5605b0775998 -> interface_1_out_0x5605b0775998 [label="H"];
    op_0x5605beb97a00 -> interface_1_out_0x5605beb88910 [label="k_1"];
    interface_1_in_0x5605beb88b40 -> interface_1_out_0x5605beb88b40 [label="k_1"];
    interface_1_in_0x5605beb88c30 -> interface_1_out_0x5605beb88c30 [label="g"];
    interface_1_in_0x5605beb88c80 -> interface_1_out_0x5605beb88c80 [label="g^-1*s^-1*C_out"];
    interface_1_in_0x5605beb97a28 -> op_0x5605beb97a00 [label="H"];
}

// Stage tensor.
subgraph cluster_subgraph_2 {
    label = "Subgraph 2";
    // Reductions.
    reduce_0x7f7a20007890 [label="Sum", shape=box];
    // Output.
    subgraph cluster_subgraph_2_out {
        label = "";
        interface_2_out_0x5605b0775920 [label="N", shape=none];
        interface_2_out_0x5605beb88c30 [label="g", shape=none];
        interface_2_out_0x5605beb97a28 [label="H", shape=none];
        interface_2_out_0x5605beb88b40 [label="k_1", shape=none];
        interface_2_out_0x5605b0775998 [label="H", shape=none];
        interface_2_out_0x5605beb88c80 [label="g^-1*s^-1*C_out", shape=none];
    }
    {
        rank = same;
        reduce_0x7f7a20007890;
        interface_2_out_0x5605b0775920;
        interface_2_out_0x5605beb88c30;
        interface_2_out_0x5605beb97a28;
        interface_2_out_0x5605beb88b40;
        interface_2_out_0x5605b0775998;
        interface_2_out_0x5605beb88c80;
    }
    // Input 0.
    subgraph cluster_subgraph_2_in_0 {
        label = "";
        interface_2_in_0x5605b0775920 [label="N", shape=none];
        interface_2_in_0x5605bebdfc80 [label="C_in", shape=none];
        interface_2_in_0x5605beb97a28 [label="H", shape=none];
        interface_2_in_0x5605beb88b40 [label="k_1", shape=none];
        interface_2_in_0x5605b0775998 [label="H", shape=none];
        interface_2_in_0x5605beb88c80 [label="g^-1*s^-1*C_out", shape=none];
    }
    {
        rank = same;
        interface_2_in_0x5605b0775920;
        interface_2_in_0x5605bebdfc80;
        interface_2_in_0x5605beb97a28;
        interface_2_in_0x5605beb88b40;
        interface_2_in_0x5605b0775998;
        interface_2_in_0x5605beb88c80;
    }
    // Op's.
    op_0x5605bebdfc40 [label="Split"];
    // Dimension's.
    interface_2_in_0x5605b0775920 -> interface_2_out_0x5605b0775920 [label="N"];
    interface_2_in_0x5605b0775998 -> interface_2_out_0x5605b0775998 [label="H"];
    interface_2_in_0x5605beb88b40 -> interface_2_out_0x5605beb88b40 [label="k_1"];
    op_0x5605bebdfc40 -> interface_2_out_0x5605beb88c30 [label="g"];
    interface_2_in_0x5605beb88c80 -> interface_2_out_0x5605beb88c80 [label="g^-1*s^-1*C_out"];
    interface_2_in_0x5605beb97a28 -> interface_2_out_0x5605beb97a28 [label="H"];
    interface_2_in_0x5605bebdfc80 -> op_0x5605bebdfc40 [label="C_in"];
    op_0x5605bebdfc40 -> reduce_0x7f7a20007890 [label="g^-1*C_in"];
}

// Stage tensor.
subgraph cluster_subgraph_3 {
    label = "Subgraph 3";
    // Reductions.
    // Output.
    subgraph cluster_subgraph_3_out {
        label = "";
        interface_3_out_0x5605b0775920 [label="N", shape=none];
        interface_3_out_0x5605bebdfc80 [label="C_in", shape=none];
        interface_3_out_0x5605beb97a28 [label="H", shape=none];
        interface_3_out_0x5605beb88b40 [label="k_1", shape=none];
        interface_3_out_0x5605b0775998 [label="H", shape=none];
        interface_3_out_0x5605beb88c80 [label="g^-1*s^-1*C_out", shape=none];
    }
    {
        rank = same;
        interface_3_out_0x5605b0775920;
        interface_3_out_0x5605bebdfc80;
        interface_3_out_0x5605beb97a28;
        interface_3_out_0x5605beb88b40;
        interface_3_out_0x5605b0775998;
        interface_3_out_0x5605beb88c80;
    }
    // Input 0.
    subgraph cluster_subgraph_3_in_0 {
        label = "";
        interface_3_in_0x5605b0775920 [label="N", shape=none];
        interface_3_in_0x5605bebd0a30 [label="C_in", shape=none];
        interface_3_in_0x5605beb97a28 [label="H", shape=none];
        interface_3_in_0x5605bebd0a80 [label="k_1", shape=none];
        interface_3_in_0x5605b0775998 [label="H", shape=none];
    }
    // Input 1.
    subgraph cluster_subgraph_3_in_1 {
        label = "";
        interface_3_in_0x5605bebd0a48 [label="C_in", shape=none];
        interface_3_in_0x5605bebd0a98 [label="k_1", shape=none];
        interface_3_in_0x5605bebd08b8 [label="g^-1*s^-1*C_out", shape=none];
    }
    {
        rank = same;
        interface_3_in_0x5605b0775920;
        interface_3_in_0x5605bebd0a30;
        interface_3_in_0x5605beb97a28;
        interface_3_in_0x5605bebd0a80;
        interface_3_in_0x5605b0775998;
        interface_3_in_0x5605bebd0a48;
        interface_3_in_0x5605bebd0a98;
        interface_3_in_0x5605bebd08b8;
    }
    // Op's.
    op_0x5605beb88d78 [label="Expand"];
    op_0x5605bebd0880 [label="Share"];
    op_0x5605bebd0a10 [label="Share"];
    op_0x5605bebd0a60 [label="Share"];
    // Dimension's.
    interface_3_in_0x5605b0775920 -> interface_3_out_0x5605b0775920 [label="N"];
    interface_3_in_0x5605b0775998 -> interface_3_out_0x5605b0775998 [label="H"];
    op_0x5605bebd0a60 -> interface_3_out_0x5605beb88b40 [label="k_1"];
    op_0x5605bebd0880 -> interface_3_out_0x5605beb88c80 [label="g^-1*s^-1*C_out"];
    interface_3_in_0x5605beb97a28 -> interface_3_out_0x5605beb97a28 [label="H"];
    op_0x5605beb88d78 -> op_0x5605bebd0880 [label="g^-1*s^-1*C_out"];
    interface_3_in_0x5605bebd08b8 -> op_0x5605bebd0880 [label="g^-1*s^-1*C_out"];
    interface_3_in_0x5605bebd0a30 -> op_0x5605bebd0a10 [label="C_in"];
    interface_3_in_0x5605bebd0a48 -> op_0x5605bebd0a10 [label="C_in"];
    interface_3_in_0x5605bebd0a80 -> op_0x5605bebd0a60 [label="k_1"];
    interface_3_in_0x5605bebd0a98 -> op_0x5605bebd0a60 [label="k_1"];
    op_0x5605bebd0a10 -> interface_3_out_0x5605bebdfc80 [label="C_in"];
}

// Stage tensor.
subgraph cluster_subgraph_4 {
    label = "Subgraph 4";
    // Reductions.
    // Output.
    subgraph cluster_subgraph_4_out {
        label = "";
        interface_4_out_0x5605b0775920 [label="N", shape=none];
        interface_4_out_0x5605bebd0a30 [label="C_in", shape=none];
        interface_4_out_0x5605beb97a28 [label="H", shape=none];
        interface_4_out_0x5605bebd0a80 [label="k_1", shape=none];
        interface_4_out_0x5605b0775998 [label="H", shape=none];
    }
    {
        rank = same;
        interface_4_out_0x5605b0775920;
        interface_4_out_0x5605bebd0a30;
        interface_4_out_0x5605beb97a28;
        interface_4_out_0x5605bebd0a80;
        interface_4_out_0x5605b0775998;
    }
    // Input 0.
    subgraph cluster_subgraph_4_in_0 {
        label = "";
        interface_4_in_0x5605b0775920 [label="N", shape=none];
        interface_4_in_0x5605bebd0a30 [label="C_in", shape=none];
        interface_4_in_0x5605beb97a28 [label="H", shape=none];
        interface_4_in_0x5605bec30ba8 [label="H", shape=none];
    }
    {
        rank = same;
        interface_4_in_0x5605b0775920;
        interface_4_in_0x5605bebd0a30;
        interface_4_in_0x5605beb97a28;
        interface_4_in_0x5605bec30ba8;
    }
    // Op's.
    op_0x5605bec30b80 [label="Unfold"];
    // Dimension's.
    interface_4_in_0x5605b0775920 -> interface_4_out_0x5605b0775920 [label="N"];
    op_0x5605bec30b80 -> interface_4_out_0x5605b0775998 [label="H"];
    interface_4_in_0x5605beb97a28 -> interface_4_out_0x5605beb97a28 [label="H"];
    interface_4_in_0x5605bebd0a30 -> interface_4_out_0x5605bebd0a30 [label="C_in"];
    op_0x5605bec30b80 -> interface_4_out_0x5605bebd0a80 [label="k_1"];
    interface_4_in_0x5605bec30ba8 -> op_0x5605bec30b80 [label="H"];
}

// Input tensor.
subgraph cluster_subgraph_5 {
    label = "Input 0";
    interface_5_out_0x5605b0775920 [label="N", shape=none];
    interface_5_out_0x5605bebd0a30 [label="C_in", shape=none];
    interface_5_out_0x5605beb97a28 [label="H", shape=none];
    interface_5_out_0x5605bec30ba8 [label="H", shape=none];
}

interface_5_out_0x5605b0775920 -> interface_4_in_0x5605b0775920;
interface_5_out_0x5605bebd0a30 -> interface_4_in_0x5605bebd0a30;
interface_5_out_0x5605beb97a28 -> interface_4_in_0x5605beb97a28;
interface_5_out_0x5605bec30ba8 -> interface_4_in_0x5605bec30ba8;

interface_4_out_0x5605b0775920 -> interface_3_in_0x5605b0775920;
interface_4_out_0x5605bebd0a30 -> interface_3_in_0x5605bebd0a30;
interface_4_out_0x5605beb97a28 -> interface_3_in_0x5605beb97a28;
interface_4_out_0x5605bebd0a80 -> interface_3_in_0x5605bebd0a80;
interface_4_out_0x5605b0775998 -> interface_3_in_0x5605b0775998;

// Input tensor.
subgraph cluster_subgraph_6 {
    label = "Input 2";
    interface_6_out_0x5605bebd0a48 [label="C_in", shape=none];
    interface_6_out_0x5605bebd0a98 [label="k_1", shape=none];
    interface_6_out_0x5605bebd08b8 [label="g^-1*s^-1*C_out", shape=none];
}

interface_6_out_0x5605bebd0a48 -> interface_3_in_0x5605bebd0a48;
interface_6_out_0x5605bebd0a98 -> interface_3_in_0x5605bebd0a98;
interface_6_out_0x5605bebd08b8 -> interface_3_in_0x5605bebd08b8;

interface_3_out_0x5605b0775920 -> interface_2_in_0x5605b0775920;
interface_3_out_0x5605bebdfc80 -> interface_2_in_0x5605bebdfc80;
interface_3_out_0x5605beb97a28 -> interface_2_in_0x5605beb97a28;
interface_3_out_0x5605beb88b40 -> interface_2_in_0x5605beb88b40;
interface_3_out_0x5605b0775998 -> interface_2_in_0x5605b0775998;
interface_3_out_0x5605beb88c80 -> interface_2_in_0x5605beb88c80;

interface_2_out_0x5605b0775920 -> interface_1_in_0x5605b0775920;
interface_2_out_0x5605beb88c30 -> interface_1_in_0x5605beb88c30;
interface_2_out_0x5605beb97a28 -> interface_1_in_0x5605beb97a28;
interface_2_out_0x5605beb88b40 -> interface_1_in_0x5605beb88b40;
interface_2_out_0x5605b0775998 -> interface_1_in_0x5605b0775998;
interface_2_out_0x5605beb88c80 -> interface_1_in_0x5605beb88c80;

interface_1_out_0x5605b0775920 -> interface_0_in_0x5605b0775920;
interface_1_out_0x5605beb88c30 -> interface_0_in_0x5605beb88c30;
interface_1_out_0x5605beb88910 -> interface_0_in_0x5605beb88910;
interface_1_out_0x5605b0775970 -> interface_0_in_0x5605b0775970;
interface_1_out_0x5605beb88b40 -> interface_0_in_0x5605beb88b40;
interface_1_out_0x5605b0775998 -> interface_0_in_0x5605b0775998;
interface_1_out_0x5605beb88c80 -> interface_0_in_0x5605beb88c80;

// Input tensor.
subgraph cluster_subgraph_7 {
    label = "Input 1";
    interface_7_out_0x5605beb88838 [label="C_out", shape=none];
    interface_7_out_0x5605beb88c48 [label="g", shape=none];
    interface_7_out_0x5605beb88928 [label="k_1", shape=none];
    interface_7_out_0x5605beb88b58 [label="k_1", shape=none];
    interface_7_out_0x5605beb88c98 [label="g^-1*s^-1*C_out", shape=none];
}

interface_7_out_0x5605beb88838 -> interface_0_in_0x5605beb88838;
interface_7_out_0x5605beb88c48 -> interface_0_in_0x5605beb88c48;
interface_7_out_0x5605beb88928 -> interface_0_in_0x5605beb88928;
interface_7_out_0x5605beb88b58 -> interface_0_in_0x5605beb88b58;
interface_7_out_0x5605beb88c98 -> interface_0_in_0x5605beb88c98;

{
    rank = same;
    interface_5_out_0x5605b0775920;
    interface_5_out_0x5605bebd0a30;
    interface_5_out_0x5605beb97a28;
    interface_5_out_0x5605bec30ba8;
    interface_7_out_0x5605beb88838;
    interface_7_out_0x5605beb88c48;
    interface_7_out_0x5605beb88928;
    interface_7_out_0x5605beb88b58;
    interface_7_out_0x5605beb88c98;
    interface_6_out_0x5605bebd0a48;
    interface_6_out_0x5605bebd0a98;
    interface_6_out_0x5605bebd08b8;
}
subgraph cluster_subgraph_output {
    label = "Output";
    interface_8_in_0x5605b0775920 [label="N", shape=none];
    interface_8_in_0x5605b0775948 [label="C_out", shape=none];
    interface_8_in_0x5605b0775970 [label="H", shape=none];
    interface_8_in_0x5605b0775998 [label="H", shape=none];
}
interface_0_out_0x5605b0775920 -> interface_8_in_0x5605b0775920;
interface_0_out_0x5605b0775948 -> interface_8_in_0x5605b0775948;
interface_0_out_0x5605b0775970 -> interface_8_in_0x5605b0775970;
interface_0_out_0x5605b0775998 -> interface_8_in_0x5605b0775998;

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
		t_7 = torch.einsum("nljokpm, iljkm -> niop", t_6, in_1)

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
		t_7 = torch.einsum("nljokpm, iljkm -> niop", t_6, in_1)

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
		t_7 = torch.einsum("nljokpm, iljkm -> niop", t_6, in_1)

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
		t_7 = torch.einsum("nljokpm, iljkm -> niop", t_6, in_1)

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
		t_7 = torch.einsum("nljokpm, iljkm -> niop", t_6, in_1)

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
		t_7 = torch.einsum("nljokpm, iljkm -> niop", t_6, in_1)

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
		t_7 = torch.einsum("nljokpm, iljkm -> niop", t_6, in_1)

		# No need to crop the output tensor.
		y = t_7

		return y

