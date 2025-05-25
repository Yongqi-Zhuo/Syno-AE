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
        interface_0_in_0x7fd5ec005160 [label="H", shape=none];
        interface_0_in_0x5621811c9bb8 [label="H", shape=none];
        interface_0_in_0x7fd5ec008198 [label="g^-1*C_out", shape=none];
        interface_0_in_0x7fd5ec008180 [label="g", shape=none];
    }
    {
        rank = same;
        interface_0_in_0x5621811c9b40;
        interface_0_in_0x7fd5ec005160;
        interface_0_in_0x5621811c9bb8;
        interface_0_in_0x7fd5ec008198;
        interface_0_in_0x7fd5ec008180;
    }
    // Op's.
    op_0x7fd5ec005140 [label="Shift"];
    op_0x7fd5ec008140 [label="Merge"];
    // Dimension's.
    interface_0_in_0x5621811c9b40 -> interface_0_out_0x5621811c9b40 [label="N"];
    op_0x7fd5ec008140 -> interface_0_out_0x5621811c9b68 [label="C_out"];
    op_0x7fd5ec005140 -> interface_0_out_0x5621811c9b90 [label="H"];
    interface_0_in_0x5621811c9bb8 -> interface_0_out_0x5621811c9bb8 [label="H"];
    interface_0_in_0x7fd5ec005160 -> op_0x7fd5ec005140 [label="H"];
    interface_0_in_0x7fd5ec008180 -> op_0x7fd5ec008140 [label="g"];
    interface_0_in_0x7fd5ec008198 -> op_0x7fd5ec008140 [label="g^-1*C_out"];
}

// Stage tensor.
subgraph cluster_subgraph_1 {
    label = "Subgraph 1";
    // Reductions.
    reduce_0x7fce64005a20 [label="Sum", shape=box];
    reduce_0x7fce640019b0 [label="Sum", shape=box];
    reduce_0x7fce64001998 [label="Sum", shape=box];
    // Output.
    subgraph cluster_subgraph_1_out {
        label = "";
        interface_1_out_0x5621811c9b40 [label="N", shape=none];
        interface_1_out_0x7fd5ec005160 [label="H", shape=none];
        interface_1_out_0x5621811c9bb8 [label="H", shape=none];
        interface_1_out_0x7fd5ec008198 [label="g^-1*C_out", shape=none];
        interface_1_out_0x7fd5ec008180 [label="g", shape=none];
    }
    {
        rank = same;
        reduce_0x7fce64005a20;
        reduce_0x7fce640019b0;
        reduce_0x7fce64001998;
        interface_1_out_0x5621811c9b40;
        interface_1_out_0x7fd5ec005160;
        interface_1_out_0x5621811c9bb8;
        interface_1_out_0x7fd5ec008198;
        interface_1_out_0x7fd5ec008180;
    }
    // Input 0.
    subgraph cluster_subgraph_1_in_0 {
        label = "";
        interface_1_in_0x5621811c9b40 [label="N", shape=none];
        interface_1_in_0x7fd5e0004800 [label="g^-1*s^-1*C_in", shape=none];
        interface_1_in_0x7fd5ec005160 [label="H", shape=none];
        interface_1_in_0x5621811c9bb8 [label="H", shape=none];
        interface_1_in_0x7fd0e400cde0 [label="k_1", shape=none];
        interface_1_in_0x7fd5e00045d0 [label="k_1", shape=none];
        interface_1_in_0x7fd5ec008198 [label="g^-1*C_out", shape=none];
    }
    // Input 1.
    subgraph cluster_subgraph_1_in_1 {
        label = "";
        interface_1_in_0x7fd5e0004818 [label="g^-1*s^-1*C_in", shape=none];
        interface_1_in_0x7fd0e400cdf8 [label="k_1", shape=none];
        interface_1_in_0x7fd5e00045e8 [label="k_1", shape=none];
        interface_1_in_0x7fd4bc004a78 [label="g", shape=none];
    }
    {
        rank = same;
        interface_1_in_0x5621811c9b40;
        interface_1_in_0x7fd5e0004800;
        interface_1_in_0x7fd5ec005160;
        interface_1_in_0x5621811c9bb8;
        interface_1_in_0x7fd0e400cde0;
        interface_1_in_0x7fd5e00045d0;
        interface_1_in_0x7fd5ec008198;
        interface_1_in_0x7fd5e0004818;
        interface_1_in_0x7fd0e400cdf8;
        interface_1_in_0x7fd5e00045e8;
        interface_1_in_0x7fd4bc004a78;
    }
    // Op's.
    op_0x7fd0e400cdc0 [label="Share"];
    op_0x7fd4bc004a40 [label="Share"];
    op_0x7fd5e00045b0 [label="Share"];
    op_0x7fd5e00047e0 [label="Share"];
    op_0x7fd5e0004a58 [label="Expand"];
    // Dimension's.
    interface_1_in_0x5621811c9b40 -> interface_1_out_0x5621811c9b40 [label="N"];
    interface_1_in_0x5621811c9bb8 -> interface_1_out_0x5621811c9bb8 [label="H"];
    op_0x7fd5e00045b0 -> reduce_0x7fce64001998 [label="k_1"];
    op_0x7fd0e400cdc0 -> reduce_0x7fce640019b0 [label="k_1"];
    op_0x7fd5e00047e0 -> reduce_0x7fce64005a20 [label="g^-1*s^-1*C_in"];
    interface_1_in_0x7fd0e400cde0 -> op_0x7fd0e400cdc0 [label="k_1"];
    interface_1_in_0x7fd0e400cdf8 -> op_0x7fd0e400cdc0 [label="k_1"];
    op_0x7fd5e0004a58 -> op_0x7fd4bc004a40 [label="g"];
    interface_1_in_0x7fd4bc004a78 -> op_0x7fd4bc004a40 [label="g"];
    interface_1_in_0x7fd5e00045d0 -> op_0x7fd5e00045b0 [label="k_1"];
    interface_1_in_0x7fd5e00045e8 -> op_0x7fd5e00045b0 [label="k_1"];
    interface_1_in_0x7fd5e0004800 -> op_0x7fd5e00047e0 [label="g^-1*s^-1*C_in"];
    interface_1_in_0x7fd5e0004818 -> op_0x7fd5e00047e0 [label="g^-1*s^-1*C_in"];
    interface_1_in_0x7fd5ec005160 -> interface_1_out_0x7fd5ec005160 [label="H"];
    op_0x7fd4bc004a40 -> interface_1_out_0x7fd5ec008180 [label="g"];
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
        interface_2_out_0x7fd5e0004800 [label="g^-1*s^-1*C_in", shape=none];
        interface_2_out_0x7fd5ec005160 [label="H", shape=none];
        interface_2_out_0x5621811c9bb8 [label="H", shape=none];
        interface_2_out_0x7fd0e400cde0 [label="k_1", shape=none];
        interface_2_out_0x7fd5e00045d0 [label="k_1", shape=none];
        interface_2_out_0x7fd5ec008198 [label="g^-1*C_out", shape=none];
    }
    {
        rank = same;
        interface_2_out_0x5621811c9b40;
        interface_2_out_0x7fd5e0004800;
        interface_2_out_0x7fd5ec005160;
        interface_2_out_0x5621811c9bb8;
        interface_2_out_0x7fd0e400cde0;
        interface_2_out_0x7fd5e00045d0;
        interface_2_out_0x7fd5ec008198;
    }
    // Input 0.
    subgraph cluster_subgraph_2_in_0 {
        label = "";
        interface_2_in_0x5621811c9b40 [label="N", shape=none];
        interface_2_in_0x7fd5e0004800 [label="g^-1*s^-1*C_in", shape=none];
        interface_2_in_0x7fd5ec005160 [label="H", shape=none];
        interface_2_in_0x7fd228054de8 [label="H", shape=none];
        interface_2_in_0x7fd5ec008198 [label="g^-1*C_out", shape=none];
    }
    {
        rank = same;
        interface_2_in_0x5621811c9b40;
        interface_2_in_0x7fd5e0004800;
        interface_2_in_0x7fd5ec005160;
        interface_2_in_0x7fd228054de8;
        interface_2_in_0x7fd5ec008198;
    }
    // Op's.
    op_0x7fd228054dc0 [label="Unfold"];
    op_0x7fd4f8020a00 [label="Unfold"];
    // Dimension's.
    interface_2_in_0x5621811c9b40 -> interface_2_out_0x5621811c9b40 [label="N"];
    op_0x7fd4f8020a00 -> interface_2_out_0x5621811c9bb8 [label="H"];
    op_0x7fd4f8020a00 -> interface_2_out_0x7fd0e400cde0 [label="k_1"];
    interface_2_in_0x7fd228054de8 -> op_0x7fd228054dc0 [label="H"];
    op_0x7fd228054dc0 -> op_0x7fd4f8020a00 [label="H"];
    op_0x7fd228054dc0 -> interface_2_out_0x7fd5e00045d0 [label="k_1"];
    interface_2_in_0x7fd5e0004800 -> interface_2_out_0x7fd5e0004800 [label="g^-1*s^-1*C_in"];
    interface_2_in_0x7fd5ec005160 -> interface_2_out_0x7fd5ec005160 [label="H"];
    interface_2_in_0x7fd5ec008198 -> interface_2_out_0x7fd5ec008198 [label="g^-1*C_out"];
}

// Stage tensor.
subgraph cluster_subgraph_3 {
    label = "Subgraph 3";
    // Reductions.
    reduce_0x7fce64003010 [label="Sum", shape=box];
    // Output.
    subgraph cluster_subgraph_3_out {
        label = "";
        interface_3_out_0x5621811c9b40 [label="N", shape=none];
        interface_3_out_0x7fd5e0004800 [label="g^-1*s^-1*C_in", shape=none];
        interface_3_out_0x7fd5ec005160 [label="H", shape=none];
        interface_3_out_0x7fd228054de8 [label="H", shape=none];
        interface_3_out_0x7fd5ec008198 [label="g^-1*C_out", shape=none];
    }
    {
        rank = same;
        reduce_0x7fce64003010;
        interface_3_out_0x5621811c9b40;
        interface_3_out_0x7fd5e0004800;
        interface_3_out_0x7fd5ec005160;
        interface_3_out_0x7fd228054de8;
        interface_3_out_0x7fd5ec008198;
    }
    // Input 0.
    subgraph cluster_subgraph_3_in_0 {
        label = "";
        interface_3_in_0x5621811c9b40 [label="N", shape=none];
        interface_3_in_0x7fd4a4232fe0 [label="g*s", shape=none];
        interface_3_in_0x7fd5e0004800 [label="g^-1*s^-1*C_in", shape=none];
        interface_3_in_0x7fd5ec005160 [label="H", shape=none];
        interface_3_in_0x7fd228054de8 [label="H", shape=none];
    }
    // Input 1.
    subgraph cluster_subgraph_3_in_1 {
        label = "";
        interface_3_in_0x7fd4a4232ff8 [label="g*s", shape=none];
        interface_3_in_0x7fd038054268 [label="g^-1*C_out", shape=none];
    }
    {
        rank = same;
        interface_3_in_0x5621811c9b40;
        interface_3_in_0x7fd4a4232fe0;
        interface_3_in_0x7fd5e0004800;
        interface_3_in_0x7fd5ec005160;
        interface_3_in_0x7fd228054de8;
        interface_3_in_0x7fd4a4232ff8;
        interface_3_in_0x7fd038054268;
    }
    // Op's.
    op_0x5621811b6cf8 [label="Expand"];
    op_0x7fd038054230 [label="Share"];
    op_0x7fd4a4232fc0 [label="Share"];
    // Dimension's.
    interface_3_in_0x5621811c9b40 -> interface_3_out_0x5621811c9b40 [label="N"];
    op_0x7fd4a4232fc0 -> reduce_0x7fce64003010 [label="g*s"];
    op_0x5621811b6cf8 -> op_0x7fd038054230 [label="g^-1*C_out"];
    interface_3_in_0x7fd038054268 -> op_0x7fd038054230 [label="g^-1*C_out"];
    interface_3_in_0x7fd228054de8 -> interface_3_out_0x7fd228054de8 [label="H"];
    interface_3_in_0x7fd4a4232fe0 -> op_0x7fd4a4232fc0 [label="g*s"];
    interface_3_in_0x7fd4a4232ff8 -> op_0x7fd4a4232fc0 [label="g*s"];
    interface_3_in_0x7fd5e0004800 -> interface_3_out_0x7fd5e0004800 [label="g^-1*s^-1*C_in"];
    interface_3_in_0x7fd5ec005160 -> interface_3_out_0x7fd5ec005160 [label="H"];
    op_0x7fd038054230 -> interface_3_out_0x7fd5ec008198 [label="g^-1*C_out"];
}

// Stage tensor.
subgraph cluster_subgraph_4 {
    label = "Subgraph 4";
    // Reductions.
    // Output.
    subgraph cluster_subgraph_4_out {
        label = "";
        interface_4_out_0x5621811c9b40 [label="N", shape=none];
        interface_4_out_0x7fd4a4232fe0 [label="g*s", shape=none];
        interface_4_out_0x7fd5e0004800 [label="g^-1*s^-1*C_in", shape=none];
        interface_4_out_0x7fd5ec005160 [label="H", shape=none];
        interface_4_out_0x7fd228054de8 [label="H", shape=none];
    }
    {
        rank = same;
        interface_4_out_0x5621811c9b40;
        interface_4_out_0x7fd4a4232fe0;
        interface_4_out_0x7fd5e0004800;
        interface_4_out_0x7fd5ec005160;
        interface_4_out_0x7fd228054de8;
    }
    // Input 0.
    subgraph cluster_subgraph_4_in_0 {
        label = "";
        interface_4_in_0x5621811c9b40 [label="N", shape=none];
        interface_4_in_0x7fc3d03afa80 [label="C_in", shape=none];
        interface_4_in_0x7fd5ec005160 [label="H", shape=none];
        interface_4_in_0x7fd228054de8 [label="H", shape=none];
    }
    {
        rank = same;
        interface_4_in_0x5621811c9b40;
        interface_4_in_0x7fc3d03afa80;
        interface_4_in_0x7fd5ec005160;
        interface_4_in_0x7fd228054de8;
    }
    // Op's.
    op_0x7fc3d03afa40 [label="Split"];
    // Dimension's.
    interface_4_in_0x5621811c9b40 -> interface_4_out_0x5621811c9b40 [label="N"];
    interface_4_in_0x7fc3d03afa80 -> op_0x7fc3d03afa40 [label="C_in"];
    interface_4_in_0x7fd228054de8 -> interface_4_out_0x7fd228054de8 [label="H"];
    op_0x7fc3d03afa40 -> interface_4_out_0x7fd4a4232fe0 [label="g*s"];
    op_0x7fc3d03afa40 -> interface_4_out_0x7fd5e0004800 [label="g^-1*s^-1*C_in"];
    interface_4_in_0x7fd5ec005160 -> interface_4_out_0x7fd5ec005160 [label="H"];
}

// Input tensor.
subgraph cluster_subgraph_5 {
    label = "Input 0";
    interface_5_out_0x5621811c9b40 [label="N", shape=none];
    interface_5_out_0x7fc3d03afa80 [label="C_in", shape=none];
    interface_5_out_0x7fd5ec005160 [label="H", shape=none];
    interface_5_out_0x7fd228054de8 [label="H", shape=none];
}

interface_5_out_0x5621811c9b40 -> interface_4_in_0x5621811c9b40;
interface_5_out_0x7fc3d03afa80 -> interface_4_in_0x7fc3d03afa80;
interface_5_out_0x7fd5ec005160 -> interface_4_in_0x7fd5ec005160;
interface_5_out_0x7fd228054de8 -> interface_4_in_0x7fd228054de8;

interface_4_out_0x5621811c9b40 -> interface_3_in_0x5621811c9b40;
interface_4_out_0x7fd4a4232fe0 -> interface_3_in_0x7fd4a4232fe0;
interface_4_out_0x7fd5e0004800 -> interface_3_in_0x7fd5e0004800;
interface_4_out_0x7fd5ec005160 -> interface_3_in_0x7fd5ec005160;
interface_4_out_0x7fd228054de8 -> interface_3_in_0x7fd228054de8;

// Input tensor.
subgraph cluster_subgraph_6 {
    label = "Input 2";
    interface_6_out_0x7fd4a4232ff8 [label="g*s", shape=none];
    interface_6_out_0x7fd038054268 [label="g^-1*C_out", shape=none];
}

interface_6_out_0x7fd4a4232ff8 -> interface_3_in_0x7fd4a4232ff8;
interface_6_out_0x7fd038054268 -> interface_3_in_0x7fd038054268;

interface_3_out_0x5621811c9b40 -> interface_2_in_0x5621811c9b40;
interface_3_out_0x7fd5e0004800 -> interface_2_in_0x7fd5e0004800;
interface_3_out_0x7fd5ec005160 -> interface_2_in_0x7fd5ec005160;
interface_3_out_0x7fd228054de8 -> interface_2_in_0x7fd228054de8;
interface_3_out_0x7fd5ec008198 -> interface_2_in_0x7fd5ec008198;

interface_2_out_0x5621811c9b40 -> interface_1_in_0x5621811c9b40;
interface_2_out_0x7fd5e0004800 -> interface_1_in_0x7fd5e0004800;
interface_2_out_0x7fd5ec005160 -> interface_1_in_0x7fd5ec005160;
interface_2_out_0x5621811c9bb8 -> interface_1_in_0x5621811c9bb8;
interface_2_out_0x7fd0e400cde0 -> interface_1_in_0x7fd0e400cde0;
interface_2_out_0x7fd5e00045d0 -> interface_1_in_0x7fd5e00045d0;
interface_2_out_0x7fd5ec008198 -> interface_1_in_0x7fd5ec008198;

// Input tensor.
subgraph cluster_subgraph_7 {
    label = "Input 1";
    interface_7_out_0x7fd5e0004818 [label="g^-1*s^-1*C_in", shape=none];
    interface_7_out_0x7fd0e400cdf8 [label="k_1", shape=none];
    interface_7_out_0x7fd5e00045e8 [label="k_1", shape=none];
    interface_7_out_0x7fd4bc004a78 [label="g", shape=none];
}

interface_7_out_0x7fd5e0004818 -> interface_1_in_0x7fd5e0004818;
interface_7_out_0x7fd0e400cdf8 -> interface_1_in_0x7fd0e400cdf8;
interface_7_out_0x7fd5e00045e8 -> interface_1_in_0x7fd5e00045e8;
interface_7_out_0x7fd4bc004a78 -> interface_1_in_0x7fd4bc004a78;

interface_1_out_0x5621811c9b40 -> interface_0_in_0x5621811c9b40;
interface_1_out_0x7fd5ec005160 -> interface_0_in_0x7fd5ec005160;
interface_1_out_0x5621811c9bb8 -> interface_0_in_0x5621811c9bb8;
interface_1_out_0x7fd5ec008198 -> interface_0_in_0x7fd5ec008198;
interface_1_out_0x7fd5ec008180 -> interface_0_in_0x7fd5ec008180;

{
    rank = same;
    interface_5_out_0x5621811c9b40;
    interface_5_out_0x7fc3d03afa80;
    interface_5_out_0x7fd5ec005160;
    interface_5_out_0x7fd228054de8;
    interface_7_out_0x7fd5e0004818;
    interface_7_out_0x7fd0e400cdf8;
    interface_7_out_0x7fd5e00045e8;
    interface_7_out_0x7fd4bc004a78;
    interface_6_out_0x7fd4a4232ff8;
    interface_6_out_0x7fd038054268;
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
			torch.randn([2, 3, 3, 32]),
			torch.randn([64, 4]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]
		in_2 = self.weights[1]

		# No contraction needed.
		t_3 = in_0

		# [C_in]@Split7156f2737a83a060 -> [g*s]@Sharedc15ce1c9326f917, [g^-1*s^-1*C_in]@Share77b21cfebfb4fc10
		t_3 = torch.reshape(t_3, (128, 64, 2, 56, 56, ))

		# Perform contraction.
		t_4 = torch.einsum("kjmnl, ji -> kmnli", t_3, in_2)

		# No contraction needed.
		t_5 = t_4

		# [H]@Unfold06bdd1022a1467b1 -> [H]@Unfold3df8d2ea6f83a02b, [k_1]@Share26cfa48d169008e4
		t_5 = torch.reshape(t_5, (128, 112, 56, 4, ))
		t_5 = torch.nn.functional.unfold(t_5, (3, 1, ), padding=(1, 0, ))
		t_5 = torch.reshape(t_5, (128, 2, 56, 3, 56, 4, ))

		# [H]@Unfold3df8d2ea6f83a02b -> [H]@Iteratorb0a1def4ad5784ec, [k_1]@Share02da0a485106ab3d
		t_5 = torch.reshape(t_5, (128, 336, 56, 4, ))
		t_5 = torch.nn.functional.unfold(t_5, (3, 1, ), padding=(1, 0, ))
		t_5 = torch.reshape(t_5, (128, 2, 56, 3, 3, 56, 4, ))

		# Permute to match the output of this subgraph.
		t_5 = torch.permute(t_5, (0, 1, 2, 5, 4, 3, 6, ))

		# Perform contraction.
		t_6 = torch.einsum("mlonikp, likj -> monpj", t_5, in_1)

		# No contraction needed.
		t_7 = t_6

		# [g]@Merge402ce7fe20a0a5fb, [g^-1*C_out]@Merge402ce7fe20a0a5f8 -> [C_out]@Iteratorc7f8eb87a5a0a9e0
		t_7 = torch.permute(t_7, (0, 1, 2, 4, 3, ))
		t_7 = torch.reshape(t_7, (128, 56, 56, 128, ))

		# [H]@Shift41a433c05e30b91d -> [H]@Iterator96123ba3184da39c
		t_7 = torch.roll(t_7, self.shift_direction, 1)

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
			torch.randn([4, 3, 3, 32]),
			torch.randn([64, 8]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]
		in_2 = self.weights[1]

		# No contraction needed.
		t_3 = in_0

		# [C_in]@Split7156f2737a83a060 -> [g*s]@Sharedc15ce1c9326f917, [g^-1*s^-1*C_in]@Share77b21cfebfb4fc10
		t_3 = torch.reshape(t_3, (128, 64, 4, 28, 28, ))

		# Perform contraction.
		t_4 = torch.einsum("kjmnl, ji -> kmnli", t_3, in_2)

		# No contraction needed.
		t_5 = t_4

		# [H]@Unfold06bdd1022a1467b1 -> [H]@Unfold3df8d2ea6f83a02b, [k_1]@Share26cfa48d169008e4
		t_5 = torch.reshape(t_5, (128, 112, 28, 8, ))
		t_5 = torch.nn.functional.unfold(t_5, (3, 1, ), padding=(1, 0, ))
		t_5 = torch.reshape(t_5, (128, 4, 28, 3, 28, 8, ))

		# [H]@Unfold3df8d2ea6f83a02b -> [H]@Iteratorb0a1def4ad5784ec, [k_1]@Share02da0a485106ab3d
		t_5 = torch.reshape(t_5, (128, 336, 28, 8, ))
		t_5 = torch.nn.functional.unfold(t_5, (3, 1, ), padding=(1, 0, ))
		t_5 = torch.reshape(t_5, (128, 4, 28, 3, 3, 28, 8, ))

		# Permute to match the output of this subgraph.
		t_5 = torch.permute(t_5, (0, 1, 2, 5, 4, 3, 6, ))

		# Perform contraction.
		t_6 = torch.einsum("mlonikp, likj -> monpj", t_5, in_1)

		# No contraction needed.
		t_7 = t_6

		# [g]@Merge402ce7fe20a0a5fb, [g^-1*C_out]@Merge402ce7fe20a0a5f8 -> [C_out]@Iteratorc7f8eb87a5a0a9e0
		t_7 = torch.permute(t_7, (0, 1, 2, 4, 3, ))
		t_7 = torch.reshape(t_7, (128, 28, 28, 256, ))

		# [H]@Shift41a433c05e30b91d -> [H]@Iterator96123ba3184da39c
		t_7 = torch.roll(t_7, self.shift_direction, 1)

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
			torch.randn([8, 3, 3, 32]),
			torch.randn([64, 16]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]
		in_2 = self.weights[1]

		# No contraction needed.
		t_3 = in_0

		# [C_in]@Split7156f2737a83a060 -> [g*s]@Sharedc15ce1c9326f917, [g^-1*s^-1*C_in]@Share77b21cfebfb4fc10
		t_3 = torch.reshape(t_3, (128, 64, 8, 14, 14, ))

		# Perform contraction.
		t_4 = torch.einsum("kjmnl, ji -> kmnli", t_3, in_2)

		# No contraction needed.
		t_5 = t_4

		# [H]@Unfold06bdd1022a1467b1 -> [H]@Unfold3df8d2ea6f83a02b, [k_1]@Share26cfa48d169008e4
		t_5 = torch.reshape(t_5, (128, 112, 14, 16, ))
		t_5 = torch.nn.functional.unfold(t_5, (3, 1, ), padding=(1, 0, ))
		t_5 = torch.reshape(t_5, (128, 8, 14, 3, 14, 16, ))

		# [H]@Unfold3df8d2ea6f83a02b -> [H]@Iteratorb0a1def4ad5784ec, [k_1]@Share02da0a485106ab3d
		t_5 = torch.reshape(t_5, (128, 336, 14, 16, ))
		t_5 = torch.nn.functional.unfold(t_5, (3, 1, ), padding=(1, 0, ))
		t_5 = torch.reshape(t_5, (128, 8, 14, 3, 3, 14, 16, ))

		# Permute to match the output of this subgraph.
		t_5 = torch.permute(t_5, (0, 1, 2, 5, 4, 3, 6, ))

		# Perform contraction.
		t_6 = torch.einsum("mlonikp, likj -> monpj", t_5, in_1)

		# No contraction needed.
		t_7 = t_6

		# [g]@Merge402ce7fe20a0a5fb, [g^-1*C_out]@Merge402ce7fe20a0a5f8 -> [C_out]@Iteratorc7f8eb87a5a0a9e0
		t_7 = torch.permute(t_7, (0, 1, 2, 4, 3, ))
		t_7 = torch.reshape(t_7, (128, 14, 14, 512, ))

		# [H]@Shift41a433c05e30b91d -> [H]@Iterator96123ba3184da39c
		t_7 = torch.roll(t_7, self.shift_direction, 1)

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
			torch.randn([16, 3, 3, 32]),
			torch.randn([64, 32]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]
		in_2 = self.weights[1]

		# No contraction needed.
		t_3 = in_0

		# [C_in]@Split7156f2737a83a060 -> [g*s]@Sharedc15ce1c9326f917, [g^-1*s^-1*C_in]@Share77b21cfebfb4fc10
		t_3 = torch.reshape(t_3, (128, 64, 16, 7, 7, ))

		# Perform contraction.
		t_4 = torch.einsum("kjmnl, ji -> kmnli", t_3, in_2)

		# No contraction needed.
		t_5 = t_4

		# [H]@Unfold06bdd1022a1467b1 -> [H]@Unfold3df8d2ea6f83a02b, [k_1]@Share26cfa48d169008e4
		t_5 = torch.reshape(t_5, (128, 112, 7, 32, ))
		t_5 = torch.nn.functional.unfold(t_5, (3, 1, ), padding=(1, 0, ))
		t_5 = torch.reshape(t_5, (128, 16, 7, 3, 7, 32, ))

		# [H]@Unfold3df8d2ea6f83a02b -> [H]@Iteratorb0a1def4ad5784ec, [k_1]@Share02da0a485106ab3d
		t_5 = torch.reshape(t_5, (128, 336, 7, 32, ))
		t_5 = torch.nn.functional.unfold(t_5, (3, 1, ), padding=(1, 0, ))
		t_5 = torch.reshape(t_5, (128, 16, 7, 3, 3, 7, 32, ))

		# Permute to match the output of this subgraph.
		t_5 = torch.permute(t_5, (0, 1, 2, 5, 4, 3, 6, ))

		# Perform contraction.
		t_6 = torch.einsum("mlonikp, likj -> monpj", t_5, in_1)

		# No contraction needed.
		t_7 = t_6

		# [g]@Merge402ce7fe20a0a5fb, [g^-1*C_out]@Merge402ce7fe20a0a5f8 -> [C_out]@Iteratorc7f8eb87a5a0a9e0
		t_7 = torch.permute(t_7, (0, 1, 2, 4, 3, ))
		t_7 = torch.reshape(t_7, (128, 7, 7, 1024, ))

		# [H]@Shift41a433c05e30b91d -> [H]@Iterator96123ba3184da39c
		t_7 = torch.roll(t_7, self.shift_direction, 1)

		# Permute to match the output of this subgraph.
		t_7 = torch.permute(t_7, (0, 3, 1, 2, ))

		# No need to crop the output tensor.
		y = t_7

		return y

