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
        interface_0_out_0x5596d7788c60 [label="N", shape=none];
        interface_0_out_0x5596d7788c88 [label="C_out", shape=none];
        interface_0_out_0x5596d7788cb0 [label="H", shape=none];
        interface_0_out_0x5596d7788cd8 [label="H", shape=none];
    }
    {
        rank = same;
        interface_0_out_0x5596d7788c60;
        interface_0_out_0x5596d7788c88;
        interface_0_out_0x5596d7788cb0;
        interface_0_out_0x5596d7788cd8;
    }
    // Input 0.
    subgraph cluster_subgraph_0_in_0 {
        label = "";
        interface_0_in_0x5596d7788c60 [label="N", shape=none];
        interface_0_in_0x5596d7877780 [label="s", shape=none];
        interface_0_in_0x5596d7877798 [label="s^-1*C_out", shape=none];
        interface_0_in_0x5596d7788cb0 [label="H", shape=none];
        interface_0_in_0x5596d7788cd8 [label="H", shape=none];
    }
    {
        rank = same;
        interface_0_in_0x5596d7788c60;
        interface_0_in_0x5596d7877780;
        interface_0_in_0x5596d7877798;
        interface_0_in_0x5596d7788cb0;
        interface_0_in_0x5596d7788cd8;
    }
    // Op's.
    op_0x5596d7877740 [label="Merge"];
    // Dimension's.
    interface_0_in_0x5596d7788c60 -> interface_0_out_0x5596d7788c60 [label="N"];
    op_0x5596d7877740 -> interface_0_out_0x5596d7788c88 [label="C_out"];
    interface_0_in_0x5596d7788cb0 -> interface_0_out_0x5596d7788cb0 [label="H"];
    interface_0_in_0x5596d7788cd8 -> interface_0_out_0x5596d7788cd8 [label="H"];
    interface_0_in_0x5596d7877780 -> op_0x5596d7877740 [label="s"];
    interface_0_in_0x5596d7877798 -> op_0x5596d7877740 [label="s^-1*C_out"];
}

// Stage tensor.
subgraph cluster_subgraph_1 {
    label = "Subgraph 1";
    // Reductions.
    reduce_0x7ef0e4001cc0 [label="Sum", shape=box];
    // Output.
    subgraph cluster_subgraph_1_out {
        label = "";
        interface_1_out_0x5596d7788c60 [label="N", shape=none];
        interface_1_out_0x5596d7877780 [label="s", shape=none];
        interface_1_out_0x5596d7877798 [label="s^-1*C_out", shape=none];
        interface_1_out_0x5596d7788cb0 [label="H", shape=none];
        interface_1_out_0x5596d7788cd8 [label="H", shape=none];
    }
    {
        rank = same;
        reduce_0x7ef0e4001cc0;
        interface_1_out_0x5596d7788c60;
        interface_1_out_0x5596d7877780;
        interface_1_out_0x5596d7877798;
        interface_1_out_0x5596d7788cb0;
        interface_1_out_0x5596d7788cd8;
    }
    // Input 0.
    subgraph cluster_subgraph_1_in_0 {
        label = "";
        interface_1_in_0x5596d7788c60 [label="N", shape=none];
        interface_1_in_0x5596d7877780 [label="s", shape=none];
        interface_1_in_0x5596d7788cb0 [label="H", shape=none];
        interface_1_in_0x5596d7788cd8 [label="H", shape=none];
        interface_1_in_0x5596d7875210 [label="k_1^2", shape=none];
    }
    // Input 1.
    subgraph cluster_subgraph_1_in_1 {
        label = "";
        interface_1_in_0x5596d7875278 [label="s^-1*C_out", shape=none];
        interface_1_in_0x5596d7875228 [label="k_1^2", shape=none];
    }
    {
        rank = same;
        interface_1_in_0x5596d7788c60;
        interface_1_in_0x5596d7877780;
        interface_1_in_0x5596d7788cb0;
        interface_1_in_0x5596d7788cd8;
        interface_1_in_0x5596d7875210;
        interface_1_in_0x5596d7875278;
        interface_1_in_0x5596d7875228;
    }
    // Op's.
    op_0x5596d78751f0 [label="Share"];
    op_0x5596d7875240 [label="Share"];
    op_0x5596d7875638 [label="Expand"];
    // Dimension's.
    interface_1_in_0x5596d7788c60 -> interface_1_out_0x5596d7788c60 [label="N"];
    interface_1_in_0x5596d7788cb0 -> interface_1_out_0x5596d7788cb0 [label="H"];
    interface_1_in_0x5596d7788cd8 -> interface_1_out_0x5596d7788cd8 [label="H"];
    interface_1_in_0x5596d7875210 -> op_0x5596d78751f0 [label="k_1^2"];
    interface_1_in_0x5596d7875228 -> op_0x5596d78751f0 [label="k_1^2"];
    op_0x5596d7875638 -> op_0x5596d7875240 [label="s^-1*C_out"];
    interface_1_in_0x5596d7875278 -> op_0x5596d7875240 [label="s^-1*C_out"];
    interface_1_in_0x5596d7877780 -> interface_1_out_0x5596d7877780 [label="s"];
    op_0x5596d7875240 -> interface_1_out_0x5596d7877798 [label="s^-1*C_out"];
    op_0x5596d78751f0 -> reduce_0x7ef0e4001cc0 [label="k_1^2"];
}

// Stage tensor.
subgraph cluster_subgraph_2 {
    label = "Subgraph 2";
    // Reductions.
    reduce_0x7ef0e4005768 [label="Sum", shape=box];
    // Output.
    subgraph cluster_subgraph_2_out {
        label = "";
        interface_2_out_0x5596d7788c60 [label="N", shape=none];
        interface_2_out_0x5596d7877780 [label="s", shape=none];
        interface_2_out_0x5596d7788cb0 [label="H", shape=none];
        interface_2_out_0x5596d7788cd8 [label="H", shape=none];
        interface_2_out_0x5596d7875210 [label="k_1^2", shape=none];
    }
    {
        rank = same;
        reduce_0x7ef0e4005768;
        interface_2_out_0x5596d7788c60;
        interface_2_out_0x5596d7877780;
        interface_2_out_0x5596d7788cb0;
        interface_2_out_0x5596d7788cd8;
        interface_2_out_0x5596d7875210;
    }
    // Input 0.
    subgraph cluster_subgraph_2_in_0 {
        label = "";
        interface_2_in_0x5596d7788c60 [label="N", shape=none];
        interface_2_in_0x5596d7876c50 [label="C_in", shape=none];
        interface_2_in_0x5596d7788cb0 [label="H", shape=none];
        interface_2_in_0x5596d7788cd8 [label="H", shape=none];
        interface_2_in_0x5596d7875210 [label="k_1^2", shape=none];
    }
    {
        rank = same;
        interface_2_in_0x5596d7788c60;
        interface_2_in_0x5596d7876c50;
        interface_2_in_0x5596d7788cb0;
        interface_2_in_0x5596d7788cd8;
        interface_2_in_0x5596d7875210;
    }
    // Op's.
    op_0x5596d7876c10 [label="Split"];
    // Dimension's.
    interface_2_in_0x5596d7788c60 -> interface_2_out_0x5596d7788c60 [label="N"];
    interface_2_in_0x5596d7788cb0 -> interface_2_out_0x5596d7788cb0 [label="H"];
    interface_2_in_0x5596d7788cd8 -> interface_2_out_0x5596d7788cd8 [label="H"];
    interface_2_in_0x5596d7875210 -> interface_2_out_0x5596d7875210 [label="k_1^2"];
    interface_2_in_0x5596d7876c50 -> op_0x5596d7876c10 [label="C_in"];
    op_0x5596d7876c10 -> interface_2_out_0x5596d7877780 [label="s"];
    op_0x5596d7876c10 -> reduce_0x7ef0e4005768 [label="s^-1*C_in"];
}

// Stage tensor.
subgraph cluster_subgraph_3 {
    label = "Subgraph 3";
    // Reductions.
    // Output.
    subgraph cluster_subgraph_3_out {
        label = "";
        interface_3_out_0x5596d7788c60 [label="N", shape=none];
        interface_3_out_0x5596d7876c50 [label="C_in", shape=none];
        interface_3_out_0x5596d7788cb0 [label="H", shape=none];
        interface_3_out_0x5596d7788cd8 [label="H", shape=none];
        interface_3_out_0x5596d7875210 [label="k_1^2", shape=none];
    }
    {
        rank = same;
        interface_3_out_0x5596d7788c60;
        interface_3_out_0x5596d7876c50;
        interface_3_out_0x5596d7788cb0;
        interface_3_out_0x5596d7788cd8;
        interface_3_out_0x5596d7875210;
    }
    // Input 0.
    subgraph cluster_subgraph_3_in_0 {
        label = "";
        interface_3_in_0x5596d7788c60 [label="N", shape=none];
        interface_3_in_0x5596d787bb30 [label="C_in", shape=none];
        interface_3_in_0x5596d7788cd8 [label="H", shape=none];
        interface_3_in_0x5596d7788cb0 [label="H", shape=none];
    }
    // Input 1.
    subgraph cluster_subgraph_3_in_1 {
        label = "";
        interface_3_in_0x5596d787bb48 [label="C_in", shape=none];
        interface_3_in_0x5596d7875318 [label="k_1^2", shape=none];
    }
    {
        rank = same;
        interface_3_in_0x5596d7788c60;
        interface_3_in_0x5596d787bb30;
        interface_3_in_0x5596d7788cd8;
        interface_3_in_0x5596d7788cb0;
        interface_3_in_0x5596d787bb48;
        interface_3_in_0x5596d7875318;
    }
    // Op's.
    op_0x5596d78752e0 [label="Share"];
    op_0x5596d7875678 [label="Expand"];
    op_0x5596d787bb10 [label="Share"];
    // Dimension's.
    interface_3_in_0x5596d7788c60 -> interface_3_out_0x5596d7788c60 [label="N"];
    interface_3_in_0x5596d7788cb0 -> interface_3_out_0x5596d7788cb0 [label="H"];
    interface_3_in_0x5596d7788cd8 -> interface_3_out_0x5596d7788cd8 [label="H"];
    op_0x5596d78752e0 -> interface_3_out_0x5596d7875210 [label="k_1^2"];
    op_0x5596d7875678 -> op_0x5596d78752e0 [label="k_1^2"];
    interface_3_in_0x5596d7875318 -> op_0x5596d78752e0 [label="k_1^2"];
    op_0x5596d787bb10 -> interface_3_out_0x5596d7876c50 [label="C_in"];
    interface_3_in_0x5596d787bb30 -> op_0x5596d787bb10 [label="C_in"];
    interface_3_in_0x5596d787bb48 -> op_0x5596d787bb10 [label="C_in"];
}

// Input tensor.
subgraph cluster_subgraph_4 {
    label = "Input 0";
    interface_4_out_0x5596d7788c60 [label="N", shape=none];
    interface_4_out_0x5596d787bb30 [label="C_in", shape=none];
    interface_4_out_0x5596d7788cd8 [label="H", shape=none];
    interface_4_out_0x5596d7788cb0 [label="H", shape=none];
}

interface_4_out_0x5596d7788c60 -> interface_3_in_0x5596d7788c60;
interface_4_out_0x5596d787bb30 -> interface_3_in_0x5596d787bb30;
interface_4_out_0x5596d7788cd8 -> interface_3_in_0x5596d7788cd8;
interface_4_out_0x5596d7788cb0 -> interface_3_in_0x5596d7788cb0;

// Input tensor.
subgraph cluster_subgraph_5 {
    label = "Input 2";
    interface_5_out_0x5596d787bb48 [label="C_in", shape=none];
    interface_5_out_0x5596d7875318 [label="k_1^2", shape=none];
}

interface_5_out_0x5596d787bb48 -> interface_3_in_0x5596d787bb48;
interface_5_out_0x5596d7875318 -> interface_3_in_0x5596d7875318;

interface_3_out_0x5596d7788c60 -> interface_2_in_0x5596d7788c60;
interface_3_out_0x5596d7876c50 -> interface_2_in_0x5596d7876c50;
interface_3_out_0x5596d7788cb0 -> interface_2_in_0x5596d7788cb0;
interface_3_out_0x5596d7788cd8 -> interface_2_in_0x5596d7788cd8;
interface_3_out_0x5596d7875210 -> interface_2_in_0x5596d7875210;

interface_2_out_0x5596d7788c60 -> interface_1_in_0x5596d7788c60;
interface_2_out_0x5596d7877780 -> interface_1_in_0x5596d7877780;
interface_2_out_0x5596d7788cb0 -> interface_1_in_0x5596d7788cb0;
interface_2_out_0x5596d7788cd8 -> interface_1_in_0x5596d7788cd8;
interface_2_out_0x5596d7875210 -> interface_1_in_0x5596d7875210;

// Input tensor.
subgraph cluster_subgraph_6 {
    label = "Input 1";
    interface_6_out_0x5596d7875278 [label="s^-1*C_out", shape=none];
    interface_6_out_0x5596d7875228 [label="k_1^2", shape=none];
}

interface_6_out_0x5596d7875278 -> interface_1_in_0x5596d7875278;
interface_6_out_0x5596d7875228 -> interface_1_in_0x5596d7875228;

interface_1_out_0x5596d7788c60 -> interface_0_in_0x5596d7788c60;
interface_1_out_0x5596d7877780 -> interface_0_in_0x5596d7877780;
interface_1_out_0x5596d7877798 -> interface_0_in_0x5596d7877798;
interface_1_out_0x5596d7788cb0 -> interface_0_in_0x5596d7788cb0;
interface_1_out_0x5596d7788cd8 -> interface_0_in_0x5596d7788cd8;

{
    rank = same;
    interface_4_out_0x5596d7788c60;
    interface_4_out_0x5596d787bb30;
    interface_4_out_0x5596d7788cd8;
    interface_4_out_0x5596d7788cb0;
    interface_6_out_0x5596d7875278;
    interface_6_out_0x5596d7875228;
    interface_5_out_0x5596d787bb48;
    interface_5_out_0x5596d7875318;
}
subgraph cluster_subgraph_output {
    label = "Output";
    interface_7_in_0x5596d7788c60 [label="N", shape=none];
    interface_7_in_0x5596d7788c88 [label="C_out", shape=none];
    interface_7_in_0x5596d7788cb0 [label="H", shape=none];
    interface_7_in_0x5596d7788cd8 [label="H", shape=none];
}
interface_0_out_0x5596d7788c60 -> interface_7_in_0x5596d7788c60;
interface_0_out_0x5596d7788c88 -> interface_7_in_0x5596d7788c88;
interface_0_out_0x5596d7788cb0 -> interface_7_in_0x5596d7788cb0;
interface_0_out_0x5596d7788cd8 -> interface_7_in_0x5596d7788cd8;

}

"""
class kernel_generated_0(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([12, 9]),
			torch.randn([24, 9]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]
		in_2 = self.weights[1]

		# Perform contraction.
		t_3 = torch.einsum("kjml, ji -> kjlmi", in_0, in_2)

		# No contraction needed.
		t_4 = t_3

		# [C_in]@Split75a539c6b0ba4a63 -> [s]@Merge03a73148aa81036c, [s^-1*C_in]@Reducee9b9071fb9943ecb
		t_4 = torch.reshape(t_4, (1, 2, 12, 112, 112, 9, ))

		# [s^-1*C_in]@Reduce
		t_4 = torch.sum(t_4, dim=(2, ))

		# Perform contraction.
		t_5 = torch.einsum("knlmi, ji -> knjlm", t_4, in_1)

		# No contraction needed.
		t_6 = t_5

		# [s]@Merge03a73148aa81036c, [s^-1*C_out]@Merge03a73148aa81036f -> [C_out]@Iteratorc7f8eb87a5a0a9e0
		t_6 = torch.reshape(t_6, (1, 24, 112, 112, ))

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
			torch.randn([24, 9]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]
		in_2 = self.weights[1]

		# Perform contraction.
		t_3 = torch.einsum("kjml, ji -> kjlmi", in_0, in_2)

		# No contraction needed.
		t_4 = t_3

		# [C_in]@Split75a539c6b0ba4a63 -> [s]@Merge03a73148aa81036c, [s^-1*C_in]@Reducee9b9071fb9943ecb
		t_4 = torch.reshape(t_4, (1, 2, 12, 56, 56, 9, ))

		# [s^-1*C_in]@Reduce
		t_4 = torch.sum(t_4, dim=(2, ))

		# Perform contraction.
		t_5 = torch.einsum("knlmi, ji -> knjlm", t_4, in_1)

		# No contraction needed.
		t_6 = t_5

		# [s]@Merge03a73148aa81036c, [s^-1*C_out]@Merge03a73148aa81036f -> [C_out]@Iteratorc7f8eb87a5a0a9e0
		t_6 = torch.reshape(t_6, (1, 96, 56, 56, ))

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
			torch.randn([48, 9]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]
		in_2 = self.weights[1]

		# Perform contraction.
		t_3 = torch.einsum("kjml, ji -> kjlmi", in_0, in_2)

		# No contraction needed.
		t_4 = t_3

		# [C_in]@Split75a539c6b0ba4a63 -> [s]@Merge03a73148aa81036c, [s^-1*C_in]@Reducee9b9071fb9943ecb
		t_4 = torch.reshape(t_4, (1, 2, 24, 56, 56, 9, ))

		# [s^-1*C_in]@Reduce
		t_4 = torch.sum(t_4, dim=(2, ))

		# Perform contraction.
		t_5 = torch.einsum("knlmi, ji -> knjlm", t_4, in_1)

		# No contraction needed.
		t_6 = t_5

		# [s]@Merge03a73148aa81036c, [s^-1*C_out]@Merge03a73148aa81036f -> [C_out]@Iteratorc7f8eb87a5a0a9e0
		t_6 = torch.reshape(t_6, (1, 192, 56, 56, ))

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
			torch.randn([48, 9]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]
		in_2 = self.weights[1]

		# Perform contraction.
		t_3 = torch.einsum("kjml, ji -> kjlmi", in_0, in_2)

		# No contraction needed.
		t_4 = t_3

		# [C_in]@Split75a539c6b0ba4a63 -> [s]@Merge03a73148aa81036c, [s^-1*C_in]@Reducee9b9071fb9943ecb
		t_4 = torch.reshape(t_4, (1, 2, 24, 28, 28, 9, ))

		# [s^-1*C_in]@Reduce
		t_4 = torch.sum(t_4, dim=(2, ))

		# Perform contraction.
		t_5 = torch.einsum("knlmi, ji -> knjlm", t_4, in_1)

		# No contraction needed.
		t_6 = t_5

		# [s]@Merge03a73148aa81036c, [s^-1*C_out]@Merge03a73148aa81036f -> [C_out]@Iteratorc7f8eb87a5a0a9e0
		t_6 = torch.reshape(t_6, (1, 192, 28, 28, ))

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
			torch.randn([64, 9]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]
		in_2 = self.weights[1]

		# Perform contraction.
		t_3 = torch.einsum("kjml, ji -> kjlmi", in_0, in_2)

		# No contraction needed.
		t_4 = t_3

		# [C_in]@Split75a539c6b0ba4a63 -> [s]@Merge03a73148aa81036c, [s^-1*C_in]@Reducee9b9071fb9943ecb
		t_4 = torch.reshape(t_4, (1, 2, 32, 28, 28, 9, ))

		# [s^-1*C_in]@Reduce
		t_4 = torch.sum(t_4, dim=(2, ))

		# Perform contraction.
		t_5 = torch.einsum("knlmi, ji -> knjlm", t_4, in_1)

		# No contraction needed.
		t_6 = t_5

		# [s]@Merge03a73148aa81036c, [s^-1*C_out]@Merge03a73148aa81036f -> [C_out]@Iteratorc7f8eb87a5a0a9e0
		t_6 = torch.reshape(t_6, (1, 256, 28, 28, ))

		# No need to crop the output tensor.
		y = t_6

		return y

