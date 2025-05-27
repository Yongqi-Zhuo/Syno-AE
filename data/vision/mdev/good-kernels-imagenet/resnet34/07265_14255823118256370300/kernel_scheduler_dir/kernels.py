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
        interface_0_out_0x5590c9c880c0 [label="N", shape=none];
        interface_0_out_0x5590c9c880e8 [label="C_out", shape=none];
        interface_0_out_0x5590c9c88110 [label="H", shape=none];
        interface_0_out_0x5590c9c88138 [label="H", shape=none];
    }
    {
        rank = same;
        interface_0_out_0x5590c9c880c0;
        interface_0_out_0x5590c9c880e8;
        interface_0_out_0x5590c9c88110;
        interface_0_out_0x5590c9c88138;
    }
    // Input 0.
    subgraph cluster_subgraph_0_in_0 {
        label = "";
        interface_0_in_0x5590c9c880c0 [label="N", shape=none];
        interface_0_in_0x5590c9c880e8 [label="C_out", shape=none];
        interface_0_in_0x5590c9c88110 [label="H", shape=none];
        interface_0_in_0x5590da8a9490 [label="H", shape=none];
    }
    {
        rank = same;
        interface_0_in_0x5590c9c880c0;
        interface_0_in_0x5590c9c880e8;
        interface_0_in_0x5590c9c88110;
        interface_0_in_0x5590da8a9490;
    }
    // Op's.
    op_0x5590da8a9470 [label="Shift"];
    // Dimension's.
    interface_0_in_0x5590c9c880c0 -> interface_0_out_0x5590c9c880c0 [label="N"];
    interface_0_in_0x5590c9c880e8 -> interface_0_out_0x5590c9c880e8 [label="C_out"];
    interface_0_in_0x5590c9c88110 -> interface_0_out_0x5590c9c88110 [label="H"];
    op_0x5590da8a9470 -> interface_0_out_0x5590c9c88138 [label="H"];
    interface_0_in_0x5590da8a9490 -> op_0x5590da8a9470 [label="H"];
}

// Stage tensor.
subgraph cluster_subgraph_1 {
    label = "Subgraph 1";
    // Reductions.
    reduce_0x7f51b0002ce8 [label="Sum", shape=box];
    // Output.
    subgraph cluster_subgraph_1_out {
        label = "";
        interface_1_out_0x5590c9c880c0 [label="N", shape=none];
        interface_1_out_0x5590c9c880e8 [label="C_out", shape=none];
        interface_1_out_0x5590c9c88110 [label="H", shape=none];
        interface_1_out_0x5590da8a9490 [label="H", shape=none];
    }
    {
        rank = same;
        reduce_0x7f51b0002ce8;
        interface_1_out_0x5590c9c880c0;
        interface_1_out_0x5590c9c880e8;
        interface_1_out_0x5590c9c88110;
        interface_1_out_0x5590da8a9490;
    }
    // Input 0.
    subgraph cluster_subgraph_1_in_0 {
        label = "";
        interface_1_in_0x5590c9c880c0 [label="N", shape=none];
        interface_1_in_0x5590c9c880e8 [label="C_out", shape=none];
        interface_1_in_0x5590da8ae4c0 [label="H", shape=none];
        interface_1_in_0x5590da8ae4d8 [label="s", shape=none];
        interface_1_in_0x5590da8a9490 [label="H", shape=none];
    }
    {
        rank = same;
        interface_1_in_0x5590c9c880c0;
        interface_1_in_0x5590c9c880e8;
        interface_1_in_0x5590da8ae4c0;
        interface_1_in_0x5590da8ae4d8;
        interface_1_in_0x5590da8a9490;
    }
    // Op's.
    op_0x5590da8a94d0 [label="Shift"];
    op_0x5590da8a9c20 [label="Split"];
    op_0x5590da8ae480 [label="Merge"];
    // Dimension's.
    interface_1_in_0x5590c9c880c0 -> interface_1_out_0x5590c9c880c0 [label="N"];
    interface_1_in_0x5590c9c880e8 -> interface_1_out_0x5590c9c880e8 [label="C_out"];
    op_0x5590da8a9c20 -> interface_1_out_0x5590c9c88110 [label="H"];
    interface_1_in_0x5590da8a9490 -> interface_1_out_0x5590da8a9490 [label="H"];
    op_0x5590da8ae480 -> op_0x5590da8a94d0 [label="s*H"];
    op_0x5590da8a94d0 -> op_0x5590da8a9c20 [label="s*H"];
    interface_1_in_0x5590da8ae4c0 -> op_0x5590da8ae480 [label="H"];
    interface_1_in_0x5590da8ae4d8 -> op_0x5590da8ae480 [label="s"];
    op_0x5590da8a9c20 -> reduce_0x7f51b0002ce8 [label="s"];
}

// Stage tensor.
subgraph cluster_subgraph_2 {
    label = "Subgraph 2";
    // Reductions.
    // Output.
    subgraph cluster_subgraph_2_out {
        label = "";
        interface_2_out_0x5590c9c880c0 [label="N", shape=none];
        interface_2_out_0x5590c9c880e8 [label="C_out", shape=none];
        interface_2_out_0x5590da8ae4c0 [label="H", shape=none];
        interface_2_out_0x5590da8ae4d8 [label="s", shape=none];
        interface_2_out_0x5590da8a9490 [label="H", shape=none];
    }
    {
        rank = same;
        interface_2_out_0x5590c9c880c0;
        interface_2_out_0x5590c9c880e8;
        interface_2_out_0x5590da8ae4c0;
        interface_2_out_0x5590da8ae4d8;
        interface_2_out_0x5590da8a9490;
    }
    // Input 0.
    subgraph cluster_subgraph_2_in_0 {
        label = "";
        interface_2_in_0x5590c9c880c0 [label="N", shape=none];
        interface_2_in_0x5590da8a74a0 [label="C_out", shape=none];
        interface_2_in_0x5590da8ae4c0 [label="H", shape=none];
        interface_2_in_0x5590da8a9490 [label="H", shape=none];
    }
    // Input 1.
    subgraph cluster_subgraph_2_in_1 {
        label = "";
        interface_2_in_0x5590da8a74b8 [label="C_out", shape=none];
        interface_2_in_0x5590da8a7648 [label="s", shape=none];
    }
    {
        rank = same;
        interface_2_in_0x5590c9c880c0;
        interface_2_in_0x5590da8a74a0;
        interface_2_in_0x5590da8ae4c0;
        interface_2_in_0x5590da8a9490;
        interface_2_in_0x5590da8a74b8;
        interface_2_in_0x5590da8a7648;
    }
    // Op's.
    op_0x5590da8a7480 [label="Share"];
    op_0x5590da8a7610 [label="Share"];
    op_0x5590da8a7a78 [label="Expand"];
    // Dimension's.
    interface_2_in_0x5590c9c880c0 -> interface_2_out_0x5590c9c880c0 [label="N"];
    op_0x5590da8a7480 -> interface_2_out_0x5590c9c880e8 [label="C_out"];
    interface_2_in_0x5590da8a74a0 -> op_0x5590da8a7480 [label="C_out"];
    interface_2_in_0x5590da8a74b8 -> op_0x5590da8a7480 [label="C_out"];
    op_0x5590da8a7a78 -> op_0x5590da8a7610 [label="s"];
    interface_2_in_0x5590da8a7648 -> op_0x5590da8a7610 [label="s"];
    interface_2_in_0x5590da8a9490 -> interface_2_out_0x5590da8a9490 [label="H"];
    interface_2_in_0x5590da8ae4c0 -> interface_2_out_0x5590da8ae4c0 [label="H"];
    op_0x5590da8a7610 -> interface_2_out_0x5590da8ae4d8 [label="s"];
}

// Stage tensor.
subgraph cluster_subgraph_3 {
    label = "Subgraph 3";
    // Reductions.
    reduce_0x7f51b0001a98 [label="Sum", shape=box];
    reduce_0x7f51b0005a48 [label="Sum", shape=box];
    // Output.
    subgraph cluster_subgraph_3_out {
        label = "";
        interface_3_out_0x5590c9c880c0 [label="N", shape=none];
        interface_3_out_0x5590da8a74a0 [label="C_out", shape=none];
        interface_3_out_0x5590da8ae4c0 [label="H", shape=none];
        interface_3_out_0x5590da8a9490 [label="H", shape=none];
    }
    {
        rank = same;
        reduce_0x7f51b0001a98;
        reduce_0x7f51b0005a48;
        interface_3_out_0x5590c9c880c0;
        interface_3_out_0x5590da8a74a0;
        interface_3_out_0x5590da8ae4c0;
        interface_3_out_0x5590da8a9490;
    }
    // Input 0.
    subgraph cluster_subgraph_3_in_0 {
        label = "";
        interface_3_in_0x5590c9c880c0 [label="N", shape=none];
        interface_3_in_0x5590da8a7720 [label="k_1", shape=none];
        interface_3_in_0x5590da8ae4c0 [label="H", shape=none];
        interface_3_in_0x5590da8a76d0 [label="C_in", shape=none];
        interface_3_in_0x5590da8a9490 [label="H", shape=none];
    }
    // Input 1.
    subgraph cluster_subgraph_3_in_1 {
        label = "";
        interface_3_in_0x5590da8a7698 [label="C_out", shape=none];
        interface_3_in_0x5590da8a7738 [label="k_1", shape=none];
        interface_3_in_0x5590da8a76e8 [label="C_in", shape=none];
    }
    {
        rank = same;
        interface_3_in_0x5590c9c880c0;
        interface_3_in_0x5590da8a7720;
        interface_3_in_0x5590da8ae4c0;
        interface_3_in_0x5590da8a76d0;
        interface_3_in_0x5590da8a9490;
        interface_3_in_0x5590da8a7698;
        interface_3_in_0x5590da8a7738;
        interface_3_in_0x5590da8a76e8;
    }
    // Op's.
    op_0x5590da8a7660 [label="Share"];
    op_0x5590da8a76b0 [label="Share"];
    op_0x5590da8a7700 [label="Share"];
    op_0x5590da8a7a98 [label="Expand"];
    // Dimension's.
    interface_3_in_0x5590c9c880c0 -> interface_3_out_0x5590c9c880c0 [label="N"];
    op_0x5590da8a7660 -> interface_3_out_0x5590da8a74a0 [label="C_out"];
    op_0x5590da8a7a98 -> op_0x5590da8a7660 [label="C_out"];
    interface_3_in_0x5590da8a7698 -> op_0x5590da8a7660 [label="C_out"];
    interface_3_in_0x5590da8a76d0 -> op_0x5590da8a76b0 [label="C_in"];
    interface_3_in_0x5590da8a76e8 -> op_0x5590da8a76b0 [label="C_in"];
    interface_3_in_0x5590da8a7720 -> op_0x5590da8a7700 [label="k_1"];
    interface_3_in_0x5590da8a7738 -> op_0x5590da8a7700 [label="k_1"];
    interface_3_in_0x5590da8a9490 -> interface_3_out_0x5590da8a9490 [label="H"];
    interface_3_in_0x5590da8ae4c0 -> interface_3_out_0x5590da8ae4c0 [label="H"];
    op_0x5590da8a7700 -> reduce_0x7f51b0001a98 [label="k_1"];
    op_0x5590da8a76b0 -> reduce_0x7f51b0005a48 [label="C_in"];
}

// Stage tensor.
subgraph cluster_subgraph_4 {
    label = "Subgraph 4";
    // Reductions.
    // Output.
    subgraph cluster_subgraph_4_out {
        label = "";
        interface_4_out_0x5590c9c880c0 [label="N", shape=none];
        interface_4_out_0x5590da8a7720 [label="k_1", shape=none];
        interface_4_out_0x5590da8ae4c0 [label="H", shape=none];
        interface_4_out_0x5590da8a76d0 [label="C_in", shape=none];
        interface_4_out_0x5590da8a9490 [label="H", shape=none];
    }
    {
        rank = same;
        interface_4_out_0x5590c9c880c0;
        interface_4_out_0x5590da8a7720;
        interface_4_out_0x5590da8ae4c0;
        interface_4_out_0x5590da8a76d0;
        interface_4_out_0x5590da8a9490;
    }
    // Input 0.
    subgraph cluster_subgraph_4_in_0 {
        label = "";
        interface_4_in_0x5590c9c880c0 [label="N", shape=none];
        interface_4_in_0x5590da8a76d0 [label="C_in", shape=none];
        interface_4_in_0x5590da8a9490 [label="H", shape=none];
        interface_4_in_0x5590da8bf0a8 [label="H", shape=none];
    }
    {
        rank = same;
        interface_4_in_0x5590c9c880c0;
        interface_4_in_0x5590da8a76d0;
        interface_4_in_0x5590da8a9490;
        interface_4_in_0x5590da8bf0a8;
    }
    // Op's.
    op_0x5590da8bf080 [label="Unfold"];
    // Dimension's.
    interface_4_in_0x5590c9c880c0 -> interface_4_out_0x5590c9c880c0 [label="N"];
    interface_4_in_0x5590da8a76d0 -> interface_4_out_0x5590da8a76d0 [label="C_in"];
    op_0x5590da8bf080 -> interface_4_out_0x5590da8a7720 [label="k_1"];
    interface_4_in_0x5590da8a9490 -> interface_4_out_0x5590da8a9490 [label="H"];
    op_0x5590da8bf080 -> interface_4_out_0x5590da8ae4c0 [label="H"];
    interface_4_in_0x5590da8bf0a8 -> op_0x5590da8bf080 [label="H"];
}

// Input tensor.
subgraph cluster_subgraph_5 {
    label = "Input 0";
    interface_5_out_0x5590c9c880c0 [label="N", shape=none];
    interface_5_out_0x5590da8a76d0 [label="C_in", shape=none];
    interface_5_out_0x5590da8a9490 [label="H", shape=none];
    interface_5_out_0x5590da8bf0a8 [label="H", shape=none];
}

interface_5_out_0x5590c9c880c0 -> interface_4_in_0x5590c9c880c0;
interface_5_out_0x5590da8a76d0 -> interface_4_in_0x5590da8a76d0;
interface_5_out_0x5590da8a9490 -> interface_4_in_0x5590da8a9490;
interface_5_out_0x5590da8bf0a8 -> interface_4_in_0x5590da8bf0a8;

interface_4_out_0x5590c9c880c0 -> interface_3_in_0x5590c9c880c0;
interface_4_out_0x5590da8a7720 -> interface_3_in_0x5590da8a7720;
interface_4_out_0x5590da8ae4c0 -> interface_3_in_0x5590da8ae4c0;
interface_4_out_0x5590da8a76d0 -> interface_3_in_0x5590da8a76d0;
interface_4_out_0x5590da8a9490 -> interface_3_in_0x5590da8a9490;

// Input tensor.
subgraph cluster_subgraph_6 {
    label = "Input 2";
    interface_6_out_0x5590da8a7698 [label="C_out", shape=none];
    interface_6_out_0x5590da8a7738 [label="k_1", shape=none];
    interface_6_out_0x5590da8a76e8 [label="C_in", shape=none];
}

interface_6_out_0x5590da8a7698 -> interface_3_in_0x5590da8a7698;
interface_6_out_0x5590da8a7738 -> interface_3_in_0x5590da8a7738;
interface_6_out_0x5590da8a76e8 -> interface_3_in_0x5590da8a76e8;

interface_3_out_0x5590c9c880c0 -> interface_2_in_0x5590c9c880c0;
interface_3_out_0x5590da8a74a0 -> interface_2_in_0x5590da8a74a0;
interface_3_out_0x5590da8ae4c0 -> interface_2_in_0x5590da8ae4c0;
interface_3_out_0x5590da8a9490 -> interface_2_in_0x5590da8a9490;

// Input tensor.
subgraph cluster_subgraph_7 {
    label = "Input 1";
    interface_7_out_0x5590da8a74b8 [label="C_out", shape=none];
    interface_7_out_0x5590da8a7648 [label="s", shape=none];
}

interface_7_out_0x5590da8a74b8 -> interface_2_in_0x5590da8a74b8;
interface_7_out_0x5590da8a7648 -> interface_2_in_0x5590da8a7648;

interface_2_out_0x5590c9c880c0 -> interface_1_in_0x5590c9c880c0;
interface_2_out_0x5590c9c880e8 -> interface_1_in_0x5590c9c880e8;
interface_2_out_0x5590da8ae4c0 -> interface_1_in_0x5590da8ae4c0;
interface_2_out_0x5590da8ae4d8 -> interface_1_in_0x5590da8ae4d8;
interface_2_out_0x5590da8a9490 -> interface_1_in_0x5590da8a9490;

interface_1_out_0x5590c9c880c0 -> interface_0_in_0x5590c9c880c0;
interface_1_out_0x5590c9c880e8 -> interface_0_in_0x5590c9c880e8;
interface_1_out_0x5590c9c88110 -> interface_0_in_0x5590c9c88110;
interface_1_out_0x5590da8a9490 -> interface_0_in_0x5590da8a9490;

{
    rank = same;
    interface_5_out_0x5590c9c880c0;
    interface_5_out_0x5590da8a76d0;
    interface_5_out_0x5590da8a9490;
    interface_5_out_0x5590da8bf0a8;
    interface_7_out_0x5590da8a74b8;
    interface_7_out_0x5590da8a7648;
    interface_6_out_0x5590da8a7698;
    interface_6_out_0x5590da8a7738;
    interface_6_out_0x5590da8a76e8;
}
subgraph cluster_subgraph_output {
    label = "Output";
    interface_8_in_0x5590c9c880c0 [label="N", shape=none];
    interface_8_in_0x5590c9c880e8 [label="C_out", shape=none];
    interface_8_in_0x5590c9c88110 [label="H", shape=none];
    interface_8_in_0x5590c9c88138 [label="H", shape=none];
}
interface_0_out_0x5590c9c880c0 -> interface_8_in_0x5590c9c880c0;
interface_0_out_0x5590c9c880e8 -> interface_8_in_0x5590c9c880e8;
interface_0_out_0x5590c9c88110 -> interface_8_in_0x5590c9c88110;
interface_0_out_0x5590c9c88138 -> interface_8_in_0x5590c9c88138;

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

