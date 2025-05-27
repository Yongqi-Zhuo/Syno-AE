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
        interface_0_out_0x55f1ee7b7da0 [label="N", shape=none];
        interface_0_out_0x55f1ee7b7dc8 [label="C_out", shape=none];
        interface_0_out_0x55f1ee7b7df0 [label="H", shape=none];
        interface_0_out_0x55f1ee7b7e18 [label="H", shape=none];
    }
    {
        rank = same;
        interface_0_out_0x55f1ee7b7da0;
        interface_0_out_0x55f1ee7b7dc8;
        interface_0_out_0x55f1ee7b7df0;
        interface_0_out_0x55f1ee7b7e18;
    }
    // Input 0.
    subgraph cluster_subgraph_0_in_0 {
        label = "";
        interface_0_in_0x55f1ee7b7da0 [label="N", shape=none];
        interface_0_in_0x55f1f89df280 [label="s", shape=none];
        interface_0_in_0x55f1f89df298 [label="s^-1*C_out", shape=none];
        interface_0_in_0x55f1ee7b7df0 [label="H", shape=none];
        interface_0_in_0x55f1ee7b7e18 [label="H", shape=none];
    }
    {
        rank = same;
        interface_0_in_0x55f1ee7b7da0;
        interface_0_in_0x55f1f89df280;
        interface_0_in_0x55f1f89df298;
        interface_0_in_0x55f1ee7b7df0;
        interface_0_in_0x55f1ee7b7e18;
    }
    // Op's.
    op_0x55f1f89df240 [label="Merge"];
    // Dimension's.
    interface_0_in_0x55f1ee7b7da0 -> interface_0_out_0x55f1ee7b7da0 [label="N"];
    op_0x55f1f89df240 -> interface_0_out_0x55f1ee7b7dc8 [label="C_out"];
    interface_0_in_0x55f1ee7b7df0 -> interface_0_out_0x55f1ee7b7df0 [label="H"];
    interface_0_in_0x55f1ee7b7e18 -> interface_0_out_0x55f1ee7b7e18 [label="H"];
    interface_0_in_0x55f1f89df280 -> op_0x55f1f89df240 [label="s"];
    interface_0_in_0x55f1f89df298 -> op_0x55f1f89df240 [label="s^-1*C_out"];
}

// Stage tensor.
subgraph cluster_subgraph_1 {
    label = "Subgraph 1";
    // Reductions.
    reduce_0x7f5f78003cc0 [label="Sum", shape=box];
    // Output.
    subgraph cluster_subgraph_1_out {
        label = "";
        interface_1_out_0x55f1ee7b7da0 [label="N", shape=none];
        interface_1_out_0x55f1f89df280 [label="s", shape=none];
        interface_1_out_0x55f1f89df298 [label="s^-1*C_out", shape=none];
        interface_1_out_0x55f1ee7b7df0 [label="H", shape=none];
        interface_1_out_0x55f1ee7b7e18 [label="H", shape=none];
    }
    {
        rank = same;
        reduce_0x7f5f78003cc0;
        interface_1_out_0x55f1ee7b7da0;
        interface_1_out_0x55f1f89df280;
        interface_1_out_0x55f1f89df298;
        interface_1_out_0x55f1ee7b7df0;
        interface_1_out_0x55f1ee7b7e18;
    }
    // Input 0.
    subgraph cluster_subgraph_1_in_0 {
        label = "";
        interface_1_in_0x55f1ee7b7da0 [label="N", shape=none];
        interface_1_in_0x55f1f89df280 [label="s", shape=none];
        interface_1_in_0x55f1ee7b7df0 [label="H", shape=none];
        interface_1_in_0x55f1ee7b7e18 [label="H", shape=none];
        interface_1_in_0x55f1f89dd9c0 [label="k_1^2", shape=none];
    }
    // Input 1.
    subgraph cluster_subgraph_1_in_1 {
        label = "";
        interface_1_in_0x55f1f89dda28 [label="s^-1*C_out", shape=none];
        interface_1_in_0x55f1f89dd9d8 [label="k_1^2", shape=none];
    }
    {
        rank = same;
        interface_1_in_0x55f1ee7b7da0;
        interface_1_in_0x55f1f89df280;
        interface_1_in_0x55f1ee7b7df0;
        interface_1_in_0x55f1ee7b7e18;
        interface_1_in_0x55f1f89dd9c0;
        interface_1_in_0x55f1f89dda28;
        interface_1_in_0x55f1f89dd9d8;
    }
    // Op's.
    op_0x55f1f88b2998 [label="Expand"];
    op_0x55f1f89dd9a0 [label="Share"];
    op_0x55f1f89dd9f0 [label="Share"];
    // Dimension's.
    interface_1_in_0x55f1ee7b7da0 -> interface_1_out_0x55f1ee7b7da0 [label="N"];
    interface_1_in_0x55f1ee7b7df0 -> interface_1_out_0x55f1ee7b7df0 [label="H"];
    interface_1_in_0x55f1ee7b7e18 -> interface_1_out_0x55f1ee7b7e18 [label="H"];
    interface_1_in_0x55f1f89dd9c0 -> op_0x55f1f89dd9a0 [label="k_1^2"];
    interface_1_in_0x55f1f89dd9d8 -> op_0x55f1f89dd9a0 [label="k_1^2"];
    op_0x55f1f88b2998 -> op_0x55f1f89dd9f0 [label="s^-1*C_out"];
    interface_1_in_0x55f1f89dda28 -> op_0x55f1f89dd9f0 [label="s^-1*C_out"];
    interface_1_in_0x55f1f89df280 -> interface_1_out_0x55f1f89df280 [label="s"];
    op_0x55f1f89dd9f0 -> interface_1_out_0x55f1f89df298 [label="s^-1*C_out"];
    op_0x55f1f89dd9a0 -> reduce_0x7f5f78003cc0 [label="k_1^2"];
}

// Stage tensor.
subgraph cluster_subgraph_2 {
    label = "Subgraph 2";
    // Reductions.
    reduce_0x7f5f78007668 [label="Sum", shape=box];
    // Output.
    subgraph cluster_subgraph_2_out {
        label = "";
        interface_2_out_0x55f1ee7b7da0 [label="N", shape=none];
        interface_2_out_0x55f1f89df280 [label="s", shape=none];
        interface_2_out_0x55f1ee7b7df0 [label="H", shape=none];
        interface_2_out_0x55f1ee7b7e18 [label="H", shape=none];
        interface_2_out_0x55f1f89dd9c0 [label="k_1^2", shape=none];
    }
    {
        rank = same;
        reduce_0x7f5f78007668;
        interface_2_out_0x55f1ee7b7da0;
        interface_2_out_0x55f1f89df280;
        interface_2_out_0x55f1ee7b7df0;
        interface_2_out_0x55f1ee7b7e18;
        interface_2_out_0x55f1f89dd9c0;
    }
    // Input 0.
    subgraph cluster_subgraph_2_in_0 {
        label = "";
        interface_2_in_0x55f1ee7b7da0 [label="N", shape=none];
        interface_2_in_0x55f1f89de520 [label="C_in", shape=none];
        interface_2_in_0x55f1ee7b7df0 [label="H", shape=none];
        interface_2_in_0x55f1ee7b7e18 [label="H", shape=none];
        interface_2_in_0x55f1f89dd9c0 [label="k_1^2", shape=none];
    }
    {
        rank = same;
        interface_2_in_0x55f1ee7b7da0;
        interface_2_in_0x55f1f89de520;
        interface_2_in_0x55f1ee7b7df0;
        interface_2_in_0x55f1ee7b7e18;
        interface_2_in_0x55f1f89dd9c0;
    }
    // Op's.
    op_0x55f1f89de4e0 [label="Split"];
    // Dimension's.
    interface_2_in_0x55f1ee7b7da0 -> interface_2_out_0x55f1ee7b7da0 [label="N"];
    interface_2_in_0x55f1ee7b7df0 -> interface_2_out_0x55f1ee7b7df0 [label="H"];
    interface_2_in_0x55f1ee7b7e18 -> interface_2_out_0x55f1ee7b7e18 [label="H"];
    interface_2_in_0x55f1f89dd9c0 -> interface_2_out_0x55f1f89dd9c0 [label="k_1^2"];
    interface_2_in_0x55f1f89de520 -> op_0x55f1f89de4e0 [label="C_in"];
    op_0x55f1f89de4e0 -> interface_2_out_0x55f1f89df280 [label="s"];
    op_0x55f1f89de4e0 -> reduce_0x7f5f78007668 [label="s^-1*C_in"];
}

// Stage tensor.
subgraph cluster_subgraph_3 {
    label = "Subgraph 3";
    // Reductions.
    // Output.
    subgraph cluster_subgraph_3_out {
        label = "";
        interface_3_out_0x55f1ee7b7da0 [label="N", shape=none];
        interface_3_out_0x55f1f89de520 [label="C_in", shape=none];
        interface_3_out_0x55f1ee7b7df0 [label="H", shape=none];
        interface_3_out_0x55f1ee7b7e18 [label="H", shape=none];
        interface_3_out_0x55f1f89dd9c0 [label="k_1^2", shape=none];
    }
    {
        rank = same;
        interface_3_out_0x55f1ee7b7da0;
        interface_3_out_0x55f1f89de520;
        interface_3_out_0x55f1ee7b7df0;
        interface_3_out_0x55f1ee7b7e18;
        interface_3_out_0x55f1f89dd9c0;
    }
    // Input 0.
    subgraph cluster_subgraph_3_in_0 {
        label = "";
        interface_3_in_0x55f1ee7b7da0 [label="N", shape=none];
        interface_3_in_0x55f1f89ddb50 [label="C_in", shape=none];
        interface_3_in_0x55f1ee7b7e18 [label="H", shape=none];
        interface_3_in_0x55f1ee7b7df0 [label="H", shape=none];
    }
    // Input 1.
    subgraph cluster_subgraph_3_in_1 {
        label = "";
        interface_3_in_0x55f1f89ddb68 [label="C_in", shape=none];
        interface_3_in_0x55f1f89ddb18 [label="k_1^2", shape=none];
    }
    {
        rank = same;
        interface_3_in_0x55f1ee7b7da0;
        interface_3_in_0x55f1f89ddb50;
        interface_3_in_0x55f1ee7b7e18;
        interface_3_in_0x55f1ee7b7df0;
        interface_3_in_0x55f1f89ddb68;
        interface_3_in_0x55f1f89ddb18;
    }
    // Op's.
    op_0x55f1f88b29d8 [label="Expand"];
    op_0x55f1f89ddae0 [label="Share"];
    op_0x55f1f89ddb30 [label="Share"];
    // Dimension's.
    interface_3_in_0x55f1ee7b7da0 -> interface_3_out_0x55f1ee7b7da0 [label="N"];
    interface_3_in_0x55f1ee7b7df0 -> interface_3_out_0x55f1ee7b7df0 [label="H"];
    interface_3_in_0x55f1ee7b7e18 -> interface_3_out_0x55f1ee7b7e18 [label="H"];
    op_0x55f1f89ddae0 -> interface_3_out_0x55f1f89dd9c0 [label="k_1^2"];
    op_0x55f1f88b29d8 -> op_0x55f1f89ddae0 [label="k_1^2"];
    interface_3_in_0x55f1f89ddb18 -> op_0x55f1f89ddae0 [label="k_1^2"];
    interface_3_in_0x55f1f89ddb50 -> op_0x55f1f89ddb30 [label="C_in"];
    interface_3_in_0x55f1f89ddb68 -> op_0x55f1f89ddb30 [label="C_in"];
    op_0x55f1f89ddb30 -> interface_3_out_0x55f1f89de520 [label="C_in"];
}

// Input tensor.
subgraph cluster_subgraph_4 {
    label = "Input 0";
    interface_4_out_0x55f1ee7b7da0 [label="N", shape=none];
    interface_4_out_0x55f1f89ddb50 [label="C_in", shape=none];
    interface_4_out_0x55f1ee7b7e18 [label="H", shape=none];
    interface_4_out_0x55f1ee7b7df0 [label="H", shape=none];
}

interface_4_out_0x55f1ee7b7da0 -> interface_3_in_0x55f1ee7b7da0;
interface_4_out_0x55f1f89ddb50 -> interface_3_in_0x55f1f89ddb50;
interface_4_out_0x55f1ee7b7e18 -> interface_3_in_0x55f1ee7b7e18;
interface_4_out_0x55f1ee7b7df0 -> interface_3_in_0x55f1ee7b7df0;

// Input tensor.
subgraph cluster_subgraph_5 {
    label = "Input 2";
    interface_5_out_0x55f1f89ddb68 [label="C_in", shape=none];
    interface_5_out_0x55f1f89ddb18 [label="k_1^2", shape=none];
}

interface_5_out_0x55f1f89ddb68 -> interface_3_in_0x55f1f89ddb68;
interface_5_out_0x55f1f89ddb18 -> interface_3_in_0x55f1f89ddb18;

interface_3_out_0x55f1ee7b7da0 -> interface_2_in_0x55f1ee7b7da0;
interface_3_out_0x55f1f89de520 -> interface_2_in_0x55f1f89de520;
interface_3_out_0x55f1ee7b7df0 -> interface_2_in_0x55f1ee7b7df0;
interface_3_out_0x55f1ee7b7e18 -> interface_2_in_0x55f1ee7b7e18;
interface_3_out_0x55f1f89dd9c0 -> interface_2_in_0x55f1f89dd9c0;

interface_2_out_0x55f1ee7b7da0 -> interface_1_in_0x55f1ee7b7da0;
interface_2_out_0x55f1f89df280 -> interface_1_in_0x55f1f89df280;
interface_2_out_0x55f1ee7b7df0 -> interface_1_in_0x55f1ee7b7df0;
interface_2_out_0x55f1ee7b7e18 -> interface_1_in_0x55f1ee7b7e18;
interface_2_out_0x55f1f89dd9c0 -> interface_1_in_0x55f1f89dd9c0;

// Input tensor.
subgraph cluster_subgraph_6 {
    label = "Input 1";
    interface_6_out_0x55f1f89dda28 [label="s^-1*C_out", shape=none];
    interface_6_out_0x55f1f89dd9d8 [label="k_1^2", shape=none];
}

interface_6_out_0x55f1f89dda28 -> interface_1_in_0x55f1f89dda28;
interface_6_out_0x55f1f89dd9d8 -> interface_1_in_0x55f1f89dd9d8;

interface_1_out_0x55f1ee7b7da0 -> interface_0_in_0x55f1ee7b7da0;
interface_1_out_0x55f1f89df280 -> interface_0_in_0x55f1f89df280;
interface_1_out_0x55f1f89df298 -> interface_0_in_0x55f1f89df298;
interface_1_out_0x55f1ee7b7df0 -> interface_0_in_0x55f1ee7b7df0;
interface_1_out_0x55f1ee7b7e18 -> interface_0_in_0x55f1ee7b7e18;

{
    rank = same;
    interface_4_out_0x55f1ee7b7da0;
    interface_4_out_0x55f1f89ddb50;
    interface_4_out_0x55f1ee7b7e18;
    interface_4_out_0x55f1ee7b7df0;
    interface_6_out_0x55f1f89dda28;
    interface_6_out_0x55f1f89dd9d8;
    interface_5_out_0x55f1f89ddb68;
    interface_5_out_0x55f1f89ddb18;
}
subgraph cluster_subgraph_output {
    label = "Output";
    interface_7_in_0x55f1ee7b7da0 [label="N", shape=none];
    interface_7_in_0x55f1ee7b7dc8 [label="C_out", shape=none];
    interface_7_in_0x55f1ee7b7df0 [label="H", shape=none];
    interface_7_in_0x55f1ee7b7e18 [label="H", shape=none];
}
interface_0_out_0x55f1ee7b7da0 -> interface_7_in_0x55f1ee7b7da0;
interface_0_out_0x55f1ee7b7dc8 -> interface_7_in_0x55f1ee7b7dc8;
interface_0_out_0x55f1ee7b7df0 -> interface_7_in_0x55f1ee7b7df0;
interface_0_out_0x55f1ee7b7e18 -> interface_7_in_0x55f1ee7b7e18;

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

