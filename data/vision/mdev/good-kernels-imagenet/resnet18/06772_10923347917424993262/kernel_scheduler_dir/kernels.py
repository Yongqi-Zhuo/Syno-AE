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
        interface_0_out_0x55a308c0a8f0 [label="N", shape=none];
        interface_0_out_0x55a308c0a918 [label="C_out", shape=none];
        interface_0_out_0x55a308c0a940 [label="H", shape=none];
        interface_0_out_0x55a308c0a968 [label="H", shape=none];
    }
    {
        rank = same;
        interface_0_out_0x55a308c0a8f0;
        interface_0_out_0x55a308c0a918;
        interface_0_out_0x55a308c0a940;
        interface_0_out_0x55a308c0a968;
    }
    // Input 0.
    subgraph cluster_subgraph_0_in_0 {
        label = "";
        interface_0_in_0x55a308c0a8f0 [label="N", shape=none];
        interface_0_in_0x55a3093b9590 [label="H", shape=none];
        interface_0_in_0x55a308c0a918 [label="C_out", shape=none];
        interface_0_in_0x55a308c0a940 [label="H", shape=none];
    }
    {
        rank = same;
        interface_0_in_0x55a308c0a8f0;
        interface_0_in_0x55a3093b9590;
        interface_0_in_0x55a308c0a918;
        interface_0_in_0x55a308c0a940;
    }
    // Op's.
    op_0x55a3093b9570 [label="Shift"];
    // Dimension's.
    interface_0_in_0x55a308c0a8f0 -> interface_0_out_0x55a308c0a8f0 [label="N"];
    interface_0_in_0x55a308c0a918 -> interface_0_out_0x55a308c0a918 [label="C_out"];
    interface_0_in_0x55a308c0a940 -> interface_0_out_0x55a308c0a940 [label="H"];
    op_0x55a3093b9570 -> interface_0_out_0x55a308c0a968 [label="H"];
    interface_0_in_0x55a3093b9590 -> op_0x55a3093b9570 [label="H"];
}

// Stage tensor.
subgraph cluster_subgraph_1 {
    label = "Subgraph 1";
    // Reductions.
    reduce_0x7effd8002ce8 [label="Sum", shape=box];
    // Output.
    subgraph cluster_subgraph_1_out {
        label = "";
        interface_1_out_0x55a308c0a8f0 [label="N", shape=none];
        interface_1_out_0x55a3093b9590 [label="H", shape=none];
        interface_1_out_0x55a308c0a918 [label="C_out", shape=none];
        interface_1_out_0x55a308c0a940 [label="H", shape=none];
    }
    {
        rank = same;
        reduce_0x7effd8002ce8;
        interface_1_out_0x55a308c0a8f0;
        interface_1_out_0x55a3093b9590;
        interface_1_out_0x55a308c0a918;
        interface_1_out_0x55a308c0a940;
    }
    // Input 0.
    subgraph cluster_subgraph_1_in_0 {
        label = "";
        interface_1_in_0x55a308c0a8f0 [label="N", shape=none];
        interface_1_in_0x55a3093b9590 [label="H", shape=none];
        interface_1_in_0x55a3093bb5b0 [label="H", shape=none];
        interface_1_in_0x55a308c0a918 [label="C_out", shape=none];
        interface_1_in_0x55a3093bb5c8 [label="s", shape=none];
    }
    {
        rank = same;
        interface_1_in_0x55a308c0a8f0;
        interface_1_in_0x55a3093b9590;
        interface_1_in_0x55a3093bb5b0;
        interface_1_in_0x55a308c0a918;
        interface_1_in_0x55a3093bb5c8;
    }
    // Op's.
    op_0x55a3093b9600 [label="Shift"];
    op_0x55a3093bb570 [label="Merge"];
    op_0x55a3093bdd60 [label="Split"];
    // Dimension's.
    interface_1_in_0x55a308c0a8f0 -> interface_1_out_0x55a308c0a8f0 [label="N"];
    interface_1_in_0x55a308c0a918 -> interface_1_out_0x55a308c0a918 [label="C_out"];
    op_0x55a3093bdd60 -> interface_1_out_0x55a308c0a940 [label="H"];
    interface_1_in_0x55a3093b9590 -> interface_1_out_0x55a3093b9590 [label="H"];
    op_0x55a3093bb570 -> op_0x55a3093b9600 [label="s*H"];
    interface_1_in_0x55a3093bb5b0 -> op_0x55a3093bb570 [label="H"];
    interface_1_in_0x55a3093bb5c8 -> op_0x55a3093bb570 [label="s"];
    op_0x55a3093b9600 -> op_0x55a3093bdd60 [label="s*H"];
    op_0x55a3093bdd60 -> reduce_0x7effd8002ce8 [label="s"];
}

// Stage tensor.
subgraph cluster_subgraph_2 {
    label = "Subgraph 2";
    // Reductions.
    // Output.
    subgraph cluster_subgraph_2_out {
        label = "";
        interface_2_out_0x55a308c0a8f0 [label="N", shape=none];
        interface_2_out_0x55a3093b9590 [label="H", shape=none];
        interface_2_out_0x55a3093bb5b0 [label="H", shape=none];
        interface_2_out_0x55a308c0a918 [label="C_out", shape=none];
        interface_2_out_0x55a3093bb5c8 [label="s", shape=none];
    }
    {
        rank = same;
        interface_2_out_0x55a308c0a8f0;
        interface_2_out_0x55a3093b9590;
        interface_2_out_0x55a3093bb5b0;
        interface_2_out_0x55a308c0a918;
        interface_2_out_0x55a3093bb5c8;
    }
    // Input 0.
    subgraph cluster_subgraph_2_in_0 {
        label = "";
        interface_2_in_0x55a308c0a8f0 [label="N", shape=none];
        interface_2_in_0x55a3093b9590 [label="H", shape=none];
        interface_2_in_0x55a3093bb5b0 [label="H", shape=none];
        interface_2_in_0x55a3093b8720 [label="C_out", shape=none];
    }
    // Input 1.
    subgraph cluster_subgraph_2_in_1 {
        label = "";
        interface_2_in_0x55a3093b8738 [label="C_out", shape=none];
        interface_2_in_0x55a3093b8b98 [label="s", shape=none];
    }
    {
        rank = same;
        interface_2_in_0x55a308c0a8f0;
        interface_2_in_0x55a3093b9590;
        interface_2_in_0x55a3093bb5b0;
        interface_2_in_0x55a3093b8720;
        interface_2_in_0x55a3093b8738;
        interface_2_in_0x55a3093b8b98;
    }
    // Op's.
    op_0x55a3093b8700 [label="Share"];
    op_0x55a3093b8b60 [label="Share"];
    op_0x55a3093b8cd8 [label="Expand"];
    // Dimension's.
    interface_2_in_0x55a308c0a8f0 -> interface_2_out_0x55a308c0a8f0 [label="N"];
    op_0x55a3093b8700 -> interface_2_out_0x55a308c0a918 [label="C_out"];
    interface_2_in_0x55a3093b8720 -> op_0x55a3093b8700 [label="C_out"];
    interface_2_in_0x55a3093b8738 -> op_0x55a3093b8700 [label="C_out"];
    op_0x55a3093b8cd8 -> op_0x55a3093b8b60 [label="s"];
    interface_2_in_0x55a3093b8b98 -> op_0x55a3093b8b60 [label="s"];
    interface_2_in_0x55a3093b9590 -> interface_2_out_0x55a3093b9590 [label="H"];
    interface_2_in_0x55a3093bb5b0 -> interface_2_out_0x55a3093bb5b0 [label="H"];
    op_0x55a3093b8b60 -> interface_2_out_0x55a3093bb5c8 [label="s"];
}

// Stage tensor.
subgraph cluster_subgraph_3 {
    label = "Subgraph 3";
    // Reductions.
    reduce_0x7effd8005b48 [label="Sum", shape=box];
    reduce_0x7effd8001a98 [label="Sum", shape=box];
    // Output.
    subgraph cluster_subgraph_3_out {
        label = "";
        interface_3_out_0x55a308c0a8f0 [label="N", shape=none];
        interface_3_out_0x55a3093b9590 [label="H", shape=none];
        interface_3_out_0x55a3093bb5b0 [label="H", shape=none];
        interface_3_out_0x55a3093b8720 [label="C_out", shape=none];
    }
    {
        rank = same;
        reduce_0x7effd8005b48;
        reduce_0x7effd8001a98;
        interface_3_out_0x55a308c0a8f0;
        interface_3_out_0x55a3093b9590;
        interface_3_out_0x55a3093bb5b0;
        interface_3_out_0x55a3093b8720;
    }
    // Input 0.
    subgraph cluster_subgraph_3_in_0 {
        label = "";
        interface_3_in_0x55a308c0a8f0 [label="N", shape=none];
        interface_3_in_0x55a3093ce3f0 [label="C_in", shape=none];
        interface_3_in_0x55a3093b9590 [label="H", shape=none];
        interface_3_in_0x55a3093bb5b0 [label="H", shape=none];
        interface_3_in_0x55a3093ce440 [label="k_1", shape=none];
    }
    // Input 1.
    subgraph cluster_subgraph_3_in_1 {
        label = "";
        interface_3_in_0x55a3093ce408 [label="C_in", shape=none];
        interface_3_in_0x55a3093ce458 [label="k_1", shape=none];
        interface_3_in_0x55a3093ce3b8 [label="C_out", shape=none];
    }
    {
        rank = same;
        interface_3_in_0x55a308c0a8f0;
        interface_3_in_0x55a3093ce3f0;
        interface_3_in_0x55a3093b9590;
        interface_3_in_0x55a3093bb5b0;
        interface_3_in_0x55a3093ce440;
        interface_3_in_0x55a3093ce408;
        interface_3_in_0x55a3093ce458;
        interface_3_in_0x55a3093ce3b8;
    }
    // Op's.
    op_0x55a3093b8cf8 [label="Expand"];
    op_0x55a3093ce380 [label="Share"];
    op_0x55a3093ce3d0 [label="Share"];
    op_0x55a3093ce420 [label="Share"];
    // Dimension's.
    interface_3_in_0x55a308c0a8f0 -> interface_3_out_0x55a308c0a8f0 [label="N"];
    op_0x55a3093ce380 -> interface_3_out_0x55a3093b8720 [label="C_out"];
    interface_3_in_0x55a3093b9590 -> interface_3_out_0x55a3093b9590 [label="H"];
    interface_3_in_0x55a3093bb5b0 -> interface_3_out_0x55a3093bb5b0 [label="H"];
    op_0x55a3093b8cf8 -> op_0x55a3093ce380 [label="C_out"];
    interface_3_in_0x55a3093ce3b8 -> op_0x55a3093ce380 [label="C_out"];
    interface_3_in_0x55a3093ce3f0 -> op_0x55a3093ce3d0 [label="C_in"];
    interface_3_in_0x55a3093ce408 -> op_0x55a3093ce3d0 [label="C_in"];
    interface_3_in_0x55a3093ce440 -> op_0x55a3093ce420 [label="k_1"];
    interface_3_in_0x55a3093ce458 -> op_0x55a3093ce420 [label="k_1"];
    op_0x55a3093ce420 -> reduce_0x7effd8001a98 [label="k_1"];
    op_0x55a3093ce3d0 -> reduce_0x7effd8005b48 [label="C_in"];
}

// Stage tensor.
subgraph cluster_subgraph_4 {
    label = "Subgraph 4";
    // Reductions.
    // Output.
    subgraph cluster_subgraph_4_out {
        label = "";
        interface_4_out_0x55a308c0a8f0 [label="N", shape=none];
        interface_4_out_0x55a3093ce3f0 [label="C_in", shape=none];
        interface_4_out_0x55a3093b9590 [label="H", shape=none];
        interface_4_out_0x55a3093bb5b0 [label="H", shape=none];
        interface_4_out_0x55a3093ce440 [label="k_1", shape=none];
    }
    {
        rank = same;
        interface_4_out_0x55a308c0a8f0;
        interface_4_out_0x55a3093ce3f0;
        interface_4_out_0x55a3093b9590;
        interface_4_out_0x55a3093bb5b0;
        interface_4_out_0x55a3093ce440;
    }
    // Input 0.
    subgraph cluster_subgraph_4_in_0 {
        label = "";
        interface_4_in_0x55a308c0a8f0 [label="N", shape=none];
        interface_4_in_0x55a3093ce3f0 [label="C_in", shape=none];
        interface_4_in_0x55a3093b9590 [label="H", shape=none];
        interface_4_in_0x55a3093bb9e8 [label="H", shape=none];
    }
    {
        rank = same;
        interface_4_in_0x55a308c0a8f0;
        interface_4_in_0x55a3093ce3f0;
        interface_4_in_0x55a3093b9590;
        interface_4_in_0x55a3093bb9e8;
    }
    // Op's.
    op_0x55a3093bb9c0 [label="Unfold"];
    // Dimension's.
    interface_4_in_0x55a308c0a8f0 -> interface_4_out_0x55a308c0a8f0 [label="N"];
    interface_4_in_0x55a3093b9590 -> interface_4_out_0x55a3093b9590 [label="H"];
    op_0x55a3093bb9c0 -> interface_4_out_0x55a3093bb5b0 [label="H"];
    interface_4_in_0x55a3093bb9e8 -> op_0x55a3093bb9c0 [label="H"];
    interface_4_in_0x55a3093ce3f0 -> interface_4_out_0x55a3093ce3f0 [label="C_in"];
    op_0x55a3093bb9c0 -> interface_4_out_0x55a3093ce440 [label="k_1"];
}

// Input tensor.
subgraph cluster_subgraph_5 {
    label = "Input 0";
    interface_5_out_0x55a308c0a8f0 [label="N", shape=none];
    interface_5_out_0x55a3093ce3f0 [label="C_in", shape=none];
    interface_5_out_0x55a3093b9590 [label="H", shape=none];
    interface_5_out_0x55a3093bb9e8 [label="H", shape=none];
}

interface_5_out_0x55a308c0a8f0 -> interface_4_in_0x55a308c0a8f0;
interface_5_out_0x55a3093ce3f0 -> interface_4_in_0x55a3093ce3f0;
interface_5_out_0x55a3093b9590 -> interface_4_in_0x55a3093b9590;
interface_5_out_0x55a3093bb9e8 -> interface_4_in_0x55a3093bb9e8;

interface_4_out_0x55a308c0a8f0 -> interface_3_in_0x55a308c0a8f0;
interface_4_out_0x55a3093ce3f0 -> interface_3_in_0x55a3093ce3f0;
interface_4_out_0x55a3093b9590 -> interface_3_in_0x55a3093b9590;
interface_4_out_0x55a3093bb5b0 -> interface_3_in_0x55a3093bb5b0;
interface_4_out_0x55a3093ce440 -> interface_3_in_0x55a3093ce440;

// Input tensor.
subgraph cluster_subgraph_6 {
    label = "Input 2";
    interface_6_out_0x55a3093ce408 [label="C_in", shape=none];
    interface_6_out_0x55a3093ce458 [label="k_1", shape=none];
    interface_6_out_0x55a3093ce3b8 [label="C_out", shape=none];
}

interface_6_out_0x55a3093ce408 -> interface_3_in_0x55a3093ce408;
interface_6_out_0x55a3093ce458 -> interface_3_in_0x55a3093ce458;
interface_6_out_0x55a3093ce3b8 -> interface_3_in_0x55a3093ce3b8;

interface_3_out_0x55a308c0a8f0 -> interface_2_in_0x55a308c0a8f0;
interface_3_out_0x55a3093b9590 -> interface_2_in_0x55a3093b9590;
interface_3_out_0x55a3093bb5b0 -> interface_2_in_0x55a3093bb5b0;
interface_3_out_0x55a3093b8720 -> interface_2_in_0x55a3093b8720;

// Input tensor.
subgraph cluster_subgraph_7 {
    label = "Input 1";
    interface_7_out_0x55a3093b8738 [label="C_out", shape=none];
    interface_7_out_0x55a3093b8b98 [label="s", shape=none];
}

interface_7_out_0x55a3093b8738 -> interface_2_in_0x55a3093b8738;
interface_7_out_0x55a3093b8b98 -> interface_2_in_0x55a3093b8b98;

interface_2_out_0x55a308c0a8f0 -> interface_1_in_0x55a308c0a8f0;
interface_2_out_0x55a3093b9590 -> interface_1_in_0x55a3093b9590;
interface_2_out_0x55a3093bb5b0 -> interface_1_in_0x55a3093bb5b0;
interface_2_out_0x55a308c0a918 -> interface_1_in_0x55a308c0a918;
interface_2_out_0x55a3093bb5c8 -> interface_1_in_0x55a3093bb5c8;

interface_1_out_0x55a308c0a8f0 -> interface_0_in_0x55a308c0a8f0;
interface_1_out_0x55a3093b9590 -> interface_0_in_0x55a3093b9590;
interface_1_out_0x55a308c0a918 -> interface_0_in_0x55a308c0a918;
interface_1_out_0x55a308c0a940 -> interface_0_in_0x55a308c0a940;

{
    rank = same;
    interface_5_out_0x55a308c0a8f0;
    interface_5_out_0x55a3093ce3f0;
    interface_5_out_0x55a3093b9590;
    interface_5_out_0x55a3093bb9e8;
    interface_7_out_0x55a3093b8738;
    interface_7_out_0x55a3093b8b98;
    interface_6_out_0x55a3093ce408;
    interface_6_out_0x55a3093ce458;
    interface_6_out_0x55a3093ce3b8;
}
subgraph cluster_subgraph_output {
    label = "Output";
    interface_8_in_0x55a308c0a8f0 [label="N", shape=none];
    interface_8_in_0x55a308c0a918 [label="C_out", shape=none];
    interface_8_in_0x55a308c0a940 [label="H", shape=none];
    interface_8_in_0x55a308c0a968 [label="H", shape=none];
}
interface_0_out_0x55a308c0a8f0 -> interface_8_in_0x55a308c0a8f0;
interface_0_out_0x55a308c0a918 -> interface_8_in_0x55a308c0a918;
interface_0_out_0x55a308c0a940 -> interface_8_in_0x55a308c0a940;
interface_0_out_0x55a308c0a968 -> interface_8_in_0x55a308c0a968;

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

		# No contraction needed.
		t_3 = in_0

		# [H]@Unfold9ee82d943ec7d29d -> [H]@Merge5f50103ea583163b, [k_1]@Shared4e0659d169008e4
		t_3 = torch.reshape(t_3, (1024, 3584, 56, 1, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (1024, 64, 56, 3, 56, ))

		# Permute to match the output of this subgraph.
		t_3 = torch.permute(t_3, (0, 1, 2, 4, 3, ))

		# Perform contraction.
		t_4 = torch.einsum("ljmnk, jki -> lmni", t_3, in_2)

		# Perform contraction.
		t_5 = torch.einsum("klmi, ij -> klmij", t_4, in_1)

		# No contraction needed.
		t_6 = t_5

		# [H]@Merge5f50103ea583163b, [s]@Merge5f50103ea5831638 -> [s*H]@Shift3c9c8e9d3c84cb9b
		t_6 = torch.permute(t_6, (0, 1, 3, 2, 4, ))
		t_6 = torch.reshape(t_6, (1024, 56, 64, 112, ))

		# [s*H]@Shift3c9c8e9d3c84cb9b -> [s*H]@Splitdb1af055f999951a
		t_6 = torch.roll(t_6, self.shift_direction, 3)

		# [s*H]@Splitdb1af055f999951a -> [H]@Iterator96123ba3184da39c, [s]@Reduced95c644a3c072d9a
		t_6 = torch.reshape(t_6, (1024, 56, 64, 56, 2, ))

		# [s]@Reduce
		t_6 = torch.sum(t_6, dim=(4, ))

		# No contraction needed.
		t_7 = t_6

		# [H]@Shift6b179c72f0c6dbad -> [H]@Iteratorb0a1def4ad5784ec
		t_7 = torch.roll(t_7, self.shift_direction, 1)

		# Permute to match the output of this subgraph.
		t_7 = torch.permute(t_7, (0, 2, 3, 1, ))

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
			torch.randn([64, 3, 128]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]
		in_2 = self.weights[1]

		# No contraction needed.
		t_3 = in_0

		# [H]@Unfold9ee82d943ec7d29d -> [H]@Merge5f50103ea583163b, [k_1]@Shared4e0659d169008e4
		t_3 = torch.reshape(t_3, (1024, 1792, 28, 1, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (1024, 64, 28, 3, 28, ))

		# Permute to match the output of this subgraph.
		t_3 = torch.permute(t_3, (0, 1, 2, 4, 3, ))

		# Perform contraction.
		t_4 = torch.einsum("ljmnk, jki -> lmni", t_3, in_2)

		# Perform contraction.
		t_5 = torch.einsum("klmi, ij -> klmij", t_4, in_1)

		# No contraction needed.
		t_6 = t_5

		# [H]@Merge5f50103ea583163b, [s]@Merge5f50103ea5831638 -> [s*H]@Shift3c9c8e9d3c84cb9b
		t_6 = torch.permute(t_6, (0, 1, 3, 2, 4, ))
		t_6 = torch.reshape(t_6, (1024, 28, 128, 56, ))

		# [s*H]@Shift3c9c8e9d3c84cb9b -> [s*H]@Splitdb1af055f999951a
		t_6 = torch.roll(t_6, self.shift_direction, 3)

		# [s*H]@Splitdb1af055f999951a -> [H]@Iterator96123ba3184da39c, [s]@Reduced95c644a3c072d9a
		t_6 = torch.reshape(t_6, (1024, 28, 128, 28, 2, ))

		# [s]@Reduce
		t_6 = torch.sum(t_6, dim=(4, ))

		# No contraction needed.
		t_7 = t_6

		# [H]@Shift6b179c72f0c6dbad -> [H]@Iteratorb0a1def4ad5784ec
		t_7 = torch.roll(t_7, self.shift_direction, 1)

		# Permute to match the output of this subgraph.
		t_7 = torch.permute(t_7, (0, 2, 3, 1, ))

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

		# No contraction needed.
		t_3 = in_0

		# [H]@Unfold9ee82d943ec7d29d -> [H]@Merge5f50103ea583163b, [k_1]@Shared4e0659d169008e4
		t_3 = torch.reshape(t_3, (1024, 3584, 28, 1, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (1024, 128, 28, 3, 28, ))

		# Permute to match the output of this subgraph.
		t_3 = torch.permute(t_3, (0, 1, 2, 4, 3, ))

		# Perform contraction.
		t_4 = torch.einsum("ljmnk, jki -> lmni", t_3, in_2)

		# Perform contraction.
		t_5 = torch.einsum("klmi, ij -> klmij", t_4, in_1)

		# No contraction needed.
		t_6 = t_5

		# [H]@Merge5f50103ea583163b, [s]@Merge5f50103ea5831638 -> [s*H]@Shift3c9c8e9d3c84cb9b
		t_6 = torch.permute(t_6, (0, 1, 3, 2, 4, ))
		t_6 = torch.reshape(t_6, (1024, 28, 128, 56, ))

		# [s*H]@Shift3c9c8e9d3c84cb9b -> [s*H]@Splitdb1af055f999951a
		t_6 = torch.roll(t_6, self.shift_direction, 3)

		# [s*H]@Splitdb1af055f999951a -> [H]@Iterator96123ba3184da39c, [s]@Reduced95c644a3c072d9a
		t_6 = torch.reshape(t_6, (1024, 28, 128, 28, 2, ))

		# [s]@Reduce
		t_6 = torch.sum(t_6, dim=(4, ))

		# No contraction needed.
		t_7 = t_6

		# [H]@Shift6b179c72f0c6dbad -> [H]@Iteratorb0a1def4ad5784ec
		t_7 = torch.roll(t_7, self.shift_direction, 1)

		# Permute to match the output of this subgraph.
		t_7 = torch.permute(t_7, (0, 2, 3, 1, ))

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
			torch.randn([128, 3, 256]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]
		in_2 = self.weights[1]

		# No contraction needed.
		t_3 = in_0

		# [H]@Unfold9ee82d943ec7d29d -> [H]@Merge5f50103ea583163b, [k_1]@Shared4e0659d169008e4
		t_3 = torch.reshape(t_3, (1024, 1792, 14, 1, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (1024, 128, 14, 3, 14, ))

		# Permute to match the output of this subgraph.
		t_3 = torch.permute(t_3, (0, 1, 2, 4, 3, ))

		# Perform contraction.
		t_4 = torch.einsum("ljmnk, jki -> lmni", t_3, in_2)

		# Perform contraction.
		t_5 = torch.einsum("klmi, ij -> klmij", t_4, in_1)

		# No contraction needed.
		t_6 = t_5

		# [H]@Merge5f50103ea583163b, [s]@Merge5f50103ea5831638 -> [s*H]@Shift3c9c8e9d3c84cb9b
		t_6 = torch.permute(t_6, (0, 1, 3, 2, 4, ))
		t_6 = torch.reshape(t_6, (1024, 14, 256, 28, ))

		# [s*H]@Shift3c9c8e9d3c84cb9b -> [s*H]@Splitdb1af055f999951a
		t_6 = torch.roll(t_6, self.shift_direction, 3)

		# [s*H]@Splitdb1af055f999951a -> [H]@Iterator96123ba3184da39c, [s]@Reduced95c644a3c072d9a
		t_6 = torch.reshape(t_6, (1024, 14, 256, 14, 2, ))

		# [s]@Reduce
		t_6 = torch.sum(t_6, dim=(4, ))

		# No contraction needed.
		t_7 = t_6

		# [H]@Shift6b179c72f0c6dbad -> [H]@Iteratorb0a1def4ad5784ec
		t_7 = torch.roll(t_7, self.shift_direction, 1)

		# Permute to match the output of this subgraph.
		t_7 = torch.permute(t_7, (0, 2, 3, 1, ))

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

		# No contraction needed.
		t_3 = in_0

		# [H]@Unfold9ee82d943ec7d29d -> [H]@Merge5f50103ea583163b, [k_1]@Shared4e0659d169008e4
		t_3 = torch.reshape(t_3, (1024, 3584, 14, 1, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (1024, 256, 14, 3, 14, ))

		# Permute to match the output of this subgraph.
		t_3 = torch.permute(t_3, (0, 1, 2, 4, 3, ))

		# Perform contraction.
		t_4 = torch.einsum("ljmnk, jki -> lmni", t_3, in_2)

		# Perform contraction.
		t_5 = torch.einsum("klmi, ij -> klmij", t_4, in_1)

		# No contraction needed.
		t_6 = t_5

		# [H]@Merge5f50103ea583163b, [s]@Merge5f50103ea5831638 -> [s*H]@Shift3c9c8e9d3c84cb9b
		t_6 = torch.permute(t_6, (0, 1, 3, 2, 4, ))
		t_6 = torch.reshape(t_6, (1024, 14, 256, 28, ))

		# [s*H]@Shift3c9c8e9d3c84cb9b -> [s*H]@Splitdb1af055f999951a
		t_6 = torch.roll(t_6, self.shift_direction, 3)

		# [s*H]@Splitdb1af055f999951a -> [H]@Iterator96123ba3184da39c, [s]@Reduced95c644a3c072d9a
		t_6 = torch.reshape(t_6, (1024, 14, 256, 14, 2, ))

		# [s]@Reduce
		t_6 = torch.sum(t_6, dim=(4, ))

		# No contraction needed.
		t_7 = t_6

		# [H]@Shift6b179c72f0c6dbad -> [H]@Iteratorb0a1def4ad5784ec
		t_7 = torch.roll(t_7, self.shift_direction, 1)

		# Permute to match the output of this subgraph.
		t_7 = torch.permute(t_7, (0, 2, 3, 1, ))

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
			torch.randn([256, 3, 512]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]
		in_2 = self.weights[1]

		# No contraction needed.
		t_3 = in_0

		# [H]@Unfold9ee82d943ec7d29d -> [H]@Merge5f50103ea583163b, [k_1]@Shared4e0659d169008e4
		t_3 = torch.reshape(t_3, (1024, 1792, 7, 1, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (1024, 256, 7, 3, 7, ))

		# Permute to match the output of this subgraph.
		t_3 = torch.permute(t_3, (0, 1, 2, 4, 3, ))

		# Perform contraction.
		t_4 = torch.einsum("ljmnk, jki -> lmni", t_3, in_2)

		# Perform contraction.
		t_5 = torch.einsum("klmi, ij -> klmij", t_4, in_1)

		# No contraction needed.
		t_6 = t_5

		# [H]@Merge5f50103ea583163b, [s]@Merge5f50103ea5831638 -> [s*H]@Shift3c9c8e9d3c84cb9b
		t_6 = torch.permute(t_6, (0, 1, 3, 2, 4, ))
		t_6 = torch.reshape(t_6, (1024, 7, 512, 14, ))

		# [s*H]@Shift3c9c8e9d3c84cb9b -> [s*H]@Splitdb1af055f999951a
		t_6 = torch.roll(t_6, self.shift_direction, 3)

		# [s*H]@Splitdb1af055f999951a -> [H]@Iterator96123ba3184da39c, [s]@Reduced95c644a3c072d9a
		t_6 = torch.reshape(t_6, (1024, 7, 512, 7, 2, ))

		# [s]@Reduce
		t_6 = torch.sum(t_6, dim=(4, ))

		# No contraction needed.
		t_7 = t_6

		# [H]@Shift6b179c72f0c6dbad -> [H]@Iteratorb0a1def4ad5784ec
		t_7 = torch.roll(t_7, self.shift_direction, 1)

		# Permute to match the output of this subgraph.
		t_7 = torch.permute(t_7, (0, 2, 3, 1, ))

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

		# No contraction needed.
		t_3 = in_0

		# [H]@Unfold9ee82d943ec7d29d -> [H]@Merge5f50103ea583163b, [k_1]@Shared4e0659d169008e4
		t_3 = torch.reshape(t_3, (1024, 3584, 7, 1, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (1024, 512, 7, 3, 7, ))

		# Permute to match the output of this subgraph.
		t_3 = torch.permute(t_3, (0, 1, 2, 4, 3, ))

		# Perform contraction.
		t_4 = torch.einsum("ljmnk, jki -> lmni", t_3, in_2)

		# Perform contraction.
		t_5 = torch.einsum("klmi, ij -> klmij", t_4, in_1)

		# No contraction needed.
		t_6 = t_5

		# [H]@Merge5f50103ea583163b, [s]@Merge5f50103ea5831638 -> [s*H]@Shift3c9c8e9d3c84cb9b
		t_6 = torch.permute(t_6, (0, 1, 3, 2, 4, ))
		t_6 = torch.reshape(t_6, (1024, 7, 512, 14, ))

		# [s*H]@Shift3c9c8e9d3c84cb9b -> [s*H]@Splitdb1af055f999951a
		t_6 = torch.roll(t_6, self.shift_direction, 3)

		# [s*H]@Splitdb1af055f999951a -> [H]@Iterator96123ba3184da39c, [s]@Reduced95c644a3c072d9a
		t_6 = torch.reshape(t_6, (1024, 7, 512, 7, 2, ))

		# [s]@Reduce
		t_6 = torch.sum(t_6, dim=(4, ))

		# No contraction needed.
		t_7 = t_6

		# [H]@Shift6b179c72f0c6dbad -> [H]@Iteratorb0a1def4ad5784ec
		t_7 = torch.roll(t_7, self.shift_direction, 1)

		# Permute to match the output of this subgraph.
		t_7 = torch.permute(t_7, (0, 2, 3, 1, ))

		# No need to crop the output tensor.
		y = t_7

		return y

