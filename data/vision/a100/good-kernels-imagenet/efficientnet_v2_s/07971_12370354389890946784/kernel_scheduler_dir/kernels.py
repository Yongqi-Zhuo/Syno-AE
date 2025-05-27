import torch
import random
"""
digraph kernel_preview {
newrank = true;

// Stage tensor.
subgraph cluster_subgraph_0 {
    label = "Subgraph 0";
    // Reductions.
    reduce_0x7fdbac002e58 [label="Sum", shape=box];
    reduce_0x7fdbac0032a8 [label="Sum", shape=box];
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
        reduce_0x7fdbac002e58;
        reduce_0x7fdbac0032a8;
        interface_0_out_0x56459a9d6050;
        interface_0_out_0x56459a9d6078;
        interface_0_out_0x56459a9d60a0;
        interface_0_out_0x56459a9d60c8;
    }
    // Input 0.
    subgraph cluster_subgraph_0_in_0 {
        label = "";
        interface_0_in_0x56459a9d6050 [label="N", shape=none];
        interface_0_in_0x56459a9d60a0 [label="H", shape=none];
        interface_0_in_0x56459c2586b0 [label="s", shape=none];
        interface_0_in_0x56459a9d60c8 [label="H", shape=none];
        interface_0_in_0x56459c25ee60 [label="k_1^2*s", shape=none];
    }
    // Input 1.
    subgraph cluster_subgraph_0_in_1 {
        label = "";
        interface_0_in_0x56459c2582b8 [label="C_out", shape=none];
        interface_0_in_0x56459c2586c8 [label="s", shape=none];
        interface_0_in_0x56459c25ee78 [label="k_1^2*s", shape=none];
    }
    {
        rank = same;
        interface_0_in_0x56459a9d6050;
        interface_0_in_0x56459a9d60a0;
        interface_0_in_0x56459c2586b0;
        interface_0_in_0x56459a9d60c8;
        interface_0_in_0x56459c25ee60;
        interface_0_in_0x56459c2582b8;
        interface_0_in_0x56459c2586c8;
        interface_0_in_0x56459c25ee78;
    }
    // Op's.
    op_0x56459c258280 [label="Share"];
    op_0x56459c258690 [label="Share"];
    op_0x56459c258778 [label="Expand"];
    op_0x56459c25ee40 [label="Share"];
    // Dimension's.
    interface_0_in_0x56459a9d6050 -> interface_0_out_0x56459a9d6050 [label="N"];
    op_0x56459c258280 -> interface_0_out_0x56459a9d6078 [label="C_out"];
    interface_0_in_0x56459a9d60a0 -> interface_0_out_0x56459a9d60a0 [label="H"];
    interface_0_in_0x56459a9d60c8 -> interface_0_out_0x56459a9d60c8 [label="H"];
    op_0x56459c258778 -> op_0x56459c258280 [label="C_out"];
    interface_0_in_0x56459c2582b8 -> op_0x56459c258280 [label="C_out"];
    interface_0_in_0x56459c2586b0 -> op_0x56459c258690 [label="s"];
    interface_0_in_0x56459c2586c8 -> op_0x56459c258690 [label="s"];
    interface_0_in_0x56459c25ee60 -> op_0x56459c25ee40 [label="k_1^2*s"];
    interface_0_in_0x56459c25ee78 -> op_0x56459c25ee40 [label="k_1^2*s"];
    op_0x56459c258690 -> reduce_0x7fdbac002e58 [label="s"];
    op_0x56459c25ee40 -> reduce_0x7fdbac0032a8 [label="k_1^2*s"];
}

// Stage tensor.
subgraph cluster_subgraph_1 {
    label = "Subgraph 1";
    // Reductions.
    // Output.
    subgraph cluster_subgraph_1_out {
        label = "";
        interface_1_out_0x56459a9d6050 [label="N", shape=none];
        interface_1_out_0x56459a9d60a0 [label="H", shape=none];
        interface_1_out_0x56459c2586b0 [label="s", shape=none];
        interface_1_out_0x56459a9d60c8 [label="H", shape=none];
        interface_1_out_0x56459c25ee60 [label="k_1^2*s", shape=none];
    }
    {
        rank = same;
        interface_1_out_0x56459a9d6050;
        interface_1_out_0x56459a9d60a0;
        interface_1_out_0x56459c2586b0;
        interface_1_out_0x56459a9d60c8;
        interface_1_out_0x56459c25ee60;
    }
    // Input 0.
    subgraph cluster_subgraph_1_in_0 {
        label = "";
        interface_1_in_0x56459a9d6050 [label="N", shape=none];
        interface_1_in_0x56459c2606a0 [label="H", shape=none];
        interface_1_in_0x56459c2606b8 [label="s", shape=none];
        interface_1_in_0x56459a9d60c8 [label="H", shape=none];
        interface_1_in_0x56459c25ee60 [label="k_1^2*s", shape=none];
    }
    {
        rank = same;
        interface_1_in_0x56459a9d6050;
        interface_1_in_0x56459c2606a0;
        interface_1_in_0x56459c2606b8;
        interface_1_in_0x56459a9d60c8;
        interface_1_in_0x56459c25ee60;
    }
    // Op's.
    op_0x56459c2592d0 [label="Shift"];
    op_0x56459c260660 [label="Merge"];
    op_0x56459c268170 [label="Split"];
    // Dimension's.
    interface_1_in_0x56459a9d6050 -> interface_1_out_0x56459a9d6050 [label="N"];
    op_0x56459c268170 -> interface_1_out_0x56459a9d60a0 [label="H"];
    interface_1_in_0x56459a9d60c8 -> interface_1_out_0x56459a9d60c8 [label="H"];
    op_0x56459c268170 -> interface_1_out_0x56459c2586b0 [label="s"];
    op_0x56459c260660 -> op_0x56459c2592d0 [label="s*H"];
    interface_1_in_0x56459c25ee60 -> interface_1_out_0x56459c25ee60 [label="k_1^2*s"];
    interface_1_in_0x56459c2606a0 -> op_0x56459c260660 [label="H"];
    interface_1_in_0x56459c2606b8 -> op_0x56459c260660 [label="s"];
    op_0x56459c2592d0 -> op_0x56459c268170 [label="s*H"];
}

// Stage tensor.
subgraph cluster_subgraph_2 {
    label = "Subgraph 2";
    // Reductions.
    reduce_0x7fdbac005c70 [label="Sum", shape=box];
    // Output.
    subgraph cluster_subgraph_2_out {
        label = "";
        interface_2_out_0x56459a9d6050 [label="N", shape=none];
        interface_2_out_0x56459c2606a0 [label="H", shape=none];
        interface_2_out_0x56459c2606b8 [label="s", shape=none];
        interface_2_out_0x56459a9d60c8 [label="H", shape=none];
        interface_2_out_0x56459c25ee60 [label="k_1^2*s", shape=none];
    }
    {
        rank = same;
        reduce_0x7fdbac005c70;
        interface_2_out_0x56459a9d6050;
        interface_2_out_0x56459c2606a0;
        interface_2_out_0x56459c2606b8;
        interface_2_out_0x56459a9d60c8;
        interface_2_out_0x56459c25ee60;
    }
    // Input 0.
    subgraph cluster_subgraph_2_in_0 {
        label = "";
        interface_2_in_0x56459a9d6050 [label="N", shape=none];
        interface_2_in_0x56459c25eaf0 [label="C_in", shape=none];
        interface_2_in_0x56459a9d60c8 [label="H", shape=none];
        interface_2_in_0x56459c2606a0 [label="H", shape=none];
    }
    // Input 1.
    subgraph cluster_subgraph_2_in_1 {
        label = "";
        interface_2_in_0x56459c25ef68 [label="s", shape=none];
        interface_2_in_0x56459c25eb08 [label="C_in", shape=none];
        interface_2_in_0x56459c25eec8 [label="k_1^2*s", shape=none];
    }
    {
        rank = same;
        interface_2_in_0x56459a9d6050;
        interface_2_in_0x56459c25eaf0;
        interface_2_in_0x56459a9d60c8;
        interface_2_in_0x56459c2606a0;
        interface_2_in_0x56459c25ef68;
        interface_2_in_0x56459c25eb08;
        interface_2_in_0x56459c25eec8;
    }
    // Op's.
    op_0x56459c2588d8 [label="Expand"];
    op_0x56459c2588f8 [label="Expand"];
    op_0x56459c25ead0 [label="Share"];
    op_0x56459c25ee90 [label="Share"];
    op_0x56459c25ef30 [label="Share"];
    // Dimension's.
    interface_2_in_0x56459a9d6050 -> interface_2_out_0x56459a9d6050 [label="N"];
    interface_2_in_0x56459a9d60c8 -> interface_2_out_0x56459a9d60c8 [label="H"];
    interface_2_in_0x56459c25eaf0 -> op_0x56459c25ead0 [label="C_in"];
    interface_2_in_0x56459c25eb08 -> op_0x56459c25ead0 [label="C_in"];
    op_0x56459c25ee90 -> interface_2_out_0x56459c25ee60 [label="k_1^2*s"];
    op_0x56459c2588d8 -> op_0x56459c25ee90 [label="k_1^2*s"];
    interface_2_in_0x56459c25eec8 -> op_0x56459c25ee90 [label="k_1^2*s"];
    op_0x56459c2588f8 -> op_0x56459c25ef30 [label="s"];
    interface_2_in_0x56459c25ef68 -> op_0x56459c25ef30 [label="s"];
    interface_2_in_0x56459c2606a0 -> interface_2_out_0x56459c2606a0 [label="H"];
    op_0x56459c25ef30 -> interface_2_out_0x56459c2606b8 [label="s"];
    op_0x56459c25ead0 -> reduce_0x7fdbac005c70 [label="C_in"];
}

// Input tensor.
subgraph cluster_subgraph_3 {
    label = "Input 0";
    interface_3_out_0x56459a9d6050 [label="N", shape=none];
    interface_3_out_0x56459c25eaf0 [label="C_in", shape=none];
    interface_3_out_0x56459a9d60c8 [label="H", shape=none];
    interface_3_out_0x56459c2606a0 [label="H", shape=none];
}

interface_3_out_0x56459a9d6050 -> interface_2_in_0x56459a9d6050;
interface_3_out_0x56459c25eaf0 -> interface_2_in_0x56459c25eaf0;
interface_3_out_0x56459a9d60c8 -> interface_2_in_0x56459a9d60c8;
interface_3_out_0x56459c2606a0 -> interface_2_in_0x56459c2606a0;

// Input tensor.
subgraph cluster_subgraph_4 {
    label = "Input 2";
    interface_4_out_0x56459c25ef68 [label="s", shape=none];
    interface_4_out_0x56459c25eb08 [label="C_in", shape=none];
    interface_4_out_0x56459c25eec8 [label="k_1^2*s", shape=none];
}

interface_4_out_0x56459c25ef68 -> interface_2_in_0x56459c25ef68;
interface_4_out_0x56459c25eb08 -> interface_2_in_0x56459c25eb08;
interface_4_out_0x56459c25eec8 -> interface_2_in_0x56459c25eec8;

interface_2_out_0x56459a9d6050 -> interface_1_in_0x56459a9d6050;
interface_2_out_0x56459c2606a0 -> interface_1_in_0x56459c2606a0;
interface_2_out_0x56459c2606b8 -> interface_1_in_0x56459c2606b8;
interface_2_out_0x56459a9d60c8 -> interface_1_in_0x56459a9d60c8;
interface_2_out_0x56459c25ee60 -> interface_1_in_0x56459c25ee60;

interface_1_out_0x56459a9d6050 -> interface_0_in_0x56459a9d6050;
interface_1_out_0x56459a9d60a0 -> interface_0_in_0x56459a9d60a0;
interface_1_out_0x56459c2586b0 -> interface_0_in_0x56459c2586b0;
interface_1_out_0x56459a9d60c8 -> interface_0_in_0x56459a9d60c8;
interface_1_out_0x56459c25ee60 -> interface_0_in_0x56459c25ee60;

// Input tensor.
subgraph cluster_subgraph_5 {
    label = "Input 1";
    interface_5_out_0x56459c2582b8 [label="C_out", shape=none];
    interface_5_out_0x56459c2586c8 [label="s", shape=none];
    interface_5_out_0x56459c25ee78 [label="k_1^2*s", shape=none];
}

interface_5_out_0x56459c2582b8 -> interface_0_in_0x56459c2582b8;
interface_5_out_0x56459c2586c8 -> interface_0_in_0x56459c2586c8;
interface_5_out_0x56459c25ee78 -> interface_0_in_0x56459c25ee78;

{
    rank = same;
    interface_3_out_0x56459a9d6050;
    interface_3_out_0x56459c25eaf0;
    interface_3_out_0x56459a9d60c8;
    interface_3_out_0x56459c2606a0;
    interface_5_out_0x56459c2582b8;
    interface_5_out_0x56459c2586c8;
    interface_5_out_0x56459c25ee78;
    interface_4_out_0x56459c25ef68;
    interface_4_out_0x56459c25eb08;
    interface_4_out_0x56459c25eec8;
}
subgraph cluster_subgraph_output {
    label = "Output";
    interface_6_in_0x56459a9d6050 [label="N", shape=none];
    interface_6_in_0x56459a9d6078 [label="C_out", shape=none];
    interface_6_in_0x56459a9d60a0 [label="H", shape=none];
    interface_6_in_0x56459a9d60c8 [label="H", shape=none];
}
interface_0_out_0x56459a9d6050 -> interface_6_in_0x56459a9d6050;
interface_0_out_0x56459a9d6078 -> interface_6_in_0x56459a9d6078;
interface_0_out_0x56459a9d60a0 -> interface_6_in_0x56459a9d60a0;
interface_0_out_0x56459a9d60c8 -> interface_6_in_0x56459a9d60c8;

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

