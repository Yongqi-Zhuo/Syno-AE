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
    reduce_0x561f594ee0f8 [label="Sum", shape=box];
    reduce_0x561f594ee110 [label="Sum", shape=box];
    reduce_0x561f594ee250 [label="Sum", shape=box];
    // Output.
    subgraph cluster_subgraph_0_out {
        label = "";
        interface_0_out_0x7ef618000b60 [label="N", shape=none];
        interface_0_out_0x7ef5fc000b60 [label="C_out", shape=none];
        interface_0_out_0x7ef610000b60 [label="H", shape=none];
        interface_0_out_0x7ef60c000b60 [label="H", shape=none];
    }
    {
        rank = same;
        reduce_0x561f594ee198;
        reduce_0x561f594ee0f8;
        reduce_0x561f594ee110;
        reduce_0x561f594ee250;
        interface_0_out_0x7ef618000b60;
        interface_0_out_0x7ef5fc000b60;
        interface_0_out_0x7ef610000b60;
        interface_0_out_0x7ef60c000b60;
    }
    // Input 0.
    subgraph cluster_subgraph_0_in_0 {
        label = "";
        interface_0_in_0x7ef618000b60 [label="N", shape=none];
        interface_0_in_0x561f594eec10 [label="g", shape=none];
        interface_0_in_0x561f594eeb70 [label="k_1", shape=none];
        interface_0_in_0x7ef610000b60 [label="H", shape=none];
        interface_0_in_0x561f594eebc0 [label="k_1", shape=none];
        interface_0_in_0x7ef60c000b60 [label="H", shape=none];
        interface_0_in_0x561f594eec60 [label="g^-1*s^-1*C_out", shape=none];
    }
    // Input 1.
    subgraph cluster_subgraph_0_in_1 {
        label = "";
        interface_0_in_0x561f594eeb38 [label="C_out", shape=none];
        interface_0_in_0x561f594eec28 [label="g", shape=none];
        interface_0_in_0x561f594eeb88 [label="k_1", shape=none];
        interface_0_in_0x561f594eebd8 [label="k_1", shape=none];
        interface_0_in_0x561f594eec78 [label="g^-1*s^-1*C_out", shape=none];
    }
    {
        rank = same;
        interface_0_in_0x7ef618000b60;
        interface_0_in_0x561f594eec10;
        interface_0_in_0x561f594eeb70;
        interface_0_in_0x7ef610000b60;
        interface_0_in_0x561f594eebc0;
        interface_0_in_0x7ef60c000b60;
        interface_0_in_0x561f594eec60;
        interface_0_in_0x561f594eeb38;
        interface_0_in_0x561f594eec28;
        interface_0_in_0x561f594eeb88;
        interface_0_in_0x561f594eebd8;
        interface_0_in_0x561f594eec78;
    }
    // Op's.
    op_0x561f594eeb00 [label="Share"];
    op_0x561f594eeb50 [label="Share"];
    op_0x561f594eeba0 [label="Share"];
    op_0x561f594eebf0 [label="Share"];
    op_0x561f594eec40 [label="Share"];
    op_0x561f594ef0b8 [label="Expand"];
    // Dimension's.
    op_0x561f594eeb50 -> reduce_0x561f594ee0f8 [label="k_1"];
    op_0x561f594eeba0 -> reduce_0x561f594ee110 [label="k_1"];
    op_0x561f594eebf0 -> reduce_0x561f594ee198 [label="g"];
    op_0x561f594eec40 -> reduce_0x561f594ee250 [label="g^-1*s^-1*C_out"];
    op_0x561f594ef0b8 -> op_0x561f594eeb00 [label="C_out"];
    interface_0_in_0x561f594eeb38 -> op_0x561f594eeb00 [label="C_out"];
    interface_0_in_0x561f594eeb70 -> op_0x561f594eeb50 [label="k_1"];
    interface_0_in_0x561f594eeb88 -> op_0x561f594eeb50 [label="k_1"];
    interface_0_in_0x561f594eebc0 -> op_0x561f594eeba0 [label="k_1"];
    interface_0_in_0x561f594eebd8 -> op_0x561f594eeba0 [label="k_1"];
    interface_0_in_0x561f594eec10 -> op_0x561f594eebf0 [label="g"];
    interface_0_in_0x561f594eec28 -> op_0x561f594eebf0 [label="g"];
    interface_0_in_0x561f594eec60 -> op_0x561f594eec40 [label="g^-1*s^-1*C_out"];
    interface_0_in_0x561f594eec78 -> op_0x561f594eec40 [label="g^-1*s^-1*C_out"];
    op_0x561f594eeb00 -> interface_0_out_0x7ef5fc000b60 [label="C_out"];
    interface_0_in_0x7ef60c000b60 -> interface_0_out_0x7ef60c000b60 [label="H"];
    interface_0_in_0x7ef610000b60 -> interface_0_out_0x7ef610000b60 [label="H"];
    interface_0_in_0x7ef618000b60 -> interface_0_out_0x7ef618000b60 [label="N"];
}

// Stage tensor.
subgraph cluster_subgraph_1 {
    label = "Subgraph 1";
    // Reductions.
    // Output.
    subgraph cluster_subgraph_1_out {
        label = "";
        interface_1_out_0x7ef618000b60 [label="N", shape=none];
        interface_1_out_0x561f594eec10 [label="g", shape=none];
        interface_1_out_0x561f594eeb70 [label="k_1", shape=none];
        interface_1_out_0x7ef610000b60 [label="H", shape=none];
        interface_1_out_0x561f594eebc0 [label="k_1", shape=none];
        interface_1_out_0x7ef60c000b60 [label="H", shape=none];
        interface_1_out_0x561f594eec60 [label="g^-1*s^-1*C_out", shape=none];
    }
    {
        rank = same;
        interface_1_out_0x7ef618000b60;
        interface_1_out_0x561f594eec10;
        interface_1_out_0x561f594eeb70;
        interface_1_out_0x7ef610000b60;
        interface_1_out_0x561f594eebc0;
        interface_1_out_0x7ef60c000b60;
        interface_1_out_0x561f594eec60;
    }
    // Input 0.
    subgraph cluster_subgraph_1_in_0 {
        label = "";
        interface_1_in_0x7ef618000b60 [label="N", shape=none];
        interface_1_in_0x561f594eec10 [label="g", shape=none];
        interface_1_in_0x561f594ef528 [label="H", shape=none];
        interface_1_in_0x561f594ef568 [label="H", shape=none];
        interface_1_in_0x561f594eec60 [label="g^-1*s^-1*C_out", shape=none];
    }
    {
        rank = same;
        interface_1_in_0x7ef618000b60;
        interface_1_in_0x561f594eec10;
        interface_1_in_0x561f594ef528;
        interface_1_in_0x561f594ef568;
        interface_1_in_0x561f594eec60;
    }
    // Op's.
    op_0x561f594ef500 [label="Unfold"];
    op_0x561f594ef540 [label="Unfold"];
    // Dimension's.
    op_0x561f594ef500 -> interface_1_out_0x561f594eeb70 [label="k_1"];
    op_0x561f594ef540 -> interface_1_out_0x561f594eebc0 [label="k_1"];
    interface_1_in_0x561f594eec10 -> interface_1_out_0x561f594eec10 [label="g"];
    interface_1_in_0x561f594eec60 -> interface_1_out_0x561f594eec60 [label="g^-1*s^-1*C_out"];
    interface_1_in_0x561f594ef528 -> op_0x561f594ef500 [label="H"];
    interface_1_in_0x561f594ef568 -> op_0x561f594ef540 [label="H"];
    op_0x561f594ef540 -> interface_1_out_0x7ef60c000b60 [label="H"];
    op_0x561f594ef500 -> interface_1_out_0x7ef610000b60 [label="H"];
    interface_1_in_0x7ef618000b60 -> interface_1_out_0x7ef618000b60 [label="N"];
}

// Stage tensor.
subgraph cluster_subgraph_2 {
    label = "Subgraph 2";
    // Reductions.
    reduce_0x561f594ee028 [label="Sum", shape=box];
    // Output.
    subgraph cluster_subgraph_2_out {
        label = "";
        interface_2_out_0x7ef618000b60 [label="N", shape=none];
        interface_2_out_0x561f594eec10 [label="g", shape=none];
        interface_2_out_0x561f594ef528 [label="H", shape=none];
        interface_2_out_0x561f594ef568 [label="H", shape=none];
        interface_2_out_0x561f594eec60 [label="g^-1*s^-1*C_out", shape=none];
    }
    {
        rank = same;
        reduce_0x561f594ee028;
        interface_2_out_0x7ef618000b60;
        interface_2_out_0x561f594eec10;
        interface_2_out_0x561f594ef528;
        interface_2_out_0x561f594ef568;
        interface_2_out_0x561f594eec60;
    }
    // Input 0.
    subgraph cluster_subgraph_2_in_0 {
        label = "";
        interface_2_in_0x7ef618000b60 [label="N", shape=none];
        interface_2_in_0x561f594ef9c0 [label="C_in", shape=none];
        interface_2_in_0x561f594ef528 [label="H", shape=none];
        interface_2_in_0x561f594ef568 [label="H", shape=none];
        interface_2_in_0x561f594eec60 [label="g^-1*s^-1*C_out", shape=none];
    }
    {
        rank = same;
        interface_2_in_0x7ef618000b60;
        interface_2_in_0x561f594ef9c0;
        interface_2_in_0x561f594ef528;
        interface_2_in_0x561f594ef568;
        interface_2_in_0x561f594eec60;
    }
    // Op's.
    op_0x561f594ef980 [label="Split"];
    // Dimension's.
    op_0x561f594ef980 -> reduce_0x561f594ee028 [label="g^-1*C_in"];
    op_0x561f594ef980 -> interface_2_out_0x561f594eec10 [label="g"];
    interface_2_in_0x561f594eec60 -> interface_2_out_0x561f594eec60 [label="g^-1*s^-1*C_out"];
    interface_2_in_0x561f594ef528 -> interface_2_out_0x561f594ef528 [label="H"];
    interface_2_in_0x561f594ef568 -> interface_2_out_0x561f594ef568 [label="H"];
    interface_2_in_0x561f594ef9c0 -> op_0x561f594ef980 [label="C_in"];
    interface_2_in_0x7ef618000b60 -> interface_2_out_0x7ef618000b60 [label="N"];
}

// Stage tensor.
subgraph cluster_subgraph_3 {
    label = "Subgraph 3";
    // Reductions.
    reduce_0x561f594ee0e0 [label="Sum", shape=box];
    // Output.
    subgraph cluster_subgraph_3_out {
        label = "";
        interface_3_out_0x7ef618000b60 [label="N", shape=none];
        interface_3_out_0x561f594ef9c0 [label="C_in", shape=none];
        interface_3_out_0x561f594ef528 [label="H", shape=none];
        interface_3_out_0x561f594ef568 [label="H", shape=none];
        interface_3_out_0x561f594eec60 [label="g^-1*s^-1*C_out", shape=none];
    }
    {
        rank = same;
        reduce_0x561f594ee0e0;
        interface_3_out_0x7ef618000b60;
        interface_3_out_0x561f594ef9c0;
        interface_3_out_0x561f594ef528;
        interface_3_out_0x561f594ef568;
        interface_3_out_0x561f594eec60;
    }
    // Input 0.
    subgraph cluster_subgraph_3_in_0 {
        label = "";
        interface_3_in_0x7ef618000b60 [label="N", shape=none];
        interface_3_in_0x561f594eed00 [label="C_in", shape=none];
        interface_3_in_0x561f594ef528 [label="H", shape=none];
        interface_3_in_0x561f594eecb0 [label="k_1", shape=none];
        interface_3_in_0x561f594ef568 [label="H", shape=none];
    }
    // Input 1.
    subgraph cluster_subgraph_3_in_1 {
        label = "";
        interface_3_in_0x561f594eed18 [label="C_in", shape=none];
        interface_3_in_0x561f594eecc8 [label="k_1", shape=none];
        interface_3_in_0x561f594eed68 [label="g^-1*s^-1*C_out", shape=none];
    }
    {
        rank = same;
        interface_3_in_0x7ef618000b60;
        interface_3_in_0x561f594eed00;
        interface_3_in_0x561f594ef528;
        interface_3_in_0x561f594eecb0;
        interface_3_in_0x561f594ef568;
        interface_3_in_0x561f594eed18;
        interface_3_in_0x561f594eecc8;
        interface_3_in_0x561f594eed68;
    }
    // Op's.
    op_0x561f594eec90 [label="Share"];
    op_0x561f594eece0 [label="Share"];
    op_0x561f594eed30 [label="Share"];
    op_0x561f594ef0d8 [label="Expand"];
    // Dimension's.
    op_0x561f594eec90 -> reduce_0x561f594ee0e0 [label="k_1"];
    op_0x561f594eed30 -> interface_3_out_0x561f594eec60 [label="g^-1*s^-1*C_out"];
    interface_3_in_0x561f594eecb0 -> op_0x561f594eec90 [label="k_1"];
    interface_3_in_0x561f594eecc8 -> op_0x561f594eec90 [label="k_1"];
    interface_3_in_0x561f594eed00 -> op_0x561f594eece0 [label="C_in"];
    interface_3_in_0x561f594eed18 -> op_0x561f594eece0 [label="C_in"];
    op_0x561f594ef0d8 -> op_0x561f594eed30 [label="g^-1*s^-1*C_out"];
    interface_3_in_0x561f594eed68 -> op_0x561f594eed30 [label="g^-1*s^-1*C_out"];
    interface_3_in_0x561f594ef528 -> interface_3_out_0x561f594ef528 [label="H"];
    interface_3_in_0x561f594ef568 -> interface_3_out_0x561f594ef568 [label="H"];
    op_0x561f594eece0 -> interface_3_out_0x561f594ef9c0 [label="C_in"];
    interface_3_in_0x7ef618000b60 -> interface_3_out_0x7ef618000b60 [label="N"];
}

// Stage tensor.
subgraph cluster_subgraph_4 {
    label = "Subgraph 4";
    // Reductions.
    // Output.
    subgraph cluster_subgraph_4_out {
        label = "";
        interface_4_out_0x7ef618000b60 [label="N", shape=none];
        interface_4_out_0x561f594eed00 [label="C_in", shape=none];
        interface_4_out_0x561f594ef528 [label="H", shape=none];
        interface_4_out_0x561f594eecb0 [label="k_1", shape=none];
        interface_4_out_0x561f594ef568 [label="H", shape=none];
    }
    {
        rank = same;
        interface_4_out_0x7ef618000b60;
        interface_4_out_0x561f594eed00;
        interface_4_out_0x561f594ef528;
        interface_4_out_0x561f594eecb0;
        interface_4_out_0x561f594ef568;
    }
    // Input 0.
    subgraph cluster_subgraph_4_in_0 {
        label = "";
        interface_4_in_0x7ef618000b60 [label="N", shape=none];
        interface_4_in_0x561f594eed00 [label="C_in", shape=none];
        interface_4_in_0x561f594ef528 [label="H", shape=none];
        interface_4_in_0x561f594ef5a8 [label="H", shape=none];
    }
    {
        rank = same;
        interface_4_in_0x7ef618000b60;
        interface_4_in_0x561f594eed00;
        interface_4_in_0x561f594ef528;
        interface_4_in_0x561f594ef5a8;
    }
    // Op's.
    op_0x561f594ef580 [label="Unfold"];
    // Dimension's.
    op_0x561f594ef580 -> interface_4_out_0x561f594eecb0 [label="k_1"];
    interface_4_in_0x561f594eed00 -> interface_4_out_0x561f594eed00 [label="C_in"];
    interface_4_in_0x561f594ef528 -> interface_4_out_0x561f594ef528 [label="H"];
    op_0x561f594ef580 -> interface_4_out_0x561f594ef568 [label="H"];
    interface_4_in_0x561f594ef5a8 -> op_0x561f594ef580 [label="H"];
    interface_4_in_0x7ef618000b60 -> interface_4_out_0x7ef618000b60 [label="N"];
}

// Input tensor.
subgraph cluster_subgraph_5 {
    label = "Input 0";
    interface_5_out_0x7ef618000b60 [label="N", shape=none];
    interface_5_out_0x561f594eed00 [label="C_in", shape=none];
    interface_5_out_0x561f594ef528 [label="H", shape=none];
    interface_5_out_0x561f594ef5a8 [label="H", shape=none];
}

interface_5_out_0x7ef618000b60 -> interface_4_in_0x7ef618000b60;
interface_5_out_0x561f594eed00 -> interface_4_in_0x561f594eed00;
interface_5_out_0x561f594ef528 -> interface_4_in_0x561f594ef528;
interface_5_out_0x561f594ef5a8 -> interface_4_in_0x561f594ef5a8;

interface_4_out_0x7ef618000b60 -> interface_3_in_0x7ef618000b60;
interface_4_out_0x561f594eed00 -> interface_3_in_0x561f594eed00;
interface_4_out_0x561f594ef528 -> interface_3_in_0x561f594ef528;
interface_4_out_0x561f594eecb0 -> interface_3_in_0x561f594eecb0;
interface_4_out_0x561f594ef568 -> interface_3_in_0x561f594ef568;

// Input tensor.
subgraph cluster_subgraph_6 {
    label = "Input 2";
    interface_6_out_0x561f594eed18 [label="C_in", shape=none];
    interface_6_out_0x561f594eecc8 [label="k_1", shape=none];
    interface_6_out_0x561f594eed68 [label="g^-1*s^-1*C_out", shape=none];
}

interface_6_out_0x561f594eed18 -> interface_3_in_0x561f594eed18;
interface_6_out_0x561f594eecc8 -> interface_3_in_0x561f594eecc8;
interface_6_out_0x561f594eed68 -> interface_3_in_0x561f594eed68;

interface_3_out_0x7ef618000b60 -> interface_2_in_0x7ef618000b60;
interface_3_out_0x561f594ef9c0 -> interface_2_in_0x561f594ef9c0;
interface_3_out_0x561f594ef528 -> interface_2_in_0x561f594ef528;
interface_3_out_0x561f594ef568 -> interface_2_in_0x561f594ef568;
interface_3_out_0x561f594eec60 -> interface_2_in_0x561f594eec60;

interface_2_out_0x7ef618000b60 -> interface_1_in_0x7ef618000b60;
interface_2_out_0x561f594eec10 -> interface_1_in_0x561f594eec10;
interface_2_out_0x561f594ef528 -> interface_1_in_0x561f594ef528;
interface_2_out_0x561f594ef568 -> interface_1_in_0x561f594ef568;
interface_2_out_0x561f594eec60 -> interface_1_in_0x561f594eec60;

interface_1_out_0x7ef618000b60 -> interface_0_in_0x7ef618000b60;
interface_1_out_0x561f594eec10 -> interface_0_in_0x561f594eec10;
interface_1_out_0x561f594eeb70 -> interface_0_in_0x561f594eeb70;
interface_1_out_0x7ef610000b60 -> interface_0_in_0x7ef610000b60;
interface_1_out_0x561f594eebc0 -> interface_0_in_0x561f594eebc0;
interface_1_out_0x7ef60c000b60 -> interface_0_in_0x7ef60c000b60;
interface_1_out_0x561f594eec60 -> interface_0_in_0x561f594eec60;

// Input tensor.
subgraph cluster_subgraph_7 {
    label = "Input 1";
    interface_7_out_0x561f594eeb38 [label="C_out", shape=none];
    interface_7_out_0x561f594eec28 [label="g", shape=none];
    interface_7_out_0x561f594eeb88 [label="k_1", shape=none];
    interface_7_out_0x561f594eebd8 [label="k_1", shape=none];
    interface_7_out_0x561f594eec78 [label="g^-1*s^-1*C_out", shape=none];
}

interface_7_out_0x561f594eeb38 -> interface_0_in_0x561f594eeb38;
interface_7_out_0x561f594eec28 -> interface_0_in_0x561f594eec28;
interface_7_out_0x561f594eeb88 -> interface_0_in_0x561f594eeb88;
interface_7_out_0x561f594eebd8 -> interface_0_in_0x561f594eebd8;
interface_7_out_0x561f594eec78 -> interface_0_in_0x561f594eec78;

{
    rank = same;
    interface_5_out_0x7ef618000b60;
    interface_5_out_0x561f594eed00;
    interface_5_out_0x561f594ef528;
    interface_5_out_0x561f594ef5a8;
    interface_7_out_0x561f594eeb38;
    interface_7_out_0x561f594eec28;
    interface_7_out_0x561f594eeb88;
    interface_7_out_0x561f594eebd8;
    interface_7_out_0x561f594eec78;
    interface_6_out_0x561f594eed18;
    interface_6_out_0x561f594eecc8;
    interface_6_out_0x561f594eed68;
}
subgraph cluster_subgraph_output {
    label = "Output";
    interface_8_in_0x7ef618000b60 [label="N", shape=none];
    interface_8_in_0x7ef5fc000b60 [label="C_out", shape=none];
    interface_8_in_0x7ef610000b60 [label="H", shape=none];
    interface_8_in_0x7ef60c000b60 [label="H", shape=none];
}
interface_0_out_0x7ef618000b60 -> interface_8_in_0x7ef618000b60;
interface_0_out_0x7ef5fc000b60 -> interface_8_in_0x7ef5fc000b60;
interface_0_out_0x7ef610000b60 -> interface_8_in_0x7ef610000b60;
interface_0_out_0x7ef60c000b60 -> interface_8_in_0x7ef60c000b60;

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
		t_3 = torch.reshape(t_3, (1, 3584, 56, 1, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (1, 64, 56, 3, 56, ))

		# Perform contraction.
		t_4 = torch.einsum("njlim, jik -> njlmk", t_3, in_2)

		# No contraction needed.
		t_5 = t_4

		# [C_in]@Splitc2d52f3525ba6cc4 -> [g]@Sharec7a8ce455b828537, [g^-1*C_in]@Reduceef9903cafc29eea1
		t_5 = torch.reshape(t_5, (1, 32, 2, 56, 56, 1, ))

		# [g^-1*C_in]@Reduce
		t_5 = torch.sum(t_5, dim=(2, ))

		# No contraction needed.
		t_6 = t_5

		# [H]@Unfold87ed2fb8f6552d8f -> [H]@Iterator96123ba3184da39c, [k_1]@Share02da0a485106ab3d
		t_6 = torch.reshape(t_6, (1, 32, 56, 56, ))
		t_6 = torch.nn.functional.unfold(t_6, (3, 1, ), padding=(1, 0, ))
		t_6 = torch.reshape(t_6, (1, 32, 3, 56, 56, 1, ))

		# [H]@Unfolde73c9e24012bc66d -> [H]@Iteratorb0a1def4ad5784ec, [k_1]@Share20826c8af74ae67f
		t_6 = torch.reshape(t_6, (1, 5376, 56, 1, ))
		t_6 = torch.nn.functional.unfold(t_6, (3, 1, ), padding=(1, 0, ))
		t_6 = torch.reshape(t_6, (1, 32, 3, 56, 3, 56, 1, ))

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
		t_3 = torch.reshape(t_3, (1, 1792, 28, 1, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (1, 64, 28, 3, 28, ))

		# Perform contraction.
		t_4 = torch.einsum("njlim, jik -> njlmk", t_3, in_2)

		# No contraction needed.
		t_5 = t_4

		# [C_in]@Splitc2d52f3525ba6cc4 -> [g]@Sharec7a8ce455b828537, [g^-1*C_in]@Reduceef9903cafc29eea1
		t_5 = torch.reshape(t_5, (1, 32, 2, 28, 28, 2, ))

		# [g^-1*C_in]@Reduce
		t_5 = torch.sum(t_5, dim=(2, ))

		# No contraction needed.
		t_6 = t_5

		# [H]@Unfold87ed2fb8f6552d8f -> [H]@Iterator96123ba3184da39c, [k_1]@Share02da0a485106ab3d
		t_6 = torch.reshape(t_6, (1, 32, 28, 56, ))
		t_6 = torch.nn.functional.unfold(t_6, (3, 1, ), padding=(1, 0, ))
		t_6 = torch.reshape(t_6, (1, 32, 3, 28, 28, 2, ))

		# [H]@Unfolde73c9e24012bc66d -> [H]@Iteratorb0a1def4ad5784ec, [k_1]@Share20826c8af74ae67f
		t_6 = torch.reshape(t_6, (1, 2688, 28, 2, ))
		t_6 = torch.nn.functional.unfold(t_6, (3, 1, ), padding=(1, 0, ))
		t_6 = torch.reshape(t_6, (1, 32, 3, 28, 3, 28, 2, ))

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
		t_3 = torch.reshape(t_3, (1, 3584, 28, 1, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (1, 128, 28, 3, 28, ))

		# Perform contraction.
		t_4 = torch.einsum("njlim, jik -> njlmk", t_3, in_2)

		# No contraction needed.
		t_5 = t_4

		# [C_in]@Splitc2d52f3525ba6cc4 -> [g]@Sharec7a8ce455b828537, [g^-1*C_in]@Reduceef9903cafc29eea1
		t_5 = torch.reshape(t_5, (1, 32, 4, 28, 28, 2, ))

		# [g^-1*C_in]@Reduce
		t_5 = torch.sum(t_5, dim=(2, ))

		# No contraction needed.
		t_6 = t_5

		# [H]@Unfold87ed2fb8f6552d8f -> [H]@Iterator96123ba3184da39c, [k_1]@Share02da0a485106ab3d
		t_6 = torch.reshape(t_6, (1, 32, 28, 56, ))
		t_6 = torch.nn.functional.unfold(t_6, (3, 1, ), padding=(1, 0, ))
		t_6 = torch.reshape(t_6, (1, 32, 3, 28, 28, 2, ))

		# [H]@Unfolde73c9e24012bc66d -> [H]@Iteratorb0a1def4ad5784ec, [k_1]@Share20826c8af74ae67f
		t_6 = torch.reshape(t_6, (1, 2688, 28, 2, ))
		t_6 = torch.nn.functional.unfold(t_6, (3, 1, ), padding=(1, 0, ))
		t_6 = torch.reshape(t_6, (1, 32, 3, 28, 3, 28, 2, ))

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
		t_3 = torch.reshape(t_3, (1, 1792, 14, 1, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (1, 128, 14, 3, 14, ))

		# Perform contraction.
		t_4 = torch.einsum("njlim, jik -> njlmk", t_3, in_2)

		# No contraction needed.
		t_5 = t_4

		# [C_in]@Splitc2d52f3525ba6cc4 -> [g]@Sharec7a8ce455b828537, [g^-1*C_in]@Reduceef9903cafc29eea1
		t_5 = torch.reshape(t_5, (1, 32, 4, 14, 14, 4, ))

		# [g^-1*C_in]@Reduce
		t_5 = torch.sum(t_5, dim=(2, ))

		# No contraction needed.
		t_6 = t_5

		# [H]@Unfold87ed2fb8f6552d8f -> [H]@Iterator96123ba3184da39c, [k_1]@Share02da0a485106ab3d
		t_6 = torch.reshape(t_6, (1, 32, 14, 56, ))
		t_6 = torch.nn.functional.unfold(t_6, (3, 1, ), padding=(1, 0, ))
		t_6 = torch.reshape(t_6, (1, 32, 3, 14, 14, 4, ))

		# [H]@Unfolde73c9e24012bc66d -> [H]@Iteratorb0a1def4ad5784ec, [k_1]@Share20826c8af74ae67f
		t_6 = torch.reshape(t_6, (1, 1344, 14, 4, ))
		t_6 = torch.nn.functional.unfold(t_6, (3, 1, ), padding=(1, 0, ))
		t_6 = torch.reshape(t_6, (1, 32, 3, 14, 3, 14, 4, ))

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
		t_3 = torch.reshape(t_3, (1, 3584, 14, 1, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (1, 256, 14, 3, 14, ))

		# Perform contraction.
		t_4 = torch.einsum("njlim, jik -> njlmk", t_3, in_2)

		# No contraction needed.
		t_5 = t_4

		# [C_in]@Splitc2d52f3525ba6cc4 -> [g]@Sharec7a8ce455b828537, [g^-1*C_in]@Reduceef9903cafc29eea1
		t_5 = torch.reshape(t_5, (1, 32, 8, 14, 14, 4, ))

		# [g^-1*C_in]@Reduce
		t_5 = torch.sum(t_5, dim=(2, ))

		# No contraction needed.
		t_6 = t_5

		# [H]@Unfold87ed2fb8f6552d8f -> [H]@Iterator96123ba3184da39c, [k_1]@Share02da0a485106ab3d
		t_6 = torch.reshape(t_6, (1, 32, 14, 56, ))
		t_6 = torch.nn.functional.unfold(t_6, (3, 1, ), padding=(1, 0, ))
		t_6 = torch.reshape(t_6, (1, 32, 3, 14, 14, 4, ))

		# [H]@Unfolde73c9e24012bc66d -> [H]@Iteratorb0a1def4ad5784ec, [k_1]@Share20826c8af74ae67f
		t_6 = torch.reshape(t_6, (1, 1344, 14, 4, ))
		t_6 = torch.nn.functional.unfold(t_6, (3, 1, ), padding=(1, 0, ))
		t_6 = torch.reshape(t_6, (1, 32, 3, 14, 3, 14, 4, ))

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
		t_3 = torch.reshape(t_3, (1, 1792, 7, 1, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (1, 256, 7, 3, 7, ))

		# Perform contraction.
		t_4 = torch.einsum("njlim, jik -> njlmk", t_3, in_2)

		# No contraction needed.
		t_5 = t_4

		# [C_in]@Splitc2d52f3525ba6cc4 -> [g]@Sharec7a8ce455b828537, [g^-1*C_in]@Reduceef9903cafc29eea1
		t_5 = torch.reshape(t_5, (1, 32, 8, 7, 7, 8, ))

		# [g^-1*C_in]@Reduce
		t_5 = torch.sum(t_5, dim=(2, ))

		# No contraction needed.
		t_6 = t_5

		# [H]@Unfold87ed2fb8f6552d8f -> [H]@Iterator96123ba3184da39c, [k_1]@Share02da0a485106ab3d
		t_6 = torch.reshape(t_6, (1, 32, 7, 56, ))
		t_6 = torch.nn.functional.unfold(t_6, (3, 1, ), padding=(1, 0, ))
		t_6 = torch.reshape(t_6, (1, 32, 3, 7, 7, 8, ))

		# [H]@Unfolde73c9e24012bc66d -> [H]@Iteratorb0a1def4ad5784ec, [k_1]@Share20826c8af74ae67f
		t_6 = torch.reshape(t_6, (1, 672, 7, 8, ))
		t_6 = torch.nn.functional.unfold(t_6, (3, 1, ), padding=(1, 0, ))
		t_6 = torch.reshape(t_6, (1, 32, 3, 7, 3, 7, 8, ))

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
		t_3 = torch.reshape(t_3, (1, 3584, 7, 1, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (1, 512, 7, 3, 7, ))

		# Perform contraction.
		t_4 = torch.einsum("njlim, jik -> njlmk", t_3, in_2)

		# No contraction needed.
		t_5 = t_4

		# [C_in]@Splitc2d52f3525ba6cc4 -> [g]@Sharec7a8ce455b828537, [g^-1*C_in]@Reduceef9903cafc29eea1
		t_5 = torch.reshape(t_5, (1, 32, 16, 7, 7, 8, ))

		# [g^-1*C_in]@Reduce
		t_5 = torch.sum(t_5, dim=(2, ))

		# No contraction needed.
		t_6 = t_5

		# [H]@Unfold87ed2fb8f6552d8f -> [H]@Iterator96123ba3184da39c, [k_1]@Share02da0a485106ab3d
		t_6 = torch.reshape(t_6, (1, 32, 7, 56, ))
		t_6 = torch.nn.functional.unfold(t_6, (3, 1, ), padding=(1, 0, ))
		t_6 = torch.reshape(t_6, (1, 32, 3, 7, 7, 8, ))

		# [H]@Unfolde73c9e24012bc66d -> [H]@Iteratorb0a1def4ad5784ec, [k_1]@Share20826c8af74ae67f
		t_6 = torch.reshape(t_6, (1, 672, 7, 8, ))
		t_6 = torch.nn.functional.unfold(t_6, (3, 1, ), padding=(1, 0, ))
		t_6 = torch.reshape(t_6, (1, 32, 3, 7, 3, 7, 8, ))

		# Perform contraction.
		t_7 = torch.einsum("pljoknm, iljkm -> pion", t_6, in_1)

		# No need to crop the output tensor.
		y = t_7

		return y

