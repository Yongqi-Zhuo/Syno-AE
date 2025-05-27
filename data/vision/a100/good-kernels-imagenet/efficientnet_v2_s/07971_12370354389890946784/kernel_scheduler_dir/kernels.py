import torch
import random
"""
digraph kernel_preview {
newrank = true;

// Stage tensor.
subgraph cluster_subgraph_0 {
    label = "Subgraph 0";
    // Reductions.
    reduce_0x7fc32c004e58 [label="Sum", shape=box];
    reduce_0x7fc32c0052a8 [label="Sum", shape=box];
    // Output.
    subgraph cluster_subgraph_0_out {
        label = "";
        interface_0_out_0x5604185d74e0 [label="N", shape=none];
        interface_0_out_0x5604185d7508 [label="C_out", shape=none];
        interface_0_out_0x5604185d7530 [label="H", shape=none];
        interface_0_out_0x5604185d7558 [label="H", shape=none];
    }
    {
        rank = same;
        reduce_0x7fc32c004e58;
        reduce_0x7fc32c0052a8;
        interface_0_out_0x5604185d74e0;
        interface_0_out_0x5604185d7508;
        interface_0_out_0x5604185d7530;
        interface_0_out_0x5604185d7558;
    }
    // Input 0.
    subgraph cluster_subgraph_0_in_0 {
        label = "";
        interface_0_in_0x5604185d74e0 [label="N", shape=none];
        interface_0_in_0x5604185d7530 [label="H", shape=none];
        interface_0_in_0x560419917570 [label="s", shape=none];
        interface_0_in_0x5604185d7558 [label="H", shape=none];
        interface_0_in_0x56041991cb00 [label="k_1^2*s", shape=none];
    }
    // Input 1.
    subgraph cluster_subgraph_0_in_1 {
        label = "";
        interface_0_in_0x5604199172b8 [label="C_out", shape=none];
        interface_0_in_0x560419917588 [label="s", shape=none];
        interface_0_in_0x56041991cb18 [label="k_1^2*s", shape=none];
    }
    {
        rank = same;
        interface_0_in_0x5604185d74e0;
        interface_0_in_0x5604185d7530;
        interface_0_in_0x560419917570;
        interface_0_in_0x5604185d7558;
        interface_0_in_0x56041991cb00;
        interface_0_in_0x5604199172b8;
        interface_0_in_0x560419917588;
        interface_0_in_0x56041991cb18;
    }
    // Op's.
    op_0x560419917280 [label="Share"];
    op_0x560419917550 [label="Share"];
    op_0x560419917758 [label="Expand"];
    op_0x56041991cae0 [label="Share"];
    // Dimension's.
    interface_0_in_0x5604185d74e0 -> interface_0_out_0x5604185d74e0 [label="N"];
    op_0x560419917280 -> interface_0_out_0x5604185d7508 [label="C_out"];
    interface_0_in_0x5604185d7530 -> interface_0_out_0x5604185d7530 [label="H"];
    interface_0_in_0x5604185d7558 -> interface_0_out_0x5604185d7558 [label="H"];
    op_0x560419917758 -> op_0x560419917280 [label="C_out"];
    interface_0_in_0x5604199172b8 -> op_0x560419917280 [label="C_out"];
    interface_0_in_0x560419917570 -> op_0x560419917550 [label="s"];
    interface_0_in_0x560419917588 -> op_0x560419917550 [label="s"];
    interface_0_in_0x56041991cb00 -> op_0x56041991cae0 [label="k_1^2*s"];
    interface_0_in_0x56041991cb18 -> op_0x56041991cae0 [label="k_1^2*s"];
    op_0x560419917550 -> reduce_0x7fc32c004e58 [label="s"];
    op_0x56041991cae0 -> reduce_0x7fc32c0052a8 [label="k_1^2*s"];
}

// Stage tensor.
subgraph cluster_subgraph_1 {
    label = "Subgraph 1";
    // Reductions.
    // Output.
    subgraph cluster_subgraph_1_out {
        label = "";
        interface_1_out_0x5604185d74e0 [label="N", shape=none];
        interface_1_out_0x5604185d7530 [label="H", shape=none];
        interface_1_out_0x560419917570 [label="s", shape=none];
        interface_1_out_0x5604185d7558 [label="H", shape=none];
        interface_1_out_0x56041991cb00 [label="k_1^2*s", shape=none];
    }
    {
        rank = same;
        interface_1_out_0x5604185d74e0;
        interface_1_out_0x5604185d7530;
        interface_1_out_0x560419917570;
        interface_1_out_0x5604185d7558;
        interface_1_out_0x56041991cb00;
    }
    // Input 0.
    subgraph cluster_subgraph_1_in_0 {
        label = "";
        interface_1_in_0x5604185d74e0 [label="N", shape=none];
        interface_1_in_0x560419920f40 [label="H", shape=none];
        interface_1_in_0x560419920f58 [label="s", shape=none];
        interface_1_in_0x5604185d7558 [label="H", shape=none];
        interface_1_in_0x56041991cb00 [label="k_1^2*s", shape=none];
    }
    {
        rank = same;
        interface_1_in_0x5604185d74e0;
        interface_1_in_0x560419920f40;
        interface_1_in_0x560419920f58;
        interface_1_in_0x5604185d7558;
        interface_1_in_0x56041991cb00;
    }
    // Op's.
    op_0x560419918160 [label="Shift"];
    op_0x560419920f00 [label="Merge"];
    op_0x5604199441c0 [label="Split"];
    // Dimension's.
    interface_1_in_0x5604185d74e0 -> interface_1_out_0x5604185d74e0 [label="N"];
    op_0x5604199441c0 -> interface_1_out_0x5604185d7530 [label="H"];
    interface_1_in_0x5604185d7558 -> interface_1_out_0x5604185d7558 [label="H"];
    op_0x5604199441c0 -> interface_1_out_0x560419917570 [label="s"];
    op_0x560419920f00 -> op_0x560419918160 [label="s*H"];
    interface_1_in_0x56041991cb00 -> interface_1_out_0x56041991cb00 [label="k_1^2*s"];
    interface_1_in_0x560419920f40 -> op_0x560419920f00 [label="H"];
    interface_1_in_0x560419920f58 -> op_0x560419920f00 [label="s"];
    op_0x560419918160 -> op_0x5604199441c0 [label="s*H"];
}

// Stage tensor.
subgraph cluster_subgraph_2 {
    label = "Subgraph 2";
    // Reductions.
    reduce_0x7fc32c007b70 [label="Sum", shape=box];
    // Output.
    subgraph cluster_subgraph_2_out {
        label = "";
        interface_2_out_0x5604185d74e0 [label="N", shape=none];
        interface_2_out_0x560419920f40 [label="H", shape=none];
        interface_2_out_0x560419920f58 [label="s", shape=none];
        interface_2_out_0x5604185d7558 [label="H", shape=none];
        interface_2_out_0x56041991cb00 [label="k_1^2*s", shape=none];
    }
    {
        rank = same;
        reduce_0x7fc32c007b70;
        interface_2_out_0x5604185d74e0;
        interface_2_out_0x560419920f40;
        interface_2_out_0x560419920f58;
        interface_2_out_0x5604185d7558;
        interface_2_out_0x56041991cb00;
    }
    // Input 0.
    subgraph cluster_subgraph_2_in_0 {
        label = "";
        interface_2_in_0x5604185d74e0 [label="N", shape=none];
        interface_2_in_0x560419917660 [label="C_in", shape=none];
        interface_2_in_0x5604185d7558 [label="H", shape=none];
        interface_2_in_0x560419920f40 [label="H", shape=none];
    }
    // Input 1.
    subgraph cluster_subgraph_2_in_1 {
        label = "";
        interface_2_in_0x56041991cc08 [label="s", shape=none];
        interface_2_in_0x560419917678 [label="C_in", shape=none];
        interface_2_in_0x56041991cb68 [label="k_1^2*s", shape=none];
    }
    {
        rank = same;
        interface_2_in_0x5604185d74e0;
        interface_2_in_0x560419917660;
        interface_2_in_0x5604185d7558;
        interface_2_in_0x560419920f40;
        interface_2_in_0x56041991cc08;
        interface_2_in_0x560419917678;
        interface_2_in_0x56041991cb68;
    }
    // Op's.
    op_0x560419917640 [label="Share"];
    op_0x560419917878 [label="Expand"];
    op_0x560419917898 [label="Expand"];
    op_0x56041991cb30 [label="Share"];
    op_0x56041991cbd0 [label="Share"];
    // Dimension's.
    interface_2_in_0x5604185d74e0 -> interface_2_out_0x5604185d74e0 [label="N"];
    interface_2_in_0x5604185d7558 -> interface_2_out_0x5604185d7558 [label="H"];
    interface_2_in_0x560419917660 -> op_0x560419917640 [label="C_in"];
    interface_2_in_0x560419917678 -> op_0x560419917640 [label="C_in"];
    op_0x56041991cb30 -> interface_2_out_0x56041991cb00 [label="k_1^2*s"];
    op_0x560419917878 -> op_0x56041991cb30 [label="k_1^2*s"];
    interface_2_in_0x56041991cb68 -> op_0x56041991cb30 [label="k_1^2*s"];
    op_0x560419917898 -> op_0x56041991cbd0 [label="s"];
    interface_2_in_0x56041991cc08 -> op_0x56041991cbd0 [label="s"];
    interface_2_in_0x560419920f40 -> interface_2_out_0x560419920f40 [label="H"];
    op_0x56041991cbd0 -> interface_2_out_0x560419920f58 [label="s"];
    op_0x560419917640 -> reduce_0x7fc32c007b70 [label="C_in"];
}

// Input tensor.
subgraph cluster_subgraph_3 {
    label = "Input 0";
    interface_3_out_0x5604185d74e0 [label="N", shape=none];
    interface_3_out_0x560419917660 [label="C_in", shape=none];
    interface_3_out_0x5604185d7558 [label="H", shape=none];
    interface_3_out_0x560419920f40 [label="H", shape=none];
}

interface_3_out_0x5604185d74e0 -> interface_2_in_0x5604185d74e0;
interface_3_out_0x560419917660 -> interface_2_in_0x560419917660;
interface_3_out_0x5604185d7558 -> interface_2_in_0x5604185d7558;
interface_3_out_0x560419920f40 -> interface_2_in_0x560419920f40;

// Input tensor.
subgraph cluster_subgraph_4 {
    label = "Input 2";
    interface_4_out_0x56041991cc08 [label="s", shape=none];
    interface_4_out_0x560419917678 [label="C_in", shape=none];
    interface_4_out_0x56041991cb68 [label="k_1^2*s", shape=none];
}

interface_4_out_0x56041991cc08 -> interface_2_in_0x56041991cc08;
interface_4_out_0x560419917678 -> interface_2_in_0x560419917678;
interface_4_out_0x56041991cb68 -> interface_2_in_0x56041991cb68;

interface_2_out_0x5604185d74e0 -> interface_1_in_0x5604185d74e0;
interface_2_out_0x560419920f40 -> interface_1_in_0x560419920f40;
interface_2_out_0x560419920f58 -> interface_1_in_0x560419920f58;
interface_2_out_0x5604185d7558 -> interface_1_in_0x5604185d7558;
interface_2_out_0x56041991cb00 -> interface_1_in_0x56041991cb00;

interface_1_out_0x5604185d74e0 -> interface_0_in_0x5604185d74e0;
interface_1_out_0x5604185d7530 -> interface_0_in_0x5604185d7530;
interface_1_out_0x560419917570 -> interface_0_in_0x560419917570;
interface_1_out_0x5604185d7558 -> interface_0_in_0x5604185d7558;
interface_1_out_0x56041991cb00 -> interface_0_in_0x56041991cb00;

// Input tensor.
subgraph cluster_subgraph_5 {
    label = "Input 1";
    interface_5_out_0x5604199172b8 [label="C_out", shape=none];
    interface_5_out_0x560419917588 [label="s", shape=none];
    interface_5_out_0x56041991cb18 [label="k_1^2*s", shape=none];
}

interface_5_out_0x5604199172b8 -> interface_0_in_0x5604199172b8;
interface_5_out_0x560419917588 -> interface_0_in_0x560419917588;
interface_5_out_0x56041991cb18 -> interface_0_in_0x56041991cb18;

{
    rank = same;
    interface_3_out_0x5604185d74e0;
    interface_3_out_0x560419917660;
    interface_3_out_0x5604185d7558;
    interface_3_out_0x560419920f40;
    interface_5_out_0x5604199172b8;
    interface_5_out_0x560419917588;
    interface_5_out_0x56041991cb18;
    interface_4_out_0x56041991cc08;
    interface_4_out_0x560419917678;
    interface_4_out_0x56041991cb68;
}
subgraph cluster_subgraph_output {
    label = "Output";
    interface_6_in_0x5604185d74e0 [label="N", shape=none];
    interface_6_in_0x5604185d7508 [label="C_out", shape=none];
    interface_6_in_0x5604185d7530 [label="H", shape=none];
    interface_6_in_0x5604185d7558 [label="H", shape=none];
}
interface_0_out_0x5604185d74e0 -> interface_6_in_0x5604185d74e0;
interface_0_out_0x5604185d7508 -> interface_6_in_0x5604185d7508;
interface_0_out_0x5604185d7530 -> interface_6_in_0x5604185d7530;
interface_0_out_0x5604185d7558 -> interface_6_in_0x5604185d7558;

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

