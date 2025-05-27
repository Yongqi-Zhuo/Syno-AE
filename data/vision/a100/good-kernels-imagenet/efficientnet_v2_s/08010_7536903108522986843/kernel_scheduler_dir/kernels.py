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
        interface_0_in_0x56459c259020 [label="H", shape=none];
        interface_0_in_0x56459a9d60c8 [label="H", shape=none];
    }
    {
        rank = same;
        interface_0_in_0x56459a9d6050;
        interface_0_in_0x56459c25a880;
        interface_0_in_0x56459c25a898;
        interface_0_in_0x56459c259020;
        interface_0_in_0x56459a9d60c8;
    }
    // Op's.
    op_0x56459c259000 [label="Shift"];
    op_0x56459c25a840 [label="Merge"];
    // Dimension's.
    interface_0_in_0x56459a9d6050 -> interface_0_out_0x56459a9d6050 [label="N"];
    op_0x56459c25a840 -> interface_0_out_0x56459a9d6078 [label="C_out"];
    op_0x56459c259000 -> interface_0_out_0x56459a9d60a0 [label="H"];
    interface_0_in_0x56459a9d60c8 -> interface_0_out_0x56459a9d60c8 [label="H"];
    interface_0_in_0x56459c259020 -> op_0x56459c259000 [label="H"];
    interface_0_in_0x56459c25a880 -> op_0x56459c25a840 [label="s"];
    interface_0_in_0x56459c25a898 -> op_0x56459c25a840 [label="s^-1*C_out"];
}

// Stage tensor.
subgraph cluster_subgraph_1 {
    label = "Subgraph 1";
    // Reductions.
    reduce_0x7fdbac001cc0 [label="Sum", shape=box];
    // Output.
    subgraph cluster_subgraph_1_out {
        label = "";
        interface_1_out_0x56459a9d6050 [label="N", shape=none];
        interface_1_out_0x56459c25a880 [label="s", shape=none];
        interface_1_out_0x56459c25a898 [label="s^-1*C_out", shape=none];
        interface_1_out_0x56459c259020 [label="H", shape=none];
        interface_1_out_0x56459a9d60c8 [label="H", shape=none];
    }
    {
        rank = same;
        reduce_0x7fdbac001cc0;
        interface_1_out_0x56459a9d6050;
        interface_1_out_0x56459c25a880;
        interface_1_out_0x56459c25a898;
        interface_1_out_0x56459c259020;
        interface_1_out_0x56459a9d60c8;
    }
    // Input 0.
    subgraph cluster_subgraph_1_in_0 {
        label = "";
        interface_1_in_0x56459a9d6050 [label="N", shape=none];
        interface_1_in_0x56459c25a880 [label="s", shape=none];
        interface_1_in_0x56459c259020 [label="H", shape=none];
        interface_1_in_0x56459a9d60c8 [label="H", shape=none];
        interface_1_in_0x56459c258390 [label="k_1^2", shape=none];
    }
    // Input 1.
    subgraph cluster_subgraph_1_in_1 {
        label = "";
        interface_1_in_0x56459c2583f8 [label="s^-1*C_out", shape=none];
        interface_1_in_0x56459c2583a8 [label="k_1^2", shape=none];
    }
    {
        rank = same;
        interface_1_in_0x56459a9d6050;
        interface_1_in_0x56459c25a880;
        interface_1_in_0x56459c259020;
        interface_1_in_0x56459a9d60c8;
        interface_1_in_0x56459c258390;
        interface_1_in_0x56459c2583f8;
        interface_1_in_0x56459c2583a8;
    }
    // Op's.
    op_0x56459c258370 [label="Share"];
    op_0x56459c2583c0 [label="Share"];
    op_0x56459c258798 [label="Expand"];
    // Dimension's.
    interface_1_in_0x56459a9d6050 -> interface_1_out_0x56459a9d6050 [label="N"];
    interface_1_in_0x56459a9d60c8 -> interface_1_out_0x56459a9d60c8 [label="H"];
    interface_1_in_0x56459c258390 -> op_0x56459c258370 [label="k_1^2"];
    interface_1_in_0x56459c2583a8 -> op_0x56459c258370 [label="k_1^2"];
    op_0x56459c258798 -> op_0x56459c2583c0 [label="s^-1*C_out"];
    interface_1_in_0x56459c2583f8 -> op_0x56459c2583c0 [label="s^-1*C_out"];
    interface_1_in_0x56459c259020 -> interface_1_out_0x56459c259020 [label="H"];
    interface_1_in_0x56459c25a880 -> interface_1_out_0x56459c25a880 [label="s"];
    op_0x56459c2583c0 -> interface_1_out_0x56459c25a898 [label="s^-1*C_out"];
    op_0x56459c258370 -> reduce_0x7fdbac001cc0 [label="k_1^2"];
}

// Stage tensor.
subgraph cluster_subgraph_2 {
    label = "Subgraph 2";
    // Reductions.
    reduce_0x7fdbac005768 [label="Sum", shape=box];
    reduce_0x7fdbac001ee8 [label="Sum", shape=box];
    // Output.
    subgraph cluster_subgraph_2_out {
        label = "";
        interface_2_out_0x56459a9d6050 [label="N", shape=none];
        interface_2_out_0x56459c25a880 [label="s", shape=none];
        interface_2_out_0x56459c259020 [label="H", shape=none];
        interface_2_out_0x56459a9d60c8 [label="H", shape=none];
        interface_2_out_0x56459c258390 [label="k_1^2", shape=none];
    }
    {
        rank = same;
        reduce_0x7fdbac005768;
        reduce_0x7fdbac001ee8;
        interface_2_out_0x56459a9d6050;
        interface_2_out_0x56459c25a880;
        interface_2_out_0x56459c259020;
        interface_2_out_0x56459a9d60c8;
        interface_2_out_0x56459c258390;
    }
    // Input 0.
    subgraph cluster_subgraph_2_in_0 {
        label = "";
        interface_2_in_0x56459a9d6050 [label="N", shape=none];
        interface_2_in_0x56459c25a880 [label="s", shape=none];
        interface_2_in_0x56459c2584d0 [label="s^-1*C_in", shape=none];
        interface_2_in_0x56459c259020 [label="H", shape=none];
        interface_2_in_0x56459c258520 [label="k_2", shape=none];
        interface_2_in_0x56459a9d60c8 [label="H", shape=none];
    }
    // Input 1.
    subgraph cluster_subgraph_2_in_1 {
        label = "";
        interface_2_in_0x56459c2584e8 [label="s^-1*C_in", shape=none];
        interface_2_in_0x56459c258538 [label="k_2", shape=none];
        interface_2_in_0x56459c258498 [label="k_1^2", shape=none];
    }
    {
        rank = same;
        interface_2_in_0x56459a9d6050;
        interface_2_in_0x56459c25a880;
        interface_2_in_0x56459c2584d0;
        interface_2_in_0x56459c259020;
        interface_2_in_0x56459c258520;
        interface_2_in_0x56459a9d60c8;
        interface_2_in_0x56459c2584e8;
        interface_2_in_0x56459c258538;
        interface_2_in_0x56459c258498;
    }
    // Op's.
    op_0x56459c258460 [label="Share"];
    op_0x56459c2584b0 [label="Share"];
    op_0x56459c258500 [label="Share"];
    op_0x56459c2587d8 [label="Expand"];
    // Dimension's.
    interface_2_in_0x56459a9d6050 -> interface_2_out_0x56459a9d6050 [label="N"];
    interface_2_in_0x56459a9d60c8 -> interface_2_out_0x56459a9d60c8 [label="H"];
    op_0x56459c258460 -> interface_2_out_0x56459c258390 [label="k_1^2"];
    op_0x56459c2587d8 -> op_0x56459c258460 [label="k_1^2"];
    interface_2_in_0x56459c258498 -> op_0x56459c258460 [label="k_1^2"];
    interface_2_in_0x56459c2584d0 -> op_0x56459c2584b0 [label="s^-1*C_in"];
    interface_2_in_0x56459c2584e8 -> op_0x56459c2584b0 [label="s^-1*C_in"];
    interface_2_in_0x56459c258520 -> op_0x56459c258500 [label="k_2"];
    interface_2_in_0x56459c258538 -> op_0x56459c258500 [label="k_2"];
    interface_2_in_0x56459c259020 -> interface_2_out_0x56459c259020 [label="H"];
    interface_2_in_0x56459c25a880 -> interface_2_out_0x56459c25a880 [label="s"];
    op_0x56459c258500 -> reduce_0x7fdbac001ee8 [label="k_2"];
    op_0x56459c2584b0 -> reduce_0x7fdbac005768 [label="s^-1*C_in"];
}

// Stage tensor.
subgraph cluster_subgraph_3 {
    label = "Subgraph 3";
    // Reductions.
    // Output.
    subgraph cluster_subgraph_3_out {
        label = "";
        interface_3_out_0x56459a9d6050 [label="N", shape=none];
        interface_3_out_0x56459c25a880 [label="s", shape=none];
        interface_3_out_0x56459c2584d0 [label="s^-1*C_in", shape=none];
        interface_3_out_0x56459c259020 [label="H", shape=none];
        interface_3_out_0x56459c258520 [label="k_2", shape=none];
        interface_3_out_0x56459a9d60c8 [label="H", shape=none];
    }
    {
        rank = same;
        interface_3_out_0x56459a9d6050;
        interface_3_out_0x56459c25a880;
        interface_3_out_0x56459c2584d0;
        interface_3_out_0x56459c259020;
        interface_3_out_0x56459c258520;
        interface_3_out_0x56459a9d60c8;
    }
    // Input 0.
    subgraph cluster_subgraph_3_in_0 {
        label = "";
        interface_3_in_0x56459a9d6050 [label="N", shape=none];
        interface_3_in_0x56459c25b9c0 [label="C_in", shape=none];
        interface_3_in_0x56459c259020 [label="H", shape=none];
        interface_3_in_0x56459c25c5a8 [label="H", shape=none];
    }
    {
        rank = same;
        interface_3_in_0x56459a9d6050;
        interface_3_in_0x56459c25b9c0;
        interface_3_in_0x56459c259020;
        interface_3_in_0x56459c25c5a8;
    }
    // Op's.
    op_0x56459c25b980 [label="Split"];
    op_0x56459c25c580 [label="Unfold"];
    // Dimension's.
    interface_3_in_0x56459a9d6050 -> interface_3_out_0x56459a9d6050 [label="N"];
    op_0x56459c25c580 -> interface_3_out_0x56459a9d60c8 [label="H"];
    op_0x56459c25b980 -> interface_3_out_0x56459c2584d0 [label="s^-1*C_in"];
    op_0x56459c25c580 -> interface_3_out_0x56459c258520 [label="k_2"];
    interface_3_in_0x56459c259020 -> interface_3_out_0x56459c259020 [label="H"];
    op_0x56459c25b980 -> interface_3_out_0x56459c25a880 [label="s"];
    interface_3_in_0x56459c25b9c0 -> op_0x56459c25b980 [label="C_in"];
    interface_3_in_0x56459c25c5a8 -> op_0x56459c25c580 [label="H"];
}

// Input tensor.
subgraph cluster_subgraph_4 {
    label = "Input 0";
    interface_4_out_0x56459a9d6050 [label="N", shape=none];
    interface_4_out_0x56459c25b9c0 [label="C_in", shape=none];
    interface_4_out_0x56459c259020 [label="H", shape=none];
    interface_4_out_0x56459c25c5a8 [label="H", shape=none];
}

interface_4_out_0x56459a9d6050 -> interface_3_in_0x56459a9d6050;
interface_4_out_0x56459c25b9c0 -> interface_3_in_0x56459c25b9c0;
interface_4_out_0x56459c259020 -> interface_3_in_0x56459c259020;
interface_4_out_0x56459c25c5a8 -> interface_3_in_0x56459c25c5a8;

interface_3_out_0x56459a9d6050 -> interface_2_in_0x56459a9d6050;
interface_3_out_0x56459c25a880 -> interface_2_in_0x56459c25a880;
interface_3_out_0x56459c2584d0 -> interface_2_in_0x56459c2584d0;
interface_3_out_0x56459c259020 -> interface_2_in_0x56459c259020;
interface_3_out_0x56459c258520 -> interface_2_in_0x56459c258520;
interface_3_out_0x56459a9d60c8 -> interface_2_in_0x56459a9d60c8;

// Input tensor.
subgraph cluster_subgraph_5 {
    label = "Input 2";
    interface_5_out_0x56459c2584e8 [label="s^-1*C_in", shape=none];
    interface_5_out_0x56459c258538 [label="k_2", shape=none];
    interface_5_out_0x56459c258498 [label="k_1^2", shape=none];
}

interface_5_out_0x56459c2584e8 -> interface_2_in_0x56459c2584e8;
interface_5_out_0x56459c258538 -> interface_2_in_0x56459c258538;
interface_5_out_0x56459c258498 -> interface_2_in_0x56459c258498;

interface_2_out_0x56459a9d6050 -> interface_1_in_0x56459a9d6050;
interface_2_out_0x56459c25a880 -> interface_1_in_0x56459c25a880;
interface_2_out_0x56459c259020 -> interface_1_in_0x56459c259020;
interface_2_out_0x56459a9d60c8 -> interface_1_in_0x56459a9d60c8;
interface_2_out_0x56459c258390 -> interface_1_in_0x56459c258390;

// Input tensor.
subgraph cluster_subgraph_6 {
    label = "Input 1";
    interface_6_out_0x56459c2583f8 [label="s^-1*C_out", shape=none];
    interface_6_out_0x56459c2583a8 [label="k_1^2", shape=none];
}

interface_6_out_0x56459c2583f8 -> interface_1_in_0x56459c2583f8;
interface_6_out_0x56459c2583a8 -> interface_1_in_0x56459c2583a8;

interface_1_out_0x56459a9d6050 -> interface_0_in_0x56459a9d6050;
interface_1_out_0x56459c25a880 -> interface_0_in_0x56459c25a880;
interface_1_out_0x56459c25a898 -> interface_0_in_0x56459c25a898;
interface_1_out_0x56459c259020 -> interface_0_in_0x56459c259020;
interface_1_out_0x56459a9d60c8 -> interface_0_in_0x56459a9d60c8;

{
    rank = same;
    interface_4_out_0x56459a9d6050;
    interface_4_out_0x56459c25b9c0;
    interface_4_out_0x56459c259020;
    interface_4_out_0x56459c25c5a8;
    interface_6_out_0x56459c2583f8;
    interface_6_out_0x56459c2583a8;
    interface_5_out_0x56459c2584e8;
    interface_5_out_0x56459c258538;
    interface_5_out_0x56459c258498;
}
subgraph cluster_subgraph_output {
    label = "Output";
    interface_7_in_0x56459a9d6050 [label="N", shape=none];
    interface_7_in_0x56459a9d6078 [label="C_out", shape=none];
    interface_7_in_0x56459a9d60a0 [label="H", shape=none];
    interface_7_in_0x56459a9d60c8 [label="H", shape=none];
}
interface_0_out_0x56459a9d6050 -> interface_7_in_0x56459a9d6050;
interface_0_out_0x56459a9d6078 -> interface_7_in_0x56459a9d6078;
interface_0_out_0x56459a9d60a0 -> interface_7_in_0x56459a9d60a0;
interface_0_out_0x56459a9d60c8 -> interface_7_in_0x56459a9d60c8;

}

"""
class kernel_generated_0(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([12, 9]),
			torch.randn([12, 7, 9]),
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

		# [H]@Unfold411df36b3e389f9b -> [H]@Iteratorb0a1def4ad5784ec, [k_2]@Share537524b85569cbbe
		t_3 = torch.reshape(t_3, (1, 2688, 112, 1, ))
		t_3 = torch.nn.functional.unfold(t_3, (7, 1, ), padding=(3, 0, ))
		t_3 = torch.reshape(t_3, (1, 2, 12, 112, 7, 112, ))

		# Perform contraction.
		t_4 = torch.einsum("lojnkm, jki -> lonmi", t_3, in_2)

		# Perform contraction.
		t_5 = torch.einsum("knmli, ji -> knjml", t_4, in_1)

		# No contraction needed.
		t_6 = t_5

		# [s]@Merge03a73148aa81036c, [s^-1*C_out]@Merge03a73148aa81036f -> [C_out]@Iteratorc7f8eb87a5a0a9e0
		t_6 = torch.reshape(t_6, (1, 24, 112, 112, ))

		# [H]@Shift41a433c05e30b91d -> [H]@Iterator96123ba3184da39c
		t_6 = torch.roll(t_6, self.shift_direction, 2)

		# No need to crop the output tensor.
		y = t_6

		return y

class kernel_generated_1(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([48, 9]),
			torch.randn([12, 7, 9]),
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

		# [H]@Unfold411df36b3e389f9b -> [H]@Iteratorb0a1def4ad5784ec, [k_2]@Share537524b85569cbbe
		t_3 = torch.reshape(t_3, (1, 1344, 56, 1, ))
		t_3 = torch.nn.functional.unfold(t_3, (7, 1, ), padding=(3, 0, ))
		t_3 = torch.reshape(t_3, (1, 2, 12, 56, 7, 56, ))

		# Perform contraction.
		t_4 = torch.einsum("lojnkm, jki -> lonmi", t_3, in_2)

		# Perform contraction.
		t_5 = torch.einsum("knmli, ji -> knjml", t_4, in_1)

		# No contraction needed.
		t_6 = t_5

		# [s]@Merge03a73148aa81036c, [s^-1*C_out]@Merge03a73148aa81036f -> [C_out]@Iteratorc7f8eb87a5a0a9e0
		t_6 = torch.reshape(t_6, (1, 96, 56, 56, ))

		# [H]@Shift41a433c05e30b91d -> [H]@Iterator96123ba3184da39c
		t_6 = torch.roll(t_6, self.shift_direction, 2)

		# No need to crop the output tensor.
		y = t_6

		return y

class kernel_generated_2(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([96, 9]),
			torch.randn([24, 7, 9]),
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

		# [H]@Unfold411df36b3e389f9b -> [H]@Iteratorb0a1def4ad5784ec, [k_2]@Share537524b85569cbbe
		t_3 = torch.reshape(t_3, (1, 2688, 56, 1, ))
		t_3 = torch.nn.functional.unfold(t_3, (7, 1, ), padding=(3, 0, ))
		t_3 = torch.reshape(t_3, (1, 2, 24, 56, 7, 56, ))

		# Perform contraction.
		t_4 = torch.einsum("lojnkm, jki -> lonmi", t_3, in_2)

		# Perform contraction.
		t_5 = torch.einsum("knmli, ji -> knjml", t_4, in_1)

		# No contraction needed.
		t_6 = t_5

		# [s]@Merge03a73148aa81036c, [s^-1*C_out]@Merge03a73148aa81036f -> [C_out]@Iteratorc7f8eb87a5a0a9e0
		t_6 = torch.reshape(t_6, (1, 192, 56, 56, ))

		# [H]@Shift41a433c05e30b91d -> [H]@Iterator96123ba3184da39c
		t_6 = torch.roll(t_6, self.shift_direction, 2)

		# No need to crop the output tensor.
		y = t_6

		return y

class kernel_generated_3(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([96, 9]),
			torch.randn([24, 7, 9]),
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

		# [H]@Unfold411df36b3e389f9b -> [H]@Iteratorb0a1def4ad5784ec, [k_2]@Share537524b85569cbbe
		t_3 = torch.reshape(t_3, (1, 1344, 28, 1, ))
		t_3 = torch.nn.functional.unfold(t_3, (7, 1, ), padding=(3, 0, ))
		t_3 = torch.reshape(t_3, (1, 2, 24, 28, 7, 28, ))

		# Perform contraction.
		t_4 = torch.einsum("lojnkm, jki -> lonmi", t_3, in_2)

		# Perform contraction.
		t_5 = torch.einsum("knmli, ji -> knjml", t_4, in_1)

		# No contraction needed.
		t_6 = t_5

		# [s]@Merge03a73148aa81036c, [s^-1*C_out]@Merge03a73148aa81036f -> [C_out]@Iteratorc7f8eb87a5a0a9e0
		t_6 = torch.reshape(t_6, (1, 192, 28, 28, ))

		# [H]@Shift41a433c05e30b91d -> [H]@Iterator96123ba3184da39c
		t_6 = torch.roll(t_6, self.shift_direction, 2)

		# No need to crop the output tensor.
		y = t_6

		return y

class kernel_generated_4(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([128, 9]),
			torch.randn([32, 7, 9]),
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

		# [H]@Unfold411df36b3e389f9b -> [H]@Iteratorb0a1def4ad5784ec, [k_2]@Share537524b85569cbbe
		t_3 = torch.reshape(t_3, (1, 1792, 28, 1, ))
		t_3 = torch.nn.functional.unfold(t_3, (7, 1, ), padding=(3, 0, ))
		t_3 = torch.reshape(t_3, (1, 2, 32, 28, 7, 28, ))

		# Perform contraction.
		t_4 = torch.einsum("lojnkm, jki -> lonmi", t_3, in_2)

		# Perform contraction.
		t_5 = torch.einsum("knmli, ji -> knjml", t_4, in_1)

		# No contraction needed.
		t_6 = t_5

		# [s]@Merge03a73148aa81036c, [s^-1*C_out]@Merge03a73148aa81036f -> [C_out]@Iteratorc7f8eb87a5a0a9e0
		t_6 = torch.reshape(t_6, (1, 256, 28, 28, ))

		# [H]@Shift41a433c05e30b91d -> [H]@Iterator96123ba3184da39c
		t_6 = torch.roll(t_6, self.shift_direction, 2)

		# No need to crop the output tensor.
		y = t_6

		return y

