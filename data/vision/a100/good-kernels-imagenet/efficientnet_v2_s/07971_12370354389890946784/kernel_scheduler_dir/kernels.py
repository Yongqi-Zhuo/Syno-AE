import torch
import random
"""
digraph kernel_preview {
newrank = true;

// Stage tensor.
subgraph cluster_subgraph_0 {
    label = "Subgraph 0";
    // Reductions.
    reduce_0x7fc7f0002f58 [label="Sum", shape=box];
    reduce_0x7fc7f00033a8 [label="Sum", shape=box];
    // Output.
    subgraph cluster_subgraph_0_out {
        label = "";
        interface_0_out_0x5581660a87e0 [label="N", shape=none];
        interface_0_out_0x5581660a8808 [label="C_out", shape=none];
        interface_0_out_0x5581660a8830 [label="H", shape=none];
        interface_0_out_0x5581660a8858 [label="H", shape=none];
    }
    {
        rank = same;
        reduce_0x7fc7f0002f58;
        reduce_0x7fc7f00033a8;
        interface_0_out_0x5581660a87e0;
        interface_0_out_0x5581660a8808;
        interface_0_out_0x5581660a8830;
        interface_0_out_0x5581660a8858;
    }
    // Input 0.
    subgraph cluster_subgraph_0_in_0 {
        label = "";
        interface_0_in_0x5581660a87e0 [label="N", shape=none];
        interface_0_in_0x5581660a8830 [label="H", shape=none];
        interface_0_in_0x7fcf58005310 [label="s", shape=none];
        interface_0_in_0x5581660a8858 [label="H", shape=none];
        interface_0_in_0x7fcbc40054a0 [label="k_1^2*s", shape=none];
    }
    // Input 1.
    subgraph cluster_subgraph_0_in_1 {
        label = "";
        interface_0_in_0x7fcf84003f38 [label="C_out", shape=none];
        interface_0_in_0x7fcf58005328 [label="s", shape=none];
        interface_0_in_0x7fcbc40054b8 [label="k_1^2*s", shape=none];
    }
    {
        rank = same;
        interface_0_in_0x5581660a87e0;
        interface_0_in_0x5581660a8830;
        interface_0_in_0x7fcf58005310;
        interface_0_in_0x5581660a8858;
        interface_0_in_0x7fcbc40054a0;
        interface_0_in_0x7fcf84003f38;
        interface_0_in_0x7fcf58005328;
        interface_0_in_0x7fcbc40054b8;
    }
    // Op's.
    op_0x7fcbc4005480 [label="Share"];
    op_0x7fcf580052f0 [label="Share"];
    op_0x7fcf84003f00 [label="Share"];
    op_0x7fcf84004638 [label="Expand"];
    // Dimension's.
    interface_0_in_0x5581660a87e0 -> interface_0_out_0x5581660a87e0 [label="N"];
    op_0x7fcf84003f00 -> interface_0_out_0x5581660a8808 [label="C_out"];
    interface_0_in_0x5581660a8830 -> interface_0_out_0x5581660a8830 [label="H"];
    interface_0_in_0x5581660a8858 -> interface_0_out_0x5581660a8858 [label="H"];
    op_0x7fcf580052f0 -> reduce_0x7fc7f0002f58 [label="s"];
    op_0x7fcbc4005480 -> reduce_0x7fc7f00033a8 [label="k_1^2*s"];
    interface_0_in_0x7fcbc40054a0 -> op_0x7fcbc4005480 [label="k_1^2*s"];
    interface_0_in_0x7fcbc40054b8 -> op_0x7fcbc4005480 [label="k_1^2*s"];
    interface_0_in_0x7fcf58005310 -> op_0x7fcf580052f0 [label="s"];
    interface_0_in_0x7fcf58005328 -> op_0x7fcf580052f0 [label="s"];
    op_0x7fcf84004638 -> op_0x7fcf84003f00 [label="C_out"];
    interface_0_in_0x7fcf84003f38 -> op_0x7fcf84003f00 [label="C_out"];
}

// Stage tensor.
subgraph cluster_subgraph_1 {
    label = "Subgraph 1";
    // Reductions.
    // Output.
    subgraph cluster_subgraph_1_out {
        label = "";
        interface_1_out_0x5581660a87e0 [label="N", shape=none];
        interface_1_out_0x5581660a8830 [label="H", shape=none];
        interface_1_out_0x7fcf58005310 [label="s", shape=none];
        interface_1_out_0x5581660a8858 [label="H", shape=none];
        interface_1_out_0x7fcbc40054a0 [label="k_1^2*s", shape=none];
    }
    {
        rank = same;
        interface_1_out_0x5581660a87e0;
        interface_1_out_0x5581660a8830;
        interface_1_out_0x7fcf58005310;
        interface_1_out_0x5581660a8858;
        interface_1_out_0x7fcbc40054a0;
    }
    // Input 0.
    subgraph cluster_subgraph_1_in_0 {
        label = "";
        interface_1_in_0x5581660a87e0 [label="N", shape=none];
        interface_1_in_0x7fce44007bf0 [label="H", shape=none];
        interface_1_in_0x7fce44007c08 [label="s", shape=none];
        interface_1_in_0x5581660a8858 [label="H", shape=none];
        interface_1_in_0x7fcbc40054a0 [label="k_1^2*s", shape=none];
    }
    {
        rank = same;
        interface_1_in_0x5581660a87e0;
        interface_1_in_0x7fce44007bf0;
        interface_1_in_0x7fce44007c08;
        interface_1_in_0x5581660a8858;
        interface_1_in_0x7fcbc40054a0;
    }
    // Op's.
    op_0x7fc67800a1c0 [label="Shift"];
    op_0x7fccc8012e10 [label="Split"];
    op_0x7fce44007bb0 [label="Merge"];
    // Dimension's.
    interface_1_in_0x5581660a87e0 -> interface_1_out_0x5581660a87e0 [label="N"];
    op_0x7fccc8012e10 -> interface_1_out_0x5581660a8830 [label="H"];
    interface_1_in_0x5581660a8858 -> interface_1_out_0x5581660a8858 [label="H"];
    op_0x7fce44007bb0 -> op_0x7fc67800a1c0 [label="s*H"];
    interface_1_in_0x7fcbc40054a0 -> interface_1_out_0x7fcbc40054a0 [label="k_1^2*s"];
    op_0x7fc67800a1c0 -> op_0x7fccc8012e10 [label="s*H"];
    interface_1_in_0x7fce44007bf0 -> op_0x7fce44007bb0 [label="H"];
    interface_1_in_0x7fce44007c08 -> op_0x7fce44007bb0 [label="s"];
    op_0x7fccc8012e10 -> interface_1_out_0x7fcf58005310 [label="s"];
}

// Stage tensor.
subgraph cluster_subgraph_2 {
    label = "Subgraph 2";
    // Reductions.
    reduce_0x7fc7f0005e70 [label="Sum", shape=box];
    // Output.
    subgraph cluster_subgraph_2_out {
        label = "";
        interface_2_out_0x5581660a87e0 [label="N", shape=none];
        interface_2_out_0x7fce44007bf0 [label="H", shape=none];
        interface_2_out_0x7fce44007c08 [label="s", shape=none];
        interface_2_out_0x5581660a8858 [label="H", shape=none];
        interface_2_out_0x7fcbc40054a0 [label="k_1^2*s", shape=none];
    }
    {
        rank = same;
        reduce_0x7fc7f0005e70;
        interface_2_out_0x5581660a87e0;
        interface_2_out_0x7fce44007bf0;
        interface_2_out_0x7fce44007c08;
        interface_2_out_0x5581660a8858;
        interface_2_out_0x7fcbc40054a0;
    }
    // Input 0.
    subgraph cluster_subgraph_2_in_0 {
        label = "";
        interface_2_in_0x5581660a87e0 [label="N", shape=none];
        interface_2_in_0x7fc950008e30 [label="C_in", shape=none];
        interface_2_in_0x5581660a8858 [label="H", shape=none];
        interface_2_in_0x7fce44007bf0 [label="H", shape=none];
    }
    // Input 1.
    subgraph cluster_subgraph_2_in_1 {
        label = "";
        interface_2_in_0x7fcf1001f918 [label="s", shape=none];
        interface_2_in_0x7fc950008e48 [label="C_in", shape=none];
        interface_2_in_0x7fc950008c18 [label="k_1^2*s", shape=none];
    }
    {
        rank = same;
        interface_2_in_0x5581660a87e0;
        interface_2_in_0x7fc950008e30;
        interface_2_in_0x5581660a8858;
        interface_2_in_0x7fce44007bf0;
        interface_2_in_0x7fcf1001f918;
        interface_2_in_0x7fc950008e48;
        interface_2_in_0x7fc950008c18;
    }
    // Op's.
    op_0x7fc950008be0 [label="Share"];
    op_0x7fc950008e10 [label="Share"];
    op_0x7fce2c019a58 [label="Expand"];
    op_0x7fcf1001f8e0 [label="Share"];
    op_0x7fcf84004998 [label="Expand"];
    // Dimension's.
    interface_2_in_0x5581660a87e0 -> interface_2_out_0x5581660a87e0 [label="N"];
    interface_2_in_0x5581660a8858 -> interface_2_out_0x5581660a8858 [label="H"];
    op_0x7fc950008e10 -> reduce_0x7fc7f0005e70 [label="C_in"];
    op_0x7fcf84004998 -> op_0x7fc950008be0 [label="k_1^2*s"];
    interface_2_in_0x7fc950008c18 -> op_0x7fc950008be0 [label="k_1^2*s"];
    interface_2_in_0x7fc950008e30 -> op_0x7fc950008e10 [label="C_in"];
    interface_2_in_0x7fc950008e48 -> op_0x7fc950008e10 [label="C_in"];
    op_0x7fc950008be0 -> interface_2_out_0x7fcbc40054a0 [label="k_1^2*s"];
    interface_2_in_0x7fce44007bf0 -> interface_2_out_0x7fce44007bf0 [label="H"];
    op_0x7fcf1001f8e0 -> interface_2_out_0x7fce44007c08 [label="s"];
    op_0x7fce2c019a58 -> op_0x7fcf1001f8e0 [label="s"];
    interface_2_in_0x7fcf1001f918 -> op_0x7fcf1001f8e0 [label="s"];
}

// Input tensor.
subgraph cluster_subgraph_3 {
    label = "Input 0";
    interface_3_out_0x5581660a87e0 [label="N", shape=none];
    interface_3_out_0x7fc950008e30 [label="C_in", shape=none];
    interface_3_out_0x5581660a8858 [label="H", shape=none];
    interface_3_out_0x7fce44007bf0 [label="H", shape=none];
}

interface_3_out_0x5581660a87e0 -> interface_2_in_0x5581660a87e0;
interface_3_out_0x7fc950008e30 -> interface_2_in_0x7fc950008e30;
interface_3_out_0x5581660a8858 -> interface_2_in_0x5581660a8858;
interface_3_out_0x7fce44007bf0 -> interface_2_in_0x7fce44007bf0;

// Input tensor.
subgraph cluster_subgraph_4 {
    label = "Input 2";
    interface_4_out_0x7fcf1001f918 [label="s", shape=none];
    interface_4_out_0x7fc950008e48 [label="C_in", shape=none];
    interface_4_out_0x7fc950008c18 [label="k_1^2*s", shape=none];
}

interface_4_out_0x7fcf1001f918 -> interface_2_in_0x7fcf1001f918;
interface_4_out_0x7fc950008e48 -> interface_2_in_0x7fc950008e48;
interface_4_out_0x7fc950008c18 -> interface_2_in_0x7fc950008c18;

interface_2_out_0x5581660a87e0 -> interface_1_in_0x5581660a87e0;
interface_2_out_0x7fce44007bf0 -> interface_1_in_0x7fce44007bf0;
interface_2_out_0x7fce44007c08 -> interface_1_in_0x7fce44007c08;
interface_2_out_0x5581660a8858 -> interface_1_in_0x5581660a8858;
interface_2_out_0x7fcbc40054a0 -> interface_1_in_0x7fcbc40054a0;

interface_1_out_0x5581660a87e0 -> interface_0_in_0x5581660a87e0;
interface_1_out_0x5581660a8830 -> interface_0_in_0x5581660a8830;
interface_1_out_0x7fcf58005310 -> interface_0_in_0x7fcf58005310;
interface_1_out_0x5581660a8858 -> interface_0_in_0x5581660a8858;
interface_1_out_0x7fcbc40054a0 -> interface_0_in_0x7fcbc40054a0;

// Input tensor.
subgraph cluster_subgraph_5 {
    label = "Input 1";
    interface_5_out_0x7fcf84003f38 [label="C_out", shape=none];
    interface_5_out_0x7fcf58005328 [label="s", shape=none];
    interface_5_out_0x7fcbc40054b8 [label="k_1^2*s", shape=none];
}

interface_5_out_0x7fcf84003f38 -> interface_0_in_0x7fcf84003f38;
interface_5_out_0x7fcf58005328 -> interface_0_in_0x7fcf58005328;
interface_5_out_0x7fcbc40054b8 -> interface_0_in_0x7fcbc40054b8;

{
    rank = same;
    interface_3_out_0x5581660a87e0;
    interface_3_out_0x7fc950008e30;
    interface_3_out_0x5581660a8858;
    interface_3_out_0x7fce44007bf0;
    interface_5_out_0x7fcf84003f38;
    interface_5_out_0x7fcf58005328;
    interface_5_out_0x7fcbc40054b8;
    interface_4_out_0x7fcf1001f918;
    interface_4_out_0x7fc950008e48;
    interface_4_out_0x7fc950008c18;
}
subgraph cluster_subgraph_output {
    label = "Output";
    interface_6_in_0x5581660a87e0 [label="N", shape=none];
    interface_6_in_0x5581660a8808 [label="C_out", shape=none];
    interface_6_in_0x5581660a8830 [label="H", shape=none];
    interface_6_in_0x5581660a8858 [label="H", shape=none];
}
interface_0_out_0x5581660a87e0 -> interface_6_in_0x5581660a87e0;
interface_0_out_0x5581660a8808 -> interface_6_in_0x5581660a8808;
interface_0_out_0x5581660a8830 -> interface_6_in_0x5581660a8830;
interface_0_out_0x5581660a8858 -> interface_6_in_0x5581660a8858;

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
		t_3 = torch.einsum("ljmn, kji -> lnkmi", in_0, in_2)

		# No contraction needed.
		t_4 = t_3

		# [H]@Merge6f1a0d6b662fae84, [s]@Merge6f1a0d6b662fae85 -> [s*H]@Shift594e1a6314829db7
		t_4 = torch.reshape(t_4, (128, 224, 112, 18, ))

		# [s*H]@Shift594e1a6314829db7 -> [s*H]@Split7ee86503d19bbef6
		t_4 = torch.roll(t_4, self.shift_direction, 1)

		# [s*H]@Split7ee86503d19bbef6 -> [H]@Iterator96123ba3184da39c, [s]@Shareb15a7faee0f8b868
		t_4 = torch.reshape(t_4, (128, 112, 2, 112, 18, ))

		# Perform contraction.
		t_5 = torch.einsum("lmjni, kji -> lkmn", t_4, in_1)

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
		t_3 = torch.einsum("ljmn, kji -> lnkmi", in_0, in_2)

		# No contraction needed.
		t_4 = t_3

		# [H]@Merge6f1a0d6b662fae84, [s]@Merge6f1a0d6b662fae85 -> [s*H]@Shift594e1a6314829db7
		t_4 = torch.reshape(t_4, (128, 112, 56, 18, ))

		# [s*H]@Shift594e1a6314829db7 -> [s*H]@Split7ee86503d19bbef6
		t_4 = torch.roll(t_4, self.shift_direction, 1)

		# [s*H]@Split7ee86503d19bbef6 -> [H]@Iterator96123ba3184da39c, [s]@Shareb15a7faee0f8b868
		t_4 = torch.reshape(t_4, (128, 56, 2, 56, 18, ))

		# Perform contraction.
		t_5 = torch.einsum("lmjni, kji -> lkmn", t_4, in_1)

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
		t_3 = torch.einsum("ljmn, kji -> lnkmi", in_0, in_2)

		# No contraction needed.
		t_4 = t_3

		# [H]@Merge6f1a0d6b662fae84, [s]@Merge6f1a0d6b662fae85 -> [s*H]@Shift594e1a6314829db7
		t_4 = torch.reshape(t_4, (128, 112, 56, 18, ))

		# [s*H]@Shift594e1a6314829db7 -> [s*H]@Split7ee86503d19bbef6
		t_4 = torch.roll(t_4, self.shift_direction, 1)

		# [s*H]@Split7ee86503d19bbef6 -> [H]@Iterator96123ba3184da39c, [s]@Shareb15a7faee0f8b868
		t_4 = torch.reshape(t_4, (128, 56, 2, 56, 18, ))

		# Perform contraction.
		t_5 = torch.einsum("lmjni, kji -> lkmn", t_4, in_1)

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
		t_3 = torch.einsum("ljmn, kji -> lnkmi", in_0, in_2)

		# No contraction needed.
		t_4 = t_3

		# [H]@Merge6f1a0d6b662fae84, [s]@Merge6f1a0d6b662fae85 -> [s*H]@Shift594e1a6314829db7
		t_4 = torch.reshape(t_4, (128, 56, 28, 18, ))

		# [s*H]@Shift594e1a6314829db7 -> [s*H]@Split7ee86503d19bbef6
		t_4 = torch.roll(t_4, self.shift_direction, 1)

		# [s*H]@Split7ee86503d19bbef6 -> [H]@Iterator96123ba3184da39c, [s]@Shareb15a7faee0f8b868
		t_4 = torch.reshape(t_4, (128, 28, 2, 28, 18, ))

		# Perform contraction.
		t_5 = torch.einsum("lmjni, kji -> lkmn", t_4, in_1)

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
		t_3 = torch.einsum("ljmn, kji -> lnkmi", in_0, in_2)

		# No contraction needed.
		t_4 = t_3

		# [H]@Merge6f1a0d6b662fae84, [s]@Merge6f1a0d6b662fae85 -> [s*H]@Shift594e1a6314829db7
		t_4 = torch.reshape(t_4, (128, 56, 28, 18, ))

		# [s*H]@Shift594e1a6314829db7 -> [s*H]@Split7ee86503d19bbef6
		t_4 = torch.roll(t_4, self.shift_direction, 1)

		# [s*H]@Split7ee86503d19bbef6 -> [H]@Iterator96123ba3184da39c, [s]@Shareb15a7faee0f8b868
		t_4 = torch.reshape(t_4, (128, 28, 2, 28, 18, ))

		# Perform contraction.
		t_5 = torch.einsum("lmjni, kji -> lkmn", t_4, in_1)

		# No need to crop the output tensor.
		y = t_5

		return y

