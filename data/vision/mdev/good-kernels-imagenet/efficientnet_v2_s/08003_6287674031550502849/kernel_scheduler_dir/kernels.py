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
        interface_0_in_0x55f1ee7b7dc8 [label="C_out", shape=none];
        interface_0_in_0x55f1f89ded40 [label="k_2^-1*H", shape=none];
        interface_0_in_0x55f1f89ded58 [label="k_2", shape=none];
        interface_0_in_0x55f1ee7b7e18 [label="H", shape=none];
    }
    {
        rank = same;
        interface_0_in_0x55f1ee7b7da0;
        interface_0_in_0x55f1ee7b7dc8;
        interface_0_in_0x55f1f89ded40;
        interface_0_in_0x55f1f89ded58;
        interface_0_in_0x55f1ee7b7e18;
    }
    // Op's.
    op_0x55f1f89ded00 [label="Merge"];
    // Dimension's.
    interface_0_in_0x55f1ee7b7da0 -> interface_0_out_0x55f1ee7b7da0 [label="N"];
    interface_0_in_0x55f1ee7b7dc8 -> interface_0_out_0x55f1ee7b7dc8 [label="C_out"];
    op_0x55f1f89ded00 -> interface_0_out_0x55f1ee7b7df0 [label="H"];
    interface_0_in_0x55f1ee7b7e18 -> interface_0_out_0x55f1ee7b7e18 [label="H"];
    interface_0_in_0x55f1f89ded40 -> op_0x55f1f89ded00 [label="k_2^-1*H"];
    interface_0_in_0x55f1f89ded58 -> op_0x55f1f89ded00 [label="k_2"];
}

// Stage tensor.
subgraph cluster_subgraph_1 {
    label = "Subgraph 1";
    // Reductions.
    reduce_0x7f5f78007b70 [label="Sum", shape=box];
    reduce_0x7f5f78003a98 [label="Sum", shape=box];
    // Output.
    subgraph cluster_subgraph_1_out {
        label = "";
        interface_1_out_0x55f1ee7b7da0 [label="N", shape=none];
        interface_1_out_0x55f1ee7b7dc8 [label="C_out", shape=none];
        interface_1_out_0x55f1f89ded40 [label="k_2^-1*H", shape=none];
        interface_1_out_0x55f1f89ded58 [label="k_2", shape=none];
        interface_1_out_0x55f1ee7b7e18 [label="H", shape=none];
    }
    {
        rank = same;
        reduce_0x7f5f78007b70;
        reduce_0x7f5f78003a98;
        interface_1_out_0x55f1ee7b7da0;
        interface_1_out_0x55f1ee7b7dc8;
        interface_1_out_0x55f1f89ded40;
        interface_1_out_0x55f1f89ded58;
        interface_1_out_0x55f1ee7b7e18;
    }
    // Input 0.
    subgraph cluster_subgraph_1_in_0 {
        label = "";
        interface_1_in_0x55f1ee7b7da0 [label="N", shape=none];
        interface_1_in_0x55f1f89ddba0 [label="C_in", shape=none];
        interface_1_in_0x55f1f89ded40 [label="k_2^-1*H", shape=none];
        interface_1_in_0x55f1f89e2c20 [label="k_1", shape=none];
        interface_1_in_0x55f1f89ded58 [label="k_2", shape=none];
        interface_1_in_0x55f1ee7b7e18 [label="H", shape=none];
    }
    // Input 1.
    subgraph cluster_subgraph_1_in_1 {
        label = "";
        interface_1_in_0x55f1f89dd938 [label="C_out", shape=none];
        interface_1_in_0x55f1f89ddbb8 [label="C_in", shape=none];
        interface_1_in_0x55f1f89e2c38 [label="k_1", shape=none];
    }
    {
        rank = same;
        interface_1_in_0x55f1ee7b7da0;
        interface_1_in_0x55f1f89ddba0;
        interface_1_in_0x55f1f89ded40;
        interface_1_in_0x55f1f89e2c20;
        interface_1_in_0x55f1f89ded58;
        interface_1_in_0x55f1ee7b7e18;
        interface_1_in_0x55f1f89dd938;
        interface_1_in_0x55f1f89ddbb8;
        interface_1_in_0x55f1f89e2c38;
    }
    // Op's.
    op_0x55f1f88b2978 [label="Expand"];
    op_0x55f1f89dd900 [label="Share"];
    op_0x55f1f89ddb80 [label="Share"];
    op_0x55f1f89e2c00 [label="Share"];
    // Dimension's.
    interface_1_in_0x55f1ee7b7da0 -> interface_1_out_0x55f1ee7b7da0 [label="N"];
    op_0x55f1f89dd900 -> interface_1_out_0x55f1ee7b7dc8 [label="C_out"];
    interface_1_in_0x55f1ee7b7e18 -> interface_1_out_0x55f1ee7b7e18 [label="H"];
    op_0x55f1f88b2978 -> op_0x55f1f89dd900 [label="C_out"];
    interface_1_in_0x55f1f89dd938 -> op_0x55f1f89dd900 [label="C_out"];
    interface_1_in_0x55f1f89ddba0 -> op_0x55f1f89ddb80 [label="C_in"];
    interface_1_in_0x55f1f89ddbb8 -> op_0x55f1f89ddb80 [label="C_in"];
    interface_1_in_0x55f1f89ded40 -> interface_1_out_0x55f1f89ded40 [label="k_2^-1*H"];
    interface_1_in_0x55f1f89ded58 -> interface_1_out_0x55f1f89ded58 [label="k_2"];
    interface_1_in_0x55f1f89e2c20 -> op_0x55f1f89e2c00 [label="k_1"];
    interface_1_in_0x55f1f89e2c38 -> op_0x55f1f89e2c00 [label="k_1"];
    op_0x55f1f89e2c00 -> reduce_0x7f5f78003a98 [label="k_1"];
    op_0x55f1f89ddb80 -> reduce_0x7f5f78007b70 [label="C_in"];
}

// Stage tensor.
subgraph cluster_subgraph_2 {
    label = "Subgraph 2";
    // Reductions.
    // Output.
    subgraph cluster_subgraph_2_out {
        label = "";
        interface_2_out_0x55f1ee7b7da0 [label="N", shape=none];
        interface_2_out_0x55f1f89ddba0 [label="C_in", shape=none];
        interface_2_out_0x55f1f89ded40 [label="k_2^-1*H", shape=none];
        interface_2_out_0x55f1f89e2c20 [label="k_1", shape=none];
        interface_2_out_0x55f1f89ded58 [label="k_2", shape=none];
        interface_2_out_0x55f1ee7b7e18 [label="H", shape=none];
    }
    {
        rank = same;
        interface_2_out_0x55f1ee7b7da0;
        interface_2_out_0x55f1f89ddba0;
        interface_2_out_0x55f1f89ded40;
        interface_2_out_0x55f1f89e2c20;
        interface_2_out_0x55f1f89ded58;
        interface_2_out_0x55f1ee7b7e18;
    }
    // Input 0.
    subgraph cluster_subgraph_2_in_0 {
        label = "";
        interface_2_in_0x55f1ee7b7da0 [label="N", shape=none];
        interface_2_in_0x55f1f89ddba0 [label="C_in", shape=none];
        interface_2_in_0x55f1f89e4810 [label="H", shape=none];
        interface_2_in_0x55f1ee7b7e18 [label="H", shape=none];
    }
    {
        rank = same;
        interface_2_in_0x55f1ee7b7da0;
        interface_2_in_0x55f1f89ddba0;
        interface_2_in_0x55f1f89e4810;
        interface_2_in_0x55f1ee7b7e18;
    }
    // Op's.
    op_0x55f1f88a6100 [label="Unfold"];
    op_0x55f1f89e47d0 [label="Split"];
    // Dimension's.
    interface_2_in_0x55f1ee7b7da0 -> interface_2_out_0x55f1ee7b7da0 [label="N"];
    interface_2_in_0x55f1ee7b7e18 -> interface_2_out_0x55f1ee7b7e18 [label="H"];
    op_0x55f1f89e47d0 -> op_0x55f1f88a6100 [label="k_2"];
    interface_2_in_0x55f1f89ddba0 -> interface_2_out_0x55f1f89ddba0 [label="C_in"];
    op_0x55f1f89e47d0 -> interface_2_out_0x55f1f89ded40 [label="k_2^-1*H"];
    op_0x55f1f88a6100 -> interface_2_out_0x55f1f89ded58 [label="k_2"];
    op_0x55f1f88a6100 -> interface_2_out_0x55f1f89e2c20 [label="k_1"];
    interface_2_in_0x55f1f89e4810 -> op_0x55f1f89e47d0 [label="H"];
}

// Input tensor.
subgraph cluster_subgraph_3 {
    label = "Input 0";
    interface_3_out_0x55f1ee7b7da0 [label="N", shape=none];
    interface_3_out_0x55f1f89ddba0 [label="C_in", shape=none];
    interface_3_out_0x55f1f89e4810 [label="H", shape=none];
    interface_3_out_0x55f1ee7b7e18 [label="H", shape=none];
}

interface_3_out_0x55f1ee7b7da0 -> interface_2_in_0x55f1ee7b7da0;
interface_3_out_0x55f1f89ddba0 -> interface_2_in_0x55f1f89ddba0;
interface_3_out_0x55f1f89e4810 -> interface_2_in_0x55f1f89e4810;
interface_3_out_0x55f1ee7b7e18 -> interface_2_in_0x55f1ee7b7e18;

interface_2_out_0x55f1ee7b7da0 -> interface_1_in_0x55f1ee7b7da0;
interface_2_out_0x55f1f89ddba0 -> interface_1_in_0x55f1f89ddba0;
interface_2_out_0x55f1f89ded40 -> interface_1_in_0x55f1f89ded40;
interface_2_out_0x55f1f89e2c20 -> interface_1_in_0x55f1f89e2c20;
interface_2_out_0x55f1f89ded58 -> interface_1_in_0x55f1f89ded58;
interface_2_out_0x55f1ee7b7e18 -> interface_1_in_0x55f1ee7b7e18;

// Input tensor.
subgraph cluster_subgraph_4 {
    label = "Input 1";
    interface_4_out_0x55f1f89dd938 [label="C_out", shape=none];
    interface_4_out_0x55f1f89ddbb8 [label="C_in", shape=none];
    interface_4_out_0x55f1f89e2c38 [label="k_1", shape=none];
}

interface_4_out_0x55f1f89dd938 -> interface_1_in_0x55f1f89dd938;
interface_4_out_0x55f1f89ddbb8 -> interface_1_in_0x55f1f89ddbb8;
interface_4_out_0x55f1f89e2c38 -> interface_1_in_0x55f1f89e2c38;

interface_1_out_0x55f1ee7b7da0 -> interface_0_in_0x55f1ee7b7da0;
interface_1_out_0x55f1ee7b7dc8 -> interface_0_in_0x55f1ee7b7dc8;
interface_1_out_0x55f1f89ded40 -> interface_0_in_0x55f1f89ded40;
interface_1_out_0x55f1f89ded58 -> interface_0_in_0x55f1f89ded58;
interface_1_out_0x55f1ee7b7e18 -> interface_0_in_0x55f1ee7b7e18;

{
    rank = same;
    interface_3_out_0x55f1ee7b7da0;
    interface_3_out_0x55f1f89ddba0;
    interface_3_out_0x55f1f89e4810;
    interface_3_out_0x55f1ee7b7e18;
    interface_4_out_0x55f1f89dd938;
    interface_4_out_0x55f1f89ddbb8;
    interface_4_out_0x55f1f89e2c38;
}
subgraph cluster_subgraph_output {
    label = "Output";
    interface_5_in_0x55f1ee7b7da0 [label="N", shape=none];
    interface_5_in_0x55f1ee7b7dc8 [label="C_out", shape=none];
    interface_5_in_0x55f1ee7b7df0 [label="H", shape=none];
    interface_5_in_0x55f1ee7b7e18 [label="H", shape=none];
}
interface_0_out_0x55f1ee7b7da0 -> interface_5_in_0x55f1ee7b7da0;
interface_0_out_0x55f1ee7b7dc8 -> interface_5_in_0x55f1ee7b7dc8;
interface_0_out_0x55f1ee7b7df0 -> interface_5_in_0x55f1ee7b7df0;
interface_0_out_0x55f1ee7b7e18 -> interface_5_in_0x55f1ee7b7e18;

}

"""
class kernel_generated_0(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([24, 24, 3]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]

		# No contraction needed.
		t_2 = in_0

		# [H]@Split90c103914770ccee -> [k_2^-1*H]@Merge064b304184ad1926, [k_2]@Unfold468cf54ac1b57bee
		t_2 = torch.reshape(t_2, (1, 24, 16, 7, 112, ))

		# [k_2]@Unfold468cf54ac1b57bee -> [k_2]@Merge064b304184ad1927, [k_1]@Share26cfa48d169008e4
		t_2 = torch.reshape(t_2, (1, 384, 7, 112, ))
		t_2 = torch.nn.functional.unfold(t_2, (3, 1, ), padding=(1, 0, ))
		t_2 = torch.reshape(t_2, (1, 24, 16, 3, 7, 112, ))

		# Perform contraction.
		t_3 = torch.einsum("ljnkom, ijk -> linom", t_2, in_1)

		# No contraction needed.
		t_4 = t_3

		# [k_2^-1*H]@Merge064b304184ad1926, [k_2]@Merge064b304184ad1927 -> [H]@Iterator96123ba3184da39c
		t_4 = torch.reshape(t_4, (1, 24, 112, 112, ))

		# No need to crop the output tensor.
		y = t_4

		return y

class kernel_generated_1(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([96, 24, 3]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]

		# No contraction needed.
		t_2 = in_0

		# [H]@Split90c103914770ccee -> [k_2^-1*H]@Merge064b304184ad1926, [k_2]@Unfold468cf54ac1b57bee
		t_2 = torch.reshape(t_2, (1, 24, 8, 7, 56, ))

		# [k_2]@Unfold468cf54ac1b57bee -> [k_2]@Merge064b304184ad1927, [k_1]@Share26cfa48d169008e4
		t_2 = torch.reshape(t_2, (1, 192, 7, 56, ))
		t_2 = torch.nn.functional.unfold(t_2, (3, 1, ), padding=(1, 0, ))
		t_2 = torch.reshape(t_2, (1, 24, 8, 3, 7, 56, ))

		# Perform contraction.
		t_3 = torch.einsum("ljnkom, ijk -> linom", t_2, in_1)

		# No contraction needed.
		t_4 = t_3

		# [k_2^-1*H]@Merge064b304184ad1926, [k_2]@Merge064b304184ad1927 -> [H]@Iterator96123ba3184da39c
		t_4 = torch.reshape(t_4, (1, 96, 56, 56, ))

		# No need to crop the output tensor.
		y = t_4

		return y

class kernel_generated_2(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([192, 48, 3]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]

		# No contraction needed.
		t_2 = in_0

		# [H]@Split90c103914770ccee -> [k_2^-1*H]@Merge064b304184ad1926, [k_2]@Unfold468cf54ac1b57bee
		t_2 = torch.reshape(t_2, (1, 48, 8, 7, 56, ))

		# [k_2]@Unfold468cf54ac1b57bee -> [k_2]@Merge064b304184ad1927, [k_1]@Share26cfa48d169008e4
		t_2 = torch.reshape(t_2, (1, 384, 7, 56, ))
		t_2 = torch.nn.functional.unfold(t_2, (3, 1, ), padding=(1, 0, ))
		t_2 = torch.reshape(t_2, (1, 48, 8, 3, 7, 56, ))

		# Perform contraction.
		t_3 = torch.einsum("ljnkom, ijk -> linom", t_2, in_1)

		# No contraction needed.
		t_4 = t_3

		# [k_2^-1*H]@Merge064b304184ad1926, [k_2]@Merge064b304184ad1927 -> [H]@Iterator96123ba3184da39c
		t_4 = torch.reshape(t_4, (1, 192, 56, 56, ))

		# No need to crop the output tensor.
		y = t_4

		return y

class kernel_generated_3(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([192, 48, 3]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]

		# No contraction needed.
		t_2 = in_0

		# [H]@Split90c103914770ccee -> [k_2^-1*H]@Merge064b304184ad1926, [k_2]@Unfold468cf54ac1b57bee
		t_2 = torch.reshape(t_2, (1, 48, 4, 7, 28, ))

		# [k_2]@Unfold468cf54ac1b57bee -> [k_2]@Merge064b304184ad1927, [k_1]@Share26cfa48d169008e4
		t_2 = torch.reshape(t_2, (1, 192, 7, 28, ))
		t_2 = torch.nn.functional.unfold(t_2, (3, 1, ), padding=(1, 0, ))
		t_2 = torch.reshape(t_2, (1, 48, 4, 3, 7, 28, ))

		# Perform contraction.
		t_3 = torch.einsum("ljnkom, ijk -> linom", t_2, in_1)

		# No contraction needed.
		t_4 = t_3

		# [k_2^-1*H]@Merge064b304184ad1926, [k_2]@Merge064b304184ad1927 -> [H]@Iterator96123ba3184da39c
		t_4 = torch.reshape(t_4, (1, 192, 28, 28, ))

		# No need to crop the output tensor.
		y = t_4

		return y

class kernel_generated_4(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([256, 64, 3]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]

		# No contraction needed.
		t_2 = in_0

		# [H]@Split90c103914770ccee -> [k_2^-1*H]@Merge064b304184ad1926, [k_2]@Unfold468cf54ac1b57bee
		t_2 = torch.reshape(t_2, (1, 64, 4, 7, 28, ))

		# [k_2]@Unfold468cf54ac1b57bee -> [k_2]@Merge064b304184ad1927, [k_1]@Share26cfa48d169008e4
		t_2 = torch.reshape(t_2, (1, 256, 7, 28, ))
		t_2 = torch.nn.functional.unfold(t_2, (3, 1, ), padding=(1, 0, ))
		t_2 = torch.reshape(t_2, (1, 64, 4, 3, 7, 28, ))

		# Perform contraction.
		t_3 = torch.einsum("ljnkom, ijk -> linom", t_2, in_1)

		# No contraction needed.
		t_4 = t_3

		# [k_2^-1*H]@Merge064b304184ad1926, [k_2]@Merge064b304184ad1927 -> [H]@Iterator96123ba3184da39c
		t_4 = torch.reshape(t_4, (1, 256, 28, 28, ))

		# No need to crop the output tensor.
		y = t_4

		return y

