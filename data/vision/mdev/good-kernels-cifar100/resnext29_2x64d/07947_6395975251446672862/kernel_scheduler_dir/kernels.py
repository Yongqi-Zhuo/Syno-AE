import torch
import random
"""
digraph kernel_preview {
newrank = true;

// Stage tensor.
subgraph cluster_subgraph_0 {
    label = "Subgraph 0";
    // Reductions.
    // Output.
    subgraph cluster_subgraph_0_out {
        label = "";
        interface_0_out_0x5621811c9b40 [label="N", shape=none];
        interface_0_out_0x5621811c9b68 [label="C_out", shape=none];
        interface_0_out_0x5621811c9b90 [label="H", shape=none];
        interface_0_out_0x5621811c9bb8 [label="H", shape=none];
    }
    {
        rank = same;
        interface_0_out_0x5621811c9b40;
        interface_0_out_0x5621811c9b68;
        interface_0_out_0x5621811c9b90;
        interface_0_out_0x5621811c9bb8;
    }
    // Input 0.
    subgraph cluster_subgraph_0_in_0 {
        label = "";
        interface_0_in_0x5621811c9b40 [label="N", shape=none];
        interface_0_in_0x5621811c9b90 [label="H", shape=none];
        interface_0_in_0x5621811c9bb8 [label="H", shape=none];
        interface_0_in_0x7fd5ec008198 [label="g^-1*C_out", shape=none];
        interface_0_in_0x7fd5ec008180 [label="g", shape=none];
    }
    {
        rank = same;
        interface_0_in_0x5621811c9b40;
        interface_0_in_0x5621811c9b90;
        interface_0_in_0x5621811c9bb8;
        interface_0_in_0x7fd5ec008198;
        interface_0_in_0x7fd5ec008180;
    }
    // Op's.
    op_0x7fd5ec008140 [label="Merge"];
    // Dimension's.
    interface_0_in_0x5621811c9b40 -> interface_0_out_0x5621811c9b40 [label="N"];
    op_0x7fd5ec008140 -> interface_0_out_0x5621811c9b68 [label="C_out"];
    interface_0_in_0x5621811c9b90 -> interface_0_out_0x5621811c9b90 [label="H"];
    interface_0_in_0x5621811c9bb8 -> interface_0_out_0x5621811c9bb8 [label="H"];
    interface_0_in_0x7fd5ec008180 -> op_0x7fd5ec008140 [label="g"];
    interface_0_in_0x7fd5ec008198 -> op_0x7fd5ec008140 [label="g^-1*C_out"];
}

// Stage tensor.
subgraph cluster_subgraph_1 {
    label = "Subgraph 1";
    // Reductions.
    reduce_0x7fce64005a20 [label="Sum", shape=box];
    reduce_0x7fce64001998 [label="Sum", shape=box];
    // Output.
    subgraph cluster_subgraph_1_out {
        label = "";
        interface_1_out_0x5621811c9b40 [label="N", shape=none];
        interface_1_out_0x5621811c9b90 [label="H", shape=none];
        interface_1_out_0x5621811c9bb8 [label="H", shape=none];
        interface_1_out_0x7fd5ec008198 [label="g^-1*C_out", shape=none];
        interface_1_out_0x7fd5ec008180 [label="g", shape=none];
    }
    {
        rank = same;
        reduce_0x7fce64005a20;
        reduce_0x7fce64001998;
        interface_1_out_0x5621811c9b40;
        interface_1_out_0x5621811c9b90;
        interface_1_out_0x5621811c9bb8;
        interface_1_out_0x7fd5ec008198;
        interface_1_out_0x7fd5ec008180;
    }
    // Input 0.
    subgraph cluster_subgraph_1_in_0 {
        label = "";
        interface_1_in_0x5621811c9b40 [label="N", shape=none];
        interface_1_in_0x7fd0380542f0 [label="g^-1*s^-1*C_in", shape=none];
        interface_1_in_0x5621811c9b90 [label="H", shape=none];
        interface_1_in_0x5621811c9bb8 [label="H", shape=none];
        interface_1_in_0x7fd038054750 [label="k_1", shape=none];
        interface_1_in_0x7fd5ec008198 [label="g^-1*C_out", shape=none];
    }
    // Input 1.
    subgraph cluster_subgraph_1_in_1 {
        label = "";
        interface_1_in_0x7fd038054308 [label="g^-1*s^-1*C_in", shape=none];
        interface_1_in_0x7fd038054768 [label="k_1", shape=none];
        interface_1_in_0x7fd0380543a8 [label="g", shape=none];
    }
    {
        rank = same;
        interface_1_in_0x5621811c9b40;
        interface_1_in_0x7fd0380542f0;
        interface_1_in_0x5621811c9b90;
        interface_1_in_0x5621811c9bb8;
        interface_1_in_0x7fd038054750;
        interface_1_in_0x7fd5ec008198;
        interface_1_in_0x7fd038054308;
        interface_1_in_0x7fd038054768;
        interface_1_in_0x7fd0380543a8;
    }
    // Op's.
    op_0x5621811b6d18 [label="Expand"];
    op_0x7fd0380542d0 [label="Share"];
    op_0x7fd038054370 [label="Share"];
    op_0x7fd038054730 [label="Share"];
    // Dimension's.
    interface_1_in_0x5621811c9b40 -> interface_1_out_0x5621811c9b40 [label="N"];
    interface_1_in_0x5621811c9b90 -> interface_1_out_0x5621811c9b90 [label="H"];
    interface_1_in_0x5621811c9bb8 -> interface_1_out_0x5621811c9bb8 [label="H"];
    op_0x7fd038054730 -> reduce_0x7fce64001998 [label="k_1"];
    op_0x7fd0380542d0 -> reduce_0x7fce64005a20 [label="g^-1*s^-1*C_in"];
    interface_1_in_0x7fd0380542f0 -> op_0x7fd0380542d0 [label="g^-1*s^-1*C_in"];
    interface_1_in_0x7fd038054308 -> op_0x7fd0380542d0 [label="g^-1*s^-1*C_in"];
    op_0x5621811b6d18 -> op_0x7fd038054370 [label="g"];
    interface_1_in_0x7fd0380543a8 -> op_0x7fd038054370 [label="g"];
    interface_1_in_0x7fd038054750 -> op_0x7fd038054730 [label="k_1"];
    interface_1_in_0x7fd038054768 -> op_0x7fd038054730 [label="k_1"];
    op_0x7fd038054370 -> interface_1_out_0x7fd5ec008180 [label="g"];
    interface_1_in_0x7fd5ec008198 -> interface_1_out_0x7fd5ec008198 [label="g^-1*C_out"];
}

// Stage tensor.
subgraph cluster_subgraph_2 {
    label = "Subgraph 2";
    // Reductions.
    // Output.
    subgraph cluster_subgraph_2_out {
        label = "";
        interface_2_out_0x5621811c9b40 [label="N", shape=none];
        interface_2_out_0x7fd0380542f0 [label="g^-1*s^-1*C_in", shape=none];
        interface_2_out_0x5621811c9b90 [label="H", shape=none];
        interface_2_out_0x5621811c9bb8 [label="H", shape=none];
        interface_2_out_0x7fd038054750 [label="k_1", shape=none];
        interface_2_out_0x7fd5ec008198 [label="g^-1*C_out", shape=none];
    }
    {
        rank = same;
        interface_2_out_0x5621811c9b40;
        interface_2_out_0x7fd0380542f0;
        interface_2_out_0x5621811c9b90;
        interface_2_out_0x5621811c9bb8;
        interface_2_out_0x7fd038054750;
        interface_2_out_0x7fd5ec008198;
    }
    // Input 0.
    subgraph cluster_subgraph_2_in_0 {
        label = "";
        interface_2_in_0x5621811c9b40 [label="N", shape=none];
        interface_2_in_0x7fd0380542f0 [label="g^-1*s^-1*C_in", shape=none];
        interface_2_in_0x5621811c9b90 [label="H", shape=none];
        interface_2_in_0x7fd4f8020968 [label="H", shape=none];
        interface_2_in_0x7fd5ec008198 [label="g^-1*C_out", shape=none];
    }
    {
        rank = same;
        interface_2_in_0x5621811c9b40;
        interface_2_in_0x7fd0380542f0;
        interface_2_in_0x5621811c9b90;
        interface_2_in_0x7fd4f8020968;
        interface_2_in_0x7fd5ec008198;
    }
    // Op's.
    op_0x7fd4f8020940 [label="Unfold"];
    // Dimension's.
    interface_2_in_0x5621811c9b40 -> interface_2_out_0x5621811c9b40 [label="N"];
    interface_2_in_0x5621811c9b90 -> interface_2_out_0x5621811c9b90 [label="H"];
    op_0x7fd4f8020940 -> interface_2_out_0x5621811c9bb8 [label="H"];
    interface_2_in_0x7fd0380542f0 -> interface_2_out_0x7fd0380542f0 [label="g^-1*s^-1*C_in"];
    op_0x7fd4f8020940 -> interface_2_out_0x7fd038054750 [label="k_1"];
    interface_2_in_0x7fd4f8020968 -> op_0x7fd4f8020940 [label="H"];
    interface_2_in_0x7fd5ec008198 -> interface_2_out_0x7fd5ec008198 [label="g^-1*C_out"];
}

// Stage tensor.
subgraph cluster_subgraph_3 {
    label = "Subgraph 3";
    // Reductions.
    reduce_0x7fce64003010 [label="Sum", shape=box];
    reduce_0x7fce640019b0 [label="Sum", shape=box];
    // Output.
    subgraph cluster_subgraph_3_out {
        label = "";
        interface_3_out_0x5621811c9b40 [label="N", shape=none];
        interface_3_out_0x7fd0380542f0 [label="g^-1*s^-1*C_in", shape=none];
        interface_3_out_0x5621811c9b90 [label="H", shape=none];
        interface_3_out_0x7fd4f8020968 [label="H", shape=none];
        interface_3_out_0x7fd5ec008198 [label="g^-1*C_out", shape=none];
    }
    {
        rank = same;
        reduce_0x7fce64003010;
        reduce_0x7fce640019b0;
        interface_3_out_0x5621811c9b40;
        interface_3_out_0x7fd0380542f0;
        interface_3_out_0x5621811c9b90;
        interface_3_out_0x7fd4f8020968;
        interface_3_out_0x7fd5ec008198;
    }
    // Input 0.
    subgraph cluster_subgraph_3_in_0 {
        label = "";
        interface_3_in_0x5621811c9b40 [label="N", shape=none];
        interface_3_in_0x7fd4bc0055a0 [label="g*s", shape=none];
        interface_3_in_0x7fd0380542f0 [label="g^-1*s^-1*C_in", shape=none];
        interface_3_in_0x5621811c9b90 [label="H", shape=none];
        interface_3_in_0x7fd0e400cde0 [label="k_1", shape=none];
        interface_3_in_0x7fd4f8020968 [label="H", shape=none];
    }
    // Input 1.
    subgraph cluster_subgraph_3_in_1 {
        label = "";
        interface_3_in_0x7fd4bc0055b8 [label="g*s", shape=none];
        interface_3_in_0x7fd0e400cdf8 [label="k_1", shape=none];
        interface_3_in_0x7fd4bc004b18 [label="g^-1*C_out", shape=none];
    }
    {
        rank = same;
        interface_3_in_0x5621811c9b40;
        interface_3_in_0x7fd4bc0055a0;
        interface_3_in_0x7fd0380542f0;
        interface_3_in_0x5621811c9b90;
        interface_3_in_0x7fd0e400cde0;
        interface_3_in_0x7fd4f8020968;
        interface_3_in_0x7fd4bc0055b8;
        interface_3_in_0x7fd0e400cdf8;
        interface_3_in_0x7fd4bc004b18;
    }
    // Op's.
    op_0x7fd0e400cdc0 [label="Share"];
    op_0x7fd4bc004ae0 [label="Share"];
    op_0x7fd4bc005580 [label="Share"];
    op_0x7fd5e0004a78 [label="Expand"];
    // Dimension's.
    interface_3_in_0x5621811c9b40 -> interface_3_out_0x5621811c9b40 [label="N"];
    interface_3_in_0x5621811c9b90 -> interface_3_out_0x5621811c9b90 [label="H"];
    op_0x7fd0e400cdc0 -> reduce_0x7fce640019b0 [label="k_1"];
    op_0x7fd4bc005580 -> reduce_0x7fce64003010 [label="g*s"];
    interface_3_in_0x7fd0380542f0 -> interface_3_out_0x7fd0380542f0 [label="g^-1*s^-1*C_in"];
    interface_3_in_0x7fd0e400cde0 -> op_0x7fd0e400cdc0 [label="k_1"];
    interface_3_in_0x7fd0e400cdf8 -> op_0x7fd0e400cdc0 [label="k_1"];
    op_0x7fd5e0004a78 -> op_0x7fd4bc004ae0 [label="g^-1*C_out"];
    interface_3_in_0x7fd4bc004b18 -> op_0x7fd4bc004ae0 [label="g^-1*C_out"];
    interface_3_in_0x7fd4bc0055a0 -> op_0x7fd4bc005580 [label="g*s"];
    interface_3_in_0x7fd4bc0055b8 -> op_0x7fd4bc005580 [label="g*s"];
    interface_3_in_0x7fd4f8020968 -> interface_3_out_0x7fd4f8020968 [label="H"];
    op_0x7fd4bc004ae0 -> interface_3_out_0x7fd5ec008198 [label="g^-1*C_out"];
}

// Stage tensor.
subgraph cluster_subgraph_4 {
    label = "Subgraph 4";
    // Reductions.
    // Output.
    subgraph cluster_subgraph_4_out {
        label = "";
        interface_4_out_0x5621811c9b40 [label="N", shape=none];
        interface_4_out_0x7fd4bc0055a0 [label="g*s", shape=none];
        interface_4_out_0x7fd0380542f0 [label="g^-1*s^-1*C_in", shape=none];
        interface_4_out_0x5621811c9b90 [label="H", shape=none];
        interface_4_out_0x7fd0e400cde0 [label="k_1", shape=none];
        interface_4_out_0x7fd4f8020968 [label="H", shape=none];
    }
    {
        rank = same;
        interface_4_out_0x5621811c9b40;
        interface_4_out_0x7fd4bc0055a0;
        interface_4_out_0x7fd0380542f0;
        interface_4_out_0x5621811c9b90;
        interface_4_out_0x7fd0e400cde0;
        interface_4_out_0x7fd4f8020968;
    }
    // Input 0.
    subgraph cluster_subgraph_4_in_0 {
        label = "";
        interface_4_in_0x5621811c9b40 [label="N", shape=none];
        interface_4_in_0x7fc3d03afd00 [label="C_in", shape=none];
        interface_4_in_0x7fd038066270 [label="H", shape=none];
        interface_4_in_0x7fd4f8020968 [label="H", shape=none];
    }
    {
        rank = same;
        interface_4_in_0x5621811c9b40;
        interface_4_in_0x7fc3d03afd00;
        interface_4_in_0x7fd038066270;
        interface_4_in_0x7fd4f8020968;
    }
    // Op's.
    op_0x7fc3d03afcc0 [label="Split"];
    op_0x7fd038066250 [label="Shift"];
    op_0x7fd4f8020a40 [label="Unfold"];
    // Dimension's.
    interface_4_in_0x5621811c9b40 -> interface_4_out_0x5621811c9b40 [label="N"];
    op_0x7fd4f8020a40 -> interface_4_out_0x5621811c9b90 [label="H"];
    interface_4_in_0x7fc3d03afd00 -> op_0x7fc3d03afcc0 [label="C_in"];
    op_0x7fc3d03afcc0 -> interface_4_out_0x7fd0380542f0 [label="g^-1*s^-1*C_in"];
    interface_4_in_0x7fd038066270 -> op_0x7fd038066250 [label="H"];
    op_0x7fd4f8020a40 -> interface_4_out_0x7fd0e400cde0 [label="k_1"];
    op_0x7fc3d03afcc0 -> interface_4_out_0x7fd4bc0055a0 [label="g*s"];
    interface_4_in_0x7fd4f8020968 -> interface_4_out_0x7fd4f8020968 [label="H"];
    op_0x7fd038066250 -> op_0x7fd4f8020a40 [label="H"];
}

// Input tensor.
subgraph cluster_subgraph_5 {
    label = "Input 0";
    interface_5_out_0x5621811c9b40 [label="N", shape=none];
    interface_5_out_0x7fc3d03afd00 [label="C_in", shape=none];
    interface_5_out_0x7fd038066270 [label="H", shape=none];
    interface_5_out_0x7fd4f8020968 [label="H", shape=none];
}

interface_5_out_0x5621811c9b40 -> interface_4_in_0x5621811c9b40;
interface_5_out_0x7fc3d03afd00 -> interface_4_in_0x7fc3d03afd00;
interface_5_out_0x7fd038066270 -> interface_4_in_0x7fd038066270;
interface_5_out_0x7fd4f8020968 -> interface_4_in_0x7fd4f8020968;

interface_4_out_0x5621811c9b40 -> interface_3_in_0x5621811c9b40;
interface_4_out_0x7fd4bc0055a0 -> interface_3_in_0x7fd4bc0055a0;
interface_4_out_0x7fd0380542f0 -> interface_3_in_0x7fd0380542f0;
interface_4_out_0x5621811c9b90 -> interface_3_in_0x5621811c9b90;
interface_4_out_0x7fd0e400cde0 -> interface_3_in_0x7fd0e400cde0;
interface_4_out_0x7fd4f8020968 -> interface_3_in_0x7fd4f8020968;

// Input tensor.
subgraph cluster_subgraph_6 {
    label = "Input 1";
    interface_6_out_0x7fd4bc0055b8 [label="g*s", shape=none];
    interface_6_out_0x7fd0e400cdf8 [label="k_1", shape=none];
    interface_6_out_0x7fd4bc004b18 [label="g^-1*C_out", shape=none];
}

interface_6_out_0x7fd4bc0055b8 -> interface_3_in_0x7fd4bc0055b8;
interface_6_out_0x7fd0e400cdf8 -> interface_3_in_0x7fd0e400cdf8;
interface_6_out_0x7fd4bc004b18 -> interface_3_in_0x7fd4bc004b18;

interface_3_out_0x5621811c9b40 -> interface_2_in_0x5621811c9b40;
interface_3_out_0x7fd0380542f0 -> interface_2_in_0x7fd0380542f0;
interface_3_out_0x5621811c9b90 -> interface_2_in_0x5621811c9b90;
interface_3_out_0x7fd4f8020968 -> interface_2_in_0x7fd4f8020968;
interface_3_out_0x7fd5ec008198 -> interface_2_in_0x7fd5ec008198;

interface_2_out_0x5621811c9b40 -> interface_1_in_0x5621811c9b40;
interface_2_out_0x7fd0380542f0 -> interface_1_in_0x7fd0380542f0;
interface_2_out_0x5621811c9b90 -> interface_1_in_0x5621811c9b90;
interface_2_out_0x5621811c9bb8 -> interface_1_in_0x5621811c9bb8;
interface_2_out_0x7fd038054750 -> interface_1_in_0x7fd038054750;
interface_2_out_0x7fd5ec008198 -> interface_1_in_0x7fd5ec008198;

// Input tensor.
subgraph cluster_subgraph_7 {
    label = "Input 2";
    interface_7_out_0x7fd038054308 [label="g^-1*s^-1*C_in", shape=none];
    interface_7_out_0x7fd038054768 [label="k_1", shape=none];
    interface_7_out_0x7fd0380543a8 [label="g", shape=none];
}

interface_7_out_0x7fd038054308 -> interface_1_in_0x7fd038054308;
interface_7_out_0x7fd038054768 -> interface_1_in_0x7fd038054768;
interface_7_out_0x7fd0380543a8 -> interface_1_in_0x7fd0380543a8;

interface_1_out_0x5621811c9b40 -> interface_0_in_0x5621811c9b40;
interface_1_out_0x5621811c9b90 -> interface_0_in_0x5621811c9b90;
interface_1_out_0x5621811c9bb8 -> interface_0_in_0x5621811c9bb8;
interface_1_out_0x7fd5ec008198 -> interface_0_in_0x7fd5ec008198;
interface_1_out_0x7fd5ec008180 -> interface_0_in_0x7fd5ec008180;

{
    rank = same;
    interface_5_out_0x5621811c9b40;
    interface_5_out_0x7fc3d03afd00;
    interface_5_out_0x7fd038066270;
    interface_5_out_0x7fd4f8020968;
    interface_6_out_0x7fd4bc0055b8;
    interface_6_out_0x7fd0e400cdf8;
    interface_6_out_0x7fd4bc004b18;
    interface_7_out_0x7fd038054308;
    interface_7_out_0x7fd038054768;
    interface_7_out_0x7fd0380543a8;
}
subgraph cluster_subgraph_output {
    label = "Output";
    interface_8_in_0x5621811c9b40 [label="N", shape=none];
    interface_8_in_0x5621811c9b68 [label="C_out", shape=none];
    interface_8_in_0x5621811c9b90 [label="H", shape=none];
    interface_8_in_0x5621811c9bb8 [label="H", shape=none];
}
interface_0_out_0x5621811c9b40 -> interface_8_in_0x5621811c9b40;
interface_0_out_0x5621811c9b68 -> interface_8_in_0x5621811c9b68;
interface_0_out_0x5621811c9b90 -> interface_8_in_0x5621811c9b90;
interface_0_out_0x5621811c9bb8 -> interface_8_in_0x5621811c9bb8;

}

"""
class kernel_generated_0(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([64, 3, 4]),
			torch.randn([2, 3, 32]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]
		in_2 = self.weights[1]

		# No contraction needed.
		t_3 = in_0

		# [C_in]@Splitfaea1e47551cefb0 -> [g*s]@Share8fb28f0c9326f917, [g^-1*s^-1*C_in]@Share5d155fcebfb4fc10
		t_3 = torch.reshape(t_3, (128, 64, 2, 56, 56, ))

		# [H]@Shift50434f3e383b3310 -> [H]@Unfold87ed2fb8f6552d8f
		t_3 = torch.roll(t_3, self.shift_direction, 3)

		# [H]@Unfold87ed2fb8f6552d8f -> [H]@Iterator96123ba3184da39c, [k_1]@Share02da0a485106ab3d
		t_3 = torch.reshape(t_3, (128, 128, 56, 56, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (128, 64, 2, 3, 56, 56, ))

		# Permute to match the output of this subgraph.
		t_3 = torch.permute(t_3, (0, 1, 2, 4, 3, 5, ))

		# Perform contraction.
		t_4 = torch.einsum("lknmio, kij -> lnmoj", t_3, in_1)

		# No contraction needed.
		t_5 = t_4

		# [H]@Unfold0063bc82bd8ddf70 -> [H]@Iteratorb0a1def4ad5784ec, [k_1]@Shared4e0659d169008e4
		t_5 = torch.reshape(t_5, (128, 112, 56, 4, ))
		t_5 = torch.nn.functional.unfold(t_5, (3, 1, ), padding=(1, 0, ))
		t_5 = torch.reshape(t_5, (128, 2, 56, 3, 56, 4, ))

		# Permute to match the output of this subgraph.
		t_5 = torch.permute(t_5, (0, 1, 2, 4, 3, 5, ))

		# Perform contraction.
		t_6 = torch.einsum("limnko, ikj -> lmnoj", t_5, in_2)

		# No contraction needed.
		t_7 = t_6

		# [g]@Merge402ce7fe20a0a5fb, [g^-1*C_out]@Merge402ce7fe20a0a5f8 -> [C_out]@Iteratorc7f8eb87a5a0a9e0
		t_7 = torch.permute(t_7, (0, 1, 2, 4, 3, ))
		t_7 = torch.reshape(t_7, (128, 56, 56, 128, ))

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
			torch.randn([64, 3, 8]),
			torch.randn([4, 3, 32]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]
		in_2 = self.weights[1]

		# No contraction needed.
		t_3 = in_0

		# [C_in]@Splitfaea1e47551cefb0 -> [g*s]@Share8fb28f0c9326f917, [g^-1*s^-1*C_in]@Share5d155fcebfb4fc10
		t_3 = torch.reshape(t_3, (128, 64, 4, 28, 28, ))

		# [H]@Shift50434f3e383b3310 -> [H]@Unfold87ed2fb8f6552d8f
		t_3 = torch.roll(t_3, self.shift_direction, 3)

		# [H]@Unfold87ed2fb8f6552d8f -> [H]@Iterator96123ba3184da39c, [k_1]@Share02da0a485106ab3d
		t_3 = torch.reshape(t_3, (128, 256, 28, 28, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (128, 64, 4, 3, 28, 28, ))

		# Permute to match the output of this subgraph.
		t_3 = torch.permute(t_3, (0, 1, 2, 4, 3, 5, ))

		# Perform contraction.
		t_4 = torch.einsum("lknmio, kij -> lnmoj", t_3, in_1)

		# No contraction needed.
		t_5 = t_4

		# [H]@Unfold0063bc82bd8ddf70 -> [H]@Iteratorb0a1def4ad5784ec, [k_1]@Shared4e0659d169008e4
		t_5 = torch.reshape(t_5, (128, 112, 28, 8, ))
		t_5 = torch.nn.functional.unfold(t_5, (3, 1, ), padding=(1, 0, ))
		t_5 = torch.reshape(t_5, (128, 4, 28, 3, 28, 8, ))

		# Permute to match the output of this subgraph.
		t_5 = torch.permute(t_5, (0, 1, 2, 4, 3, 5, ))

		# Perform contraction.
		t_6 = torch.einsum("limnko, ikj -> lmnoj", t_5, in_2)

		# No contraction needed.
		t_7 = t_6

		# [g]@Merge402ce7fe20a0a5fb, [g^-1*C_out]@Merge402ce7fe20a0a5f8 -> [C_out]@Iteratorc7f8eb87a5a0a9e0
		t_7 = torch.permute(t_7, (0, 1, 2, 4, 3, ))
		t_7 = torch.reshape(t_7, (128, 28, 28, 256, ))

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
			torch.randn([64, 3, 16]),
			torch.randn([8, 3, 32]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]
		in_2 = self.weights[1]

		# No contraction needed.
		t_3 = in_0

		# [C_in]@Splitfaea1e47551cefb0 -> [g*s]@Share8fb28f0c9326f917, [g^-1*s^-1*C_in]@Share5d155fcebfb4fc10
		t_3 = torch.reshape(t_3, (128, 64, 8, 14, 14, ))

		# [H]@Shift50434f3e383b3310 -> [H]@Unfold87ed2fb8f6552d8f
		t_3 = torch.roll(t_3, self.shift_direction, 3)

		# [H]@Unfold87ed2fb8f6552d8f -> [H]@Iterator96123ba3184da39c, [k_1]@Share02da0a485106ab3d
		t_3 = torch.reshape(t_3, (128, 512, 14, 14, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (128, 64, 8, 3, 14, 14, ))

		# Permute to match the output of this subgraph.
		t_3 = torch.permute(t_3, (0, 1, 2, 4, 3, 5, ))

		# Perform contraction.
		t_4 = torch.einsum("lknmio, kij -> lnmoj", t_3, in_1)

		# No contraction needed.
		t_5 = t_4

		# [H]@Unfold0063bc82bd8ddf70 -> [H]@Iteratorb0a1def4ad5784ec, [k_1]@Shared4e0659d169008e4
		t_5 = torch.reshape(t_5, (128, 112, 14, 16, ))
		t_5 = torch.nn.functional.unfold(t_5, (3, 1, ), padding=(1, 0, ))
		t_5 = torch.reshape(t_5, (128, 8, 14, 3, 14, 16, ))

		# Permute to match the output of this subgraph.
		t_5 = torch.permute(t_5, (0, 1, 2, 4, 3, 5, ))

		# Perform contraction.
		t_6 = torch.einsum("limnko, ikj -> lmnoj", t_5, in_2)

		# No contraction needed.
		t_7 = t_6

		# [g]@Merge402ce7fe20a0a5fb, [g^-1*C_out]@Merge402ce7fe20a0a5f8 -> [C_out]@Iteratorc7f8eb87a5a0a9e0
		t_7 = torch.permute(t_7, (0, 1, 2, 4, 3, ))
		t_7 = torch.reshape(t_7, (128, 14, 14, 512, ))

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
			torch.randn([64, 3, 32]),
			torch.randn([16, 3, 32]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]
		in_2 = self.weights[1]

		# No contraction needed.
		t_3 = in_0

		# [C_in]@Splitfaea1e47551cefb0 -> [g*s]@Share8fb28f0c9326f917, [g^-1*s^-1*C_in]@Share5d155fcebfb4fc10
		t_3 = torch.reshape(t_3, (128, 64, 16, 7, 7, ))

		# [H]@Shift50434f3e383b3310 -> [H]@Unfold87ed2fb8f6552d8f
		t_3 = torch.roll(t_3, self.shift_direction, 3)

		# [H]@Unfold87ed2fb8f6552d8f -> [H]@Iterator96123ba3184da39c, [k_1]@Share02da0a485106ab3d
		t_3 = torch.reshape(t_3, (128, 1024, 7, 7, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (128, 64, 16, 3, 7, 7, ))

		# Permute to match the output of this subgraph.
		t_3 = torch.permute(t_3, (0, 1, 2, 4, 3, 5, ))

		# Perform contraction.
		t_4 = torch.einsum("lknmio, kij -> lnmoj", t_3, in_1)

		# No contraction needed.
		t_5 = t_4

		# [H]@Unfold0063bc82bd8ddf70 -> [H]@Iteratorb0a1def4ad5784ec, [k_1]@Shared4e0659d169008e4
		t_5 = torch.reshape(t_5, (128, 112, 7, 32, ))
		t_5 = torch.nn.functional.unfold(t_5, (3, 1, ), padding=(1, 0, ))
		t_5 = torch.reshape(t_5, (128, 16, 7, 3, 7, 32, ))

		# Permute to match the output of this subgraph.
		t_5 = torch.permute(t_5, (0, 1, 2, 4, 3, 5, ))

		# Perform contraction.
		t_6 = torch.einsum("limnko, ikj -> lmnoj", t_5, in_2)

		# No contraction needed.
		t_7 = t_6

		# [g]@Merge402ce7fe20a0a5fb, [g^-1*C_out]@Merge402ce7fe20a0a5f8 -> [C_out]@Iteratorc7f8eb87a5a0a9e0
		t_7 = torch.permute(t_7, (0, 1, 2, 4, 3, ))
		t_7 = torch.reshape(t_7, (128, 7, 7, 1024, ))

		# Permute to match the output of this subgraph.
		t_7 = torch.permute(t_7, (0, 3, 1, 2, ))

		# No need to crop the output tensor.
		y = t_7

		return y

