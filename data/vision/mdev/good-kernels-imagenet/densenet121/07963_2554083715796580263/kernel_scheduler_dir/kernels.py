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
        interface_0_out_0x560a242c5b10 [label="N", shape=none];
        interface_0_out_0x560a242c5b38 [label="C_out", shape=none];
        interface_0_out_0x560a242c5b60 [label="H", shape=none];
        interface_0_out_0x560a242c5b88 [label="H", shape=none];
    }
    {
        rank = same;
        interface_0_out_0x560a242c5b10;
        interface_0_out_0x560a242c5b38;
        interface_0_out_0x560a242c5b60;
        interface_0_out_0x560a242c5b88;
    }
    // Input 0.
    subgraph cluster_subgraph_0_in_0 {
        label = "";
        interface_0_in_0x560a242c5b10 [label="N", shape=none];
        interface_0_in_0x560a2238a080 [label="s", shape=none];
        interface_0_in_0x560a2238a098 [label="s^-1*C_out", shape=none];
        interface_0_in_0x560a2447e6e0 [label="H", shape=none];
        interface_0_in_0x560a242c5b88 [label="H", shape=none];
    }
    {
        rank = same;
        interface_0_in_0x560a242c5b10;
        interface_0_in_0x560a2238a080;
        interface_0_in_0x560a2238a098;
        interface_0_in_0x560a2447e6e0;
        interface_0_in_0x560a242c5b88;
    }
    // Op's.
    op_0x560a2238a040 [label="Merge"];
    op_0x560a2447e6c0 [label="Shift"];
    // Dimension's.
    interface_0_in_0x560a2238a080 -> op_0x560a2238a040 [label="s"];
    interface_0_in_0x560a2238a098 -> op_0x560a2238a040 [label="s^-1*C_out"];
    interface_0_in_0x560a242c5b10 -> interface_0_out_0x560a242c5b10 [label="N"];
    op_0x560a2238a040 -> interface_0_out_0x560a242c5b38 [label="C_out"];
    op_0x560a2447e6c0 -> interface_0_out_0x560a242c5b60 [label="H"];
    interface_0_in_0x560a242c5b88 -> interface_0_out_0x560a242c5b88 [label="H"];
    interface_0_in_0x560a2447e6e0 -> op_0x560a2447e6c0 [label="H"];
}

// Stage tensor.
subgraph cluster_subgraph_1 {
    label = "Subgraph 1";
    // Reductions.
    reduce_0x7f92180055d0 [label="Sum", shape=box];
    reduce_0x7f9218001998 [label="Sum", shape=box];
    // Output.
    subgraph cluster_subgraph_1_out {
        label = "";
        interface_1_out_0x560a242c5b10 [label="N", shape=none];
        interface_1_out_0x560a2238a080 [label="s", shape=none];
        interface_1_out_0x560a2238a098 [label="s^-1*C_out", shape=none];
        interface_1_out_0x560a2447e6e0 [label="H", shape=none];
        interface_1_out_0x560a242c5b88 [label="H", shape=none];
    }
    {
        rank = same;
        reduce_0x7f92180055d0;
        reduce_0x7f9218001998;
        interface_1_out_0x560a242c5b10;
        interface_1_out_0x560a2238a080;
        interface_1_out_0x560a2238a098;
        interface_1_out_0x560a2447e6e0;
        interface_1_out_0x560a242c5b88;
    }
    // Input 0.
    subgraph cluster_subgraph_1_in_0 {
        label = "";
        interface_1_in_0x560a242c5b10 [label="N", shape=none];
        interface_1_in_0x560a2238a080 [label="s", shape=none];
        interface_1_in_0x560a242db770 [label="s^-1*C_in", shape=none];
        interface_1_in_0x560a2447e6e0 [label="H", shape=none];
        interface_1_in_0x560a242db7c0 [label="k_1", shape=none];
        interface_1_in_0x560a242c5b88 [label="H", shape=none];
    }
    // Input 1.
    subgraph cluster_subgraph_1_in_1 {
        label = "";
        interface_1_in_0x560a242db788 [label="s^-1*C_in", shape=none];
        interface_1_in_0x560a242db828 [label="s^-1*C_out", shape=none];
        interface_1_in_0x560a242db7d8 [label="k_1", shape=none];
    }
    {
        rank = same;
        interface_1_in_0x560a242c5b10;
        interface_1_in_0x560a2238a080;
        interface_1_in_0x560a242db770;
        interface_1_in_0x560a2447e6e0;
        interface_1_in_0x560a242db7c0;
        interface_1_in_0x560a242c5b88;
        interface_1_in_0x560a242db788;
        interface_1_in_0x560a242db828;
        interface_1_in_0x560a242db7d8;
    }
    // Op's.
    op_0x560a242db750 [label="Share"];
    op_0x560a242db7a0 [label="Share"];
    op_0x560a242db7f0 [label="Share"];
    op_0x560a24643078 [label="Expand"];
    // Dimension's.
    interface_1_in_0x560a2238a080 -> interface_1_out_0x560a2238a080 [label="s"];
    op_0x560a242db7f0 -> interface_1_out_0x560a2238a098 [label="s^-1*C_out"];
    interface_1_in_0x560a242c5b10 -> interface_1_out_0x560a242c5b10 [label="N"];
    interface_1_in_0x560a242c5b88 -> interface_1_out_0x560a242c5b88 [label="H"];
    interface_1_in_0x560a242db770 -> op_0x560a242db750 [label="s^-1*C_in"];
    interface_1_in_0x560a242db788 -> op_0x560a242db750 [label="s^-1*C_in"];
    interface_1_in_0x560a242db7c0 -> op_0x560a242db7a0 [label="k_1"];
    interface_1_in_0x560a242db7d8 -> op_0x560a242db7a0 [label="k_1"];
    op_0x560a24643078 -> op_0x560a242db7f0 [label="s^-1*C_out"];
    interface_1_in_0x560a242db828 -> op_0x560a242db7f0 [label="s^-1*C_out"];
    interface_1_in_0x560a2447e6e0 -> interface_1_out_0x560a2447e6e0 [label="H"];
    op_0x560a242db7a0 -> reduce_0x7f9218001998 [label="k_1"];
    op_0x560a242db750 -> reduce_0x7f92180055d0 [label="s^-1*C_in"];
}

// Stage tensor.
subgraph cluster_subgraph_2 {
    label = "Subgraph 2";
    // Reductions.
    // Output.
    subgraph cluster_subgraph_2_out {
        label = "";
        interface_2_out_0x560a242c5b10 [label="N", shape=none];
        interface_2_out_0x560a2238a080 [label="s", shape=none];
        interface_2_out_0x560a242db770 [label="s^-1*C_in", shape=none];
        interface_2_out_0x560a2447e6e0 [label="H", shape=none];
        interface_2_out_0x560a242db7c0 [label="k_1", shape=none];
        interface_2_out_0x560a242c5b88 [label="H", shape=none];
    }
    {
        rank = same;
        interface_2_out_0x560a242c5b10;
        interface_2_out_0x560a2238a080;
        interface_2_out_0x560a242db770;
        interface_2_out_0x560a2447e6e0;
        interface_2_out_0x560a242db7c0;
        interface_2_out_0x560a242c5b88;
    }
    // Input 0.
    subgraph cluster_subgraph_2_in_0 {
        label = "";
        interface_2_in_0x560a242c5b10 [label="N", shape=none];
        interface_2_in_0x560a225179e0 [label="C_in", shape=none];
        interface_2_in_0x560a2447e6e0 [label="H", shape=none];
        interface_2_in_0x560a242db7c0 [label="k_1", shape=none];
        interface_2_in_0x560a242c5b88 [label="H", shape=none];
    }
    {
        rank = same;
        interface_2_in_0x560a242c5b10;
        interface_2_in_0x560a225179e0;
        interface_2_in_0x560a2447e6e0;
        interface_2_in_0x560a242db7c0;
        interface_2_in_0x560a242c5b88;
    }
    // Op's.
    op_0x560a225179a0 [label="Split"];
    // Dimension's.
    op_0x560a225179a0 -> interface_2_out_0x560a2238a080 [label="s"];
    interface_2_in_0x560a225179e0 -> op_0x560a225179a0 [label="C_in"];
    interface_2_in_0x560a242c5b10 -> interface_2_out_0x560a242c5b10 [label="N"];
    interface_2_in_0x560a242c5b88 -> interface_2_out_0x560a242c5b88 [label="H"];
    op_0x560a225179a0 -> interface_2_out_0x560a242db770 [label="s^-1*C_in"];
    interface_2_in_0x560a242db7c0 -> interface_2_out_0x560a242db7c0 [label="k_1"];
    interface_2_in_0x560a2447e6e0 -> interface_2_out_0x560a2447e6e0 [label="H"];
}

// Stage tensor.
subgraph cluster_subgraph_3 {
    label = "Subgraph 3";
    // Reductions.
    reduce_0x7f921800c2b0 [label="Sum", shape=box];
    // Output.
    subgraph cluster_subgraph_3_out {
        label = "";
        interface_3_out_0x560a242c5b10 [label="N", shape=none];
        interface_3_out_0x560a225179e0 [label="C_in", shape=none];
        interface_3_out_0x560a2447e6e0 [label="H", shape=none];
        interface_3_out_0x560a242db7c0 [label="k_1", shape=none];
        interface_3_out_0x560a242c5b88 [label="H", shape=none];
    }
    {
        rank = same;
        reduce_0x7f921800c2b0;
        interface_3_out_0x560a242c5b10;
        interface_3_out_0x560a225179e0;
        interface_3_out_0x560a2447e6e0;
        interface_3_out_0x560a242db7c0;
        interface_3_out_0x560a242c5b88;
    }
    // Input 0.
    subgraph cluster_subgraph_3_in_0 {
        label = "";
        interface_3_in_0x560a242c5b10 [label="N", shape=none];
        interface_3_in_0x560a225179e0 [label="C_in", shape=none];
        interface_3_in_0x560a2447e6e0 [label="H", shape=none];
        interface_3_in_0x560a2447e740 [label="H", shape=none];
    }
    {
        rank = same;
        interface_3_in_0x560a242c5b10;
        interface_3_in_0x560a225179e0;
        interface_3_in_0x560a2447e6e0;
        interface_3_in_0x560a2447e740;
    }
    // Op's.
    op_0x560a21e8d300 [label="Unfold"];
    op_0x560a225179f0 [label="Split"];
    op_0x560a2447e720 [label="Shift"];
    // Dimension's.
    op_0x560a2447e720 -> op_0x560a21e8d300 [label="H"];
    interface_3_in_0x560a225179e0 -> interface_3_out_0x560a225179e0 [label="C_in"];
    op_0x560a21e8d300 -> op_0x560a225179f0 [label="g^-2*k_1*C_out^2"];
    interface_3_in_0x560a242c5b10 -> interface_3_out_0x560a242c5b10 [label="N"];
    op_0x560a21e8d300 -> interface_3_out_0x560a242c5b88 [label="H"];
    op_0x560a225179f0 -> interface_3_out_0x560a242db7c0 [label="k_1"];
    interface_3_in_0x560a2447e6e0 -> interface_3_out_0x560a2447e6e0 [label="H"];
    interface_3_in_0x560a2447e740 -> op_0x560a2447e720 [label="H"];
    op_0x560a225179f0 -> reduce_0x7f921800c2b0 [label="g^-2*C_out^2"];
}

// Input tensor.
subgraph cluster_subgraph_4 {
    label = "Input 0";
    interface_4_out_0x560a242c5b10 [label="N", shape=none];
    interface_4_out_0x560a225179e0 [label="C_in", shape=none];
    interface_4_out_0x560a2447e6e0 [label="H", shape=none];
    interface_4_out_0x560a2447e740 [label="H", shape=none];
}

interface_4_out_0x560a242c5b10 -> interface_3_in_0x560a242c5b10;
interface_4_out_0x560a225179e0 -> interface_3_in_0x560a225179e0;
interface_4_out_0x560a2447e6e0 -> interface_3_in_0x560a2447e6e0;
interface_4_out_0x560a2447e740 -> interface_3_in_0x560a2447e740;

interface_3_out_0x560a242c5b10 -> interface_2_in_0x560a242c5b10;
interface_3_out_0x560a225179e0 -> interface_2_in_0x560a225179e0;
interface_3_out_0x560a2447e6e0 -> interface_2_in_0x560a2447e6e0;
interface_3_out_0x560a242db7c0 -> interface_2_in_0x560a242db7c0;
interface_3_out_0x560a242c5b88 -> interface_2_in_0x560a242c5b88;

interface_2_out_0x560a242c5b10 -> interface_1_in_0x560a242c5b10;
interface_2_out_0x560a2238a080 -> interface_1_in_0x560a2238a080;
interface_2_out_0x560a242db770 -> interface_1_in_0x560a242db770;
interface_2_out_0x560a2447e6e0 -> interface_1_in_0x560a2447e6e0;
interface_2_out_0x560a242db7c0 -> interface_1_in_0x560a242db7c0;
interface_2_out_0x560a242c5b88 -> interface_1_in_0x560a242c5b88;

// Input tensor.
subgraph cluster_subgraph_5 {
    label = "Input 1";
    interface_5_out_0x560a242db788 [label="s^-1*C_in", shape=none];
    interface_5_out_0x560a242db828 [label="s^-1*C_out", shape=none];
    interface_5_out_0x560a242db7d8 [label="k_1", shape=none];
}

interface_5_out_0x560a242db788 -> interface_1_in_0x560a242db788;
interface_5_out_0x560a242db828 -> interface_1_in_0x560a242db828;
interface_5_out_0x560a242db7d8 -> interface_1_in_0x560a242db7d8;

interface_1_out_0x560a242c5b10 -> interface_0_in_0x560a242c5b10;
interface_1_out_0x560a2238a080 -> interface_0_in_0x560a2238a080;
interface_1_out_0x560a2238a098 -> interface_0_in_0x560a2238a098;
interface_1_out_0x560a2447e6e0 -> interface_0_in_0x560a2447e6e0;
interface_1_out_0x560a242c5b88 -> interface_0_in_0x560a242c5b88;

{
    rank = same;
    interface_4_out_0x560a242c5b10;
    interface_4_out_0x560a225179e0;
    interface_4_out_0x560a2447e6e0;
    interface_4_out_0x560a2447e740;
    interface_5_out_0x560a242db788;
    interface_5_out_0x560a242db828;
    interface_5_out_0x560a242db7d8;
}
subgraph cluster_subgraph_output {
    label = "Output";
    interface_6_in_0x560a242c5b10 [label="N", shape=none];
    interface_6_in_0x560a242c5b38 [label="C_out", shape=none];
    interface_6_in_0x560a242c5b60 [label="H", shape=none];
    interface_6_in_0x560a242c5b88 [label="H", shape=none];
}
interface_0_out_0x560a242c5b10 -> interface_6_in_0x560a242c5b10;
interface_0_out_0x560a242c5b38 -> interface_6_in_0x560a242c5b38;
interface_0_out_0x560a242c5b60 -> interface_6_in_0x560a242c5b60;
interface_0_out_0x560a242c5b88 -> interface_6_in_0x560a242c5b88;

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
		t_2 = torch.reshape(t_2, (128, 7168, 56, 1, ))
		t_2 = torch.nn.functional.unfold(t_2, (3, 1, ), padding=(1, 0, ))
		t_2 = torch.reshape(t_2, (128, 128, 56, 3, 56, ))

		# [g^-2*k_1*C_out^2]@Splitf17251383f4348c7 -> [g^-2*C_out^2]@Reduce159437b921f023cf, [k_1]@Share26cfa48d169008e4
		t_2 = torch.reshape(t_2, (128, 128, 56, 1, 3, 56, ))

		# [g^-2*C_out^2]@Reduce
		t_2 = torch.sum(t_2, dim=(3, ))

		# No contraction needed.
		t_3 = t_2

		# [C_in]@Split69dd43e05c8c5ddb -> [s]@Merge03a73148aa81036c, [s^-1*C_in]@Share8de6f167adbbf8aa
		t_3 = torch.reshape(t_3, (128, 2, 64, 56, 3, 56, ))

		# Perform contraction.
		t_4 = torch.einsum("mliojn, ikj -> mlkon", t_3, in_1)

		# No contraction needed.
		t_5 = t_4

		# [s]@Merge03a73148aa81036c, [s^-1*C_out]@Merge03a73148aa81036f -> [C_out]@Iteratorc7f8eb87a5a0a9e0
		t_5 = torch.reshape(t_5, (128, 32, 56, 56, ))

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
		t_2 = torch.reshape(t_2, (128, 3584, 28, 1, ))
		t_2 = torch.nn.functional.unfold(t_2, (3, 1, ), padding=(1, 0, ))
		t_2 = torch.reshape(t_2, (128, 128, 28, 3, 28, ))

		# [g^-2*k_1*C_out^2]@Splitf17251383f4348c7 -> [g^-2*C_out^2]@Reduce159437b921f023cf, [k_1]@Share26cfa48d169008e4
		t_2 = torch.reshape(t_2, (128, 128, 28, 1, 3, 28, ))

		# [g^-2*C_out^2]@Reduce
		t_2 = torch.sum(t_2, dim=(3, ))

		# No contraction needed.
		t_3 = t_2

		# [C_in]@Split69dd43e05c8c5ddb -> [s]@Merge03a73148aa81036c, [s^-1*C_in]@Share8de6f167adbbf8aa
		t_3 = torch.reshape(t_3, (128, 2, 64, 28, 3, 28, ))

		# Perform contraction.
		t_4 = torch.einsum("mliojn, ikj -> mlkon", t_3, in_1)

		# No contraction needed.
		t_5 = t_4

		# [s]@Merge03a73148aa81036c, [s^-1*C_out]@Merge03a73148aa81036f -> [C_out]@Iteratorc7f8eb87a5a0a9e0
		t_5 = torch.reshape(t_5, (128, 32, 28, 28, ))

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
		t_2 = torch.reshape(t_2, (128, 1792, 14, 1, ))
		t_2 = torch.nn.functional.unfold(t_2, (3, 1, ), padding=(1, 0, ))
		t_2 = torch.reshape(t_2, (128, 128, 14, 3, 14, ))

		# [g^-2*k_1*C_out^2]@Splitf17251383f4348c7 -> [g^-2*C_out^2]@Reduce159437b921f023cf, [k_1]@Share26cfa48d169008e4
		t_2 = torch.reshape(t_2, (128, 128, 14, 1, 3, 14, ))

		# [g^-2*C_out^2]@Reduce
		t_2 = torch.sum(t_2, dim=(3, ))

		# No contraction needed.
		t_3 = t_2

		# [C_in]@Split69dd43e05c8c5ddb -> [s]@Merge03a73148aa81036c, [s^-1*C_in]@Share8de6f167adbbf8aa
		t_3 = torch.reshape(t_3, (128, 2, 64, 14, 3, 14, ))

		# Perform contraction.
		t_4 = torch.einsum("mliojn, ikj -> mlkon", t_3, in_1)

		# No contraction needed.
		t_5 = t_4

		# [s]@Merge03a73148aa81036c, [s^-1*C_out]@Merge03a73148aa81036f -> [C_out]@Iteratorc7f8eb87a5a0a9e0
		t_5 = torch.reshape(t_5, (128, 32, 14, 14, ))

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
		t_2 = torch.reshape(t_2, (128, 896, 7, 1, ))
		t_2 = torch.nn.functional.unfold(t_2, (3, 1, ), padding=(1, 0, ))
		t_2 = torch.reshape(t_2, (128, 128, 7, 3, 7, ))

		# [g^-2*k_1*C_out^2]@Splitf17251383f4348c7 -> [g^-2*C_out^2]@Reduce159437b921f023cf, [k_1]@Share26cfa48d169008e4
		t_2 = torch.reshape(t_2, (128, 128, 7, 1, 3, 7, ))

		# [g^-2*C_out^2]@Reduce
		t_2 = torch.sum(t_2, dim=(3, ))

		# No contraction needed.
		t_3 = t_2

		# [C_in]@Split69dd43e05c8c5ddb -> [s]@Merge03a73148aa81036c, [s^-1*C_in]@Share8de6f167adbbf8aa
		t_3 = torch.reshape(t_3, (128, 2, 64, 7, 3, 7, ))

		# Perform contraction.
		t_4 = torch.einsum("mliojn, ikj -> mlkon", t_3, in_1)

		# No contraction needed.
		t_5 = t_4

		# [s]@Merge03a73148aa81036c, [s^-1*C_out]@Merge03a73148aa81036f -> [C_out]@Iteratorc7f8eb87a5a0a9e0
		t_5 = torch.reshape(t_5, (128, 32, 7, 7, ))

		# [H]@Shift41a433c05e30b91d -> [H]@Iterator96123ba3184da39c
		t_5 = torch.roll(t_5, self.shift_direction, 2)

		# No need to crop the output tensor.
		y = t_5

		return y

