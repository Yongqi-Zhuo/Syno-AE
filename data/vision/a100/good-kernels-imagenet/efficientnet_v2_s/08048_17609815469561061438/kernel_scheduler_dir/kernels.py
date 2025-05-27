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
        interface_0_out_0x56459a9d6050 [label="N", shape=none];
        interface_0_out_0x56459a9d6078 [label="C_out", shape=none];
        interface_0_out_0x56459a9d60a0 [label="H", shape=none];
        interface_0_out_0x56459a9d60c8 [label="H", shape=none];
    }
    {
        rank = same;
        interface_0_out_0x56459a9d6050;
        interface_0_out_0x56459a9d6078;
        interface_0_out_0x56459a9d60a0;
        interface_0_out_0x56459a9d60c8;
    }
    // Input 0.
    subgraph cluster_subgraph_0_in_0 {
        label = "";
        interface_0_in_0x56459a9d6050 [label="N", shape=none];
        interface_0_in_0x56459c25a880 [label="s", shape=none];
        interface_0_in_0x56459c25a898 [label="s^-1*C_out", shape=none];
        interface_0_in_0x56459a9d60a0 [label="H", shape=none];
        interface_0_in_0x56459c259050 [label="H", shape=none];
    }
    {
        rank = same;
        interface_0_in_0x56459a9d6050;
        interface_0_in_0x56459c25a880;
        interface_0_in_0x56459c25a898;
        interface_0_in_0x56459a9d60a0;
        interface_0_in_0x56459c259050;
    }
    // Op's.
    op_0x56459c259030 [label="Shift"];
    op_0x56459c25a840 [label="Merge"];
    // Dimension's.
    interface_0_in_0x56459a9d6050 -> interface_0_out_0x56459a9d6050 [label="N"];
    op_0x56459c25a840 -> interface_0_out_0x56459a9d6078 [label="C_out"];
    interface_0_in_0x56459a9d60a0 -> interface_0_out_0x56459a9d60a0 [label="H"];
    op_0x56459c259030 -> interface_0_out_0x56459a9d60c8 [label="H"];
    interface_0_in_0x56459c259050 -> op_0x56459c259030 [label="H"];
    interface_0_in_0x56459c25a880 -> op_0x56459c25a840 [label="s"];
    interface_0_in_0x56459c25a898 -> op_0x56459c25a840 [label="s^-1*C_out"];
}

// Stage tensor.
subgraph cluster_subgraph_1 {
    label = "Subgraph 1";
    // Reductions.
    reduce_0x7fdbac001ee8 [label="Sum", shape=box];
    reduce_0x7fdbac001cc0 [label="Sum", shape=box];
    // Output.
    subgraph cluster_subgraph_1_out {
        label = "";
        interface_1_out_0x56459a9d6050 [label="N", shape=none];
        interface_1_out_0x56459c25a880 [label="s", shape=none];
        interface_1_out_0x56459c25a898 [label="s^-1*C_out", shape=none];
        interface_1_out_0x56459a9d60a0 [label="H", shape=none];
        interface_1_out_0x56459c259050 [label="H", shape=none];
    }
    {
        rank = same;
        reduce_0x7fdbac001ee8;
        reduce_0x7fdbac001cc0;
        interface_1_out_0x56459a9d6050;
        interface_1_out_0x56459c25a880;
        interface_1_out_0x56459c25a898;
        interface_1_out_0x56459a9d60a0;
        interface_1_out_0x56459c259050;
    }
    // Input 0.
    subgraph cluster_subgraph_1_in_0 {
        label = "";
        interface_1_in_0x56459a9d6050 [label="N", shape=none];
        interface_1_in_0x56459c25a880 [label="s", shape=none];
        interface_1_in_0x56459c258340 [label="k_2", shape=none];
        interface_1_in_0x56459a9d60a0 [label="H", shape=none];
        interface_1_in_0x56459c259050 [label="H", shape=none];
        interface_1_in_0x56459c258390 [label="k_1^2", shape=none];
    }
    // Input 1.
    subgraph cluster_subgraph_1_in_1 {
        label = "";
        interface_1_in_0x56459c2583f8 [label="s^-1*C_out", shape=none];
        interface_1_in_0x56459c258358 [label="k_2", shape=none];
        interface_1_in_0x56459c2583a8 [label="k_1^2", shape=none];
    }
    {
        rank = same;
        interface_1_in_0x56459a9d6050;
        interface_1_in_0x56459c25a880;
        interface_1_in_0x56459c258340;
        interface_1_in_0x56459a9d60a0;
        interface_1_in_0x56459c259050;
        interface_1_in_0x56459c258390;
        interface_1_in_0x56459c2583f8;
        interface_1_in_0x56459c258358;
        interface_1_in_0x56459c2583a8;
    }
    // Op's.
    op_0x56459c258320 [label="Share"];
    op_0x56459c258370 [label="Share"];
    op_0x56459c2583c0 [label="Share"];
    op_0x56459c258798 [label="Expand"];
    // Dimension's.
    interface_1_in_0x56459a9d6050 -> interface_1_out_0x56459a9d6050 [label="N"];
    interface_1_in_0x56459a9d60a0 -> interface_1_out_0x56459a9d60a0 [label="H"];
    interface_1_in_0x56459c258340 -> op_0x56459c258320 [label="k_2"];
    interface_1_in_0x56459c258358 -> op_0x56459c258320 [label="k_2"];
    interface_1_in_0x56459c258390 -> op_0x56459c258370 [label="k_1^2"];
    interface_1_in_0x56459c2583a8 -> op_0x56459c258370 [label="k_1^2"];
    op_0x56459c258798 -> op_0x56459c2583c0 [label="s^-1*C_out"];
    interface_1_in_0x56459c2583f8 -> op_0x56459c2583c0 [label="s^-1*C_out"];
    interface_1_in_0x56459c259050 -> interface_1_out_0x56459c259050 [label="H"];
    interface_1_in_0x56459c25a880 -> interface_1_out_0x56459c25a880 [label="s"];
    op_0x56459c2583c0 -> interface_1_out_0x56459c25a898 [label="s^-1*C_out"];
    op_0x56459c258370 -> reduce_0x7fdbac001cc0 [label="k_1^2"];
    op_0x56459c258320 -> reduce_0x7fdbac001ee8 [label="k_2"];
}

// Stage tensor.
subgraph cluster_subgraph_2 {
    label = "Subgraph 2";
    // Reductions.
    // Output.
    subgraph cluster_subgraph_2_out {
        label = "";
        interface_2_out_0x56459a9d6050 [label="N", shape=none];
        interface_2_out_0x56459c25a880 [label="s", shape=none];
        interface_2_out_0x56459c258340 [label="k_2", shape=none];
        interface_2_out_0x56459a9d60a0 [label="H", shape=none];
        interface_2_out_0x56459c259050 [label="H", shape=none];
        interface_2_out_0x56459c258390 [label="k_1^2", shape=none];
    }
    {
        rank = same;
        interface_2_out_0x56459a9d6050;
        interface_2_out_0x56459c25a880;
        interface_2_out_0x56459c258340;
        interface_2_out_0x56459a9d60a0;
        interface_2_out_0x56459c259050;
        interface_2_out_0x56459c258390;
    }
    // Input 0.
    subgraph cluster_subgraph_2_in_0 {
        label = "";
        interface_2_in_0x56459a9d6050 [label="N", shape=none];
        interface_2_in_0x56459c25a880 [label="s", shape=none];
        interface_2_in_0x56459c2592c0 [label="H", shape=none];
        interface_2_in_0x56459c259050 [label="H", shape=none];
        interface_2_in_0x56459c258390 [label="k_1^2", shape=none];
    }
    {
        rank = same;
        interface_2_in_0x56459a9d6050;
        interface_2_in_0x56459c25a880;
        interface_2_in_0x56459c2592c0;
        interface_2_in_0x56459c259050;
        interface_2_in_0x56459c258390;
    }
    // Op's.
    op_0x56459c2592a0 [label="Shift"];
    op_0x56459c25c880 [label="Unfold"];
    // Dimension's.
    interface_2_in_0x56459a9d6050 -> interface_2_out_0x56459a9d6050 [label="N"];
    op_0x56459c25c880 -> interface_2_out_0x56459a9d60a0 [label="H"];
    op_0x56459c25c880 -> interface_2_out_0x56459c258340 [label="k_2"];
    interface_2_in_0x56459c258390 -> interface_2_out_0x56459c258390 [label="k_1^2"];
    interface_2_in_0x56459c259050 -> interface_2_out_0x56459c259050 [label="H"];
    interface_2_in_0x56459c2592c0 -> op_0x56459c2592a0 [label="H"];
    interface_2_in_0x56459c25a880 -> interface_2_out_0x56459c25a880 [label="s"];
    op_0x56459c2592a0 -> op_0x56459c25c880 [label="H"];
}

// Stage tensor.
subgraph cluster_subgraph_3 {
    label = "Subgraph 3";
    // Reductions.
    reduce_0x7fdbac005768 [label="Sum", shape=box];
    // Output.
    subgraph cluster_subgraph_3_out {
        label = "";
        interface_3_out_0x56459a9d6050 [label="N", shape=none];
        interface_3_out_0x56459c25a880 [label="s", shape=none];
        interface_3_out_0x56459c2592c0 [label="H", shape=none];
        interface_3_out_0x56459c259050 [label="H", shape=none];
        interface_3_out_0x56459c258390 [label="k_1^2", shape=none];
    }
    {
        rank = same;
        reduce_0x7fdbac005768;
        interface_3_out_0x56459a9d6050;
        interface_3_out_0x56459c25a880;
        interface_3_out_0x56459c2592c0;
        interface_3_out_0x56459c259050;
        interface_3_out_0x56459c258390;
    }
    // Input 0.
    subgraph cluster_subgraph_3_in_0 {
        label = "";
        interface_3_in_0x56459a9d6050 [label="N", shape=none];
        interface_3_in_0x56459c25a880 [label="s", shape=none];
        interface_3_in_0x56459c2584d0 [label="s^-1*C_in", shape=none];
        interface_3_in_0x56459c2592c0 [label="H", shape=none];
        interface_3_in_0x56459c259050 [label="H", shape=none];
    }
    // Input 1.
    subgraph cluster_subgraph_3_in_1 {
        label = "";
        interface_3_in_0x56459c2584e8 [label="s^-1*C_in", shape=none];
        interface_3_in_0x56459c258498 [label="k_1^2", shape=none];
    }
    {
        rank = same;
        interface_3_in_0x56459a9d6050;
        interface_3_in_0x56459c25a880;
        interface_3_in_0x56459c2584d0;
        interface_3_in_0x56459c2592c0;
        interface_3_in_0x56459c259050;
        interface_3_in_0x56459c2584e8;
        interface_3_in_0x56459c258498;
    }
    // Op's.
    op_0x56459c258460 [label="Share"];
    op_0x56459c2584b0 [label="Share"];
    op_0x56459c2587d8 [label="Expand"];
    // Dimension's.
    interface_3_in_0x56459a9d6050 -> interface_3_out_0x56459a9d6050 [label="N"];
    op_0x56459c258460 -> interface_3_out_0x56459c258390 [label="k_1^2"];
    op_0x56459c2587d8 -> op_0x56459c258460 [label="k_1^2"];
    interface_3_in_0x56459c258498 -> op_0x56459c258460 [label="k_1^2"];
    interface_3_in_0x56459c2584d0 -> op_0x56459c2584b0 [label="s^-1*C_in"];
    interface_3_in_0x56459c2584e8 -> op_0x56459c2584b0 [label="s^-1*C_in"];
    interface_3_in_0x56459c259050 -> interface_3_out_0x56459c259050 [label="H"];
    interface_3_in_0x56459c2592c0 -> interface_3_out_0x56459c2592c0 [label="H"];
    interface_3_in_0x56459c25a880 -> interface_3_out_0x56459c25a880 [label="s"];
    op_0x56459c2584b0 -> reduce_0x7fdbac005768 [label="s^-1*C_in"];
}

// Stage tensor.
subgraph cluster_subgraph_4 {
    label = "Subgraph 4";
    // Reductions.
    // Output.
    subgraph cluster_subgraph_4_out {
        label = "";
        interface_4_out_0x56459a9d6050 [label="N", shape=none];
        interface_4_out_0x56459c25a880 [label="s", shape=none];
        interface_4_out_0x56459c2584d0 [label="s^-1*C_in", shape=none];
        interface_4_out_0x56459c2592c0 [label="H", shape=none];
        interface_4_out_0x56459c259050 [label="H", shape=none];
    }
    {
        rank = same;
        interface_4_out_0x56459a9d6050;
        interface_4_out_0x56459c25a880;
        interface_4_out_0x56459c2584d0;
        interface_4_out_0x56459c2592c0;
        interface_4_out_0x56459c259050;
    }
    // Input 0.
    subgraph cluster_subgraph_4_in_0 {
        label = "";
        interface_4_in_0x56459a9d6050 [label="N", shape=none];
        interface_4_in_0x56459c25b9c0 [label="C_in", shape=none];
        interface_4_in_0x56459c2592c0 [label="H", shape=none];
        interface_4_in_0x56459c259050 [label="H", shape=none];
    }
    {
        rank = same;
        interface_4_in_0x56459a9d6050;
        interface_4_in_0x56459c25b9c0;
        interface_4_in_0x56459c2592c0;
        interface_4_in_0x56459c259050;
    }
    // Op's.
    op_0x56459c25b980 [label="Split"];
    // Dimension's.
    interface_4_in_0x56459a9d6050 -> interface_4_out_0x56459a9d6050 [label="N"];
    op_0x56459c25b980 -> interface_4_out_0x56459c2584d0 [label="s^-1*C_in"];
    interface_4_in_0x56459c259050 -> interface_4_out_0x56459c259050 [label="H"];
    interface_4_in_0x56459c2592c0 -> interface_4_out_0x56459c2592c0 [label="H"];
    op_0x56459c25b980 -> interface_4_out_0x56459c25a880 [label="s"];
    interface_4_in_0x56459c25b9c0 -> op_0x56459c25b980 [label="C_in"];
}

// Input tensor.
subgraph cluster_subgraph_5 {
    label = "Input 0";
    interface_5_out_0x56459a9d6050 [label="N", shape=none];
    interface_5_out_0x56459c25b9c0 [label="C_in", shape=none];
    interface_5_out_0x56459c2592c0 [label="H", shape=none];
    interface_5_out_0x56459c259050 [label="H", shape=none];
}

interface_5_out_0x56459a9d6050 -> interface_4_in_0x56459a9d6050;
interface_5_out_0x56459c25b9c0 -> interface_4_in_0x56459c25b9c0;
interface_5_out_0x56459c2592c0 -> interface_4_in_0x56459c2592c0;
interface_5_out_0x56459c259050 -> interface_4_in_0x56459c259050;

interface_4_out_0x56459a9d6050 -> interface_3_in_0x56459a9d6050;
interface_4_out_0x56459c25a880 -> interface_3_in_0x56459c25a880;
interface_4_out_0x56459c2584d0 -> interface_3_in_0x56459c2584d0;
interface_4_out_0x56459c2592c0 -> interface_3_in_0x56459c2592c0;
interface_4_out_0x56459c259050 -> interface_3_in_0x56459c259050;

// Input tensor.
subgraph cluster_subgraph_6 {
    label = "Input 2";
    interface_6_out_0x56459c2584e8 [label="s^-1*C_in", shape=none];
    interface_6_out_0x56459c258498 [label="k_1^2", shape=none];
}

interface_6_out_0x56459c2584e8 -> interface_3_in_0x56459c2584e8;
interface_6_out_0x56459c258498 -> interface_3_in_0x56459c258498;

interface_3_out_0x56459a9d6050 -> interface_2_in_0x56459a9d6050;
interface_3_out_0x56459c25a880 -> interface_2_in_0x56459c25a880;
interface_3_out_0x56459c2592c0 -> interface_2_in_0x56459c2592c0;
interface_3_out_0x56459c259050 -> interface_2_in_0x56459c259050;
interface_3_out_0x56459c258390 -> interface_2_in_0x56459c258390;

interface_2_out_0x56459a9d6050 -> interface_1_in_0x56459a9d6050;
interface_2_out_0x56459c25a880 -> interface_1_in_0x56459c25a880;
interface_2_out_0x56459c258340 -> interface_1_in_0x56459c258340;
interface_2_out_0x56459a9d60a0 -> interface_1_in_0x56459a9d60a0;
interface_2_out_0x56459c259050 -> interface_1_in_0x56459c259050;
interface_2_out_0x56459c258390 -> interface_1_in_0x56459c258390;

// Input tensor.
subgraph cluster_subgraph_7 {
    label = "Input 1";
    interface_7_out_0x56459c2583f8 [label="s^-1*C_out", shape=none];
    interface_7_out_0x56459c258358 [label="k_2", shape=none];
    interface_7_out_0x56459c2583a8 [label="k_1^2", shape=none];
}

interface_7_out_0x56459c2583f8 -> interface_1_in_0x56459c2583f8;
interface_7_out_0x56459c258358 -> interface_1_in_0x56459c258358;
interface_7_out_0x56459c2583a8 -> interface_1_in_0x56459c2583a8;

interface_1_out_0x56459a9d6050 -> interface_0_in_0x56459a9d6050;
interface_1_out_0x56459c25a880 -> interface_0_in_0x56459c25a880;
interface_1_out_0x56459c25a898 -> interface_0_in_0x56459c25a898;
interface_1_out_0x56459a9d60a0 -> interface_0_in_0x56459a9d60a0;
interface_1_out_0x56459c259050 -> interface_0_in_0x56459c259050;

{
    rank = same;
    interface_5_out_0x56459a9d6050;
    interface_5_out_0x56459c25b9c0;
    interface_5_out_0x56459c2592c0;
    interface_5_out_0x56459c259050;
    interface_7_out_0x56459c2583f8;
    interface_7_out_0x56459c258358;
    interface_7_out_0x56459c2583a8;
    interface_6_out_0x56459c2584e8;
    interface_6_out_0x56459c258498;
}
subgraph cluster_subgraph_output {
    label = "Output";
    interface_8_in_0x56459a9d6050 [label="N", shape=none];
    interface_8_in_0x56459a9d6078 [label="C_out", shape=none];
    interface_8_in_0x56459a9d60a0 [label="H", shape=none];
    interface_8_in_0x56459a9d60c8 [label="H", shape=none];
}
interface_0_out_0x56459a9d6050 -> interface_8_in_0x56459a9d6050;
interface_0_out_0x56459a9d6078 -> interface_8_in_0x56459a9d6078;
interface_0_out_0x56459a9d60a0 -> interface_8_in_0x56459a9d60a0;
interface_0_out_0x56459a9d60c8 -> interface_8_in_0x56459a9d60c8;

}

"""
class kernel_generated_0(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([12, 7, 9]),
			torch.randn([12, 9]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]
		in_2 = self.weights[1]

		# No contraction needed.
		t_3 = in_0

		# [C_in]@Split69dd43e0c9ec9c4b -> [s]@Merge03a73148aa81036c, [s^-1*C_in]@Share010730f7adbbf8aa
		t_3 = torch.reshape(t_3, (1, 2, 12, 112, 112, ))

		# Perform contraction.
		t_4 = torch.einsum("knjml, ji -> knmli", t_3, in_2)

		# No contraction needed.
		t_5 = t_4

		# [H]@Shift55a06fa4f7c5d730 -> [H]@Unfold820e0f3eb05a896f
		t_5 = torch.roll(t_5, self.shift_direction, 2)

		# [H]@Unfold820e0f3eb05a896f -> [H]@Iterator96123ba3184da39c, [k_2]@Sharec0d065a85569cbbe
		t_5 = torch.reshape(t_5, (1, 2, 112, 1008, ))
		t_5 = torch.nn.functional.unfold(t_5, (7, 1, ), padding=(3, 0, ))
		t_5 = torch.reshape(t_5, (1, 2, 7, 112, 112, 9, ))

		# Perform contraction.
		t_6 = torch.einsum("loimnj, kij -> lokmn", t_5, in_1)

		# No contraction needed.
		t_7 = t_6

		# [s]@Merge03a73148aa81036c, [s^-1*C_out]@Merge03a73148aa81036f -> [C_out]@Iteratorc7f8eb87a5a0a9e0
		t_7 = torch.reshape(t_7, (1, 24, 112, 112, ))

		# [H]@Shift6b179c72f0c6dbad -> [H]@Iteratorb0a1def4ad5784ec
		t_7 = torch.roll(t_7, self.shift_direction, 3)

		# No need to crop the output tensor.
		y = t_7

		return y

class kernel_generated_1(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([48, 7, 9]),
			torch.randn([12, 9]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]
		in_2 = self.weights[1]

		# No contraction needed.
		t_3 = in_0

		# [C_in]@Split69dd43e0c9ec9c4b -> [s]@Merge03a73148aa81036c, [s^-1*C_in]@Share010730f7adbbf8aa
		t_3 = torch.reshape(t_3, (1, 2, 12, 56, 56, ))

		# Perform contraction.
		t_4 = torch.einsum("knjml, ji -> knmli", t_3, in_2)

		# No contraction needed.
		t_5 = t_4

		# [H]@Shift55a06fa4f7c5d730 -> [H]@Unfold820e0f3eb05a896f
		t_5 = torch.roll(t_5, self.shift_direction, 2)

		# [H]@Unfold820e0f3eb05a896f -> [H]@Iterator96123ba3184da39c, [k_2]@Sharec0d065a85569cbbe
		t_5 = torch.reshape(t_5, (1, 2, 56, 504, ))
		t_5 = torch.nn.functional.unfold(t_5, (7, 1, ), padding=(3, 0, ))
		t_5 = torch.reshape(t_5, (1, 2, 7, 56, 56, 9, ))

		# Perform contraction.
		t_6 = torch.einsum("loimnj, kij -> lokmn", t_5, in_1)

		# No contraction needed.
		t_7 = t_6

		# [s]@Merge03a73148aa81036c, [s^-1*C_out]@Merge03a73148aa81036f -> [C_out]@Iteratorc7f8eb87a5a0a9e0
		t_7 = torch.reshape(t_7, (1, 96, 56, 56, ))

		# [H]@Shift6b179c72f0c6dbad -> [H]@Iteratorb0a1def4ad5784ec
		t_7 = torch.roll(t_7, self.shift_direction, 3)

		# No need to crop the output tensor.
		y = t_7

		return y

class kernel_generated_2(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([96, 7, 9]),
			torch.randn([24, 9]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]
		in_2 = self.weights[1]

		# No contraction needed.
		t_3 = in_0

		# [C_in]@Split69dd43e0c9ec9c4b -> [s]@Merge03a73148aa81036c, [s^-1*C_in]@Share010730f7adbbf8aa
		t_3 = torch.reshape(t_3, (1, 2, 24, 56, 56, ))

		# Perform contraction.
		t_4 = torch.einsum("knjml, ji -> knmli", t_3, in_2)

		# No contraction needed.
		t_5 = t_4

		# [H]@Shift55a06fa4f7c5d730 -> [H]@Unfold820e0f3eb05a896f
		t_5 = torch.roll(t_5, self.shift_direction, 2)

		# [H]@Unfold820e0f3eb05a896f -> [H]@Iterator96123ba3184da39c, [k_2]@Sharec0d065a85569cbbe
		t_5 = torch.reshape(t_5, (1, 2, 56, 504, ))
		t_5 = torch.nn.functional.unfold(t_5, (7, 1, ), padding=(3, 0, ))
		t_5 = torch.reshape(t_5, (1, 2, 7, 56, 56, 9, ))

		# Perform contraction.
		t_6 = torch.einsum("loimnj, kij -> lokmn", t_5, in_1)

		# No contraction needed.
		t_7 = t_6

		# [s]@Merge03a73148aa81036c, [s^-1*C_out]@Merge03a73148aa81036f -> [C_out]@Iteratorc7f8eb87a5a0a9e0
		t_7 = torch.reshape(t_7, (1, 192, 56, 56, ))

		# [H]@Shift6b179c72f0c6dbad -> [H]@Iteratorb0a1def4ad5784ec
		t_7 = torch.roll(t_7, self.shift_direction, 3)

		# No need to crop the output tensor.
		y = t_7

		return y

class kernel_generated_3(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([96, 7, 9]),
			torch.randn([24, 9]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]
		in_2 = self.weights[1]

		# No contraction needed.
		t_3 = in_0

		# [C_in]@Split69dd43e0c9ec9c4b -> [s]@Merge03a73148aa81036c, [s^-1*C_in]@Share010730f7adbbf8aa
		t_3 = torch.reshape(t_3, (1, 2, 24, 28, 28, ))

		# Perform contraction.
		t_4 = torch.einsum("knjml, ji -> knmli", t_3, in_2)

		# No contraction needed.
		t_5 = t_4

		# [H]@Shift55a06fa4f7c5d730 -> [H]@Unfold820e0f3eb05a896f
		t_5 = torch.roll(t_5, self.shift_direction, 2)

		# [H]@Unfold820e0f3eb05a896f -> [H]@Iterator96123ba3184da39c, [k_2]@Sharec0d065a85569cbbe
		t_5 = torch.reshape(t_5, (1, 2, 28, 252, ))
		t_5 = torch.nn.functional.unfold(t_5, (7, 1, ), padding=(3, 0, ))
		t_5 = torch.reshape(t_5, (1, 2, 7, 28, 28, 9, ))

		# Perform contraction.
		t_6 = torch.einsum("loimnj, kij -> lokmn", t_5, in_1)

		# No contraction needed.
		t_7 = t_6

		# [s]@Merge03a73148aa81036c, [s^-1*C_out]@Merge03a73148aa81036f -> [C_out]@Iteratorc7f8eb87a5a0a9e0
		t_7 = torch.reshape(t_7, (1, 192, 28, 28, ))

		# [H]@Shift6b179c72f0c6dbad -> [H]@Iteratorb0a1def4ad5784ec
		t_7 = torch.roll(t_7, self.shift_direction, 3)

		# No need to crop the output tensor.
		y = t_7

		return y

class kernel_generated_4(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([128, 7, 9]),
			torch.randn([32, 9]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]
		in_2 = self.weights[1]

		# No contraction needed.
		t_3 = in_0

		# [C_in]@Split69dd43e0c9ec9c4b -> [s]@Merge03a73148aa81036c, [s^-1*C_in]@Share010730f7adbbf8aa
		t_3 = torch.reshape(t_3, (1, 2, 32, 28, 28, ))

		# Perform contraction.
		t_4 = torch.einsum("knjml, ji -> knmli", t_3, in_2)

		# No contraction needed.
		t_5 = t_4

		# [H]@Shift55a06fa4f7c5d730 -> [H]@Unfold820e0f3eb05a896f
		t_5 = torch.roll(t_5, self.shift_direction, 2)

		# [H]@Unfold820e0f3eb05a896f -> [H]@Iterator96123ba3184da39c, [k_2]@Sharec0d065a85569cbbe
		t_5 = torch.reshape(t_5, (1, 2, 28, 252, ))
		t_5 = torch.nn.functional.unfold(t_5, (7, 1, ), padding=(3, 0, ))
		t_5 = torch.reshape(t_5, (1, 2, 7, 28, 28, 9, ))

		# Perform contraction.
		t_6 = torch.einsum("loimnj, kij -> lokmn", t_5, in_1)

		# No contraction needed.
		t_7 = t_6

		# [s]@Merge03a73148aa81036c, [s^-1*C_out]@Merge03a73148aa81036f -> [C_out]@Iteratorc7f8eb87a5a0a9e0
		t_7 = torch.reshape(t_7, (1, 256, 28, 28, ))

		# [H]@Shift6b179c72f0c6dbad -> [H]@Iteratorb0a1def4ad5784ec
		t_7 = torch.roll(t_7, self.shift_direction, 3)

		# No need to crop the output tensor.
		y = t_7

		return y

