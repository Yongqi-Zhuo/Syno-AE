import torch
import random
"""
digraph kernel_preview {
newrank = true;

// Stage tensor.
subgraph cluster_subgraph_0 {
    label = "Subgraph 0";
    // Reductions.
    reduce_0x7f3cd0004ce8 [label="Sum", shape=box];
    // Output.
    subgraph cluster_subgraph_0_out {
        label = "";
        interface_0_out_0x560f6c4cbed0 [label="N", shape=none];
        interface_0_out_0x560f6c4cbef8 [label="C_out", shape=none];
        interface_0_out_0x560f6c4cbf20 [label="H", shape=none];
        interface_0_out_0x560f6c4cbf48 [label="H", shape=none];
    }
    {
        rank = same;
        reduce_0x7f3cd0004ce8;
        interface_0_out_0x560f6c4cbed0;
        interface_0_out_0x560f6c4cbef8;
        interface_0_out_0x560f6c4cbf20;
        interface_0_out_0x560f6c4cbf48;
    }
    // Input 0.
    subgraph cluster_subgraph_0_in_0 {
        label = "";
        interface_0_in_0x560f6c4cbed0 [label="N", shape=none];
        interface_0_in_0x560f6c4cbef8 [label="C_out", shape=none];
        interface_0_in_0x560f70f80f60 [label="H", shape=none];
        interface_0_in_0x560f70f88d88 [label="s", shape=none];
        interface_0_in_0x560f6c4cbf48 [label="H", shape=none];
    }
    {
        rank = same;
        interface_0_in_0x560f6c4cbed0;
        interface_0_in_0x560f6c4cbef8;
        interface_0_in_0x560f70f80f60;
        interface_0_in_0x560f70f88d88;
        interface_0_in_0x560f6c4cbf48;
    }
    // Op's.
    op_0x560f70f80ee0 [label="Shift"];
    op_0x560f70f80f40 [label="Shift"];
    op_0x560f70f815a0 [label="Split"];
    op_0x560f70f88d30 [label="Merge"];
    // Dimension's.
    interface_0_in_0x560f6c4cbed0 -> interface_0_out_0x560f6c4cbed0 [label="N"];
    interface_0_in_0x560f6c4cbef8 -> interface_0_out_0x560f6c4cbef8 [label="C_out"];
    op_0x560f70f815a0 -> interface_0_out_0x560f6c4cbf20 [label="H"];
    interface_0_in_0x560f6c4cbf48 -> interface_0_out_0x560f6c4cbf48 [label="H"];
    op_0x560f70f88d30 -> op_0x560f70f80ee0 [label="s*H"];
    interface_0_in_0x560f70f80f60 -> op_0x560f70f80f40 [label="H"];
    op_0x560f70f80ee0 -> op_0x560f70f815a0 [label="s*H"];
    op_0x560f70f80f40 -> op_0x560f70f88d30 [label="H"];
    interface_0_in_0x560f70f88d88 -> op_0x560f70f88d30 [label="s"];
    op_0x560f70f815a0 -> reduce_0x7f3cd0004ce8 [label="s"];
}

// Stage tensor.
subgraph cluster_subgraph_1 {
    label = "Subgraph 1";
    // Reductions.
    // Output.
    subgraph cluster_subgraph_1_out {
        label = "";
        interface_1_out_0x560f6c4cbed0 [label="N", shape=none];
        interface_1_out_0x560f6c4cbef8 [label="C_out", shape=none];
        interface_1_out_0x560f70f80f60 [label="H", shape=none];
        interface_1_out_0x560f70f88d88 [label="s", shape=none];
        interface_1_out_0x560f6c4cbf48 [label="H", shape=none];
    }
    {
        rank = same;
        interface_1_out_0x560f6c4cbed0;
        interface_1_out_0x560f6c4cbef8;
        interface_1_out_0x560f70f80f60;
        interface_1_out_0x560f70f88d88;
        interface_1_out_0x560f6c4cbf48;
    }
    // Input 0.
    subgraph cluster_subgraph_1_in_0 {
        label = "";
        interface_1_in_0x560f6c4cbed0 [label="N", shape=none];
        interface_1_in_0x560f70f801a0 [label="C_out", shape=none];
        interface_1_in_0x560f70f80f60 [label="H", shape=none];
        interface_1_in_0x560f6c4cbf48 [label="H", shape=none];
    }
    // Input 1.
    subgraph cluster_subgraph_1_in_1 {
        label = "";
        interface_1_in_0x560f70f801b8 [label="C_out", shape=none];
        interface_1_in_0x560f70f80348 [label="s", shape=none];
    }
    {
        rank = same;
        interface_1_in_0x560f6c4cbed0;
        interface_1_in_0x560f70f801a0;
        interface_1_in_0x560f70f80f60;
        interface_1_in_0x560f6c4cbf48;
        interface_1_in_0x560f70f801b8;
        interface_1_in_0x560f70f80348;
    }
    // Op's.
    op_0x560f70f80180 [label="Share"];
    op_0x560f70f80310 [label="Share"];
    op_0x560f70f80678 [label="Expand"];
    // Dimension's.
    interface_1_in_0x560f6c4cbed0 -> interface_1_out_0x560f6c4cbed0 [label="N"];
    op_0x560f70f80180 -> interface_1_out_0x560f6c4cbef8 [label="C_out"];
    interface_1_in_0x560f6c4cbf48 -> interface_1_out_0x560f6c4cbf48 [label="H"];
    interface_1_in_0x560f70f801a0 -> op_0x560f70f80180 [label="C_out"];
    interface_1_in_0x560f70f801b8 -> op_0x560f70f80180 [label="C_out"];
    op_0x560f70f80678 -> op_0x560f70f80310 [label="s"];
    interface_1_in_0x560f70f80348 -> op_0x560f70f80310 [label="s"];
    interface_1_in_0x560f70f80f60 -> interface_1_out_0x560f70f80f60 [label="H"];
    op_0x560f70f80310 -> interface_1_out_0x560f70f88d88 [label="s"];
}

// Stage tensor.
subgraph cluster_subgraph_2 {
    label = "Subgraph 2";
    // Reductions.
    reduce_0x7f3cd0007948 [label="Sum", shape=box];
    reduce_0x7f3cd0003a98 [label="Sum", shape=box];
    // Output.
    subgraph cluster_subgraph_2_out {
        label = "";
        interface_2_out_0x560f6c4cbed0 [label="N", shape=none];
        interface_2_out_0x560f70f801a0 [label="C_out", shape=none];
        interface_2_out_0x560f70f80f60 [label="H", shape=none];
        interface_2_out_0x560f6c4cbf48 [label="H", shape=none];
    }
    {
        rank = same;
        reduce_0x7f3cd0007948;
        reduce_0x7f3cd0003a98;
        interface_2_out_0x560f6c4cbed0;
        interface_2_out_0x560f70f801a0;
        interface_2_out_0x560f70f80f60;
        interface_2_out_0x560f6c4cbf48;
    }
    // Input 0.
    subgraph cluster_subgraph_2_in_0 {
        label = "";
        interface_2_in_0x560f6c4cbed0 [label="N", shape=none];
        interface_2_in_0x560f70facdb0 [label="C_in", shape=none];
        interface_2_in_0x560f70f80f60 [label="H", shape=none];
        interface_2_in_0x560f70face00 [label="k_1", shape=none];
        interface_2_in_0x560f6c4cbf48 [label="H", shape=none];
    }
    // Input 1.
    subgraph cluster_subgraph_2_in_1 {
        label = "";
        interface_2_in_0x560f70facd78 [label="C_out", shape=none];
        interface_2_in_0x560f70facdc8 [label="C_in", shape=none];
        interface_2_in_0x560f70face18 [label="k_1", shape=none];
    }
    {
        rank = same;
        interface_2_in_0x560f6c4cbed0;
        interface_2_in_0x560f70facdb0;
        interface_2_in_0x560f70f80f60;
        interface_2_in_0x560f70face00;
        interface_2_in_0x560f6c4cbf48;
        interface_2_in_0x560f70facd78;
        interface_2_in_0x560f70facdc8;
        interface_2_in_0x560f70face18;
    }
    // Op's.
    op_0x560f70f806f8 [label="Expand"];
    op_0x560f70facd40 [label="Share"];
    op_0x560f70facd90 [label="Share"];
    op_0x560f70facde0 [label="Share"];
    // Dimension's.
    interface_2_in_0x560f6c4cbed0 -> interface_2_out_0x560f6c4cbed0 [label="N"];
    interface_2_in_0x560f6c4cbf48 -> interface_2_out_0x560f6c4cbf48 [label="H"];
    op_0x560f70facd40 -> interface_2_out_0x560f70f801a0 [label="C_out"];
    interface_2_in_0x560f70f80f60 -> interface_2_out_0x560f70f80f60 [label="H"];
    op_0x560f70f806f8 -> op_0x560f70facd40 [label="C_out"];
    interface_2_in_0x560f70facd78 -> op_0x560f70facd40 [label="C_out"];
    interface_2_in_0x560f70facdb0 -> op_0x560f70facd90 [label="C_in"];
    interface_2_in_0x560f70facdc8 -> op_0x560f70facd90 [label="C_in"];
    interface_2_in_0x560f70face00 -> op_0x560f70facde0 [label="k_1"];
    interface_2_in_0x560f70face18 -> op_0x560f70facde0 [label="k_1"];
    op_0x560f70facde0 -> reduce_0x7f3cd0003a98 [label="k_1"];
    op_0x560f70facd90 -> reduce_0x7f3cd0007948 [label="C_in"];
}

// Stage tensor.
subgraph cluster_subgraph_3 {
    label = "Subgraph 3";
    // Reductions.
    // Output.
    subgraph cluster_subgraph_3_out {
        label = "";
        interface_3_out_0x560f6c4cbed0 [label="N", shape=none];
        interface_3_out_0x560f70facdb0 [label="C_in", shape=none];
        interface_3_out_0x560f70f80f60 [label="H", shape=none];
        interface_3_out_0x560f70face00 [label="k_1", shape=none];
        interface_3_out_0x560f6c4cbf48 [label="H", shape=none];
    }
    {
        rank = same;
        interface_3_out_0x560f6c4cbed0;
        interface_3_out_0x560f70facdb0;
        interface_3_out_0x560f70f80f60;
        interface_3_out_0x560f70face00;
        interface_3_out_0x560f6c4cbf48;
    }
    // Input 0.
    subgraph cluster_subgraph_3_in_0 {
        label = "";
        interface_3_in_0x560f6c4cbed0 [label="N", shape=none];
        interface_3_in_0x560f70facdb0 [label="C_in", shape=none];
        interface_3_in_0x560f70f80f60 [label="H", shape=none];
        interface_3_in_0x560f70ff9f28 [label="H", shape=none];
    }
    {
        rank = same;
        interface_3_in_0x560f6c4cbed0;
        interface_3_in_0x560f70facdb0;
        interface_3_in_0x560f70f80f60;
        interface_3_in_0x560f70ff9f28;
    }
    // Op's.
    op_0x560f70ff9f00 [label="Unfold"];
    // Dimension's.
    interface_3_in_0x560f6c4cbed0 -> interface_3_out_0x560f6c4cbed0 [label="N"];
    op_0x560f70ff9f00 -> interface_3_out_0x560f6c4cbf48 [label="H"];
    interface_3_in_0x560f70f80f60 -> interface_3_out_0x560f70f80f60 [label="H"];
    interface_3_in_0x560f70facdb0 -> interface_3_out_0x560f70facdb0 [label="C_in"];
    op_0x560f70ff9f00 -> interface_3_out_0x560f70face00 [label="k_1"];
    interface_3_in_0x560f70ff9f28 -> op_0x560f70ff9f00 [label="H"];
}

// Input tensor.
subgraph cluster_subgraph_4 {
    label = "Input 0";
    interface_4_out_0x560f6c4cbed0 [label="N", shape=none];
    interface_4_out_0x560f70facdb0 [label="C_in", shape=none];
    interface_4_out_0x560f70f80f60 [label="H", shape=none];
    interface_4_out_0x560f70ff9f28 [label="H", shape=none];
}

interface_4_out_0x560f6c4cbed0 -> interface_3_in_0x560f6c4cbed0;
interface_4_out_0x560f70facdb0 -> interface_3_in_0x560f70facdb0;
interface_4_out_0x560f70f80f60 -> interface_3_in_0x560f70f80f60;
interface_4_out_0x560f70ff9f28 -> interface_3_in_0x560f70ff9f28;

interface_3_out_0x560f6c4cbed0 -> interface_2_in_0x560f6c4cbed0;
interface_3_out_0x560f70facdb0 -> interface_2_in_0x560f70facdb0;
interface_3_out_0x560f70f80f60 -> interface_2_in_0x560f70f80f60;
interface_3_out_0x560f70face00 -> interface_2_in_0x560f70face00;
interface_3_out_0x560f6c4cbf48 -> interface_2_in_0x560f6c4cbf48;

// Input tensor.
subgraph cluster_subgraph_5 {
    label = "Input 2";
    interface_5_out_0x560f70facd78 [label="C_out", shape=none];
    interface_5_out_0x560f70facdc8 [label="C_in", shape=none];
    interface_5_out_0x560f70face18 [label="k_1", shape=none];
}

interface_5_out_0x560f70facd78 -> interface_2_in_0x560f70facd78;
interface_5_out_0x560f70facdc8 -> interface_2_in_0x560f70facdc8;
interface_5_out_0x560f70face18 -> interface_2_in_0x560f70face18;

interface_2_out_0x560f6c4cbed0 -> interface_1_in_0x560f6c4cbed0;
interface_2_out_0x560f70f801a0 -> interface_1_in_0x560f70f801a0;
interface_2_out_0x560f70f80f60 -> interface_1_in_0x560f70f80f60;
interface_2_out_0x560f6c4cbf48 -> interface_1_in_0x560f6c4cbf48;

// Input tensor.
subgraph cluster_subgraph_6 {
    label = "Input 1";
    interface_6_out_0x560f70f801b8 [label="C_out", shape=none];
    interface_6_out_0x560f70f80348 [label="s", shape=none];
}

interface_6_out_0x560f70f801b8 -> interface_1_in_0x560f70f801b8;
interface_6_out_0x560f70f80348 -> interface_1_in_0x560f70f80348;

interface_1_out_0x560f6c4cbed0 -> interface_0_in_0x560f6c4cbed0;
interface_1_out_0x560f6c4cbef8 -> interface_0_in_0x560f6c4cbef8;
interface_1_out_0x560f70f80f60 -> interface_0_in_0x560f70f80f60;
interface_1_out_0x560f70f88d88 -> interface_0_in_0x560f70f88d88;
interface_1_out_0x560f6c4cbf48 -> interface_0_in_0x560f6c4cbf48;

{
    rank = same;
    interface_4_out_0x560f6c4cbed0;
    interface_4_out_0x560f70facdb0;
    interface_4_out_0x560f70f80f60;
    interface_4_out_0x560f70ff9f28;
    interface_6_out_0x560f70f801b8;
    interface_6_out_0x560f70f80348;
    interface_5_out_0x560f70facd78;
    interface_5_out_0x560f70facdc8;
    interface_5_out_0x560f70face18;
}
subgraph cluster_subgraph_output {
    label = "Output";
    interface_7_in_0x560f6c4cbed0 [label="N", shape=none];
    interface_7_in_0x560f6c4cbef8 [label="C_out", shape=none];
    interface_7_in_0x560f6c4cbf20 [label="H", shape=none];
    interface_7_in_0x560f6c4cbf48 [label="H", shape=none];
}
interface_0_out_0x560f6c4cbed0 -> interface_7_in_0x560f6c4cbed0;
interface_0_out_0x560f6c4cbef8 -> interface_7_in_0x560f6c4cbef8;
interface_0_out_0x560f6c4cbf20 -> interface_7_in_0x560f6c4cbf20;
interface_0_out_0x560f6c4cbf48 -> interface_7_in_0x560f6c4cbf48;

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

