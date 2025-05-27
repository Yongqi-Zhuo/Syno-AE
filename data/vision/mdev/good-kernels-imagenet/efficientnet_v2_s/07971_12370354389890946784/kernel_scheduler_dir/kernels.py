import torch
import random
"""
digraph kernel_preview {
newrank = true;

// Stage tensor.
subgraph cluster_subgraph_0 {
    label = "Subgraph 0";
    // Reductions.
    reduce_0x7ef0e4002e58 [label="Sum", shape=box];
    reduce_0x7ef0e40032a8 [label="Sum", shape=box];
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
        reduce_0x7ef0e4002e58;
        reduce_0x7ef0e40032a8;
        interface_0_out_0x5596d7788c60;
        interface_0_out_0x5596d7788c88;
        interface_0_out_0x5596d7788cb0;
        interface_0_out_0x5596d7788cd8;
    }
    // Input 0.
    subgraph cluster_subgraph_0_in_0 {
        label = "";
        interface_0_in_0x5596d7788c60 [label="N", shape=none];
        interface_0_in_0x5596d7788cb0 [label="H", shape=none];
        interface_0_in_0x5596d7875530 [label="s", shape=none];
        interface_0_in_0x5596d7788cd8 [label="H", shape=none];
        interface_0_in_0x5596d787bd60 [label="k_1^2*s", shape=none];
    }
    // Input 1.
    subgraph cluster_subgraph_0_in_1 {
        label = "";
        interface_0_in_0x5596d7875138 [label="C_out", shape=none];
        interface_0_in_0x5596d7875548 [label="s", shape=none];
        interface_0_in_0x5596d787bd78 [label="k_1^2*s", shape=none];
    }
    {
        rank = same;
        interface_0_in_0x5596d7788c60;
        interface_0_in_0x5596d7788cb0;
        interface_0_in_0x5596d7875530;
        interface_0_in_0x5596d7788cd8;
        interface_0_in_0x5596d787bd60;
        interface_0_in_0x5596d7875138;
        interface_0_in_0x5596d7875548;
        interface_0_in_0x5596d787bd78;
    }
    // Op's.
    op_0x5596d7875100 [label="Share"];
    op_0x5596d7875510 [label="Share"];
    op_0x5596d7875618 [label="Expand"];
    op_0x5596d787bd40 [label="Share"];
    // Dimension's.
    interface_0_in_0x5596d7788c60 -> interface_0_out_0x5596d7788c60 [label="N"];
    op_0x5596d7875100 -> interface_0_out_0x5596d7788c88 [label="C_out"];
    interface_0_in_0x5596d7788cb0 -> interface_0_out_0x5596d7788cb0 [label="H"];
    interface_0_in_0x5596d7788cd8 -> interface_0_out_0x5596d7788cd8 [label="H"];
    op_0x5596d7875618 -> op_0x5596d7875100 [label="C_out"];
    interface_0_in_0x5596d7875138 -> op_0x5596d7875100 [label="C_out"];
    interface_0_in_0x5596d7875530 -> op_0x5596d7875510 [label="s"];
    interface_0_in_0x5596d7875548 -> op_0x5596d7875510 [label="s"];
    interface_0_in_0x5596d787bd60 -> op_0x5596d787bd40 [label="k_1^2*s"];
    interface_0_in_0x5596d787bd78 -> op_0x5596d787bd40 [label="k_1^2*s"];
    op_0x5596d7875510 -> reduce_0x7ef0e4002e58 [label="s"];
    op_0x5596d787bd40 -> reduce_0x7ef0e40032a8 [label="k_1^2*s"];
}

// Stage tensor.
subgraph cluster_subgraph_1 {
    label = "Subgraph 1";
    // Reductions.
    // Output.
    subgraph cluster_subgraph_1_out {
        label = "";
        interface_1_out_0x5596d7788c60 [label="N", shape=none];
        interface_1_out_0x5596d7788cb0 [label="H", shape=none];
        interface_1_out_0x5596d7875530 [label="s", shape=none];
        interface_1_out_0x5596d7788cd8 [label="H", shape=none];
        interface_1_out_0x5596d787bd60 [label="k_1^2*s", shape=none];
    }
    {
        rank = same;
        interface_1_out_0x5596d7788c60;
        interface_1_out_0x5596d7788cb0;
        interface_1_out_0x5596d7875530;
        interface_1_out_0x5596d7788cd8;
        interface_1_out_0x5596d787bd60;
    }
    // Input 0.
    subgraph cluster_subgraph_1_in_0 {
        label = "";
        interface_1_in_0x5596d7788c60 [label="N", shape=none];
        interface_1_in_0x5596d787d5a0 [label="H", shape=none];
        interface_1_in_0x5596d787d5b8 [label="s", shape=none];
        interface_1_in_0x5596d7788cd8 [label="H", shape=none];
        interface_1_in_0x5596d787bd60 [label="k_1^2*s", shape=none];
    }
    {
        rank = same;
        interface_1_in_0x5596d7788c60;
        interface_1_in_0x5596d787d5a0;
        interface_1_in_0x5596d787d5b8;
        interface_1_in_0x5596d7788cd8;
        interface_1_in_0x5596d787bd60;
    }
    // Op's.
    op_0x5596d7876150 [label="Shift"];
    op_0x5596d787d560 [label="Merge"];
    op_0x5596d78850f0 [label="Split"];
    // Dimension's.
    interface_1_in_0x5596d7788c60 -> interface_1_out_0x5596d7788c60 [label="N"];
    op_0x5596d78850f0 -> interface_1_out_0x5596d7788cb0 [label="H"];
    interface_1_in_0x5596d7788cd8 -> interface_1_out_0x5596d7788cd8 [label="H"];
    op_0x5596d78850f0 -> interface_1_out_0x5596d7875530 [label="s"];
    op_0x5596d787d560 -> op_0x5596d7876150 [label="s*H"];
    interface_1_in_0x5596d787bd60 -> interface_1_out_0x5596d787bd60 [label="k_1^2*s"];
    interface_1_in_0x5596d787d5a0 -> op_0x5596d787d560 [label="H"];
    interface_1_in_0x5596d787d5b8 -> op_0x5596d787d560 [label="s"];
    op_0x5596d7876150 -> op_0x5596d78850f0 [label="s*H"];
}

// Stage tensor.
subgraph cluster_subgraph_2 {
    label = "Subgraph 2";
    // Reductions.
    reduce_0x7ef0e4005c70 [label="Sum", shape=box];
    // Output.
    subgraph cluster_subgraph_2_out {
        label = "";
        interface_2_out_0x5596d7788c60 [label="N", shape=none];
        interface_2_out_0x5596d787d5a0 [label="H", shape=none];
        interface_2_out_0x5596d787d5b8 [label="s", shape=none];
        interface_2_out_0x5596d7788cd8 [label="H", shape=none];
        interface_2_out_0x5596d787bd60 [label="k_1^2*s", shape=none];
    }
    {
        rank = same;
        reduce_0x7ef0e4005c70;
        interface_2_out_0x5596d7788c60;
        interface_2_out_0x5596d787d5a0;
        interface_2_out_0x5596d787d5b8;
        interface_2_out_0x5596d7788cd8;
        interface_2_out_0x5596d787bd60;
    }
    // Input 0.
    subgraph cluster_subgraph_2_in_0 {
        label = "";
        interface_2_in_0x5596d7788c60 [label="N", shape=none];
        interface_2_in_0x5596d787b9f0 [label="C_in", shape=none];
        interface_2_in_0x5596d7788cd8 [label="H", shape=none];
        interface_2_in_0x5596d787d5a0 [label="H", shape=none];
    }
    // Input 1.
    subgraph cluster_subgraph_2_in_1 {
        label = "";
        interface_2_in_0x5596d787be68 [label="s", shape=none];
        interface_2_in_0x5596d787ba08 [label="C_in", shape=none];
        interface_2_in_0x5596d787bdc8 [label="k_1^2*s", shape=none];
    }
    {
        rank = same;
        interface_2_in_0x5596d7788c60;
        interface_2_in_0x5596d787b9f0;
        interface_2_in_0x5596d7788cd8;
        interface_2_in_0x5596d787d5a0;
        interface_2_in_0x5596d787be68;
        interface_2_in_0x5596d787ba08;
        interface_2_in_0x5596d787bdc8;
    }
    // Op's.
    op_0x5596d7875778 [label="Expand"];
    op_0x5596d7875798 [label="Expand"];
    op_0x5596d787b9d0 [label="Share"];
    op_0x5596d787bd90 [label="Share"];
    op_0x5596d787be30 [label="Share"];
    // Dimension's.
    interface_2_in_0x5596d7788c60 -> interface_2_out_0x5596d7788c60 [label="N"];
    interface_2_in_0x5596d7788cd8 -> interface_2_out_0x5596d7788cd8 [label="H"];
    interface_2_in_0x5596d787b9f0 -> op_0x5596d787b9d0 [label="C_in"];
    interface_2_in_0x5596d787ba08 -> op_0x5596d787b9d0 [label="C_in"];
    op_0x5596d787bd90 -> interface_2_out_0x5596d787bd60 [label="k_1^2*s"];
    op_0x5596d7875778 -> op_0x5596d787bd90 [label="k_1^2*s"];
    interface_2_in_0x5596d787bdc8 -> op_0x5596d787bd90 [label="k_1^2*s"];
    op_0x5596d7875798 -> op_0x5596d787be30 [label="s"];
    interface_2_in_0x5596d787be68 -> op_0x5596d787be30 [label="s"];
    interface_2_in_0x5596d787d5a0 -> interface_2_out_0x5596d787d5a0 [label="H"];
    op_0x5596d787be30 -> interface_2_out_0x5596d787d5b8 [label="s"];
    op_0x5596d787b9d0 -> reduce_0x7ef0e4005c70 [label="C_in"];
}

// Input tensor.
subgraph cluster_subgraph_3 {
    label = "Input 0";
    interface_3_out_0x5596d7788c60 [label="N", shape=none];
    interface_3_out_0x5596d787b9f0 [label="C_in", shape=none];
    interface_3_out_0x5596d7788cd8 [label="H", shape=none];
    interface_3_out_0x5596d787d5a0 [label="H", shape=none];
}

interface_3_out_0x5596d7788c60 -> interface_2_in_0x5596d7788c60;
interface_3_out_0x5596d787b9f0 -> interface_2_in_0x5596d787b9f0;
interface_3_out_0x5596d7788cd8 -> interface_2_in_0x5596d7788cd8;
interface_3_out_0x5596d787d5a0 -> interface_2_in_0x5596d787d5a0;

// Input tensor.
subgraph cluster_subgraph_4 {
    label = "Input 2";
    interface_4_out_0x5596d787be68 [label="s", shape=none];
    interface_4_out_0x5596d787ba08 [label="C_in", shape=none];
    interface_4_out_0x5596d787bdc8 [label="k_1^2*s", shape=none];
}

interface_4_out_0x5596d787be68 -> interface_2_in_0x5596d787be68;
interface_4_out_0x5596d787ba08 -> interface_2_in_0x5596d787ba08;
interface_4_out_0x5596d787bdc8 -> interface_2_in_0x5596d787bdc8;

interface_2_out_0x5596d7788c60 -> interface_1_in_0x5596d7788c60;
interface_2_out_0x5596d787d5a0 -> interface_1_in_0x5596d787d5a0;
interface_2_out_0x5596d787d5b8 -> interface_1_in_0x5596d787d5b8;
interface_2_out_0x5596d7788cd8 -> interface_1_in_0x5596d7788cd8;
interface_2_out_0x5596d787bd60 -> interface_1_in_0x5596d787bd60;

interface_1_out_0x5596d7788c60 -> interface_0_in_0x5596d7788c60;
interface_1_out_0x5596d7788cb0 -> interface_0_in_0x5596d7788cb0;
interface_1_out_0x5596d7875530 -> interface_0_in_0x5596d7875530;
interface_1_out_0x5596d7788cd8 -> interface_0_in_0x5596d7788cd8;
interface_1_out_0x5596d787bd60 -> interface_0_in_0x5596d787bd60;

// Input tensor.
subgraph cluster_subgraph_5 {
    label = "Input 1";
    interface_5_out_0x5596d7875138 [label="C_out", shape=none];
    interface_5_out_0x5596d7875548 [label="s", shape=none];
    interface_5_out_0x5596d787bd78 [label="k_1^2*s", shape=none];
}

interface_5_out_0x5596d7875138 -> interface_0_in_0x5596d7875138;
interface_5_out_0x5596d7875548 -> interface_0_in_0x5596d7875548;
interface_5_out_0x5596d787bd78 -> interface_0_in_0x5596d787bd78;

{
    rank = same;
    interface_3_out_0x5596d7788c60;
    interface_3_out_0x5596d787b9f0;
    interface_3_out_0x5596d7788cd8;
    interface_3_out_0x5596d787d5a0;
    interface_5_out_0x5596d7875138;
    interface_5_out_0x5596d7875548;
    interface_5_out_0x5596d787bd78;
    interface_4_out_0x5596d787be68;
    interface_4_out_0x5596d787ba08;
    interface_4_out_0x5596d787bdc8;
}
subgraph cluster_subgraph_output {
    label = "Output";
    interface_6_in_0x5596d7788c60 [label="N", shape=none];
    interface_6_in_0x5596d7788c88 [label="C_out", shape=none];
    interface_6_in_0x5596d7788cb0 [label="H", shape=none];
    interface_6_in_0x5596d7788cd8 [label="H", shape=none];
}
interface_0_out_0x5596d7788c60 -> interface_6_in_0x5596d7788c60;
interface_0_out_0x5596d7788c88 -> interface_6_in_0x5596d7788c88;
interface_0_out_0x5596d7788cb0 -> interface_6_in_0x5596d7788cb0;
interface_0_out_0x5596d7788cd8 -> interface_6_in_0x5596d7788cd8;

}

"""
class kernel_generated_0(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([24, 2, 18]),
			torch.randn([2, 24, 18]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]
		in_2 = self.weights[1]

		# Perform contraction.
		t_3 = torch.einsum("limn, kij -> lnkmj", in_0, in_2)

		# No contraction needed.
		t_4 = t_3

		# [H]@Merge6f1a0d6b662fae84, [s]@Merge6f1a0d6b662fae85 -> [s*H]@Shift594e1a6314829db7
		t_4 = torch.reshape(t_4, (1, 224, 112, 18, ))

		# [s*H]@Shift594e1a6314829db7 -> [s*H]@Split7ee86503d19bbef6
		t_4 = torch.roll(t_4, self.shift_direction, 1)

		# [s*H]@Split7ee86503d19bbef6 -> [H]@Iterator96123ba3184da39c, [s]@Shareb15a7faee0f8b868
		t_4 = torch.reshape(t_4, (1, 112, 2, 112, 18, ))

		# Perform contraction.
		t_5 = torch.einsum("lmjnk, ijk -> limn", t_4, in_1)

		# No need to crop the output tensor.
		y = t_5

		return y

class kernel_generated_1(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([96, 2, 18]),
			torch.randn([2, 24, 18]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]
		in_2 = self.weights[1]

		# Perform contraction.
		t_3 = torch.einsum("limn, kij -> lnkmj", in_0, in_2)

		# No contraction needed.
		t_4 = t_3

		# [H]@Merge6f1a0d6b662fae84, [s]@Merge6f1a0d6b662fae85 -> [s*H]@Shift594e1a6314829db7
		t_4 = torch.reshape(t_4, (1, 112, 56, 18, ))

		# [s*H]@Shift594e1a6314829db7 -> [s*H]@Split7ee86503d19bbef6
		t_4 = torch.roll(t_4, self.shift_direction, 1)

		# [s*H]@Split7ee86503d19bbef6 -> [H]@Iterator96123ba3184da39c, [s]@Shareb15a7faee0f8b868
		t_4 = torch.reshape(t_4, (1, 56, 2, 56, 18, ))

		# Perform contraction.
		t_5 = torch.einsum("lmjnk, ijk -> limn", t_4, in_1)

		# No need to crop the output tensor.
		y = t_5

		return y

class kernel_generated_2(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([192, 2, 18]),
			torch.randn([2, 48, 18]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]
		in_2 = self.weights[1]

		# Perform contraction.
		t_3 = torch.einsum("limn, kij -> lnkmj", in_0, in_2)

		# No contraction needed.
		t_4 = t_3

		# [H]@Merge6f1a0d6b662fae84, [s]@Merge6f1a0d6b662fae85 -> [s*H]@Shift594e1a6314829db7
		t_4 = torch.reshape(t_4, (1, 112, 56, 18, ))

		# [s*H]@Shift594e1a6314829db7 -> [s*H]@Split7ee86503d19bbef6
		t_4 = torch.roll(t_4, self.shift_direction, 1)

		# [s*H]@Split7ee86503d19bbef6 -> [H]@Iterator96123ba3184da39c, [s]@Shareb15a7faee0f8b868
		t_4 = torch.reshape(t_4, (1, 56, 2, 56, 18, ))

		# Perform contraction.
		t_5 = torch.einsum("lmjnk, ijk -> limn", t_4, in_1)

		# No need to crop the output tensor.
		y = t_5

		return y

class kernel_generated_3(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([192, 2, 18]),
			torch.randn([2, 48, 18]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]
		in_2 = self.weights[1]

		# Perform contraction.
		t_3 = torch.einsum("limn, kij -> lnkmj", in_0, in_2)

		# No contraction needed.
		t_4 = t_3

		# [H]@Merge6f1a0d6b662fae84, [s]@Merge6f1a0d6b662fae85 -> [s*H]@Shift594e1a6314829db7
		t_4 = torch.reshape(t_4, (1, 56, 28, 18, ))

		# [s*H]@Shift594e1a6314829db7 -> [s*H]@Split7ee86503d19bbef6
		t_4 = torch.roll(t_4, self.shift_direction, 1)

		# [s*H]@Split7ee86503d19bbef6 -> [H]@Iterator96123ba3184da39c, [s]@Shareb15a7faee0f8b868
		t_4 = torch.reshape(t_4, (1, 28, 2, 28, 18, ))

		# Perform contraction.
		t_5 = torch.einsum("lmjnk, ijk -> limn", t_4, in_1)

		# No need to crop the output tensor.
		y = t_5

		return y

class kernel_generated_4(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([256, 2, 18]),
			torch.randn([2, 64, 18]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]
		in_2 = self.weights[1]

		# Perform contraction.
		t_3 = torch.einsum("limn, kij -> lnkmj", in_0, in_2)

		# No contraction needed.
		t_4 = t_3

		# [H]@Merge6f1a0d6b662fae84, [s]@Merge6f1a0d6b662fae85 -> [s*H]@Shift594e1a6314829db7
		t_4 = torch.reshape(t_4, (1, 56, 28, 18, ))

		# [s*H]@Shift594e1a6314829db7 -> [s*H]@Split7ee86503d19bbef6
		t_4 = torch.roll(t_4, self.shift_direction, 1)

		# [s*H]@Split7ee86503d19bbef6 -> [H]@Iterator96123ba3184da39c, [s]@Shareb15a7faee0f8b868
		t_4 = torch.reshape(t_4, (1, 28, 2, 28, 18, ))

		# Perform contraction.
		t_5 = torch.einsum("lmjnk, ijk -> limn", t_4, in_1)

		# No need to crop the output tensor.
		y = t_5

		return y

