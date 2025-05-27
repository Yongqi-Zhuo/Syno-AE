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
        interface_2_in_0x55ad0b705c20 [label="C_out", shape=none];
        interface_2_in_0x55ad0b70c6c0 [label="H", shape=none];
        interface_2_in_0x55ad0b7072d0 [label="H", shape=none];
    }
    // Input 1.
    subgraph cluster_subgraph_2_in_1 {
        label = "";
        interface_2_in_0x55ad0b705c38 [label="C_out", shape=none];
        interface_2_in_0x55ad0b705dc8 [label="s", shape=none];
    }
    {
        rank = same;
        interface_2_in_0x55acfaae6490;
        interface_2_in_0x55ad0b705c20;
        interface_2_in_0x55ad0b70c6c0;
        interface_2_in_0x55ad0b7072d0;
        interface_2_in_0x55ad0b705c38;
        interface_2_in_0x55ad0b705dc8;
    }
    // Op's.
    op_0x55ad0b705c00 [label="Share"];
    op_0x55ad0b705d90 [label="Share"];
    op_0x55ad0b706178 [label="Expand"];
    // Dimension's.
    interface_2_in_0x55acfaae6490 -> interface_2_out_0x55acfaae6490 [label="N"];
    op_0x55ad0b705c00 -> interface_2_out_0x55acfaae64b8 [label="C_out"];
    interface_2_in_0x55ad0b705c20 -> op_0x55ad0b705c00 [label="C_out"];
    interface_2_in_0x55ad0b705c38 -> op_0x55ad0b705c00 [label="C_out"];
    op_0x55ad0b706178 -> op_0x55ad0b705d90 [label="s"];
    interface_2_in_0x55ad0b705dc8 -> op_0x55ad0b705d90 [label="s"];
    interface_2_in_0x55ad0b7072d0 -> interface_2_out_0x55ad0b7072d0 [label="H"];
    interface_2_in_0x55ad0b70c6c0 -> interface_2_out_0x55ad0b70c6c0 [label="H"];
    op_0x55ad0b705d90 -> interface_2_out_0x55ad0b70c6d8 [label="s"];
}

// Stage tensor.
subgraph cluster_subgraph_3 {
    label = "Subgraph 3";
    // Reductions.
    reduce_0x7ef2c8001a98 [label="Sum", shape=box];
    reduce_0x7ef2c8005a48 [label="Sum", shape=box];
    // Output.
    subgraph cluster_subgraph_3_out {
        label = "";
        interface_3_out_0x55acfaae6490 [label="N", shape=none];
        interface_3_out_0x55ad0b705c20 [label="C_out", shape=none];
        interface_3_out_0x55ad0b70c6c0 [label="H", shape=none];
        interface_3_out_0x55ad0b7072d0 [label="H", shape=none];
    }
    {
        rank = same;
        reduce_0x7ef2c8001a98;
        reduce_0x7ef2c8005a48;
        interface_3_out_0x55acfaae6490;
        interface_3_out_0x55ad0b705c20;
        interface_3_out_0x55ad0b70c6c0;
        interface_3_out_0x55ad0b7072d0;
    }
    // Input 0.
    subgraph cluster_subgraph_3_in_0 {
        label = "";
        interface_3_in_0x55acfaae6490 [label="N", shape=none];
        interface_3_in_0x55ad0b705ea0 [label="k_1", shape=none];
        interface_3_in_0x55ad0b70c6c0 [label="H", shape=none];
        interface_3_in_0x55ad0b705e50 [label="C_in", shape=none];
        interface_3_in_0x55ad0b7072d0 [label="H", shape=none];
    }
    // Input 1.
    subgraph cluster_subgraph_3_in_1 {
        label = "";
        interface_3_in_0x55ad0b705e18 [label="C_out", shape=none];
        interface_3_in_0x55ad0b705eb8 [label="k_1", shape=none];
        interface_3_in_0x55ad0b705e68 [label="C_in", shape=none];
    }
    {
        rank = same;
        interface_3_in_0x55acfaae6490;
        interface_3_in_0x55ad0b705ea0;
        interface_3_in_0x55ad0b70c6c0;
        interface_3_in_0x55ad0b705e50;
        interface_3_in_0x55ad0b7072d0;
        interface_3_in_0x55ad0b705e18;
        interface_3_in_0x55ad0b705eb8;
        interface_3_in_0x55ad0b705e68;
    }
    // Op's.
    op_0x55ad0b705de0 [label="Share"];
    op_0x55ad0b705e30 [label="Share"];
    op_0x55ad0b705e80 [label="Share"];
    op_0x55ad0b706198 [label="Expand"];
    // Dimension's.
    interface_3_in_0x55acfaae6490 -> interface_3_out_0x55acfaae6490 [label="N"];
    op_0x55ad0b705de0 -> interface_3_out_0x55ad0b705c20 [label="C_out"];
    op_0x55ad0b706198 -> op_0x55ad0b705de0 [label="C_out"];
    interface_3_in_0x55ad0b705e18 -> op_0x55ad0b705de0 [label="C_out"];
    interface_3_in_0x55ad0b705e50 -> op_0x55ad0b705e30 [label="C_in"];
    interface_3_in_0x55ad0b705e68 -> op_0x55ad0b705e30 [label="C_in"];
    interface_3_in_0x55ad0b705ea0 -> op_0x55ad0b705e80 [label="k_1"];
    interface_3_in_0x55ad0b705eb8 -> op_0x55ad0b705e80 [label="k_1"];
    interface_3_in_0x55ad0b7072d0 -> interface_3_out_0x55ad0b7072d0 [label="H"];
    interface_3_in_0x55ad0b70c6c0 -> interface_3_out_0x55ad0b70c6c0 [label="H"];
    op_0x55ad0b705e80 -> reduce_0x7ef2c8001a98 [label="k_1"];
    op_0x55ad0b705e30 -> reduce_0x7ef2c8005a48 [label="C_in"];
}

// Stage tensor.
subgraph cluster_subgraph_4 {
    label = "Subgraph 4";
    // Reductions.
    // Output.
    subgraph cluster_subgraph_4_out {
        label = "";
        interface_4_out_0x55acfaae6490 [label="N", shape=none];
        interface_4_out_0x55ad0b705ea0 [label="k_1", shape=none];
        interface_4_out_0x55ad0b70c6c0 [label="H", shape=none];
        interface_4_out_0x55ad0b705e50 [label="C_in", shape=none];
        interface_4_out_0x55ad0b7072d0 [label="H", shape=none];
    }
    {
        rank = same;
        interface_4_out_0x55acfaae6490;
        interface_4_out_0x55ad0b705ea0;
        interface_4_out_0x55ad0b70c6c0;
        interface_4_out_0x55ad0b705e50;
        interface_4_out_0x55ad0b7072d0;
    }
    // Input 0.
    subgraph cluster_subgraph_4_in_0 {
        label = "";
        interface_4_in_0x55acfaae6490 [label="N", shape=none];
        interface_4_in_0x55ad0b705e50 [label="C_in", shape=none];
        interface_4_in_0x55ad0b7072d0 [label="H", shape=none];
        interface_4_in_0x55ad0b71c4a8 [label="H", shape=none];
    }
    {
        rank = same;
        interface_4_in_0x55acfaae6490;
        interface_4_in_0x55ad0b705e50;
        interface_4_in_0x55ad0b7072d0;
        interface_4_in_0x55ad0b71c4a8;
    }
    // Op's.
    op_0x55ad0b71c480 [label="Unfold"];
    // Dimension's.
    interface_4_in_0x55acfaae6490 -> interface_4_out_0x55acfaae6490 [label="N"];
    interface_4_in_0x55ad0b705e50 -> interface_4_out_0x55ad0b705e50 [label="C_in"];
    op_0x55ad0b71c480 -> interface_4_out_0x55ad0b705ea0 [label="k_1"];
    interface_4_in_0x55ad0b7072d0 -> interface_4_out_0x55ad0b7072d0 [label="H"];
    op_0x55ad0b71c480 -> interface_4_out_0x55ad0b70c6c0 [label="H"];
    interface_4_in_0x55ad0b71c4a8 -> op_0x55ad0b71c480 [label="H"];
}

// Input tensor.
subgraph cluster_subgraph_5 {
    label = "Input 0";
    interface_5_out_0x55acfaae6490 [label="N", shape=none];
    interface_5_out_0x55ad0b705e50 [label="C_in", shape=none];
    interface_5_out_0x55ad0b7072d0 [label="H", shape=none];
    interface_5_out_0x55ad0b71c4a8 [label="H", shape=none];
}

interface_5_out_0x55acfaae6490 -> interface_4_in_0x55acfaae6490;
interface_5_out_0x55ad0b705e50 -> interface_4_in_0x55ad0b705e50;
interface_5_out_0x55ad0b7072d0 -> interface_4_in_0x55ad0b7072d0;
interface_5_out_0x55ad0b71c4a8 -> interface_4_in_0x55ad0b71c4a8;

interface_4_out_0x55acfaae6490 -> interface_3_in_0x55acfaae6490;
interface_4_out_0x55ad0b705ea0 -> interface_3_in_0x55ad0b705ea0;
interface_4_out_0x55ad0b70c6c0 -> interface_3_in_0x55ad0b70c6c0;
interface_4_out_0x55ad0b705e50 -> interface_3_in_0x55ad0b705e50;
interface_4_out_0x55ad0b7072d0 -> interface_3_in_0x55ad0b7072d0;

// Input tensor.
subgraph cluster_subgraph_6 {
    label = "Input 2";
    interface_6_out_0x55ad0b705e18 [label="C_out", shape=none];
    interface_6_out_0x55ad0b705eb8 [label="k_1", shape=none];
    interface_6_out_0x55ad0b705e68 [label="C_in", shape=none];
}

interface_6_out_0x55ad0b705e18 -> interface_3_in_0x55ad0b705e18;
interface_6_out_0x55ad0b705eb8 -> interface_3_in_0x55ad0b705eb8;
interface_6_out_0x55ad0b705e68 -> interface_3_in_0x55ad0b705e68;

interface_3_out_0x55acfaae6490 -> interface_2_in_0x55acfaae6490;
interface_3_out_0x55ad0b705c20 -> interface_2_in_0x55ad0b705c20;
interface_3_out_0x55ad0b70c6c0 -> interface_2_in_0x55ad0b70c6c0;
interface_3_out_0x55ad0b7072d0 -> interface_2_in_0x55ad0b7072d0;

// Input tensor.
subgraph cluster_subgraph_7 {
    label = "Input 1";
    interface_7_out_0x55ad0b705c38 [label="C_out", shape=none];
    interface_7_out_0x55ad0b705dc8 [label="s", shape=none];
}

interface_7_out_0x55ad0b705c38 -> interface_2_in_0x55ad0b705c38;
interface_7_out_0x55ad0b705dc8 -> interface_2_in_0x55ad0b705dc8;

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
    interface_5_out_0x55acfaae6490;
    interface_5_out_0x55ad0b705e50;
    interface_5_out_0x55ad0b7072d0;
    interface_5_out_0x55ad0b71c4a8;
    interface_7_out_0x55ad0b705c38;
    interface_7_out_0x55ad0b705dc8;
    interface_6_out_0x55ad0b705e18;
    interface_6_out_0x55ad0b705eb8;
    interface_6_out_0x55ad0b705e68;
}
subgraph cluster_subgraph_output {
    label = "Output";
    interface_8_in_0x55acfaae6490 [label="N", shape=none];
    interface_8_in_0x55acfaae64b8 [label="C_out", shape=none];
    interface_8_in_0x55acfaae64e0 [label="H", shape=none];
    interface_8_in_0x55acfaae6508 [label="H", shape=none];
}
interface_0_out_0x55acfaae6490 -> interface_8_in_0x55acfaae6490;
interface_0_out_0x55acfaae64b8 -> interface_8_in_0x55acfaae64b8;
interface_0_out_0x55acfaae64e0 -> interface_8_in_0x55acfaae64e0;
interface_0_out_0x55acfaae6508 -> interface_8_in_0x55acfaae6508;

}

"""
class kernel_generated_0(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([64, 2]),
			torch.randn([64, 3, 64]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]
		in_2 = self.weights[1]

		# Perform contraction.
		t_3 = torch.einsum("ijkl -> iljk", in_0)

		# [H]@Unfold9ee82d943ec7d29d -> [H]@Merge5f50103ea583163b, [k_1]@Shared4e0659d169008e4
		t_3 = torch.reshape(t_3, (1, 1, 56, 3584, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (1, 3, 56, 64, 56, ))

		# Perform contraction.
		t_4 = torch.einsum("lknjm, ikj -> linm", t_3, in_2)

		# Perform contraction.
		t_5 = torch.einsum("kiml, ij -> kimjl", t_4, in_1)

		# No contraction needed.
		t_6 = t_5

		# [H]@Merge5f50103ea583163b, [s]@Merge5f50103ea5831638 -> [s*H]@Shift3c9c8e9d3c84cb9b
		t_6 = torch.reshape(t_6, (1, 64, 112, 56, ))

		# [s*H]@Shift3c9c8e9d3c84cb9b -> [s*H]@Splitdb1af055f999951a
		t_6 = torch.roll(t_6, self.shift_direction, 2)

		# [s*H]@Splitdb1af055f999951a -> [H]@Iterator96123ba3184da39c, [s]@Reduced95c644a3c072d9a
		t_6 = torch.reshape(t_6, (1, 64, 56, 2, 56, ))

		# [s]@Reduce
		t_6 = torch.sum(t_6, dim=(3, ))

		# No contraction needed.
		t_7 = t_6

		# [H]@Shift6b179c72f0c6dbad -> [H]@Iteratorb0a1def4ad5784ec
		t_7 = torch.roll(t_7, self.shift_direction, 3)

		# No need to crop the output tensor.
		y = t_7

		return y

class kernel_generated_1(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([128, 2]),
			torch.randn([128, 3, 64]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]
		in_2 = self.weights[1]

		# Perform contraction.
		t_3 = torch.einsum("ijkl -> iljk", in_0)

		# [H]@Unfold9ee82d943ec7d29d -> [H]@Merge5f50103ea583163b, [k_1]@Shared4e0659d169008e4
		t_3 = torch.reshape(t_3, (1, 1, 28, 1792, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (1, 3, 28, 64, 28, ))

		# Perform contraction.
		t_4 = torch.einsum("lknjm, ikj -> linm", t_3, in_2)

		# Perform contraction.
		t_5 = torch.einsum("kiml, ij -> kimjl", t_4, in_1)

		# No contraction needed.
		t_6 = t_5

		# [H]@Merge5f50103ea583163b, [s]@Merge5f50103ea5831638 -> [s*H]@Shift3c9c8e9d3c84cb9b
		t_6 = torch.reshape(t_6, (1, 128, 56, 28, ))

		# [s*H]@Shift3c9c8e9d3c84cb9b -> [s*H]@Splitdb1af055f999951a
		t_6 = torch.roll(t_6, self.shift_direction, 2)

		# [s*H]@Splitdb1af055f999951a -> [H]@Iterator96123ba3184da39c, [s]@Reduced95c644a3c072d9a
		t_6 = torch.reshape(t_6, (1, 128, 28, 2, 28, ))

		# [s]@Reduce
		t_6 = torch.sum(t_6, dim=(3, ))

		# No contraction needed.
		t_7 = t_6

		# [H]@Shift6b179c72f0c6dbad -> [H]@Iteratorb0a1def4ad5784ec
		t_7 = torch.roll(t_7, self.shift_direction, 3)

		# No need to crop the output tensor.
		y = t_7

		return y

class kernel_generated_2(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([128, 2]),
			torch.randn([128, 3, 128]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]
		in_2 = self.weights[1]

		# Perform contraction.
		t_3 = torch.einsum("ijkl -> iljk", in_0)

		# [H]@Unfold9ee82d943ec7d29d -> [H]@Merge5f50103ea583163b, [k_1]@Shared4e0659d169008e4
		t_3 = torch.reshape(t_3, (1, 1, 28, 3584, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (1, 3, 28, 128, 28, ))

		# Perform contraction.
		t_4 = torch.einsum("lknjm, ikj -> linm", t_3, in_2)

		# Perform contraction.
		t_5 = torch.einsum("kiml, ij -> kimjl", t_4, in_1)

		# No contraction needed.
		t_6 = t_5

		# [H]@Merge5f50103ea583163b, [s]@Merge5f50103ea5831638 -> [s*H]@Shift3c9c8e9d3c84cb9b
		t_6 = torch.reshape(t_6, (1, 128, 56, 28, ))

		# [s*H]@Shift3c9c8e9d3c84cb9b -> [s*H]@Splitdb1af055f999951a
		t_6 = torch.roll(t_6, self.shift_direction, 2)

		# [s*H]@Splitdb1af055f999951a -> [H]@Iterator96123ba3184da39c, [s]@Reduced95c644a3c072d9a
		t_6 = torch.reshape(t_6, (1, 128, 28, 2, 28, ))

		# [s]@Reduce
		t_6 = torch.sum(t_6, dim=(3, ))

		# No contraction needed.
		t_7 = t_6

		# [H]@Shift6b179c72f0c6dbad -> [H]@Iteratorb0a1def4ad5784ec
		t_7 = torch.roll(t_7, self.shift_direction, 3)

		# No need to crop the output tensor.
		y = t_7

		return y

class kernel_generated_3(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([256, 2]),
			torch.randn([256, 3, 128]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]
		in_2 = self.weights[1]

		# Perform contraction.
		t_3 = torch.einsum("ijkl -> iljk", in_0)

		# [H]@Unfold9ee82d943ec7d29d -> [H]@Merge5f50103ea583163b, [k_1]@Shared4e0659d169008e4
		t_3 = torch.reshape(t_3, (1, 1, 14, 1792, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (1, 3, 14, 128, 14, ))

		# Perform contraction.
		t_4 = torch.einsum("lknjm, ikj -> linm", t_3, in_2)

		# Perform contraction.
		t_5 = torch.einsum("kiml, ij -> kimjl", t_4, in_1)

		# No contraction needed.
		t_6 = t_5

		# [H]@Merge5f50103ea583163b, [s]@Merge5f50103ea5831638 -> [s*H]@Shift3c9c8e9d3c84cb9b
		t_6 = torch.reshape(t_6, (1, 256, 28, 14, ))

		# [s*H]@Shift3c9c8e9d3c84cb9b -> [s*H]@Splitdb1af055f999951a
		t_6 = torch.roll(t_6, self.shift_direction, 2)

		# [s*H]@Splitdb1af055f999951a -> [H]@Iterator96123ba3184da39c, [s]@Reduced95c644a3c072d9a
		t_6 = torch.reshape(t_6, (1, 256, 14, 2, 14, ))

		# [s]@Reduce
		t_6 = torch.sum(t_6, dim=(3, ))

		# No contraction needed.
		t_7 = t_6

		# [H]@Shift6b179c72f0c6dbad -> [H]@Iteratorb0a1def4ad5784ec
		t_7 = torch.roll(t_7, self.shift_direction, 3)

		# No need to crop the output tensor.
		y = t_7

		return y

class kernel_generated_4(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([256, 2]),
			torch.randn([256, 3, 256]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]
		in_2 = self.weights[1]

		# Perform contraction.
		t_3 = torch.einsum("ijkl -> iljk", in_0)

		# [H]@Unfold9ee82d943ec7d29d -> [H]@Merge5f50103ea583163b, [k_1]@Shared4e0659d169008e4
		t_3 = torch.reshape(t_3, (1, 1, 14, 3584, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (1, 3, 14, 256, 14, ))

		# Perform contraction.
		t_4 = torch.einsum("lknjm, ikj -> linm", t_3, in_2)

		# Perform contraction.
		t_5 = torch.einsum("kiml, ij -> kimjl", t_4, in_1)

		# No contraction needed.
		t_6 = t_5

		# [H]@Merge5f50103ea583163b, [s]@Merge5f50103ea5831638 -> [s*H]@Shift3c9c8e9d3c84cb9b
		t_6 = torch.reshape(t_6, (1, 256, 28, 14, ))

		# [s*H]@Shift3c9c8e9d3c84cb9b -> [s*H]@Splitdb1af055f999951a
		t_6 = torch.roll(t_6, self.shift_direction, 2)

		# [s*H]@Splitdb1af055f999951a -> [H]@Iterator96123ba3184da39c, [s]@Reduced95c644a3c072d9a
		t_6 = torch.reshape(t_6, (1, 256, 14, 2, 14, ))

		# [s]@Reduce
		t_6 = torch.sum(t_6, dim=(3, ))

		# No contraction needed.
		t_7 = t_6

		# [H]@Shift6b179c72f0c6dbad -> [H]@Iteratorb0a1def4ad5784ec
		t_7 = torch.roll(t_7, self.shift_direction, 3)

		# No need to crop the output tensor.
		y = t_7

		return y

class kernel_generated_5(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([512, 2]),
			torch.randn([512, 3, 256]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]
		in_2 = self.weights[1]

		# Perform contraction.
		t_3 = torch.einsum("ijkl -> iljk", in_0)

		# [H]@Unfold9ee82d943ec7d29d -> [H]@Merge5f50103ea583163b, [k_1]@Shared4e0659d169008e4
		t_3 = torch.reshape(t_3, (1, 1, 7, 1792, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (1, 3, 7, 256, 7, ))

		# Perform contraction.
		t_4 = torch.einsum("lknjm, ikj -> linm", t_3, in_2)

		# Perform contraction.
		t_5 = torch.einsum("kiml, ij -> kimjl", t_4, in_1)

		# No contraction needed.
		t_6 = t_5

		# [H]@Merge5f50103ea583163b, [s]@Merge5f50103ea5831638 -> [s*H]@Shift3c9c8e9d3c84cb9b
		t_6 = torch.reshape(t_6, (1, 512, 14, 7, ))

		# [s*H]@Shift3c9c8e9d3c84cb9b -> [s*H]@Splitdb1af055f999951a
		t_6 = torch.roll(t_6, self.shift_direction, 2)

		# [s*H]@Splitdb1af055f999951a -> [H]@Iterator96123ba3184da39c, [s]@Reduced95c644a3c072d9a
		t_6 = torch.reshape(t_6, (1, 512, 7, 2, 7, ))

		# [s]@Reduce
		t_6 = torch.sum(t_6, dim=(3, ))

		# No contraction needed.
		t_7 = t_6

		# [H]@Shift6b179c72f0c6dbad -> [H]@Iteratorb0a1def4ad5784ec
		t_7 = torch.roll(t_7, self.shift_direction, 3)

		# No need to crop the output tensor.
		y = t_7

		return y

class kernel_generated_6(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([512, 2]),
			torch.randn([512, 3, 512]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]
		in_2 = self.weights[1]

		# Perform contraction.
		t_3 = torch.einsum("ijkl -> iljk", in_0)

		# [H]@Unfold9ee82d943ec7d29d -> [H]@Merge5f50103ea583163b, [k_1]@Shared4e0659d169008e4
		t_3 = torch.reshape(t_3, (1, 1, 7, 3584, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (1, 3, 7, 512, 7, ))

		# Perform contraction.
		t_4 = torch.einsum("lknjm, ikj -> linm", t_3, in_2)

		# Perform contraction.
		t_5 = torch.einsum("kiml, ij -> kimjl", t_4, in_1)

		# No contraction needed.
		t_6 = t_5

		# [H]@Merge5f50103ea583163b, [s]@Merge5f50103ea5831638 -> [s*H]@Shift3c9c8e9d3c84cb9b
		t_6 = torch.reshape(t_6, (1, 512, 14, 7, ))

		# [s*H]@Shift3c9c8e9d3c84cb9b -> [s*H]@Splitdb1af055f999951a
		t_6 = torch.roll(t_6, self.shift_direction, 2)

		# [s*H]@Splitdb1af055f999951a -> [H]@Iterator96123ba3184da39c, [s]@Reduced95c644a3c072d9a
		t_6 = torch.reshape(t_6, (1, 512, 7, 2, 7, ))

		# [s]@Reduce
		t_6 = torch.sum(t_6, dim=(3, ))

		# No contraction needed.
		t_7 = t_6

		# [H]@Shift6b179c72f0c6dbad -> [H]@Iteratorb0a1def4ad5784ec
		t_7 = torch.roll(t_7, self.shift_direction, 3)

		# No need to crop the output tensor.
		y = t_7

		return y

