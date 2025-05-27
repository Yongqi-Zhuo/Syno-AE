import torch
import random
"""
digraph kernel_preview {
newrank = true;

// Stage tensor.
subgraph cluster_subgraph_0 {
    label = "Subgraph 0";
    // Reductions.
    reduce_0x7f7a20004ce8 [label="Sum", shape=box];
    // Output.
    subgraph cluster_subgraph_0_out {
        label = "";
        interface_0_out_0x5605b0775920 [label="N", shape=none];
        interface_0_out_0x5605b0775948 [label="C_out", shape=none];
        interface_0_out_0x5605b0775970 [label="H", shape=none];
        interface_0_out_0x5605b0775998 [label="H", shape=none];
    }
    {
        rank = same;
        reduce_0x7f7a20004ce8;
        interface_0_out_0x5605b0775920;
        interface_0_out_0x5605b0775948;
        interface_0_out_0x5605b0775970;
        interface_0_out_0x5605b0775998;
    }
    // Input 0.
    subgraph cluster_subgraph_0_in_0 {
        label = "";
        interface_0_in_0x5605b0775920 [label="N", shape=none];
        interface_0_in_0x5605b0775948 [label="C_out", shape=none];
        interface_0_in_0x5605beb89790 [label="H", shape=none];
        interface_0_in_0x5605beb8abd8 [label="s", shape=none];
        interface_0_in_0x5605b0775998 [label="H", shape=none];
    }
    {
        rank = same;
        interface_0_in_0x5605b0775920;
        interface_0_in_0x5605b0775948;
        interface_0_in_0x5605beb89790;
        interface_0_in_0x5605beb8abd8;
        interface_0_in_0x5605b0775998;
    }
    // Op's.
    op_0x5605beb89590 [label="Shift"];
    op_0x5605beb89770 [label="Shift"];
    op_0x5605beb89c20 [label="Split"];
    op_0x5605beb8ab80 [label="Merge"];
    // Dimension's.
    interface_0_in_0x5605b0775920 -> interface_0_out_0x5605b0775920 [label="N"];
    interface_0_in_0x5605b0775948 -> interface_0_out_0x5605b0775948 [label="C_out"];
    op_0x5605beb89c20 -> interface_0_out_0x5605b0775970 [label="H"];
    interface_0_in_0x5605b0775998 -> interface_0_out_0x5605b0775998 [label="H"];
    op_0x5605beb8ab80 -> op_0x5605beb89590 [label="s*H"];
    interface_0_in_0x5605beb89790 -> op_0x5605beb89770 [label="H"];
    op_0x5605beb89590 -> op_0x5605beb89c20 [label="s*H"];
    op_0x5605beb89770 -> op_0x5605beb8ab80 [label="H"];
    interface_0_in_0x5605beb8abd8 -> op_0x5605beb8ab80 [label="s"];
    op_0x5605beb89c20 -> reduce_0x7f7a20004ce8 [label="s"];
}

// Stage tensor.
subgraph cluster_subgraph_1 {
    label = "Subgraph 1";
    // Reductions.
    // Output.
    subgraph cluster_subgraph_1_out {
        label = "";
        interface_1_out_0x5605b0775920 [label="N", shape=none];
        interface_1_out_0x5605b0775948 [label="C_out", shape=none];
        interface_1_out_0x5605beb89790 [label="H", shape=none];
        interface_1_out_0x5605beb8abd8 [label="s", shape=none];
        interface_1_out_0x5605b0775998 [label="H", shape=none];
    }
    {
        rank = same;
        interface_1_out_0x5605b0775920;
        interface_1_out_0x5605b0775948;
        interface_1_out_0x5605beb89790;
        interface_1_out_0x5605beb8abd8;
        interface_1_out_0x5605b0775998;
    }
    // Input 0.
    subgraph cluster_subgraph_1_in_0 {
        label = "";
        interface_1_in_0x5605b0775920 [label="N", shape=none];
        interface_1_in_0x5605beb88820 [label="C_out", shape=none];
        interface_1_in_0x5605beb89790 [label="H", shape=none];
        interface_1_in_0x5605b0775998 [label="H", shape=none];
    }
    // Input 1.
    subgraph cluster_subgraph_1_in_1 {
        label = "";
        interface_1_in_0x5605beb88838 [label="C_out", shape=none];
        interface_1_in_0x5605beb889c8 [label="s", shape=none];
    }
    {
        rank = same;
        interface_1_in_0x5605b0775920;
        interface_1_in_0x5605beb88820;
        interface_1_in_0x5605beb89790;
        interface_1_in_0x5605b0775998;
        interface_1_in_0x5605beb88838;
        interface_1_in_0x5605beb889c8;
    }
    // Op's.
    op_0x5605beb88800 [label="Share"];
    op_0x5605beb88990 [label="Share"];
    op_0x5605beb88d18 [label="Expand"];
    // Dimension's.
    interface_1_in_0x5605b0775920 -> interface_1_out_0x5605b0775920 [label="N"];
    op_0x5605beb88800 -> interface_1_out_0x5605b0775948 [label="C_out"];
    interface_1_in_0x5605b0775998 -> interface_1_out_0x5605b0775998 [label="H"];
    interface_1_in_0x5605beb88820 -> op_0x5605beb88800 [label="C_out"];
    interface_1_in_0x5605beb88838 -> op_0x5605beb88800 [label="C_out"];
    op_0x5605beb88d18 -> op_0x5605beb88990 [label="s"];
    interface_1_in_0x5605beb889c8 -> op_0x5605beb88990 [label="s"];
    interface_1_in_0x5605beb89790 -> interface_1_out_0x5605beb89790 [label="H"];
    op_0x5605beb88990 -> interface_1_out_0x5605beb8abd8 [label="s"];
}

// Stage tensor.
subgraph cluster_subgraph_2 {
    label = "Subgraph 2";
    // Reductions.
    reduce_0x7f7a20007948 [label="Sum", shape=box];
    reduce_0x7f7a20003a98 [label="Sum", shape=box];
    // Output.
    subgraph cluster_subgraph_2_out {
        label = "";
        interface_2_out_0x5605b0775920 [label="N", shape=none];
        interface_2_out_0x5605beb88820 [label="C_out", shape=none];
        interface_2_out_0x5605beb89790 [label="H", shape=none];
        interface_2_out_0x5605b0775998 [label="H", shape=none];
    }
    {
        rank = same;
        reduce_0x7f7a20007948;
        reduce_0x7f7a20003a98;
        interface_2_out_0x5605b0775920;
        interface_2_out_0x5605beb88820;
        interface_2_out_0x5605beb89790;
        interface_2_out_0x5605b0775998;
    }
    // Input 0.
    subgraph cluster_subgraph_2_in_0 {
        label = "";
        interface_2_in_0x5605b0775920 [label="N", shape=none];
        interface_2_in_0x5605beb88a50 [label="C_in", shape=none];
        interface_2_in_0x5605beb89790 [label="H", shape=none];
        interface_2_in_0x5605beb88aa0 [label="k_1", shape=none];
        interface_2_in_0x5605b0775998 [label="H", shape=none];
    }
    // Input 1.
    subgraph cluster_subgraph_2_in_1 {
        label = "";
        interface_2_in_0x5605beb88a18 [label="C_out", shape=none];
        interface_2_in_0x5605beb88a68 [label="C_in", shape=none];
        interface_2_in_0x5605beb88ab8 [label="k_1", shape=none];
    }
    {
        rank = same;
        interface_2_in_0x5605b0775920;
        interface_2_in_0x5605beb88a50;
        interface_2_in_0x5605beb89790;
        interface_2_in_0x5605beb88aa0;
        interface_2_in_0x5605b0775998;
        interface_2_in_0x5605beb88a18;
        interface_2_in_0x5605beb88a68;
        interface_2_in_0x5605beb88ab8;
    }
    // Op's.
    op_0x5605beb889e0 [label="Share"];
    op_0x5605beb88a30 [label="Share"];
    op_0x5605beb88a80 [label="Share"];
    op_0x5605beb88d38 [label="Expand"];
    // Dimension's.
    interface_2_in_0x5605b0775920 -> interface_2_out_0x5605b0775920 [label="N"];
    interface_2_in_0x5605b0775998 -> interface_2_out_0x5605b0775998 [label="H"];
    op_0x5605beb889e0 -> interface_2_out_0x5605beb88820 [label="C_out"];
    op_0x5605beb88d38 -> op_0x5605beb889e0 [label="C_out"];
    interface_2_in_0x5605beb88a18 -> op_0x5605beb889e0 [label="C_out"];
    interface_2_in_0x5605beb88a50 -> op_0x5605beb88a30 [label="C_in"];
    interface_2_in_0x5605beb88a68 -> op_0x5605beb88a30 [label="C_in"];
    interface_2_in_0x5605beb88aa0 -> op_0x5605beb88a80 [label="k_1"];
    interface_2_in_0x5605beb88ab8 -> op_0x5605beb88a80 [label="k_1"];
    interface_2_in_0x5605beb89790 -> interface_2_out_0x5605beb89790 [label="H"];
    op_0x5605beb88a80 -> reduce_0x7f7a20003a98 [label="k_1"];
    op_0x5605beb88a30 -> reduce_0x7f7a20007948 [label="C_in"];
}

// Stage tensor.
subgraph cluster_subgraph_3 {
    label = "Subgraph 3";
    // Reductions.
    // Output.
    subgraph cluster_subgraph_3_out {
        label = "";
        interface_3_out_0x5605b0775920 [label="N", shape=none];
        interface_3_out_0x5605beb88a50 [label="C_in", shape=none];
        interface_3_out_0x5605beb89790 [label="H", shape=none];
        interface_3_out_0x5605beb88aa0 [label="k_1", shape=none];
        interface_3_out_0x5605b0775998 [label="H", shape=none];
    }
    {
        rank = same;
        interface_3_out_0x5605b0775920;
        interface_3_out_0x5605beb88a50;
        interface_3_out_0x5605beb89790;
        interface_3_out_0x5605beb88aa0;
        interface_3_out_0x5605b0775998;
    }
    // Input 0.
    subgraph cluster_subgraph_3_in_0 {
        label = "";
        interface_3_in_0x5605b0775920 [label="N", shape=none];
        interface_3_in_0x5605beb88a50 [label="C_in", shape=none];
        interface_3_in_0x5605beb89790 [label="H", shape=none];
        interface_3_in_0x5605beb97be8 [label="H", shape=none];
    }
    {
        rank = same;
        interface_3_in_0x5605b0775920;
        interface_3_in_0x5605beb88a50;
        interface_3_in_0x5605beb89790;
        interface_3_in_0x5605beb97be8;
    }
    // Op's.
    op_0x5605beb97bc0 [label="Unfold"];
    // Dimension's.
    interface_3_in_0x5605b0775920 -> interface_3_out_0x5605b0775920 [label="N"];
    op_0x5605beb97bc0 -> interface_3_out_0x5605b0775998 [label="H"];
    interface_3_in_0x5605beb88a50 -> interface_3_out_0x5605beb88a50 [label="C_in"];
    op_0x5605beb97bc0 -> interface_3_out_0x5605beb88aa0 [label="k_1"];
    interface_3_in_0x5605beb89790 -> interface_3_out_0x5605beb89790 [label="H"];
    interface_3_in_0x5605beb97be8 -> op_0x5605beb97bc0 [label="H"];
}

// Input tensor.
subgraph cluster_subgraph_4 {
    label = "Input 0";
    interface_4_out_0x5605b0775920 [label="N", shape=none];
    interface_4_out_0x5605beb88a50 [label="C_in", shape=none];
    interface_4_out_0x5605beb89790 [label="H", shape=none];
    interface_4_out_0x5605beb97be8 [label="H", shape=none];
}

interface_4_out_0x5605b0775920 -> interface_3_in_0x5605b0775920;
interface_4_out_0x5605beb88a50 -> interface_3_in_0x5605beb88a50;
interface_4_out_0x5605beb89790 -> interface_3_in_0x5605beb89790;
interface_4_out_0x5605beb97be8 -> interface_3_in_0x5605beb97be8;

interface_3_out_0x5605b0775920 -> interface_2_in_0x5605b0775920;
interface_3_out_0x5605beb88a50 -> interface_2_in_0x5605beb88a50;
interface_3_out_0x5605beb89790 -> interface_2_in_0x5605beb89790;
interface_3_out_0x5605beb88aa0 -> interface_2_in_0x5605beb88aa0;
interface_3_out_0x5605b0775998 -> interface_2_in_0x5605b0775998;

// Input tensor.
subgraph cluster_subgraph_5 {
    label = "Input 2";
    interface_5_out_0x5605beb88a18 [label="C_out", shape=none];
    interface_5_out_0x5605beb88a68 [label="C_in", shape=none];
    interface_5_out_0x5605beb88ab8 [label="k_1", shape=none];
}

interface_5_out_0x5605beb88a18 -> interface_2_in_0x5605beb88a18;
interface_5_out_0x5605beb88a68 -> interface_2_in_0x5605beb88a68;
interface_5_out_0x5605beb88ab8 -> interface_2_in_0x5605beb88ab8;

interface_2_out_0x5605b0775920 -> interface_1_in_0x5605b0775920;
interface_2_out_0x5605beb88820 -> interface_1_in_0x5605beb88820;
interface_2_out_0x5605beb89790 -> interface_1_in_0x5605beb89790;
interface_2_out_0x5605b0775998 -> interface_1_in_0x5605b0775998;

// Input tensor.
subgraph cluster_subgraph_6 {
    label = "Input 1";
    interface_6_out_0x5605beb88838 [label="C_out", shape=none];
    interface_6_out_0x5605beb889c8 [label="s", shape=none];
}

interface_6_out_0x5605beb88838 -> interface_1_in_0x5605beb88838;
interface_6_out_0x5605beb889c8 -> interface_1_in_0x5605beb889c8;

interface_1_out_0x5605b0775920 -> interface_0_in_0x5605b0775920;
interface_1_out_0x5605b0775948 -> interface_0_in_0x5605b0775948;
interface_1_out_0x5605beb89790 -> interface_0_in_0x5605beb89790;
interface_1_out_0x5605beb8abd8 -> interface_0_in_0x5605beb8abd8;
interface_1_out_0x5605b0775998 -> interface_0_in_0x5605b0775998;

{
    rank = same;
    interface_4_out_0x5605b0775920;
    interface_4_out_0x5605beb88a50;
    interface_4_out_0x5605beb89790;
    interface_4_out_0x5605beb97be8;
    interface_6_out_0x5605beb88838;
    interface_6_out_0x5605beb889c8;
    interface_5_out_0x5605beb88a18;
    interface_5_out_0x5605beb88a68;
    interface_5_out_0x5605beb88ab8;
}
subgraph cluster_subgraph_output {
    label = "Output";
    interface_7_in_0x5605b0775920 [label="N", shape=none];
    interface_7_in_0x5605b0775948 [label="C_out", shape=none];
    interface_7_in_0x5605b0775970 [label="H", shape=none];
    interface_7_in_0x5605b0775998 [label="H", shape=none];
}
interface_0_out_0x5605b0775920 -> interface_7_in_0x5605b0775920;
interface_0_out_0x5605b0775948 -> interface_7_in_0x5605b0775948;
interface_0_out_0x5605b0775970 -> interface_7_in_0x5605b0775970;
interface_0_out_0x5605b0775998 -> interface_7_in_0x5605b0775998;

}

"""
class kernel_generated_0(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([64, 2]),
			torch.randn([64, 64, 3]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]
		in_2 = self.weights[1]

		# No contraction needed.
		t_3 = in_0

		# [H]@Unfold0063bc82bd8ddf70 -> [H]@Iteratorb0a1def4ad5784ec, [k_1]@Shared4e0659d169008e4
		t_3 = torch.reshape(t_3, (1, 3584, 56, 1, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (1, 64, 56, 3, 56, ))

		# Perform contraction.
		t_4 = torch.einsum("ljnkm, ijk -> linm", t_3, in_2)

		# Perform contraction.
		t_5 = torch.einsum("kiml, ij -> kimjl", t_4, in_1)

		# No contraction needed.
		t_6 = t_5

		# [H]@Shiftb8e66ea4c8ed4afc -> [H]@Merge5f50103ea583163b
		t_6 = torch.roll(t_6, self.shift_direction, 2)

		# [H]@Merge5f50103ea583163b, [s]@Merge5f50103ea5831638 -> [s*H]@Shift3c9c8e9d3c84cb9b
		t_6 = torch.reshape(t_6, (1, 64, 112, 56, ))

		# [s*H]@Shift3c9c8e9d3c84cb9b -> [s*H]@Splitdb1af055f999951a
		t_6 = torch.roll(t_6, self.shift_direction, 2)

		# [s*H]@Splitdb1af055f999951a -> [H]@Iterator96123ba3184da39c, [s]@Reduced95c644a3c072d9a
		t_6 = torch.reshape(t_6, (1, 64, 56, 2, 56, ))

		# [s]@Reduce
		t_6 = torch.sum(t_6, dim=(3, ))

		# No need to crop the output tensor.
		y = t_6

		return y

class kernel_generated_1(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([128, 2]),
			torch.randn([128, 64, 3]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]
		in_2 = self.weights[1]

		# No contraction needed.
		t_3 = in_0

		# [H]@Unfold0063bc82bd8ddf70 -> [H]@Iteratorb0a1def4ad5784ec, [k_1]@Shared4e0659d169008e4
		t_3 = torch.reshape(t_3, (1, 1792, 28, 1, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (1, 64, 28, 3, 28, ))

		# Perform contraction.
		t_4 = torch.einsum("ljnkm, ijk -> linm", t_3, in_2)

		# Perform contraction.
		t_5 = torch.einsum("kiml, ij -> kimjl", t_4, in_1)

		# No contraction needed.
		t_6 = t_5

		# [H]@Shiftb8e66ea4c8ed4afc -> [H]@Merge5f50103ea583163b
		t_6 = torch.roll(t_6, self.shift_direction, 2)

		# [H]@Merge5f50103ea583163b, [s]@Merge5f50103ea5831638 -> [s*H]@Shift3c9c8e9d3c84cb9b
		t_6 = torch.reshape(t_6, (1, 128, 56, 28, ))

		# [s*H]@Shift3c9c8e9d3c84cb9b -> [s*H]@Splitdb1af055f999951a
		t_6 = torch.roll(t_6, self.shift_direction, 2)

		# [s*H]@Splitdb1af055f999951a -> [H]@Iterator96123ba3184da39c, [s]@Reduced95c644a3c072d9a
		t_6 = torch.reshape(t_6, (1, 128, 28, 2, 28, ))

		# [s]@Reduce
		t_6 = torch.sum(t_6, dim=(3, ))

		# No need to crop the output tensor.
		y = t_6

		return y

class kernel_generated_2(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([128, 2]),
			torch.randn([128, 128, 3]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]
		in_2 = self.weights[1]

		# No contraction needed.
		t_3 = in_0

		# [H]@Unfold0063bc82bd8ddf70 -> [H]@Iteratorb0a1def4ad5784ec, [k_1]@Shared4e0659d169008e4
		t_3 = torch.reshape(t_3, (1, 3584, 28, 1, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (1, 128, 28, 3, 28, ))

		# Perform contraction.
		t_4 = torch.einsum("ljnkm, ijk -> linm", t_3, in_2)

		# Perform contraction.
		t_5 = torch.einsum("kiml, ij -> kimjl", t_4, in_1)

		# No contraction needed.
		t_6 = t_5

		# [H]@Shiftb8e66ea4c8ed4afc -> [H]@Merge5f50103ea583163b
		t_6 = torch.roll(t_6, self.shift_direction, 2)

		# [H]@Merge5f50103ea583163b, [s]@Merge5f50103ea5831638 -> [s*H]@Shift3c9c8e9d3c84cb9b
		t_6 = torch.reshape(t_6, (1, 128, 56, 28, ))

		# [s*H]@Shift3c9c8e9d3c84cb9b -> [s*H]@Splitdb1af055f999951a
		t_6 = torch.roll(t_6, self.shift_direction, 2)

		# [s*H]@Splitdb1af055f999951a -> [H]@Iterator96123ba3184da39c, [s]@Reduced95c644a3c072d9a
		t_6 = torch.reshape(t_6, (1, 128, 28, 2, 28, ))

		# [s]@Reduce
		t_6 = torch.sum(t_6, dim=(3, ))

		# No need to crop the output tensor.
		y = t_6

		return y

class kernel_generated_3(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([256, 2]),
			torch.randn([256, 128, 3]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]
		in_2 = self.weights[1]

		# No contraction needed.
		t_3 = in_0

		# [H]@Unfold0063bc82bd8ddf70 -> [H]@Iteratorb0a1def4ad5784ec, [k_1]@Shared4e0659d169008e4
		t_3 = torch.reshape(t_3, (1, 1792, 14, 1, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (1, 128, 14, 3, 14, ))

		# Perform contraction.
		t_4 = torch.einsum("ljnkm, ijk -> linm", t_3, in_2)

		# Perform contraction.
		t_5 = torch.einsum("kiml, ij -> kimjl", t_4, in_1)

		# No contraction needed.
		t_6 = t_5

		# [H]@Shiftb8e66ea4c8ed4afc -> [H]@Merge5f50103ea583163b
		t_6 = torch.roll(t_6, self.shift_direction, 2)

		# [H]@Merge5f50103ea583163b, [s]@Merge5f50103ea5831638 -> [s*H]@Shift3c9c8e9d3c84cb9b
		t_6 = torch.reshape(t_6, (1, 256, 28, 14, ))

		# [s*H]@Shift3c9c8e9d3c84cb9b -> [s*H]@Splitdb1af055f999951a
		t_6 = torch.roll(t_6, self.shift_direction, 2)

		# [s*H]@Splitdb1af055f999951a -> [H]@Iterator96123ba3184da39c, [s]@Reduced95c644a3c072d9a
		t_6 = torch.reshape(t_6, (1, 256, 14, 2, 14, ))

		# [s]@Reduce
		t_6 = torch.sum(t_6, dim=(3, ))

		# No need to crop the output tensor.
		y = t_6

		return y

class kernel_generated_4(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([256, 2]),
			torch.randn([256, 256, 3]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]
		in_2 = self.weights[1]

		# No contraction needed.
		t_3 = in_0

		# [H]@Unfold0063bc82bd8ddf70 -> [H]@Iteratorb0a1def4ad5784ec, [k_1]@Shared4e0659d169008e4
		t_3 = torch.reshape(t_3, (1, 3584, 14, 1, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (1, 256, 14, 3, 14, ))

		# Perform contraction.
		t_4 = torch.einsum("ljnkm, ijk -> linm", t_3, in_2)

		# Perform contraction.
		t_5 = torch.einsum("kiml, ij -> kimjl", t_4, in_1)

		# No contraction needed.
		t_6 = t_5

		# [H]@Shiftb8e66ea4c8ed4afc -> [H]@Merge5f50103ea583163b
		t_6 = torch.roll(t_6, self.shift_direction, 2)

		# [H]@Merge5f50103ea583163b, [s]@Merge5f50103ea5831638 -> [s*H]@Shift3c9c8e9d3c84cb9b
		t_6 = torch.reshape(t_6, (1, 256, 28, 14, ))

		# [s*H]@Shift3c9c8e9d3c84cb9b -> [s*H]@Splitdb1af055f999951a
		t_6 = torch.roll(t_6, self.shift_direction, 2)

		# [s*H]@Splitdb1af055f999951a -> [H]@Iterator96123ba3184da39c, [s]@Reduced95c644a3c072d9a
		t_6 = torch.reshape(t_6, (1, 256, 14, 2, 14, ))

		# [s]@Reduce
		t_6 = torch.sum(t_6, dim=(3, ))

		# No need to crop the output tensor.
		y = t_6

		return y

class kernel_generated_5(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([512, 2]),
			torch.randn([512, 256, 3]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]
		in_2 = self.weights[1]

		# No contraction needed.
		t_3 = in_0

		# [H]@Unfold0063bc82bd8ddf70 -> [H]@Iteratorb0a1def4ad5784ec, [k_1]@Shared4e0659d169008e4
		t_3 = torch.reshape(t_3, (1, 1792, 7, 1, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (1, 256, 7, 3, 7, ))

		# Perform contraction.
		t_4 = torch.einsum("ljnkm, ijk -> linm", t_3, in_2)

		# Perform contraction.
		t_5 = torch.einsum("kiml, ij -> kimjl", t_4, in_1)

		# No contraction needed.
		t_6 = t_5

		# [H]@Shiftb8e66ea4c8ed4afc -> [H]@Merge5f50103ea583163b
		t_6 = torch.roll(t_6, self.shift_direction, 2)

		# [H]@Merge5f50103ea583163b, [s]@Merge5f50103ea5831638 -> [s*H]@Shift3c9c8e9d3c84cb9b
		t_6 = torch.reshape(t_6, (1, 512, 14, 7, ))

		# [s*H]@Shift3c9c8e9d3c84cb9b -> [s*H]@Splitdb1af055f999951a
		t_6 = torch.roll(t_6, self.shift_direction, 2)

		# [s*H]@Splitdb1af055f999951a -> [H]@Iterator96123ba3184da39c, [s]@Reduced95c644a3c072d9a
		t_6 = torch.reshape(t_6, (1, 512, 7, 2, 7, ))

		# [s]@Reduce
		t_6 = torch.sum(t_6, dim=(3, ))

		# No need to crop the output tensor.
		y = t_6

		return y

class kernel_generated_6(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([512, 2]),
			torch.randn([512, 512, 3]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]
		in_2 = self.weights[1]

		# No contraction needed.
		t_3 = in_0

		# [H]@Unfold0063bc82bd8ddf70 -> [H]@Iteratorb0a1def4ad5784ec, [k_1]@Shared4e0659d169008e4
		t_3 = torch.reshape(t_3, (1, 3584, 7, 1, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (1, 512, 7, 3, 7, ))

		# Perform contraction.
		t_4 = torch.einsum("ljnkm, ijk -> linm", t_3, in_2)

		# Perform contraction.
		t_5 = torch.einsum("kiml, ij -> kimjl", t_4, in_1)

		# No contraction needed.
		t_6 = t_5

		# [H]@Shiftb8e66ea4c8ed4afc -> [H]@Merge5f50103ea583163b
		t_6 = torch.roll(t_6, self.shift_direction, 2)

		# [H]@Merge5f50103ea583163b, [s]@Merge5f50103ea5831638 -> [s*H]@Shift3c9c8e9d3c84cb9b
		t_6 = torch.reshape(t_6, (1, 512, 14, 7, ))

		# [s*H]@Shift3c9c8e9d3c84cb9b -> [s*H]@Splitdb1af055f999951a
		t_6 = torch.roll(t_6, self.shift_direction, 2)

		# [s*H]@Splitdb1af055f999951a -> [H]@Iterator96123ba3184da39c, [s]@Reduced95c644a3c072d9a
		t_6 = torch.reshape(t_6, (1, 512, 7, 2, 7, ))

		# [s]@Reduce
		t_6 = torch.sum(t_6, dim=(3, ))

		# No need to crop the output tensor.
		y = t_6

		return y

