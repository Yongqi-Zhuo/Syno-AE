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
        interface_0_out_0x55e3a880e020 [label="N", shape=none];
        interface_0_out_0x55e3a880e048 [label="C_out", shape=none];
        interface_0_out_0x55e3a880e070 [label="H", shape=none];
        interface_0_out_0x55e3a880e098 [label="H", shape=none];
    }
    {
        rank = same;
        interface_0_out_0x55e3a880e020;
        interface_0_out_0x55e3a880e048;
        interface_0_out_0x55e3a880e070;
        interface_0_out_0x55e3a880e098;
    }
    // Input 0.
    subgraph cluster_subgraph_0_in_0 {
        label = "";
        interface_0_in_0x55e3a880e020 [label="N", shape=none];
        interface_0_in_0x55e3a8935800 [label="s", shape=none];
        interface_0_in_0x55e3a8935818 [label="s^-1*C_out", shape=none];
        interface_0_in_0x55e39eb542e0 [label="H", shape=none];
        interface_0_in_0x55e3a880e098 [label="H", shape=none];
    }
    {
        rank = same;
        interface_0_in_0x55e3a880e020;
        interface_0_in_0x55e3a8935800;
        interface_0_in_0x55e3a8935818;
        interface_0_in_0x55e39eb542e0;
        interface_0_in_0x55e3a880e098;
    }
    // Op's.
    op_0x55e39eb542c0 [label="Shift"];
    op_0x55e3a89357c0 [label="Merge"];
    // Dimension's.
    interface_0_in_0x55e39eb542e0 -> op_0x55e39eb542c0 [label="H"];
    interface_0_in_0x55e3a880e020 -> interface_0_out_0x55e3a880e020 [label="N"];
    op_0x55e3a89357c0 -> interface_0_out_0x55e3a880e048 [label="C_out"];
    op_0x55e39eb542c0 -> interface_0_out_0x55e3a880e070 [label="H"];
    interface_0_in_0x55e3a880e098 -> interface_0_out_0x55e3a880e098 [label="H"];
    interface_0_in_0x55e3a8935800 -> op_0x55e3a89357c0 [label="s"];
    interface_0_in_0x55e3a8935818 -> op_0x55e3a89357c0 [label="s^-1*C_out"];
}

// Stage tensor.
subgraph cluster_subgraph_1 {
    label = "Subgraph 1";
    // Reductions.
    reduce_0x7fb2b80072d0 [label="Sum", shape=box];
    reduce_0x7fb2b8003a98 [label="Sum", shape=box];
    // Output.
    subgraph cluster_subgraph_1_out {
        label = "";
        interface_1_out_0x55e3a880e020 [label="N", shape=none];
        interface_1_out_0x55e3a8935800 [label="s", shape=none];
        interface_1_out_0x55e3a8935818 [label="s^-1*C_out", shape=none];
        interface_1_out_0x55e39eb542e0 [label="H", shape=none];
        interface_1_out_0x55e3a880e098 [label="H", shape=none];
    }
    {
        rank = same;
        reduce_0x7fb2b80072d0;
        reduce_0x7fb2b8003a98;
        interface_1_out_0x55e3a880e020;
        interface_1_out_0x55e3a8935800;
        interface_1_out_0x55e3a8935818;
        interface_1_out_0x55e39eb542e0;
        interface_1_out_0x55e3a880e098;
    }
    // Input 0.
    subgraph cluster_subgraph_1_in_0 {
        label = "";
        interface_1_in_0x55e3a880e020 [label="N", shape=none];
        interface_1_in_0x55e3a8935800 [label="s", shape=none];
        interface_1_in_0x55e3a8934470 [label="s^-1*C_in", shape=none];
        interface_1_in_0x55e39eb542e0 [label="H", shape=none];
        interface_1_in_0x55e3a89346f0 [label="k_1", shape=none];
        interface_1_in_0x55e3a880e098 [label="H", shape=none];
    }
    // Input 1.
    subgraph cluster_subgraph_1_in_1 {
        label = "";
        interface_1_in_0x55e3a8934488 [label="s^-1*C_in", shape=none];
        interface_1_in_0x55e3a8934528 [label="s^-1*C_out", shape=none];
        interface_1_in_0x55e3a8934708 [label="k_1", shape=none];
    }
    {
        rank = same;
        interface_1_in_0x55e3a880e020;
        interface_1_in_0x55e3a8935800;
        interface_1_in_0x55e3a8934470;
        interface_1_in_0x55e39eb542e0;
        interface_1_in_0x55e3a89346f0;
        interface_1_in_0x55e3a880e098;
        interface_1_in_0x55e3a8934488;
        interface_1_in_0x55e3a8934528;
        interface_1_in_0x55e3a8934708;
    }
    // Op's.
    op_0x55e3a8934450 [label="Share"];
    op_0x55e3a89344f0 [label="Share"];
    op_0x55e3a89346d0 [label="Share"];
    op_0x55e3a89348f8 [label="Expand"];
    // Dimension's.
    interface_1_in_0x55e39eb542e0 -> interface_1_out_0x55e39eb542e0 [label="H"];
    interface_1_in_0x55e3a880e020 -> interface_1_out_0x55e3a880e020 [label="N"];
    interface_1_in_0x55e3a880e098 -> interface_1_out_0x55e3a880e098 [label="H"];
    interface_1_in_0x55e3a8934470 -> op_0x55e3a8934450 [label="s^-1*C_in"];
    interface_1_in_0x55e3a8934488 -> op_0x55e3a8934450 [label="s^-1*C_in"];
    op_0x55e3a89348f8 -> op_0x55e3a89344f0 [label="s^-1*C_out"];
    interface_1_in_0x55e3a8934528 -> op_0x55e3a89344f0 [label="s^-1*C_out"];
    interface_1_in_0x55e3a89346f0 -> op_0x55e3a89346d0 [label="k_1"];
    interface_1_in_0x55e3a8934708 -> op_0x55e3a89346d0 [label="k_1"];
    interface_1_in_0x55e3a8935800 -> interface_1_out_0x55e3a8935800 [label="s"];
    op_0x55e3a89344f0 -> interface_1_out_0x55e3a8935818 [label="s^-1*C_out"];
    op_0x55e3a89346d0 -> reduce_0x7fb2b8003a98 [label="k_1"];
    op_0x55e3a8934450 -> reduce_0x7fb2b80072d0 [label="s^-1*C_in"];
}

// Stage tensor.
subgraph cluster_subgraph_2 {
    label = "Subgraph 2";
    // Reductions.
    // Output.
    subgraph cluster_subgraph_2_out {
        label = "";
        interface_2_out_0x55e3a880e020 [label="N", shape=none];
        interface_2_out_0x55e3a8935800 [label="s", shape=none];
        interface_2_out_0x55e3a8934470 [label="s^-1*C_in", shape=none];
        interface_2_out_0x55e39eb542e0 [label="H", shape=none];
        interface_2_out_0x55e3a89346f0 [label="k_1", shape=none];
        interface_2_out_0x55e3a880e098 [label="H", shape=none];
    }
    {
        rank = same;
        interface_2_out_0x55e3a880e020;
        interface_2_out_0x55e3a8935800;
        interface_2_out_0x55e3a8934470;
        interface_2_out_0x55e39eb542e0;
        interface_2_out_0x55e3a89346f0;
        interface_2_out_0x55e3a880e098;
    }
    // Input 0.
    subgraph cluster_subgraph_2_in_0 {
        label = "";
        interface_2_in_0x55e3a880e020 [label="N", shape=none];
        interface_2_in_0x55e3a8936330 [label="C_in", shape=none];
        interface_2_in_0x55e39eb542e0 [label="H", shape=none];
        interface_2_in_0x55e3a89346f0 [label="k_1", shape=none];
        interface_2_in_0x55e3a880e098 [label="H", shape=none];
    }
    {
        rank = same;
        interface_2_in_0x55e3a880e020;
        interface_2_in_0x55e3a8936330;
        interface_2_in_0x55e39eb542e0;
        interface_2_in_0x55e3a89346f0;
        interface_2_in_0x55e3a880e098;
    }
    // Op's.
    op_0x55e3a89362f0 [label="Split"];
    // Dimension's.
    interface_2_in_0x55e39eb542e0 -> interface_2_out_0x55e39eb542e0 [label="H"];
    interface_2_in_0x55e3a880e020 -> interface_2_out_0x55e3a880e020 [label="N"];
    interface_2_in_0x55e3a880e098 -> interface_2_out_0x55e3a880e098 [label="H"];
    op_0x55e3a89362f0 -> interface_2_out_0x55e3a8934470 [label="s^-1*C_in"];
    interface_2_in_0x55e3a89346f0 -> interface_2_out_0x55e3a89346f0 [label="k_1"];
    op_0x55e3a89362f0 -> interface_2_out_0x55e3a8935800 [label="s"];
    interface_2_in_0x55e3a8936330 -> op_0x55e3a89362f0 [label="C_in"];
}

// Stage tensor.
subgraph cluster_subgraph_3 {
    label = "Subgraph 3";
    // Reductions.
    reduce_0x7fb2b800deb0 [label="Sum", shape=box];
    // Output.
    subgraph cluster_subgraph_3_out {
        label = "";
        interface_3_out_0x55e3a880e020 [label="N", shape=none];
        interface_3_out_0x55e3a8936330 [label="C_in", shape=none];
        interface_3_out_0x55e39eb542e0 [label="H", shape=none];
        interface_3_out_0x55e3a89346f0 [label="k_1", shape=none];
        interface_3_out_0x55e3a880e098 [label="H", shape=none];
    }
    {
        rank = same;
        reduce_0x7fb2b800deb0;
        interface_3_out_0x55e3a880e020;
        interface_3_out_0x55e3a8936330;
        interface_3_out_0x55e39eb542e0;
        interface_3_out_0x55e3a89346f0;
        interface_3_out_0x55e3a880e098;
    }
    // Input 0.
    subgraph cluster_subgraph_3_in_0 {
        label = "";
        interface_3_in_0x55e3a880e020 [label="N", shape=none];
        interface_3_in_0x55e3a8936330 [label="C_in", shape=none];
        interface_3_in_0x55e39eb542e0 [label="H", shape=none];
        interface_3_in_0x55e39eb54460 [label="H", shape=none];
    }
    {
        rank = same;
        interface_3_in_0x55e3a880e020;
        interface_3_in_0x55e3a8936330;
        interface_3_in_0x55e39eb542e0;
        interface_3_in_0x55e39eb54460;
    }
    // Op's.
    op_0x55e39eb54440 [label="Shift"];
    op_0x55e3a89368c0 [label="Unfold"];
    op_0x55e3a89547f0 [label="Split"];
    // Dimension's.
    interface_3_in_0x55e39eb542e0 -> interface_3_out_0x55e39eb542e0 [label="H"];
    interface_3_in_0x55e39eb54460 -> op_0x55e39eb54440 [label="H"];
    interface_3_in_0x55e3a880e020 -> interface_3_out_0x55e3a880e020 [label="N"];
    op_0x55e3a89368c0 -> interface_3_out_0x55e3a880e098 [label="H"];
    op_0x55e3a89547f0 -> interface_3_out_0x55e3a89346f0 [label="k_1"];
    interface_3_in_0x55e3a8936330 -> interface_3_out_0x55e3a8936330 [label="C_in"];
    op_0x55e39eb54440 -> op_0x55e3a89368c0 [label="H"];
    op_0x55e3a89368c0 -> op_0x55e3a89547f0 [label="g^-2*k_1*C_out^2"];
    op_0x55e3a89547f0 -> reduce_0x7fb2b800deb0 [label="g^-2*C_out^2"];
}

// Input tensor.
subgraph cluster_subgraph_4 {
    label = "Input 0";
    interface_4_out_0x55e3a880e020 [label="N", shape=none];
    interface_4_out_0x55e3a8936330 [label="C_in", shape=none];
    interface_4_out_0x55e39eb542e0 [label="H", shape=none];
    interface_4_out_0x55e39eb54460 [label="H", shape=none];
}

interface_4_out_0x55e3a880e020 -> interface_3_in_0x55e3a880e020;
interface_4_out_0x55e3a8936330 -> interface_3_in_0x55e3a8936330;
interface_4_out_0x55e39eb542e0 -> interface_3_in_0x55e39eb542e0;
interface_4_out_0x55e39eb54460 -> interface_3_in_0x55e39eb54460;

interface_3_out_0x55e3a880e020 -> interface_2_in_0x55e3a880e020;
interface_3_out_0x55e3a8936330 -> interface_2_in_0x55e3a8936330;
interface_3_out_0x55e39eb542e0 -> interface_2_in_0x55e39eb542e0;
interface_3_out_0x55e3a89346f0 -> interface_2_in_0x55e3a89346f0;
interface_3_out_0x55e3a880e098 -> interface_2_in_0x55e3a880e098;

interface_2_out_0x55e3a880e020 -> interface_1_in_0x55e3a880e020;
interface_2_out_0x55e3a8935800 -> interface_1_in_0x55e3a8935800;
interface_2_out_0x55e3a8934470 -> interface_1_in_0x55e3a8934470;
interface_2_out_0x55e39eb542e0 -> interface_1_in_0x55e39eb542e0;
interface_2_out_0x55e3a89346f0 -> interface_1_in_0x55e3a89346f0;
interface_2_out_0x55e3a880e098 -> interface_1_in_0x55e3a880e098;

// Input tensor.
subgraph cluster_subgraph_5 {
    label = "Input 1";
    interface_5_out_0x55e3a8934488 [label="s^-1*C_in", shape=none];
    interface_5_out_0x55e3a8934528 [label="s^-1*C_out", shape=none];
    interface_5_out_0x55e3a8934708 [label="k_1", shape=none];
}

interface_5_out_0x55e3a8934488 -> interface_1_in_0x55e3a8934488;
interface_5_out_0x55e3a8934528 -> interface_1_in_0x55e3a8934528;
interface_5_out_0x55e3a8934708 -> interface_1_in_0x55e3a8934708;

interface_1_out_0x55e3a880e020 -> interface_0_in_0x55e3a880e020;
interface_1_out_0x55e3a8935800 -> interface_0_in_0x55e3a8935800;
interface_1_out_0x55e3a8935818 -> interface_0_in_0x55e3a8935818;
interface_1_out_0x55e39eb542e0 -> interface_0_in_0x55e39eb542e0;
interface_1_out_0x55e3a880e098 -> interface_0_in_0x55e3a880e098;

{
    rank = same;
    interface_4_out_0x55e3a880e020;
    interface_4_out_0x55e3a8936330;
    interface_4_out_0x55e39eb542e0;
    interface_4_out_0x55e39eb54460;
    interface_5_out_0x55e3a8934488;
    interface_5_out_0x55e3a8934528;
    interface_5_out_0x55e3a8934708;
}
subgraph cluster_subgraph_output {
    label = "Output";
    interface_6_in_0x55e3a880e020 [label="N", shape=none];
    interface_6_in_0x55e3a880e048 [label="C_out", shape=none];
    interface_6_in_0x55e3a880e070 [label="H", shape=none];
    interface_6_in_0x55e3a880e098 [label="H", shape=none];
}
interface_0_out_0x55e3a880e020 -> interface_6_in_0x55e3a880e020;
interface_0_out_0x55e3a880e048 -> interface_6_in_0x55e3a880e048;
interface_0_out_0x55e3a880e070 -> interface_6_in_0x55e3a880e070;
interface_0_out_0x55e3a880e098 -> interface_6_in_0x55e3a880e098;

}

"""
class kernel_generated_0(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([64, 16, 3]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]

		# No contraction needed.
		t_2 = in_0

		# [H]@Shifte8f9f2c59622719c -> [H]@Unfold2f377c9d503beb1b
		t_2 = torch.roll(t_2, self.shift_direction, 3)

		# [H]@Unfold2f377c9d503beb1b -> [H]@Iteratorb0a1def4ad5784ec, [g^-2*k_1*C_out^2]@Splitf17251383f4348c7
		t_2 = torch.reshape(t_2, (1, 7168, 56, 1, ))
		t_2 = torch.nn.functional.unfold(t_2, (3, 1, ), padding=(1, 0, ))
		t_2 = torch.reshape(t_2, (1, 128, 56, 3, 56, ))

		# [g^-2*k_1*C_out^2]@Splitf17251383f4348c7 -> [g^-2*C_out^2]@Reduce159437b921f023cf, [k_1]@Share26cfa48d169008e4
		t_2 = torch.reshape(t_2, (1, 128, 56, 1, 3, 56, ))

		# [g^-2*C_out^2]@Reduce
		t_2 = torch.sum(t_2, dim=(3, ))

		# No contraction needed.
		t_3 = t_2

		# [C_in]@Split69dd43e05c8c5ddb -> [s]@Merge03a73148aa81036c, [s^-1*C_in]@Share8de6f167adbbf8aa
		t_3 = torch.reshape(t_3, (1, 2, 64, 56, 3, 56, ))

		# Perform contraction.
		t_4 = torch.einsum("moilkn, ijk -> mojln", t_3, in_1)

		# No contraction needed.
		t_5 = t_4

		# [s]@Merge03a73148aa81036c, [s^-1*C_out]@Merge03a73148aa81036f -> [C_out]@Iteratorc7f8eb87a5a0a9e0
		t_5 = torch.reshape(t_5, (1, 32, 56, 56, ))

		# [H]@Shift41a433c05e30b91d -> [H]@Iterator96123ba3184da39c
		t_5 = torch.roll(t_5, self.shift_direction, 2)

		# No need to crop the output tensor.
		y = t_5

		return y

class kernel_generated_1(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([64, 16, 3]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]

		# No contraction needed.
		t_2 = in_0

		# [H]@Shifte8f9f2c59622719c -> [H]@Unfold2f377c9d503beb1b
		t_2 = torch.roll(t_2, self.shift_direction, 3)

		# [H]@Unfold2f377c9d503beb1b -> [H]@Iteratorb0a1def4ad5784ec, [g^-2*k_1*C_out^2]@Splitf17251383f4348c7
		t_2 = torch.reshape(t_2, (1, 3584, 28, 1, ))
		t_2 = torch.nn.functional.unfold(t_2, (3, 1, ), padding=(1, 0, ))
		t_2 = torch.reshape(t_2, (1, 128, 28, 3, 28, ))

		# [g^-2*k_1*C_out^2]@Splitf17251383f4348c7 -> [g^-2*C_out^2]@Reduce159437b921f023cf, [k_1]@Share26cfa48d169008e4
		t_2 = torch.reshape(t_2, (1, 128, 28, 1, 3, 28, ))

		# [g^-2*C_out^2]@Reduce
		t_2 = torch.sum(t_2, dim=(3, ))

		# No contraction needed.
		t_3 = t_2

		# [C_in]@Split69dd43e05c8c5ddb -> [s]@Merge03a73148aa81036c, [s^-1*C_in]@Share8de6f167adbbf8aa
		t_3 = torch.reshape(t_3, (1, 2, 64, 28, 3, 28, ))

		# Perform contraction.
		t_4 = torch.einsum("moilkn, ijk -> mojln", t_3, in_1)

		# No contraction needed.
		t_5 = t_4

		# [s]@Merge03a73148aa81036c, [s^-1*C_out]@Merge03a73148aa81036f -> [C_out]@Iteratorc7f8eb87a5a0a9e0
		t_5 = torch.reshape(t_5, (1, 32, 28, 28, ))

		# [H]@Shift41a433c05e30b91d -> [H]@Iterator96123ba3184da39c
		t_5 = torch.roll(t_5, self.shift_direction, 2)

		# No need to crop the output tensor.
		y = t_5

		return y

class kernel_generated_2(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([64, 16, 3]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]

		# No contraction needed.
		t_2 = in_0

		# [H]@Shifte8f9f2c59622719c -> [H]@Unfold2f377c9d503beb1b
		t_2 = torch.roll(t_2, self.shift_direction, 3)

		# [H]@Unfold2f377c9d503beb1b -> [H]@Iteratorb0a1def4ad5784ec, [g^-2*k_1*C_out^2]@Splitf17251383f4348c7
		t_2 = torch.reshape(t_2, (1, 1792, 14, 1, ))
		t_2 = torch.nn.functional.unfold(t_2, (3, 1, ), padding=(1, 0, ))
		t_2 = torch.reshape(t_2, (1, 128, 14, 3, 14, ))

		# [g^-2*k_1*C_out^2]@Splitf17251383f4348c7 -> [g^-2*C_out^2]@Reduce159437b921f023cf, [k_1]@Share26cfa48d169008e4
		t_2 = torch.reshape(t_2, (1, 128, 14, 1, 3, 14, ))

		# [g^-2*C_out^2]@Reduce
		t_2 = torch.sum(t_2, dim=(3, ))

		# No contraction needed.
		t_3 = t_2

		# [C_in]@Split69dd43e05c8c5ddb -> [s]@Merge03a73148aa81036c, [s^-1*C_in]@Share8de6f167adbbf8aa
		t_3 = torch.reshape(t_3, (1, 2, 64, 14, 3, 14, ))

		# Perform contraction.
		t_4 = torch.einsum("moilkn, ijk -> mojln", t_3, in_1)

		# No contraction needed.
		t_5 = t_4

		# [s]@Merge03a73148aa81036c, [s^-1*C_out]@Merge03a73148aa81036f -> [C_out]@Iteratorc7f8eb87a5a0a9e0
		t_5 = torch.reshape(t_5, (1, 32, 14, 14, ))

		# [H]@Shift41a433c05e30b91d -> [H]@Iterator96123ba3184da39c
		t_5 = torch.roll(t_5, self.shift_direction, 2)

		# No need to crop the output tensor.
		y = t_5

		return y

class kernel_generated_3(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([64, 16, 3]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]

		# No contraction needed.
		t_2 = in_0

		# [H]@Shifte8f9f2c59622719c -> [H]@Unfold2f377c9d503beb1b
		t_2 = torch.roll(t_2, self.shift_direction, 3)

		# [H]@Unfold2f377c9d503beb1b -> [H]@Iteratorb0a1def4ad5784ec, [g^-2*k_1*C_out^2]@Splitf17251383f4348c7
		t_2 = torch.reshape(t_2, (1, 896, 7, 1, ))
		t_2 = torch.nn.functional.unfold(t_2, (3, 1, ), padding=(1, 0, ))
		t_2 = torch.reshape(t_2, (1, 128, 7, 3, 7, ))

		# [g^-2*k_1*C_out^2]@Splitf17251383f4348c7 -> [g^-2*C_out^2]@Reduce159437b921f023cf, [k_1]@Share26cfa48d169008e4
		t_2 = torch.reshape(t_2, (1, 128, 7, 1, 3, 7, ))

		# [g^-2*C_out^2]@Reduce
		t_2 = torch.sum(t_2, dim=(3, ))

		# No contraction needed.
		t_3 = t_2

		# [C_in]@Split69dd43e05c8c5ddb -> [s]@Merge03a73148aa81036c, [s^-1*C_in]@Share8de6f167adbbf8aa
		t_3 = torch.reshape(t_3, (1, 2, 64, 7, 3, 7, ))

		# Perform contraction.
		t_4 = torch.einsum("moilkn, ijk -> mojln", t_3, in_1)

		# No contraction needed.
		t_5 = t_4

		# [s]@Merge03a73148aa81036c, [s^-1*C_out]@Merge03a73148aa81036f -> [C_out]@Iteratorc7f8eb87a5a0a9e0
		t_5 = torch.reshape(t_5, (1, 32, 7, 7, ))

		# [H]@Shift41a433c05e30b91d -> [H]@Iterator96123ba3184da39c
		t_5 = torch.roll(t_5, self.shift_direction, 2)

		# No need to crop the output tensor.
		y = t_5

		return y

