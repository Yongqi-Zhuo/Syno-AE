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
        interface_0_in_0x5596d7788c88 [label="C_out", shape=none];
        interface_0_in_0x5596d7877240 [label="k_2^-1*H", shape=none];
        interface_0_in_0x5596d7877258 [label="k_2", shape=none];
        interface_0_in_0x5596d7788cd8 [label="H", shape=none];
    }
    {
        rank = same;
        interface_0_in_0x5596d7788c60;
        interface_0_in_0x5596d7788c88;
        interface_0_in_0x5596d7877240;
        interface_0_in_0x5596d7877258;
        interface_0_in_0x5596d7788cd8;
    }
    // Op's.
    op_0x5596d7877200 [label="Merge"];
    // Dimension's.
    interface_0_in_0x5596d7788c60 -> interface_0_out_0x5596d7788c60 [label="N"];
    interface_0_in_0x5596d7788c88 -> interface_0_out_0x5596d7788c88 [label="C_out"];
    op_0x5596d7877200 -> interface_0_out_0x5596d7788cb0 [label="H"];
    interface_0_in_0x5596d7788cd8 -> interface_0_out_0x5596d7788cd8 [label="H"];
    interface_0_in_0x5596d7877240 -> op_0x5596d7877200 [label="k_2^-1*H"];
    interface_0_in_0x5596d7877258 -> op_0x5596d7877200 [label="k_2"];
}

// Stage tensor.
subgraph cluster_subgraph_1 {
    label = "Subgraph 1";
    // Reductions.
    reduce_0x7ef0e4005c70 [label="Sum", shape=box];
    reduce_0x7ef0e4001a98 [label="Sum", shape=box];
    // Output.
    subgraph cluster_subgraph_1_out {
        label = "";
        interface_1_out_0x5596d7788c60 [label="N", shape=none];
        interface_1_out_0x5596d7788c88 [label="C_out", shape=none];
        interface_1_out_0x5596d7877240 [label="k_2^-1*H", shape=none];
        interface_1_out_0x5596d7877258 [label="k_2", shape=none];
        interface_1_out_0x5596d7788cd8 [label="H", shape=none];
    }
    {
        rank = same;
        reduce_0x7ef0e4005c70;
        reduce_0x7ef0e4001a98;
        interface_1_out_0x5596d7788c60;
        interface_1_out_0x5596d7788c88;
        interface_1_out_0x5596d7877240;
        interface_1_out_0x5596d7877258;
        interface_1_out_0x5596d7788cd8;
    }
    // Input 0.
    subgraph cluster_subgraph_1_in_0 {
        label = "";
        interface_1_in_0x5596d7788c60 [label="N", shape=none];
        interface_1_in_0x5596d7875440 [label="C_in", shape=none];
        interface_1_in_0x5596d7877240 [label="k_2^-1*H", shape=none];
        interface_1_in_0x5596d7875490 [label="k_1", shape=none];
        interface_1_in_0x5596d7877258 [label="k_2", shape=none];
        interface_1_in_0x5596d7788cd8 [label="H", shape=none];
    }
    // Input 1.
    subgraph cluster_subgraph_1_in_1 {
        label = "";
        interface_1_in_0x5596d7875138 [label="C_out", shape=none];
        interface_1_in_0x5596d7875458 [label="C_in", shape=none];
        interface_1_in_0x5596d78754a8 [label="k_1", shape=none];
    }
    {
        rank = same;
        interface_1_in_0x5596d7788c60;
        interface_1_in_0x5596d7875440;
        interface_1_in_0x5596d7877240;
        interface_1_in_0x5596d7875490;
        interface_1_in_0x5596d7877258;
        interface_1_in_0x5596d7788cd8;
        interface_1_in_0x5596d7875138;
        interface_1_in_0x5596d7875458;
        interface_1_in_0x5596d78754a8;
    }
    // Op's.
    op_0x5596d7875100 [label="Share"];
    op_0x5596d7875420 [label="Share"];
    op_0x5596d7875470 [label="Share"];
    op_0x5596d7875618 [label="Expand"];
    // Dimension's.
    interface_1_in_0x5596d7788c60 -> interface_1_out_0x5596d7788c60 [label="N"];
    op_0x5596d7875100 -> interface_1_out_0x5596d7788c88 [label="C_out"];
    interface_1_in_0x5596d7788cd8 -> interface_1_out_0x5596d7788cd8 [label="H"];
    op_0x5596d7875618 -> op_0x5596d7875100 [label="C_out"];
    interface_1_in_0x5596d7875138 -> op_0x5596d7875100 [label="C_out"];
    interface_1_in_0x5596d7875440 -> op_0x5596d7875420 [label="C_in"];
    interface_1_in_0x5596d7875458 -> op_0x5596d7875420 [label="C_in"];
    interface_1_in_0x5596d7875490 -> op_0x5596d7875470 [label="k_1"];
    interface_1_in_0x5596d78754a8 -> op_0x5596d7875470 [label="k_1"];
    interface_1_in_0x5596d7877240 -> interface_1_out_0x5596d7877240 [label="k_2^-1*H"];
    interface_1_in_0x5596d7877258 -> interface_1_out_0x5596d7877258 [label="k_2"];
    op_0x5596d7875470 -> reduce_0x7ef0e4001a98 [label="k_1"];
    op_0x5596d7875420 -> reduce_0x7ef0e4005c70 [label="C_in"];
}

// Stage tensor.
subgraph cluster_subgraph_2 {
    label = "Subgraph 2";
    // Reductions.
    // Output.
    subgraph cluster_subgraph_2_out {
        label = "";
        interface_2_out_0x5596d7788c60 [label="N", shape=none];
        interface_2_out_0x5596d7875440 [label="C_in", shape=none];
        interface_2_out_0x5596d7877240 [label="k_2^-1*H", shape=none];
        interface_2_out_0x5596d7875490 [label="k_1", shape=none];
        interface_2_out_0x5596d7877258 [label="k_2", shape=none];
        interface_2_out_0x5596d7788cd8 [label="H", shape=none];
    }
    {
        rank = same;
        interface_2_out_0x5596d7788c60;
        interface_2_out_0x5596d7875440;
        interface_2_out_0x5596d7877240;
        interface_2_out_0x5596d7875490;
        interface_2_out_0x5596d7877258;
        interface_2_out_0x5596d7788cd8;
    }
    // Input 0.
    subgraph cluster_subgraph_2_in_0 {
        label = "";
        interface_2_in_0x5596d7788c60 [label="N", shape=none];
        interface_2_in_0x5596d7875440 [label="C_in", shape=none];
        interface_2_in_0x5596d7883e70 [label="H", shape=none];
        interface_2_in_0x5596d7788cd8 [label="H", shape=none];
    }
    {
        rank = same;
        interface_2_in_0x5596d7788c60;
        interface_2_in_0x5596d7875440;
        interface_2_in_0x5596d7883e70;
        interface_2_in_0x5596d7788cd8;
    }
    // Op's.
    op_0x5596d78796c0 [label="Unfold"];
    op_0x5596d7883e30 [label="Split"];
    // Dimension's.
    interface_2_in_0x5596d7788c60 -> interface_2_out_0x5596d7788c60 [label="N"];
    interface_2_in_0x5596d7788cd8 -> interface_2_out_0x5596d7788cd8 [label="H"];
    interface_2_in_0x5596d7875440 -> interface_2_out_0x5596d7875440 [label="C_in"];
    op_0x5596d78796c0 -> interface_2_out_0x5596d7875490 [label="k_1"];
    op_0x5596d7883e30 -> interface_2_out_0x5596d7877240 [label="k_2^-1*H"];
    op_0x5596d78796c0 -> interface_2_out_0x5596d7877258 [label="k_2"];
    op_0x5596d7883e30 -> op_0x5596d78796c0 [label="k_2"];
    interface_2_in_0x5596d7883e70 -> op_0x5596d7883e30 [label="H"];
}

// Input tensor.
subgraph cluster_subgraph_3 {
    label = "Input 0";
    interface_3_out_0x5596d7788c60 [label="N", shape=none];
    interface_3_out_0x5596d7875440 [label="C_in", shape=none];
    interface_3_out_0x5596d7883e70 [label="H", shape=none];
    interface_3_out_0x5596d7788cd8 [label="H", shape=none];
}

interface_3_out_0x5596d7788c60 -> interface_2_in_0x5596d7788c60;
interface_3_out_0x5596d7875440 -> interface_2_in_0x5596d7875440;
interface_3_out_0x5596d7883e70 -> interface_2_in_0x5596d7883e70;
interface_3_out_0x5596d7788cd8 -> interface_2_in_0x5596d7788cd8;

interface_2_out_0x5596d7788c60 -> interface_1_in_0x5596d7788c60;
interface_2_out_0x5596d7875440 -> interface_1_in_0x5596d7875440;
interface_2_out_0x5596d7877240 -> interface_1_in_0x5596d7877240;
interface_2_out_0x5596d7875490 -> interface_1_in_0x5596d7875490;
interface_2_out_0x5596d7877258 -> interface_1_in_0x5596d7877258;
interface_2_out_0x5596d7788cd8 -> interface_1_in_0x5596d7788cd8;

// Input tensor.
subgraph cluster_subgraph_4 {
    label = "Input 1";
    interface_4_out_0x5596d7875138 [label="C_out", shape=none];
    interface_4_out_0x5596d7875458 [label="C_in", shape=none];
    interface_4_out_0x5596d78754a8 [label="k_1", shape=none];
}

interface_4_out_0x5596d7875138 -> interface_1_in_0x5596d7875138;
interface_4_out_0x5596d7875458 -> interface_1_in_0x5596d7875458;
interface_4_out_0x5596d78754a8 -> interface_1_in_0x5596d78754a8;

interface_1_out_0x5596d7788c60 -> interface_0_in_0x5596d7788c60;
interface_1_out_0x5596d7788c88 -> interface_0_in_0x5596d7788c88;
interface_1_out_0x5596d7877240 -> interface_0_in_0x5596d7877240;
interface_1_out_0x5596d7877258 -> interface_0_in_0x5596d7877258;
interface_1_out_0x5596d7788cd8 -> interface_0_in_0x5596d7788cd8;

{
    rank = same;
    interface_3_out_0x5596d7788c60;
    interface_3_out_0x5596d7875440;
    interface_3_out_0x5596d7883e70;
    interface_3_out_0x5596d7788cd8;
    interface_4_out_0x5596d7875138;
    interface_4_out_0x5596d7875458;
    interface_4_out_0x5596d78754a8;
}
subgraph cluster_subgraph_output {
    label = "Output";
    interface_5_in_0x5596d7788c60 [label="N", shape=none];
    interface_5_in_0x5596d7788c88 [label="C_out", shape=none];
    interface_5_in_0x5596d7788cb0 [label="H", shape=none];
    interface_5_in_0x5596d7788cd8 [label="H", shape=none];
}
interface_0_out_0x5596d7788c60 -> interface_5_in_0x5596d7788c60;
interface_0_out_0x5596d7788c88 -> interface_5_in_0x5596d7788c88;
interface_0_out_0x5596d7788cb0 -> interface_5_in_0x5596d7788cb0;
interface_0_out_0x5596d7788cd8 -> interface_5_in_0x5596d7788cd8;

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

