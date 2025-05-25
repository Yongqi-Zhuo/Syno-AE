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
        interface_0_out_0x5590ac5ec910 [label="N", shape=none];
        interface_0_out_0x5590ac5ec938 [label="C_out", shape=none];
        interface_0_out_0x5590ac5ec960 [label="H", shape=none];
        interface_0_out_0x5590ac5ec988 [label="H", shape=none];
    }
    {
        rank = same;
        interface_0_out_0x5590ac5ec910;
        interface_0_out_0x5590ac5ec938;
        interface_0_out_0x5590ac5ec960;
        interface_0_out_0x5590ac5ec988;
    }
    // Input 0.
    subgraph cluster_subgraph_0_in_0 {
        label = "";
        interface_0_in_0x5590ac5ec910 [label="N", shape=none];
        interface_0_in_0x5590ac5ec938 [label="C_out", shape=none];
        interface_0_in_0x5590ac5ec960 [label="H", shape=none];
        interface_0_in_0x5590ac5f1650 [label="H", shape=none];
    }
    {
        rank = same;
        interface_0_in_0x5590ac5ec910;
        interface_0_in_0x5590ac5ec938;
        interface_0_in_0x5590ac5ec960;
        interface_0_in_0x5590ac5f1650;
    }
    // Op's.
    op_0x5590ac5f1630 [label="Shift"];
    // Dimension's.
    interface_0_in_0x5590ac5ec910 -> interface_0_out_0x5590ac5ec910 [label="N"];
    interface_0_in_0x5590ac5ec938 -> interface_0_out_0x5590ac5ec938 [label="C_out"];
    interface_0_in_0x5590ac5ec960 -> interface_0_out_0x5590ac5ec960 [label="H"];
    op_0x5590ac5f1630 -> interface_0_out_0x5590ac5ec988 [label="H"];
    interface_0_in_0x5590ac5f1650 -> op_0x5590ac5f1630 [label="H"];
}

// Stage tensor.
subgraph cluster_subgraph_1 {
    label = "Subgraph 1";
    // Reductions.
    reduce_0x7fcec0002ce8 [label="Sum", shape=box];
    // Output.
    subgraph cluster_subgraph_1_out {
        label = "";
        interface_1_out_0x5590ac5ec910 [label="N", shape=none];
        interface_1_out_0x5590ac5ec938 [label="C_out", shape=none];
        interface_1_out_0x5590ac5ec960 [label="H", shape=none];
        interface_1_out_0x5590ac5f1650 [label="H", shape=none];
    }
    {
        rank = same;
        reduce_0x7fcec0002ce8;
        interface_1_out_0x5590ac5ec910;
        interface_1_out_0x5590ac5ec938;
        interface_1_out_0x5590ac5ec960;
        interface_1_out_0x5590ac5f1650;
    }
    // Input 0.
    subgraph cluster_subgraph_1_in_0 {
        label = "";
        interface_1_in_0x5590ac5ec910 [label="N", shape=none];
        interface_1_in_0x5590ac5ec938 [label="C_out", shape=none];
        interface_1_in_0x5590ac5ef450 [label="H", shape=none];
        interface_1_in_0x5590ac5ef468 [label="s", shape=none];
        interface_1_in_0x5590ac5f1650 [label="H", shape=none];
    }
    {
        rank = same;
        interface_1_in_0x5590ac5ec910;
        interface_1_in_0x5590ac5ec938;
        interface_1_in_0x5590ac5ef450;
        interface_1_in_0x5590ac5ef468;
        interface_1_in_0x5590ac5f1650;
    }
    // Op's.
    op_0x5590ac5ee6a0 [label="Split"];
    op_0x5590ac5ef410 [label="Merge"];
    op_0x5590ac5f1660 [label="Shift"];
    // Dimension's.
    interface_1_in_0x5590ac5ec910 -> interface_1_out_0x5590ac5ec910 [label="N"];
    interface_1_in_0x5590ac5ec938 -> interface_1_out_0x5590ac5ec938 [label="C_out"];
    op_0x5590ac5ee6a0 -> interface_1_out_0x5590ac5ec960 [label="H"];
    op_0x5590ac5f1660 -> op_0x5590ac5ee6a0 [label="s*H"];
    interface_1_in_0x5590ac5ef450 -> op_0x5590ac5ef410 [label="H"];
    interface_1_in_0x5590ac5ef468 -> op_0x5590ac5ef410 [label="s"];
    interface_1_in_0x5590ac5f1650 -> interface_1_out_0x5590ac5f1650 [label="H"];
    op_0x5590ac5ef410 -> op_0x5590ac5f1660 [label="s*H"];
    op_0x5590ac5ee6a0 -> reduce_0x7fcec0002ce8 [label="s"];
}

// Stage tensor.
subgraph cluster_subgraph_2 {
    label = "Subgraph 2";
    // Reductions.
    // Output.
    subgraph cluster_subgraph_2_out {
        label = "";
        interface_2_out_0x5590ac5ec910 [label="N", shape=none];
        interface_2_out_0x5590ac5ec938 [label="C_out", shape=none];
        interface_2_out_0x5590ac5ef450 [label="H", shape=none];
        interface_2_out_0x5590ac5ef468 [label="s", shape=none];
        interface_2_out_0x5590ac5f1650 [label="H", shape=none];
    }
    {
        rank = same;
        interface_2_out_0x5590ac5ec910;
        interface_2_out_0x5590ac5ec938;
        interface_2_out_0x5590ac5ef450;
        interface_2_out_0x5590ac5ef468;
        interface_2_out_0x5590ac5f1650;
    }
    // Input 0.
    subgraph cluster_subgraph_2_in_0 {
        label = "";
        interface_2_in_0x5590ac5ec910 [label="N", shape=none];
        interface_2_in_0x5590a8766020 [label="C_out", shape=none];
        interface_2_in_0x5590ac5ef450 [label="H", shape=none];
        interface_2_in_0x5590ac5f1650 [label="H", shape=none];
    }
    // Input 1.
    subgraph cluster_subgraph_2_in_1 {
        label = "";
        interface_2_in_0x5590a8766038 [label="C_out", shape=none];
        interface_2_in_0x5590a8766178 [label="s", shape=none];
    }
    {
        rank = same;
        interface_2_in_0x5590ac5ec910;
        interface_2_in_0x5590a8766020;
        interface_2_in_0x5590ac5ef450;
        interface_2_in_0x5590ac5f1650;
        interface_2_in_0x5590a8766038;
        interface_2_in_0x5590a8766178;
    }
    // Op's.
    op_0x5590a8766000 [label="Share"];
    op_0x5590a8766140 [label="Share"];
    op_0x5590a87ce638 [label="Expand"];
    // Dimension's.
    interface_2_in_0x5590a8766020 -> op_0x5590a8766000 [label="C_out"];
    interface_2_in_0x5590a8766038 -> op_0x5590a8766000 [label="C_out"];
    op_0x5590a87ce638 -> op_0x5590a8766140 [label="s"];
    interface_2_in_0x5590a8766178 -> op_0x5590a8766140 [label="s"];
    interface_2_in_0x5590ac5ec910 -> interface_2_out_0x5590ac5ec910 [label="N"];
    op_0x5590a8766000 -> interface_2_out_0x5590ac5ec938 [label="C_out"];
    interface_2_in_0x5590ac5ef450 -> interface_2_out_0x5590ac5ef450 [label="H"];
    op_0x5590a8766140 -> interface_2_out_0x5590ac5ef468 [label="s"];
    interface_2_in_0x5590ac5f1650 -> interface_2_out_0x5590ac5f1650 [label="H"];
}

// Stage tensor.
subgraph cluster_subgraph_3 {
    label = "Subgraph 3";
    // Reductions.
    reduce_0x7fcec0001a98 [label="Sum", shape=box];
    reduce_0x7fcec0005b48 [label="Sum", shape=box];
    // Output.
    subgraph cluster_subgraph_3_out {
        label = "";
        interface_3_out_0x5590ac5ec910 [label="N", shape=none];
        interface_3_out_0x5590a8766020 [label="C_out", shape=none];
        interface_3_out_0x5590ac5ef450 [label="H", shape=none];
        interface_3_out_0x5590ac5f1650 [label="H", shape=none];
    }
    {
        rank = same;
        reduce_0x7fcec0001a98;
        reduce_0x7fcec0005b48;
        interface_3_out_0x5590ac5ec910;
        interface_3_out_0x5590a8766020;
        interface_3_out_0x5590ac5ef450;
        interface_3_out_0x5590ac5f1650;
    }
    // Input 0.
    subgraph cluster_subgraph_3_in_0 {
        label = "";
        interface_3_in_0x5590ac5ec910 [label="N", shape=none];
        interface_3_in_0x5590a8766250 [label="k_1", shape=none];
        interface_3_in_0x5590ac5ef450 [label="H", shape=none];
        interface_3_in_0x5590a8766200 [label="C_in", shape=none];
        interface_3_in_0x5590ac5f1650 [label="H", shape=none];
    }
    // Input 1.
    subgraph cluster_subgraph_3_in_1 {
        label = "";
        interface_3_in_0x5590a87661c8 [label="C_out", shape=none];
        interface_3_in_0x5590a8766268 [label="k_1", shape=none];
        interface_3_in_0x5590a8766218 [label="C_in", shape=none];
    }
    {
        rank = same;
        interface_3_in_0x5590ac5ec910;
        interface_3_in_0x5590a8766250;
        interface_3_in_0x5590ac5ef450;
        interface_3_in_0x5590a8766200;
        interface_3_in_0x5590ac5f1650;
        interface_3_in_0x5590a87661c8;
        interface_3_in_0x5590a8766268;
        interface_3_in_0x5590a8766218;
    }
    // Op's.
    op_0x5590a8766190 [label="Share"];
    op_0x5590a87661e0 [label="Share"];
    op_0x5590a8766230 [label="Share"];
    op_0x5590a87ce658 [label="Expand"];
    // Dimension's.
    op_0x5590a8766190 -> interface_3_out_0x5590a8766020 [label="C_out"];
    op_0x5590a87ce658 -> op_0x5590a8766190 [label="C_out"];
    interface_3_in_0x5590a87661c8 -> op_0x5590a8766190 [label="C_out"];
    interface_3_in_0x5590a8766200 -> op_0x5590a87661e0 [label="C_in"];
    interface_3_in_0x5590a8766218 -> op_0x5590a87661e0 [label="C_in"];
    interface_3_in_0x5590a8766250 -> op_0x5590a8766230 [label="k_1"];
    interface_3_in_0x5590a8766268 -> op_0x5590a8766230 [label="k_1"];
    interface_3_in_0x5590ac5ec910 -> interface_3_out_0x5590ac5ec910 [label="N"];
    interface_3_in_0x5590ac5ef450 -> interface_3_out_0x5590ac5ef450 [label="H"];
    interface_3_in_0x5590ac5f1650 -> interface_3_out_0x5590ac5f1650 [label="H"];
    op_0x5590a8766230 -> reduce_0x7fcec0001a98 [label="k_1"];
    op_0x5590a87661e0 -> reduce_0x7fcec0005b48 [label="C_in"];
}

// Stage tensor.
subgraph cluster_subgraph_4 {
    label = "Subgraph 4";
    // Reductions.
    // Output.
    subgraph cluster_subgraph_4_out {
        label = "";
        interface_4_out_0x5590ac5ec910 [label="N", shape=none];
        interface_4_out_0x5590a8766250 [label="k_1", shape=none];
        interface_4_out_0x5590ac5ef450 [label="H", shape=none];
        interface_4_out_0x5590a8766200 [label="C_in", shape=none];
        interface_4_out_0x5590ac5f1650 [label="H", shape=none];
    }
    {
        rank = same;
        interface_4_out_0x5590ac5ec910;
        interface_4_out_0x5590a8766250;
        interface_4_out_0x5590ac5ef450;
        interface_4_out_0x5590a8766200;
        interface_4_out_0x5590ac5f1650;
    }
    // Input 0.
    subgraph cluster_subgraph_4_in_0 {
        label = "";
        interface_4_in_0x5590ac5ec910 [label="N", shape=none];
        interface_4_in_0x5590a8766200 [label="C_in", shape=none];
        interface_4_in_0x5590ac5f1650 [label="H", shape=none];
        interface_4_in_0x5590ac5e92a8 [label="H", shape=none];
    }
    {
        rank = same;
        interface_4_in_0x5590ac5ec910;
        interface_4_in_0x5590a8766200;
        interface_4_in_0x5590ac5f1650;
        interface_4_in_0x5590ac5e92a8;
    }
    // Op's.
    op_0x5590ac5e9280 [label="Unfold"];
    // Dimension's.
    interface_4_in_0x5590a8766200 -> interface_4_out_0x5590a8766200 [label="C_in"];
    op_0x5590ac5e9280 -> interface_4_out_0x5590a8766250 [label="k_1"];
    interface_4_in_0x5590ac5e92a8 -> op_0x5590ac5e9280 [label="H"];
    interface_4_in_0x5590ac5ec910 -> interface_4_out_0x5590ac5ec910 [label="N"];
    op_0x5590ac5e9280 -> interface_4_out_0x5590ac5ef450 [label="H"];
    interface_4_in_0x5590ac5f1650 -> interface_4_out_0x5590ac5f1650 [label="H"];
}

// Input tensor.
subgraph cluster_subgraph_5 {
    label = "Input 0";
    interface_5_out_0x5590ac5ec910 [label="N", shape=none];
    interface_5_out_0x5590a8766200 [label="C_in", shape=none];
    interface_5_out_0x5590ac5f1650 [label="H", shape=none];
    interface_5_out_0x5590ac5e92a8 [label="H", shape=none];
}

interface_5_out_0x5590ac5ec910 -> interface_4_in_0x5590ac5ec910;
interface_5_out_0x5590a8766200 -> interface_4_in_0x5590a8766200;
interface_5_out_0x5590ac5f1650 -> interface_4_in_0x5590ac5f1650;
interface_5_out_0x5590ac5e92a8 -> interface_4_in_0x5590ac5e92a8;

interface_4_out_0x5590ac5ec910 -> interface_3_in_0x5590ac5ec910;
interface_4_out_0x5590a8766250 -> interface_3_in_0x5590a8766250;
interface_4_out_0x5590ac5ef450 -> interface_3_in_0x5590ac5ef450;
interface_4_out_0x5590a8766200 -> interface_3_in_0x5590a8766200;
interface_4_out_0x5590ac5f1650 -> interface_3_in_0x5590ac5f1650;

// Input tensor.
subgraph cluster_subgraph_6 {
    label = "Input 2";
    interface_6_out_0x5590a87661c8 [label="C_out", shape=none];
    interface_6_out_0x5590a8766268 [label="k_1", shape=none];
    interface_6_out_0x5590a8766218 [label="C_in", shape=none];
}

interface_6_out_0x5590a87661c8 -> interface_3_in_0x5590a87661c8;
interface_6_out_0x5590a8766268 -> interface_3_in_0x5590a8766268;
interface_6_out_0x5590a8766218 -> interface_3_in_0x5590a8766218;

interface_3_out_0x5590ac5ec910 -> interface_2_in_0x5590ac5ec910;
interface_3_out_0x5590a8766020 -> interface_2_in_0x5590a8766020;
interface_3_out_0x5590ac5ef450 -> interface_2_in_0x5590ac5ef450;
interface_3_out_0x5590ac5f1650 -> interface_2_in_0x5590ac5f1650;

// Input tensor.
subgraph cluster_subgraph_7 {
    label = "Input 1";
    interface_7_out_0x5590a8766038 [label="C_out", shape=none];
    interface_7_out_0x5590a8766178 [label="s", shape=none];
}

interface_7_out_0x5590a8766038 -> interface_2_in_0x5590a8766038;
interface_7_out_0x5590a8766178 -> interface_2_in_0x5590a8766178;

interface_2_out_0x5590ac5ec910 -> interface_1_in_0x5590ac5ec910;
interface_2_out_0x5590ac5ec938 -> interface_1_in_0x5590ac5ec938;
interface_2_out_0x5590ac5ef450 -> interface_1_in_0x5590ac5ef450;
interface_2_out_0x5590ac5ef468 -> interface_1_in_0x5590ac5ef468;
interface_2_out_0x5590ac5f1650 -> interface_1_in_0x5590ac5f1650;

interface_1_out_0x5590ac5ec910 -> interface_0_in_0x5590ac5ec910;
interface_1_out_0x5590ac5ec938 -> interface_0_in_0x5590ac5ec938;
interface_1_out_0x5590ac5ec960 -> interface_0_in_0x5590ac5ec960;
interface_1_out_0x5590ac5f1650 -> interface_0_in_0x5590ac5f1650;

{
    rank = same;
    interface_5_out_0x5590ac5ec910;
    interface_5_out_0x5590a8766200;
    interface_5_out_0x5590ac5f1650;
    interface_5_out_0x5590ac5e92a8;
    interface_7_out_0x5590a8766038;
    interface_7_out_0x5590a8766178;
    interface_6_out_0x5590a87661c8;
    interface_6_out_0x5590a8766268;
    interface_6_out_0x5590a8766218;
}
subgraph cluster_subgraph_output {
    label = "Output";
    interface_8_in_0x5590ac5ec910 [label="N", shape=none];
    interface_8_in_0x5590ac5ec938 [label="C_out", shape=none];
    interface_8_in_0x5590ac5ec960 [label="H", shape=none];
    interface_8_in_0x5590ac5ec988 [label="H", shape=none];
}
interface_0_out_0x5590ac5ec910 -> interface_8_in_0x5590ac5ec910;
interface_0_out_0x5590ac5ec938 -> interface_8_in_0x5590ac5ec938;
interface_0_out_0x5590ac5ec960 -> interface_8_in_0x5590ac5ec960;
interface_0_out_0x5590ac5ec988 -> interface_8_in_0x5590ac5ec988;

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
		t_3 = torch.einsum("kilj -> kjil", in_0)

		# [H]@Unfold9ee82d943ec7d29d -> [H]@Merge5f50103ea583163b, [k_1]@Shared4e0659d169008e4
		t_3 = torch.reshape(t_3, (1024, 1, 56, 3584, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (1024, 3, 56, 64, 56, ))

		# Perform contraction.
		t_4 = torch.einsum("lkmjn, ikj -> limn", t_3, in_2)

		# Perform contraction.
		t_5 = torch.einsum("kilm, ij -> kiljm", t_4, in_1)

		# No contraction needed.
		t_6 = t_5

		# [H]@Merge5f50103ea583163b, [s]@Merge5f50103ea5831638 -> [s*H]@Shift3c9c8e9d3c84cb9b
		t_6 = torch.reshape(t_6, (1024, 64, 112, 56, ))

		# [s*H]@Shift3c9c8e9d3c84cb9b -> [s*H]@Splitdb1af055f999951a
		t_6 = torch.roll(t_6, self.shift_direction, 2)

		# [s*H]@Splitdb1af055f999951a -> [H]@Iterator96123ba3184da39c, [s]@Reduced95c644a3c072d9a
		t_6 = torch.reshape(t_6, (1024, 64, 56, 2, 56, ))

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
		t_3 = torch.einsum("kilj -> kjil", in_0)

		# [H]@Unfold9ee82d943ec7d29d -> [H]@Merge5f50103ea583163b, [k_1]@Shared4e0659d169008e4
		t_3 = torch.reshape(t_3, (1024, 1, 28, 1792, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (1024, 3, 28, 64, 28, ))

		# Perform contraction.
		t_4 = torch.einsum("lkmjn, ikj -> limn", t_3, in_2)

		# Perform contraction.
		t_5 = torch.einsum("kilm, ij -> kiljm", t_4, in_1)

		# No contraction needed.
		t_6 = t_5

		# [H]@Merge5f50103ea583163b, [s]@Merge5f50103ea5831638 -> [s*H]@Shift3c9c8e9d3c84cb9b
		t_6 = torch.reshape(t_6, (1024, 128, 56, 28, ))

		# [s*H]@Shift3c9c8e9d3c84cb9b -> [s*H]@Splitdb1af055f999951a
		t_6 = torch.roll(t_6, self.shift_direction, 2)

		# [s*H]@Splitdb1af055f999951a -> [H]@Iterator96123ba3184da39c, [s]@Reduced95c644a3c072d9a
		t_6 = torch.reshape(t_6, (1024, 128, 28, 2, 28, ))

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
		t_3 = torch.einsum("kilj -> kjil", in_0)

		# [H]@Unfold9ee82d943ec7d29d -> [H]@Merge5f50103ea583163b, [k_1]@Shared4e0659d169008e4
		t_3 = torch.reshape(t_3, (1024, 1, 28, 3584, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (1024, 3, 28, 128, 28, ))

		# Perform contraction.
		t_4 = torch.einsum("lkmjn, ikj -> limn", t_3, in_2)

		# Perform contraction.
		t_5 = torch.einsum("kilm, ij -> kiljm", t_4, in_1)

		# No contraction needed.
		t_6 = t_5

		# [H]@Merge5f50103ea583163b, [s]@Merge5f50103ea5831638 -> [s*H]@Shift3c9c8e9d3c84cb9b
		t_6 = torch.reshape(t_6, (1024, 128, 56, 28, ))

		# [s*H]@Shift3c9c8e9d3c84cb9b -> [s*H]@Splitdb1af055f999951a
		t_6 = torch.roll(t_6, self.shift_direction, 2)

		# [s*H]@Splitdb1af055f999951a -> [H]@Iterator96123ba3184da39c, [s]@Reduced95c644a3c072d9a
		t_6 = torch.reshape(t_6, (1024, 128, 28, 2, 28, ))

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
		t_3 = torch.einsum("kilj -> kjil", in_0)

		# [H]@Unfold9ee82d943ec7d29d -> [H]@Merge5f50103ea583163b, [k_1]@Shared4e0659d169008e4
		t_3 = torch.reshape(t_3, (1024, 1, 14, 1792, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (1024, 3, 14, 128, 14, ))

		# Perform contraction.
		t_4 = torch.einsum("lkmjn, ikj -> limn", t_3, in_2)

		# Perform contraction.
		t_5 = torch.einsum("kilm, ij -> kiljm", t_4, in_1)

		# No contraction needed.
		t_6 = t_5

		# [H]@Merge5f50103ea583163b, [s]@Merge5f50103ea5831638 -> [s*H]@Shift3c9c8e9d3c84cb9b
		t_6 = torch.reshape(t_6, (1024, 256, 28, 14, ))

		# [s*H]@Shift3c9c8e9d3c84cb9b -> [s*H]@Splitdb1af055f999951a
		t_6 = torch.roll(t_6, self.shift_direction, 2)

		# [s*H]@Splitdb1af055f999951a -> [H]@Iterator96123ba3184da39c, [s]@Reduced95c644a3c072d9a
		t_6 = torch.reshape(t_6, (1024, 256, 14, 2, 14, ))

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
		t_3 = torch.einsum("kilj -> kjil", in_0)

		# [H]@Unfold9ee82d943ec7d29d -> [H]@Merge5f50103ea583163b, [k_1]@Shared4e0659d169008e4
		t_3 = torch.reshape(t_3, (1024, 1, 14, 3584, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (1024, 3, 14, 256, 14, ))

		# Perform contraction.
		t_4 = torch.einsum("lkmjn, ikj -> limn", t_3, in_2)

		# Perform contraction.
		t_5 = torch.einsum("kilm, ij -> kiljm", t_4, in_1)

		# No contraction needed.
		t_6 = t_5

		# [H]@Merge5f50103ea583163b, [s]@Merge5f50103ea5831638 -> [s*H]@Shift3c9c8e9d3c84cb9b
		t_6 = torch.reshape(t_6, (1024, 256, 28, 14, ))

		# [s*H]@Shift3c9c8e9d3c84cb9b -> [s*H]@Splitdb1af055f999951a
		t_6 = torch.roll(t_6, self.shift_direction, 2)

		# [s*H]@Splitdb1af055f999951a -> [H]@Iterator96123ba3184da39c, [s]@Reduced95c644a3c072d9a
		t_6 = torch.reshape(t_6, (1024, 256, 14, 2, 14, ))

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
		t_3 = torch.einsum("kilj -> kjil", in_0)

		# [H]@Unfold9ee82d943ec7d29d -> [H]@Merge5f50103ea583163b, [k_1]@Shared4e0659d169008e4
		t_3 = torch.reshape(t_3, (1024, 1, 7, 1792, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (1024, 3, 7, 256, 7, ))

		# Perform contraction.
		t_4 = torch.einsum("lkmjn, ikj -> limn", t_3, in_2)

		# Perform contraction.
		t_5 = torch.einsum("kilm, ij -> kiljm", t_4, in_1)

		# No contraction needed.
		t_6 = t_5

		# [H]@Merge5f50103ea583163b, [s]@Merge5f50103ea5831638 -> [s*H]@Shift3c9c8e9d3c84cb9b
		t_6 = torch.reshape(t_6, (1024, 512, 14, 7, ))

		# [s*H]@Shift3c9c8e9d3c84cb9b -> [s*H]@Splitdb1af055f999951a
		t_6 = torch.roll(t_6, self.shift_direction, 2)

		# [s*H]@Splitdb1af055f999951a -> [H]@Iterator96123ba3184da39c, [s]@Reduced95c644a3c072d9a
		t_6 = torch.reshape(t_6, (1024, 512, 7, 2, 7, ))

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
		t_3 = torch.einsum("kilj -> kjil", in_0)

		# [H]@Unfold9ee82d943ec7d29d -> [H]@Merge5f50103ea583163b, [k_1]@Shared4e0659d169008e4
		t_3 = torch.reshape(t_3, (1024, 1, 7, 3584, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (1024, 3, 7, 512, 7, ))

		# Perform contraction.
		t_4 = torch.einsum("lkmjn, ikj -> limn", t_3, in_2)

		# Perform contraction.
		t_5 = torch.einsum("kilm, ij -> kiljm", t_4, in_1)

		# No contraction needed.
		t_6 = t_5

		# [H]@Merge5f50103ea583163b, [s]@Merge5f50103ea5831638 -> [s*H]@Shift3c9c8e9d3c84cb9b
		t_6 = torch.reshape(t_6, (1024, 512, 14, 7, ))

		# [s*H]@Shift3c9c8e9d3c84cb9b -> [s*H]@Splitdb1af055f999951a
		t_6 = torch.roll(t_6, self.shift_direction, 2)

		# [s*H]@Splitdb1af055f999951a -> [H]@Iterator96123ba3184da39c, [s]@Reduced95c644a3c072d9a
		t_6 = torch.reshape(t_6, (1024, 512, 7, 2, 7, ))

		# [s]@Reduce
		t_6 = torch.sum(t_6, dim=(3, ))

		# No contraction needed.
		t_7 = t_6

		# [H]@Shift6b179c72f0c6dbad -> [H]@Iteratorb0a1def4ad5784ec
		t_7 = torch.roll(t_7, self.shift_direction, 3)

		# No need to crop the output tensor.
		y = t_7

		return y

