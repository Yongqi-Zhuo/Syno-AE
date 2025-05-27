import torch
import random
"""
digraph kernel_preview {
newrank = true;

// Stage tensor.
subgraph cluster_subgraph_0 {
    label = "Subgraph 0";
    // Reductions.
    reduce_0x7f5f78004e58 [label="Sum", shape=box];
    reduce_0x7f5f780052a8 [label="Sum", shape=box];
    // Output.
    subgraph cluster_subgraph_0_out {
        label = "";
        interface_0_out_0x55f1ee7b7da0 [label="N", shape=none];
        interface_0_out_0x55f1ee7b7dc8 [label="C_out", shape=none];
        interface_0_out_0x55f1ee7b7df0 [label="H", shape=none];
        interface_0_out_0x55f1ee7b7e18 [label="H", shape=none];
    }
    {
        rank = same;
        reduce_0x7f5f78004e58;
        reduce_0x7f5f780052a8;
        interface_0_out_0x55f1ee7b7da0;
        interface_0_out_0x55f1ee7b7dc8;
        interface_0_out_0x55f1ee7b7df0;
        interface_0_out_0x55f1ee7b7e18;
    }
    // Input 0.
    subgraph cluster_subgraph_0_in_0 {
        label = "";
        interface_0_in_0x55f1ee7b7da0 [label="N", shape=none];
        interface_0_in_0x55f1ee7b7df0 [label="H", shape=none];
        interface_0_in_0x55f1f89ddbf0 [label="s", shape=none];
        interface_0_in_0x55f1ee7b7e18 [label="H", shape=none];
        interface_0_in_0x55f1f89e2e00 [label="k_1^2*s", shape=none];
    }
    // Input 1.
    subgraph cluster_subgraph_0_in_1 {
        label = "";
        interface_0_in_0x55f1f89dd938 [label="C_out", shape=none];
        interface_0_in_0x55f1f89ddc08 [label="s", shape=none];
        interface_0_in_0x55f1f89e2e18 [label="k_1^2*s", shape=none];
    }
    {
        rank = same;
        interface_0_in_0x55f1ee7b7da0;
        interface_0_in_0x55f1ee7b7df0;
        interface_0_in_0x55f1f89ddbf0;
        interface_0_in_0x55f1ee7b7e18;
        interface_0_in_0x55f1f89e2e00;
        interface_0_in_0x55f1f89dd938;
        interface_0_in_0x55f1f89ddc08;
        interface_0_in_0x55f1f89e2e18;
    }
    // Op's.
    op_0x55f1f88b2978 [label="Expand"];
    op_0x55f1f89dd900 [label="Share"];
    op_0x55f1f89ddbd0 [label="Share"];
    op_0x55f1f89e2de0 [label="Share"];
    // Dimension's.
    interface_0_in_0x55f1ee7b7da0 -> interface_0_out_0x55f1ee7b7da0 [label="N"];
    op_0x55f1f89dd900 -> interface_0_out_0x55f1ee7b7dc8 [label="C_out"];
    interface_0_in_0x55f1ee7b7df0 -> interface_0_out_0x55f1ee7b7df0 [label="H"];
    interface_0_in_0x55f1ee7b7e18 -> interface_0_out_0x55f1ee7b7e18 [label="H"];
    op_0x55f1f88b2978 -> op_0x55f1f89dd900 [label="C_out"];
    interface_0_in_0x55f1f89dd938 -> op_0x55f1f89dd900 [label="C_out"];
    interface_0_in_0x55f1f89ddbf0 -> op_0x55f1f89ddbd0 [label="s"];
    interface_0_in_0x55f1f89ddc08 -> op_0x55f1f89ddbd0 [label="s"];
    interface_0_in_0x55f1f89e2e00 -> op_0x55f1f89e2de0 [label="k_1^2*s"];
    interface_0_in_0x55f1f89e2e18 -> op_0x55f1f89e2de0 [label="k_1^2*s"];
    op_0x55f1f89ddbd0 -> reduce_0x7f5f78004e58 [label="s"];
    op_0x55f1f89e2de0 -> reduce_0x7f5f780052a8 [label="k_1^2*s"];
}

// Stage tensor.
subgraph cluster_subgraph_1 {
    label = "Subgraph 1";
    // Reductions.
    // Output.
    subgraph cluster_subgraph_1_out {
        label = "";
        interface_1_out_0x55f1ee7b7da0 [label="N", shape=none];
        interface_1_out_0x55f1ee7b7df0 [label="H", shape=none];
        interface_1_out_0x55f1f89ddbf0 [label="s", shape=none];
        interface_1_out_0x55f1ee7b7e18 [label="H", shape=none];
        interface_1_out_0x55f1f89e2e00 [label="k_1^2*s", shape=none];
    }
    {
        rank = same;
        interface_1_out_0x55f1ee7b7da0;
        interface_1_out_0x55f1ee7b7df0;
        interface_1_out_0x55f1f89ddbf0;
        interface_1_out_0x55f1ee7b7e18;
        interface_1_out_0x55f1f89e2e00;
    }
    // Input 0.
    subgraph cluster_subgraph_1_in_0 {
        label = "";
        interface_1_in_0x55f1ee7b7da0 [label="N", shape=none];
        interface_1_in_0x55f1f89e1ec0 [label="H", shape=none];
        interface_1_in_0x55f1f89e1ed8 [label="s", shape=none];
        interface_1_in_0x55f1ee7b7e18 [label="H", shape=none];
        interface_1_in_0x55f1f89e2e00 [label="k_1^2*s", shape=none];
    }
    {
        rank = same;
        interface_1_in_0x55f1ee7b7da0;
        interface_1_in_0x55f1f89e1ec0;
        interface_1_in_0x55f1f89e1ed8;
        interface_1_in_0x55f1ee7b7e18;
        interface_1_in_0x55f1f89e2e00;
    }
    // Op's.
    op_0x55f1eba3e560 [label="Shift"];
    op_0x55f1f89e1e80 [label="Merge"];
    op_0x55f1f8a04f40 [label="Split"];
    // Dimension's.
    op_0x55f1f89e1e80 -> op_0x55f1eba3e560 [label="s*H"];
    interface_1_in_0x55f1ee7b7da0 -> interface_1_out_0x55f1ee7b7da0 [label="N"];
    op_0x55f1f8a04f40 -> interface_1_out_0x55f1ee7b7df0 [label="H"];
    interface_1_in_0x55f1ee7b7e18 -> interface_1_out_0x55f1ee7b7e18 [label="H"];
    op_0x55f1f8a04f40 -> interface_1_out_0x55f1f89ddbf0 [label="s"];
    interface_1_in_0x55f1f89e1ec0 -> op_0x55f1f89e1e80 [label="H"];
    interface_1_in_0x55f1f89e1ed8 -> op_0x55f1f89e1e80 [label="s"];
    interface_1_in_0x55f1f89e2e00 -> interface_1_out_0x55f1f89e2e00 [label="k_1^2*s"];
    op_0x55f1eba3e560 -> op_0x55f1f8a04f40 [label="s*H"];
}

// Stage tensor.
subgraph cluster_subgraph_2 {
    label = "Subgraph 2";
    // Reductions.
    reduce_0x7f5f78007b70 [label="Sum", shape=box];
    // Output.
    subgraph cluster_subgraph_2_out {
        label = "";
        interface_2_out_0x55f1ee7b7da0 [label="N", shape=none];
        interface_2_out_0x55f1f89e1ec0 [label="H", shape=none];
        interface_2_out_0x55f1f89e1ed8 [label="s", shape=none];
        interface_2_out_0x55f1ee7b7e18 [label="H", shape=none];
        interface_2_out_0x55f1f89e2e00 [label="k_1^2*s", shape=none];
    }
    {
        rank = same;
        reduce_0x7f5f78007b70;
        interface_2_out_0x55f1ee7b7da0;
        interface_2_out_0x55f1f89e1ec0;
        interface_2_out_0x55f1f89e1ed8;
        interface_2_out_0x55f1ee7b7e18;
        interface_2_out_0x55f1f89e2e00;
    }
    // Input 0.
    subgraph cluster_subgraph_2_in_0 {
        label = "";
        interface_2_in_0x55f1ee7b7da0 [label="N", shape=none];
        interface_2_in_0x55f1f89ddce0 [label="C_in", shape=none];
        interface_2_in_0x55f1ee7b7e18 [label="H", shape=none];
        interface_2_in_0x55f1f89e1ec0 [label="H", shape=none];
    }
    // Input 1.
    subgraph cluster_subgraph_2_in_1 {
        label = "";
        interface_2_in_0x55f1f89e2f08 [label="s", shape=none];
        interface_2_in_0x55f1f89ddcf8 [label="C_in", shape=none];
        interface_2_in_0x55f1f89e2e68 [label="k_1^2*s", shape=none];
    }
    {
        rank = same;
        interface_2_in_0x55f1ee7b7da0;
        interface_2_in_0x55f1f89ddce0;
        interface_2_in_0x55f1ee7b7e18;
        interface_2_in_0x55f1f89e1ec0;
        interface_2_in_0x55f1f89e2f08;
        interface_2_in_0x55f1f89ddcf8;
        interface_2_in_0x55f1f89e2e68;
    }
    // Op's.
    op_0x55f1f88b2a98 [label="Expand"];
    op_0x55f1f88b2ab8 [label="Expand"];
    op_0x55f1f89ddcc0 [label="Share"];
    op_0x55f1f89e2e30 [label="Share"];
    op_0x55f1f89e2ed0 [label="Share"];
    // Dimension's.
    interface_2_in_0x55f1ee7b7da0 -> interface_2_out_0x55f1ee7b7da0 [label="N"];
    interface_2_in_0x55f1ee7b7e18 -> interface_2_out_0x55f1ee7b7e18 [label="H"];
    interface_2_in_0x55f1f89ddce0 -> op_0x55f1f89ddcc0 [label="C_in"];
    interface_2_in_0x55f1f89ddcf8 -> op_0x55f1f89ddcc0 [label="C_in"];
    interface_2_in_0x55f1f89e1ec0 -> interface_2_out_0x55f1f89e1ec0 [label="H"];
    op_0x55f1f89e2ed0 -> interface_2_out_0x55f1f89e1ed8 [label="s"];
    op_0x55f1f89e2e30 -> interface_2_out_0x55f1f89e2e00 [label="k_1^2*s"];
    op_0x55f1f88b2a98 -> op_0x55f1f89e2e30 [label="k_1^2*s"];
    interface_2_in_0x55f1f89e2e68 -> op_0x55f1f89e2e30 [label="k_1^2*s"];
    op_0x55f1f88b2ab8 -> op_0x55f1f89e2ed0 [label="s"];
    interface_2_in_0x55f1f89e2f08 -> op_0x55f1f89e2ed0 [label="s"];
    op_0x55f1f89ddcc0 -> reduce_0x7f5f78007b70 [label="C_in"];
}

// Input tensor.
subgraph cluster_subgraph_3 {
    label = "Input 0";
    interface_3_out_0x55f1ee7b7da0 [label="N", shape=none];
    interface_3_out_0x55f1f89ddce0 [label="C_in", shape=none];
    interface_3_out_0x55f1ee7b7e18 [label="H", shape=none];
    interface_3_out_0x55f1f89e1ec0 [label="H", shape=none];
}

interface_3_out_0x55f1ee7b7da0 -> interface_2_in_0x55f1ee7b7da0;
interface_3_out_0x55f1f89ddce0 -> interface_2_in_0x55f1f89ddce0;
interface_3_out_0x55f1ee7b7e18 -> interface_2_in_0x55f1ee7b7e18;
interface_3_out_0x55f1f89e1ec0 -> interface_2_in_0x55f1f89e1ec0;

// Input tensor.
subgraph cluster_subgraph_4 {
    label = "Input 2";
    interface_4_out_0x55f1f89e2f08 [label="s", shape=none];
    interface_4_out_0x55f1f89ddcf8 [label="C_in", shape=none];
    interface_4_out_0x55f1f89e2e68 [label="k_1^2*s", shape=none];
}

interface_4_out_0x55f1f89e2f08 -> interface_2_in_0x55f1f89e2f08;
interface_4_out_0x55f1f89ddcf8 -> interface_2_in_0x55f1f89ddcf8;
interface_4_out_0x55f1f89e2e68 -> interface_2_in_0x55f1f89e2e68;

interface_2_out_0x55f1ee7b7da0 -> interface_1_in_0x55f1ee7b7da0;
interface_2_out_0x55f1f89e1ec0 -> interface_1_in_0x55f1f89e1ec0;
interface_2_out_0x55f1f89e1ed8 -> interface_1_in_0x55f1f89e1ed8;
interface_2_out_0x55f1ee7b7e18 -> interface_1_in_0x55f1ee7b7e18;
interface_2_out_0x55f1f89e2e00 -> interface_1_in_0x55f1f89e2e00;

interface_1_out_0x55f1ee7b7da0 -> interface_0_in_0x55f1ee7b7da0;
interface_1_out_0x55f1ee7b7df0 -> interface_0_in_0x55f1ee7b7df0;
interface_1_out_0x55f1f89ddbf0 -> interface_0_in_0x55f1f89ddbf0;
interface_1_out_0x55f1ee7b7e18 -> interface_0_in_0x55f1ee7b7e18;
interface_1_out_0x55f1f89e2e00 -> interface_0_in_0x55f1f89e2e00;

// Input tensor.
subgraph cluster_subgraph_5 {
    label = "Input 1";
    interface_5_out_0x55f1f89dd938 [label="C_out", shape=none];
    interface_5_out_0x55f1f89ddc08 [label="s", shape=none];
    interface_5_out_0x55f1f89e2e18 [label="k_1^2*s", shape=none];
}

interface_5_out_0x55f1f89dd938 -> interface_0_in_0x55f1f89dd938;
interface_5_out_0x55f1f89ddc08 -> interface_0_in_0x55f1f89ddc08;
interface_5_out_0x55f1f89e2e18 -> interface_0_in_0x55f1f89e2e18;

{
    rank = same;
    interface_3_out_0x55f1ee7b7da0;
    interface_3_out_0x55f1f89ddce0;
    interface_3_out_0x55f1ee7b7e18;
    interface_3_out_0x55f1f89e1ec0;
    interface_5_out_0x55f1f89dd938;
    interface_5_out_0x55f1f89ddc08;
    interface_5_out_0x55f1f89e2e18;
    interface_4_out_0x55f1f89e2f08;
    interface_4_out_0x55f1f89ddcf8;
    interface_4_out_0x55f1f89e2e68;
}
subgraph cluster_subgraph_output {
    label = "Output";
    interface_6_in_0x55f1ee7b7da0 [label="N", shape=none];
    interface_6_in_0x55f1ee7b7dc8 [label="C_out", shape=none];
    interface_6_in_0x55f1ee7b7df0 [label="H", shape=none];
    interface_6_in_0x55f1ee7b7e18 [label="H", shape=none];
}
interface_0_out_0x55f1ee7b7da0 -> interface_6_in_0x55f1ee7b7da0;
interface_0_out_0x55f1ee7b7dc8 -> interface_6_in_0x55f1ee7b7dc8;
interface_0_out_0x55f1ee7b7df0 -> interface_6_in_0x55f1ee7b7df0;
interface_0_out_0x55f1ee7b7e18 -> interface_6_in_0x55f1ee7b7e18;

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

