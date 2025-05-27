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
        interface_0_out_0x55acfaae6490 [label="N", shape=none];
        interface_0_out_0x55acfaae64b8 [label="C_out", shape=none];
        interface_0_out_0x55acfaae64e0 [label="H", shape=none];
        interface_0_out_0x55acfaae6508 [label="H", shape=none];
    }
    {
        rank = same;
        interface_0_out_0x55acfaae6490;
        interface_0_out_0x55acfaae64b8;
        interface_0_out_0x55acfaae64e0;
        interface_0_out_0x55acfaae6508;
    }
    // Input 0.
    subgraph cluster_subgraph_0_in_0 {
        label = "";
        interface_0_in_0x55acfaae6490 [label="N", shape=none];
        interface_0_in_0x55acfaae64b8 [label="C_out", shape=none];
        interface_0_in_0x55acfaae64e0 [label="H", shape=none];
        interface_0_in_0x55ad0b7072d0 [label="H", shape=none];
    }
    {
        rank = same;
        interface_0_in_0x55acfaae6490;
        interface_0_in_0x55acfaae64b8;
        interface_0_in_0x55acfaae64e0;
        interface_0_in_0x55ad0b7072d0;
    }
    // Op's.
    op_0x55ad0b7072b0 [label="Shift"];
    // Dimension's.
    interface_0_in_0x55acfaae6490 -> interface_0_out_0x55acfaae6490 [label="N"];
    interface_0_in_0x55acfaae64b8 -> interface_0_out_0x55acfaae64b8 [label="C_out"];
    interface_0_in_0x55acfaae64e0 -> interface_0_out_0x55acfaae64e0 [label="H"];
    op_0x55ad0b7072b0 -> interface_0_out_0x55acfaae6508 [label="H"];
    interface_0_in_0x55ad0b7072d0 -> op_0x55ad0b7072b0 [label="H"];
}

// Stage tensor.
subgraph cluster_subgraph_1 {
    label = "Subgraph 1";
    // Reductions.
    reduce_0x7ef2c8002ce8 [label="Sum", shape=box];
    // Output.
    subgraph cluster_subgraph_1_out {
        label = "";
        interface_1_out_0x55acfaae6490 [label="N", shape=none];
        interface_1_out_0x55acfaae64b8 [label="C_out", shape=none];
        interface_1_out_0x55acfaae64e0 [label="H", shape=none];
        interface_1_out_0x55ad0b7072d0 [label="H", shape=none];
    }
    {
        rank = same;
        reduce_0x7ef2c8002ce8;
        interface_1_out_0x55acfaae6490;
        interface_1_out_0x55acfaae64b8;
        interface_1_out_0x55acfaae64e0;
        interface_1_out_0x55ad0b7072d0;
    }
    // Input 0.
    subgraph cluster_subgraph_1_in_0 {
        label = "";
        interface_1_in_0x55acfaae6490 [label="N", shape=none];
        interface_1_in_0x55acfaae64b8 [label="C_out", shape=none];
        interface_1_in_0x55ad0b70c6c0 [label="H", shape=none];
        interface_1_in_0x55ad0b70c6d8 [label="s", shape=none];
        interface_1_in_0x55ad0b7072d0 [label="H", shape=none];
    }
    {
        rank = same;
        interface_1_in_0x55acfaae6490;
        interface_1_in_0x55acfaae64b8;
        interface_1_in_0x55ad0b70c6c0;
        interface_1_in_0x55ad0b70c6d8;
        interface_1_in_0x55ad0b7072d0;
    }
    // Op's.
    op_0x55ad0b707310 [label="Shift"];
    op_0x55ad0b707ea0 [label="Split"];
    op_0x55ad0b70c680 [label="Merge"];
    // Dimension's.
    interface_1_in_0x55acfaae6490 -> interface_1_out_0x55acfaae6490 [label="N"];
    interface_1_in_0x55acfaae64b8 -> interface_1_out_0x55acfaae64b8 [label="C_out"];
    op_0x55ad0b707ea0 -> interface_1_out_0x55acfaae64e0 [label="H"];
    interface_1_in_0x55ad0b7072d0 -> interface_1_out_0x55ad0b7072d0 [label="H"];
    op_0x55ad0b70c680 -> op_0x55ad0b707310 [label="s*H"];
    op_0x55ad0b707310 -> op_0x55ad0b707ea0 [label="s*H"];
    interface_1_in_0x55ad0b70c6c0 -> op_0x55ad0b70c680 [label="H"];
    interface_1_in_0x55ad0b70c6d8 -> op_0x55ad0b70c680 [label="s"];
    op_0x55ad0b707ea0 -> reduce_0x7ef2c8002ce8 [label="s"];
}

// Stage tensor.
subgraph cluster_subgraph_2 {
    label = "Subgraph 2";
    // Reductions.
    reduce_0x7ef2c8001a98 [label="Sum", shape=box];
    reduce_0x7ef2c8005a48 [label="Sum", shape=box];
    // Output.
    subgraph cluster_subgraph_2_out {
        label = "";
        interface_2_out_0x55acfaae6490 [label="N", shape=none];
        interface_2_out_0x55acfaae64b8 [label="C_out", shape=none];
        interface_2_out_0x55ad0b70c6c0 [label="H", shape=none];
        interface_2_out_0x55ad0b70c6d8 [label="s", shape=none];
        interface_2_out_0x55ad0b7072d0 [label="H", shape=none];
    }
    {
        rank = same;
        reduce_0x7ef2c8001a98;
        reduce_0x7ef2c8005a48;
        interface_2_out_0x55acfaae6490;
        interface_2_out_0x55acfaae64b8;
        interface_2_out_0x55ad0b70c6c0;
        interface_2_out_0x55ad0b70c6d8;
        interface_2_out_0x55ad0b7072d0;
    }
    // Input 0.
    subgraph cluster_subgraph_2_in_0 {
        label = "";
        interface_2_in_0x55acfaae6490 [label="N", shape=none];
        interface_2_in_0x55ad0b705d10 [label="k_1", shape=none];
        interface_2_in_0x55ad0b70c6c0 [label="H", shape=none];
        interface_2_in_0x55ad0b705cc0 [label="C_in", shape=none];
        interface_2_in_0x55ad0b7072d0 [label="H", shape=none];
    }
    // Input 1.
    subgraph cluster_subgraph_2_in_1 {
        label = "";
        interface_2_in_0x55ad0b705c38 [label="C_out", shape=none];
        interface_2_in_0x55ad0b705d28 [label="k_1", shape=none];
        interface_2_in_0x55ad0b705dc8 [label="s", shape=none];
        interface_2_in_0x55ad0b705cd8 [label="C_in", shape=none];
    }
    {
        rank = same;
        interface_2_in_0x55acfaae6490;
        interface_2_in_0x55ad0b705d10;
        interface_2_in_0x55ad0b70c6c0;
        interface_2_in_0x55ad0b705cc0;
        interface_2_in_0x55ad0b7072d0;
        interface_2_in_0x55ad0b705c38;
        interface_2_in_0x55ad0b705d28;
        interface_2_in_0x55ad0b705dc8;
        interface_2_in_0x55ad0b705cd8;
    }
    // Op's.
    op_0x55ad0b705c00 [label="Share"];
    op_0x55ad0b705ca0 [label="Share"];
    op_0x55ad0b705cf0 [label="Share"];
    op_0x55ad0b705d90 [label="Share"];
    op_0x55ad0b706138 [label="Expand"];
    op_0x55ad0b706178 [label="Expand"];
    // Dimension's.
    interface_2_in_0x55acfaae6490 -> interface_2_out_0x55acfaae6490 [label="N"];
    op_0x55ad0b705c00 -> interface_2_out_0x55acfaae64b8 [label="C_out"];
    op_0x55ad0b706138 -> op_0x55ad0b705c00 [label="C_out"];
    interface_2_in_0x55ad0b705c38 -> op_0x55ad0b705c00 [label="C_out"];
    interface_2_in_0x55ad0b705cc0 -> op_0x55ad0b705ca0 [label="C_in"];
    interface_2_in_0x55ad0b705cd8 -> op_0x55ad0b705ca0 [label="C_in"];
    interface_2_in_0x55ad0b705d10 -> op_0x55ad0b705cf0 [label="k_1"];
    interface_2_in_0x55ad0b705d28 -> op_0x55ad0b705cf0 [label="k_1"];
    op_0x55ad0b706178 -> op_0x55ad0b705d90 [label="s"];
    interface_2_in_0x55ad0b705dc8 -> op_0x55ad0b705d90 [label="s"];
    interface_2_in_0x55ad0b7072d0 -> interface_2_out_0x55ad0b7072d0 [label="H"];
    interface_2_in_0x55ad0b70c6c0 -> interface_2_out_0x55ad0b70c6c0 [label="H"];
    op_0x55ad0b705d90 -> interface_2_out_0x55ad0b70c6d8 [label="s"];
    op_0x55ad0b705cf0 -> reduce_0x7ef2c8001a98 [label="k_1"];
    op_0x55ad0b705ca0 -> reduce_0x7ef2c8005a48 [label="C_in"];
}

// Stage tensor.
subgraph cluster_subgraph_3 {
    label = "Subgraph 3";
    // Reductions.
    // Output.
    subgraph cluster_subgraph_3_out {
        label = "";
        interface_3_out_0x55acfaae6490 [label="N", shape=none];
        interface_3_out_0x55ad0b705d10 [label="k_1", shape=none];
        interface_3_out_0x55ad0b70c6c0 [label="H", shape=none];
        interface_3_out_0x55ad0b705cc0 [label="C_in", shape=none];
        interface_3_out_0x55ad0b7072d0 [label="H", shape=none];
    }
    {
        rank = same;
        interface_3_out_0x55acfaae6490;
        interface_3_out_0x55ad0b705d10;
        interface_3_out_0x55ad0b70c6c0;
        interface_3_out_0x55ad0b705cc0;
        interface_3_out_0x55ad0b7072d0;
    }
    // Input 0.
    subgraph cluster_subgraph_3_in_0 {
        label = "";
        interface_3_in_0x55acfaae6490 [label="N", shape=none];
        interface_3_in_0x55ad0b705cc0 [label="C_in", shape=none];
        interface_3_in_0x55ad0b7072d0 [label="H", shape=none];
        interface_3_in_0x55ad0b71c7a8 [label="H", shape=none];
    }
    {
        rank = same;
        interface_3_in_0x55acfaae6490;
        interface_3_in_0x55ad0b705cc0;
        interface_3_in_0x55ad0b7072d0;
        interface_3_in_0x55ad0b71c7a8;
    }
    // Op's.
    op_0x55ad0b71c780 [label="Unfold"];
    // Dimension's.
    interface_3_in_0x55acfaae6490 -> interface_3_out_0x55acfaae6490 [label="N"];
    interface_3_in_0x55ad0b705cc0 -> interface_3_out_0x55ad0b705cc0 [label="C_in"];
    op_0x55ad0b71c780 -> interface_3_out_0x55ad0b705d10 [label="k_1"];
    interface_3_in_0x55ad0b7072d0 -> interface_3_out_0x55ad0b7072d0 [label="H"];
    op_0x55ad0b71c780 -> interface_3_out_0x55ad0b70c6c0 [label="H"];
    interface_3_in_0x55ad0b71c7a8 -> op_0x55ad0b71c780 [label="H"];
}

// Input tensor.
subgraph cluster_subgraph_4 {
    label = "Input 0";
    interface_4_out_0x55acfaae6490 [label="N", shape=none];
    interface_4_out_0x55ad0b705cc0 [label="C_in", shape=none];
    interface_4_out_0x55ad0b7072d0 [label="H", shape=none];
    interface_4_out_0x55ad0b71c7a8 [label="H", shape=none];
}

interface_4_out_0x55acfaae6490 -> interface_3_in_0x55acfaae6490;
interface_4_out_0x55ad0b705cc0 -> interface_3_in_0x55ad0b705cc0;
interface_4_out_0x55ad0b7072d0 -> interface_3_in_0x55ad0b7072d0;
interface_4_out_0x55ad0b71c7a8 -> interface_3_in_0x55ad0b71c7a8;

interface_3_out_0x55acfaae6490 -> interface_2_in_0x55acfaae6490;
interface_3_out_0x55ad0b705d10 -> interface_2_in_0x55ad0b705d10;
interface_3_out_0x55ad0b70c6c0 -> interface_2_in_0x55ad0b70c6c0;
interface_3_out_0x55ad0b705cc0 -> interface_2_in_0x55ad0b705cc0;
interface_3_out_0x55ad0b7072d0 -> interface_2_in_0x55ad0b7072d0;

// Input tensor.
subgraph cluster_subgraph_5 {
    label = "Input 1";
    interface_5_out_0x55ad0b705c38 [label="C_out", shape=none];
    interface_5_out_0x55ad0b705d28 [label="k_1", shape=none];
    interface_5_out_0x55ad0b705dc8 [label="s", shape=none];
    interface_5_out_0x55ad0b705cd8 [label="C_in", shape=none];
}

interface_5_out_0x55ad0b705c38 -> interface_2_in_0x55ad0b705c38;
interface_5_out_0x55ad0b705d28 -> interface_2_in_0x55ad0b705d28;
interface_5_out_0x55ad0b705dc8 -> interface_2_in_0x55ad0b705dc8;
interface_5_out_0x55ad0b705cd8 -> interface_2_in_0x55ad0b705cd8;

interface_2_out_0x55acfaae6490 -> interface_1_in_0x55acfaae6490;
interface_2_out_0x55acfaae64b8 -> interface_1_in_0x55acfaae64b8;
interface_2_out_0x55ad0b70c6c0 -> interface_1_in_0x55ad0b70c6c0;
interface_2_out_0x55ad0b70c6d8 -> interface_1_in_0x55ad0b70c6d8;
interface_2_out_0x55ad0b7072d0 -> interface_1_in_0x55ad0b7072d0;

interface_1_out_0x55acfaae6490 -> interface_0_in_0x55acfaae6490;
interface_1_out_0x55acfaae64b8 -> interface_0_in_0x55acfaae64b8;
interface_1_out_0x55acfaae64e0 -> interface_0_in_0x55acfaae64e0;
interface_1_out_0x55ad0b7072d0 -> interface_0_in_0x55ad0b7072d0;

{
    rank = same;
    interface_4_out_0x55acfaae6490;
    interface_4_out_0x55ad0b705cc0;
    interface_4_out_0x55ad0b7072d0;
    interface_4_out_0x55ad0b71c7a8;
    interface_5_out_0x55ad0b705c38;
    interface_5_out_0x55ad0b705d28;
    interface_5_out_0x55ad0b705dc8;
    interface_5_out_0x55ad0b705cd8;
}
subgraph cluster_subgraph_output {
    label = "Output";
    interface_6_in_0x55acfaae6490 [label="N", shape=none];
    interface_6_in_0x55acfaae64b8 [label="C_out", shape=none];
    interface_6_in_0x55acfaae64e0 [label="H", shape=none];
    interface_6_in_0x55acfaae6508 [label="H", shape=none];
}
interface_0_out_0x55acfaae6490 -> interface_6_in_0x55acfaae6490;
interface_0_out_0x55acfaae64b8 -> interface_6_in_0x55acfaae64b8;
interface_0_out_0x55acfaae64e0 -> interface_6_in_0x55acfaae64e0;
interface_0_out_0x55acfaae6508 -> interface_6_in_0x55acfaae6508;

}

"""
class kernel_generated_0(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([64, 3, 2, 64]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]

		# Perform contraction.
		t_2 = torch.einsum("ijkl -> iljk", in_0)

		# [H]@Unfold9ee82d948cf711ad -> [H]@Merge5f50103ea583163b, [k_1]@Share26cfa48d169008e4
		t_2 = torch.reshape(t_2, (1, 1, 56, 3584, ))
		t_2 = torch.nn.functional.unfold(t_2, (3, 1, ), padding=(1, 0, ))
		t_2 = torch.reshape(t_2, (1, 3, 56, 64, 56, ))

		# Perform contraction.
		t_3 = torch.einsum("mkojn, iklj -> mioln", t_2, in_1)

		# No contraction needed.
		t_4 = t_3

		# [H]@Merge5f50103ea583163b, [s]@Merge5f50103ea5831638 -> [s*H]@Shift3c9c8e9d3c84cb9b
		t_4 = torch.reshape(t_4, (1, 64, 112, 56, ))

		# [s*H]@Shift3c9c8e9d3c84cb9b -> [s*H]@Splitdb1af055f999951a
		t_4 = torch.roll(t_4, self.shift_direction, 2)

		# [s*H]@Splitdb1af055f999951a -> [H]@Iterator96123ba3184da39c, [s]@Reduced95c644a3c072d9a
		t_4 = torch.reshape(t_4, (1, 64, 56, 2, 56, ))

		# [s]@Reduce
		t_4 = torch.sum(t_4, dim=(3, ))

		# No contraction needed.
		t_5 = t_4

		# [H]@Shift6b179c72f0c6dbad -> [H]@Iteratorb0a1def4ad5784ec
		t_5 = torch.roll(t_5, self.shift_direction, 3)

		# No need to crop the output tensor.
		y = t_5

		return y

class kernel_generated_1(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([128, 3, 2, 64]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]

		# Perform contraction.
		t_2 = torch.einsum("ijkl -> iljk", in_0)

		# [H]@Unfold9ee82d948cf711ad -> [H]@Merge5f50103ea583163b, [k_1]@Share26cfa48d169008e4
		t_2 = torch.reshape(t_2, (1, 1, 28, 1792, ))
		t_2 = torch.nn.functional.unfold(t_2, (3, 1, ), padding=(1, 0, ))
		t_2 = torch.reshape(t_2, (1, 3, 28, 64, 28, ))

		# Perform contraction.
		t_3 = torch.einsum("mkojn, iklj -> mioln", t_2, in_1)

		# No contraction needed.
		t_4 = t_3

		# [H]@Merge5f50103ea583163b, [s]@Merge5f50103ea5831638 -> [s*H]@Shift3c9c8e9d3c84cb9b
		t_4 = torch.reshape(t_4, (1, 128, 56, 28, ))

		# [s*H]@Shift3c9c8e9d3c84cb9b -> [s*H]@Splitdb1af055f999951a
		t_4 = torch.roll(t_4, self.shift_direction, 2)

		# [s*H]@Splitdb1af055f999951a -> [H]@Iterator96123ba3184da39c, [s]@Reduced95c644a3c072d9a
		t_4 = torch.reshape(t_4, (1, 128, 28, 2, 28, ))

		# [s]@Reduce
		t_4 = torch.sum(t_4, dim=(3, ))

		# No contraction needed.
		t_5 = t_4

		# [H]@Shift6b179c72f0c6dbad -> [H]@Iteratorb0a1def4ad5784ec
		t_5 = torch.roll(t_5, self.shift_direction, 3)

		# No need to crop the output tensor.
		y = t_5

		return y

class kernel_generated_2(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([128, 3, 2, 128]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]

		# Perform contraction.
		t_2 = torch.einsum("ijkl -> iljk", in_0)

		# [H]@Unfold9ee82d948cf711ad -> [H]@Merge5f50103ea583163b, [k_1]@Share26cfa48d169008e4
		t_2 = torch.reshape(t_2, (1, 1, 28, 3584, ))
		t_2 = torch.nn.functional.unfold(t_2, (3, 1, ), padding=(1, 0, ))
		t_2 = torch.reshape(t_2, (1, 3, 28, 128, 28, ))

		# Perform contraction.
		t_3 = torch.einsum("mkojn, iklj -> mioln", t_2, in_1)

		# No contraction needed.
		t_4 = t_3

		# [H]@Merge5f50103ea583163b, [s]@Merge5f50103ea5831638 -> [s*H]@Shift3c9c8e9d3c84cb9b
		t_4 = torch.reshape(t_4, (1, 128, 56, 28, ))

		# [s*H]@Shift3c9c8e9d3c84cb9b -> [s*H]@Splitdb1af055f999951a
		t_4 = torch.roll(t_4, self.shift_direction, 2)

		# [s*H]@Splitdb1af055f999951a -> [H]@Iterator96123ba3184da39c, [s]@Reduced95c644a3c072d9a
		t_4 = torch.reshape(t_4, (1, 128, 28, 2, 28, ))

		# [s]@Reduce
		t_4 = torch.sum(t_4, dim=(3, ))

		# No contraction needed.
		t_5 = t_4

		# [H]@Shift6b179c72f0c6dbad -> [H]@Iteratorb0a1def4ad5784ec
		t_5 = torch.roll(t_5, self.shift_direction, 3)

		# No need to crop the output tensor.
		y = t_5

		return y

class kernel_generated_3(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([256, 3, 2, 128]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]

		# Perform contraction.
		t_2 = torch.einsum("ijkl -> iljk", in_0)

		# [H]@Unfold9ee82d948cf711ad -> [H]@Merge5f50103ea583163b, [k_1]@Share26cfa48d169008e4
		t_2 = torch.reshape(t_2, (1, 1, 14, 1792, ))
		t_2 = torch.nn.functional.unfold(t_2, (3, 1, ), padding=(1, 0, ))
		t_2 = torch.reshape(t_2, (1, 3, 14, 128, 14, ))

		# Perform contraction.
		t_3 = torch.einsum("mkojn, iklj -> mioln", t_2, in_1)

		# No contraction needed.
		t_4 = t_3

		# [H]@Merge5f50103ea583163b, [s]@Merge5f50103ea5831638 -> [s*H]@Shift3c9c8e9d3c84cb9b
		t_4 = torch.reshape(t_4, (1, 256, 28, 14, ))

		# [s*H]@Shift3c9c8e9d3c84cb9b -> [s*H]@Splitdb1af055f999951a
		t_4 = torch.roll(t_4, self.shift_direction, 2)

		# [s*H]@Splitdb1af055f999951a -> [H]@Iterator96123ba3184da39c, [s]@Reduced95c644a3c072d9a
		t_4 = torch.reshape(t_4, (1, 256, 14, 2, 14, ))

		# [s]@Reduce
		t_4 = torch.sum(t_4, dim=(3, ))

		# No contraction needed.
		t_5 = t_4

		# [H]@Shift6b179c72f0c6dbad -> [H]@Iteratorb0a1def4ad5784ec
		t_5 = torch.roll(t_5, self.shift_direction, 3)

		# No need to crop the output tensor.
		y = t_5

		return y

class kernel_generated_4(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([256, 3, 2, 256]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]

		# Perform contraction.
		t_2 = torch.einsum("ijkl -> iljk", in_0)

		# [H]@Unfold9ee82d948cf711ad -> [H]@Merge5f50103ea583163b, [k_1]@Share26cfa48d169008e4
		t_2 = torch.reshape(t_2, (1, 1, 14, 3584, ))
		t_2 = torch.nn.functional.unfold(t_2, (3, 1, ), padding=(1, 0, ))
		t_2 = torch.reshape(t_2, (1, 3, 14, 256, 14, ))

		# Perform contraction.
		t_3 = torch.einsum("mkojn, iklj -> mioln", t_2, in_1)

		# No contraction needed.
		t_4 = t_3

		# [H]@Merge5f50103ea583163b, [s]@Merge5f50103ea5831638 -> [s*H]@Shift3c9c8e9d3c84cb9b
		t_4 = torch.reshape(t_4, (1, 256, 28, 14, ))

		# [s*H]@Shift3c9c8e9d3c84cb9b -> [s*H]@Splitdb1af055f999951a
		t_4 = torch.roll(t_4, self.shift_direction, 2)

		# [s*H]@Splitdb1af055f999951a -> [H]@Iterator96123ba3184da39c, [s]@Reduced95c644a3c072d9a
		t_4 = torch.reshape(t_4, (1, 256, 14, 2, 14, ))

		# [s]@Reduce
		t_4 = torch.sum(t_4, dim=(3, ))

		# No contraction needed.
		t_5 = t_4

		# [H]@Shift6b179c72f0c6dbad -> [H]@Iteratorb0a1def4ad5784ec
		t_5 = torch.roll(t_5, self.shift_direction, 3)

		# No need to crop the output tensor.
		y = t_5

		return y

class kernel_generated_5(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([512, 3, 2, 256]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]

		# Perform contraction.
		t_2 = torch.einsum("ijkl -> iljk", in_0)

		# [H]@Unfold9ee82d948cf711ad -> [H]@Merge5f50103ea583163b, [k_1]@Share26cfa48d169008e4
		t_2 = torch.reshape(t_2, (1, 1, 7, 1792, ))
		t_2 = torch.nn.functional.unfold(t_2, (3, 1, ), padding=(1, 0, ))
		t_2 = torch.reshape(t_2, (1, 3, 7, 256, 7, ))

		# Perform contraction.
		t_3 = torch.einsum("mkojn, iklj -> mioln", t_2, in_1)

		# No contraction needed.
		t_4 = t_3

		# [H]@Merge5f50103ea583163b, [s]@Merge5f50103ea5831638 -> [s*H]@Shift3c9c8e9d3c84cb9b
		t_4 = torch.reshape(t_4, (1, 512, 14, 7, ))

		# [s*H]@Shift3c9c8e9d3c84cb9b -> [s*H]@Splitdb1af055f999951a
		t_4 = torch.roll(t_4, self.shift_direction, 2)

		# [s*H]@Splitdb1af055f999951a -> [H]@Iterator96123ba3184da39c, [s]@Reduced95c644a3c072d9a
		t_4 = torch.reshape(t_4, (1, 512, 7, 2, 7, ))

		# [s]@Reduce
		t_4 = torch.sum(t_4, dim=(3, ))

		# No contraction needed.
		t_5 = t_4

		# [H]@Shift6b179c72f0c6dbad -> [H]@Iteratorb0a1def4ad5784ec
		t_5 = torch.roll(t_5, self.shift_direction, 3)

		# No need to crop the output tensor.
		y = t_5

		return y

class kernel_generated_6(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([512, 3, 2, 512]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]

		# Perform contraction.
		t_2 = torch.einsum("ijkl -> iljk", in_0)

		# [H]@Unfold9ee82d948cf711ad -> [H]@Merge5f50103ea583163b, [k_1]@Share26cfa48d169008e4
		t_2 = torch.reshape(t_2, (1, 1, 7, 3584, ))
		t_2 = torch.nn.functional.unfold(t_2, (3, 1, ), padding=(1, 0, ))
		t_2 = torch.reshape(t_2, (1, 3, 7, 512, 7, ))

		# Perform contraction.
		t_3 = torch.einsum("mkojn, iklj -> mioln", t_2, in_1)

		# No contraction needed.
		t_4 = t_3

		# [H]@Merge5f50103ea583163b, [s]@Merge5f50103ea5831638 -> [s*H]@Shift3c9c8e9d3c84cb9b
		t_4 = torch.reshape(t_4, (1, 512, 14, 7, ))

		# [s*H]@Shift3c9c8e9d3c84cb9b -> [s*H]@Splitdb1af055f999951a
		t_4 = torch.roll(t_4, self.shift_direction, 2)

		# [s*H]@Splitdb1af055f999951a -> [H]@Iterator96123ba3184da39c, [s]@Reduced95c644a3c072d9a
		t_4 = torch.reshape(t_4, (1, 512, 7, 2, 7, ))

		# [s]@Reduce
		t_4 = torch.sum(t_4, dim=(3, ))

		# No contraction needed.
		t_5 = t_4

		# [H]@Shift6b179c72f0c6dbad -> [H]@Iteratorb0a1def4ad5784ec
		t_5 = torch.roll(t_5, self.shift_direction, 3)

		# No need to crop the output tensor.
		y = t_5

		return y

