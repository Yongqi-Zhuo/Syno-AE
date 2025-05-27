import torch
import random
"""
digraph kernel_preview {
newrank = true;

// Stage tensor.
subgraph cluster_subgraph_0 {
    label = "Subgraph 0";
    // Reductions.
    reduce_0x7f3cd0003ab0 [label="Sum", shape=box];
    reduce_0x7f3cd0007440 [label="Sum", shape=box];
    reduce_0x7f3cd0003a98 [label="Sum", shape=box];
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
        reduce_0x7f3cd0003ab0;
        reduce_0x7f3cd0007440;
        reduce_0x7f3cd0003a98;
        interface_0_out_0x560f6c4cbed0;
        interface_0_out_0x560f6c4cbef8;
        interface_0_out_0x560f6c4cbf20;
        interface_0_out_0x560f6c4cbf48;
    }
    // Input 0.
    subgraph cluster_subgraph_0_in_0 {
        label = "";
        interface_0_in_0x560f6c4cbed0 [label="N", shape=none];
        interface_0_in_0x560f70f802e0 [label="k_1", shape=none];
        interface_0_in_0x560f6c4cbf20 [label="H", shape=none];
        interface_0_in_0x560f70f801f0 [label="s^-1*C_in", shape=none];
        interface_0_in_0x560f70f80290 [label="k_1", shape=none];
        interface_0_in_0x560f6c4cbf48 [label="H", shape=none];
    }
    // Input 1.
    subgraph cluster_subgraph_0_in_1 {
        label = "";
        interface_0_in_0x560f70f801b8 [label="C_out", shape=none];
        interface_0_in_0x560f70f802f8 [label="k_1", shape=none];
        interface_0_in_0x560f70f80208 [label="s^-1*C_in", shape=none];
        interface_0_in_0x560f70f802a8 [label="k_1", shape=none];
    }
    {
        rank = same;
        interface_0_in_0x560f6c4cbed0;
        interface_0_in_0x560f70f802e0;
        interface_0_in_0x560f6c4cbf20;
        interface_0_in_0x560f70f801f0;
        interface_0_in_0x560f70f80290;
        interface_0_in_0x560f6c4cbf48;
        interface_0_in_0x560f70f801b8;
        interface_0_in_0x560f70f802f8;
        interface_0_in_0x560f70f80208;
        interface_0_in_0x560f70f802a8;
    }
    // Op's.
    op_0x560f70f80180 [label="Share"];
    op_0x560f70f801d0 [label="Share"];
    op_0x560f70f80270 [label="Share"];
    op_0x560f70f802c0 [label="Share"];
    op_0x560f70f80658 [label="Expand"];
    // Dimension's.
    interface_0_in_0x560f6c4cbed0 -> interface_0_out_0x560f6c4cbed0 [label="N"];
    op_0x560f70f80180 -> interface_0_out_0x560f6c4cbef8 [label="C_out"];
    interface_0_in_0x560f6c4cbf20 -> interface_0_out_0x560f6c4cbf20 [label="H"];
    interface_0_in_0x560f6c4cbf48 -> interface_0_out_0x560f6c4cbf48 [label="H"];
    op_0x560f70f80658 -> op_0x560f70f80180 [label="C_out"];
    interface_0_in_0x560f70f801b8 -> op_0x560f70f80180 [label="C_out"];
    interface_0_in_0x560f70f801f0 -> op_0x560f70f801d0 [label="s^-1*C_in"];
    interface_0_in_0x560f70f80208 -> op_0x560f70f801d0 [label="s^-1*C_in"];
    interface_0_in_0x560f70f80290 -> op_0x560f70f80270 [label="k_1"];
    interface_0_in_0x560f70f802a8 -> op_0x560f70f80270 [label="k_1"];
    interface_0_in_0x560f70f802e0 -> op_0x560f70f802c0 [label="k_1"];
    interface_0_in_0x560f70f802f8 -> op_0x560f70f802c0 [label="k_1"];
    op_0x560f70f80270 -> reduce_0x7f3cd0003a98 [label="k_1"];
    op_0x560f70f802c0 -> reduce_0x7f3cd0003ab0 [label="k_1"];
    op_0x560f70f801d0 -> reduce_0x7f3cd0007440 [label="s^-1*C_in"];
}

// Stage tensor.
subgraph cluster_subgraph_1 {
    label = "Subgraph 1";
    // Reductions.
    // Output.
    subgraph cluster_subgraph_1_out {
        label = "";
        interface_1_out_0x560f6c4cbed0 [label="N", shape=none];
        interface_1_out_0x560f70f802e0 [label="k_1", shape=none];
        interface_1_out_0x560f6c4cbf20 [label="H", shape=none];
        interface_1_out_0x560f70f801f0 [label="s^-1*C_in", shape=none];
        interface_1_out_0x560f70f80290 [label="k_1", shape=none];
        interface_1_out_0x560f6c4cbf48 [label="H", shape=none];
    }
    {
        rank = same;
        interface_1_out_0x560f6c4cbed0;
        interface_1_out_0x560f70f802e0;
        interface_1_out_0x560f6c4cbf20;
        interface_1_out_0x560f70f801f0;
        interface_1_out_0x560f70f80290;
        interface_1_out_0x560f6c4cbf48;
    }
    // Input 0.
    subgraph cluster_subgraph_1_in_0 {
        label = "";
        interface_1_in_0x560f6c4cbed0 [label="N", shape=none];
        interface_1_in_0x560f70f802e0 [label="k_1", shape=none];
        interface_1_in_0x560f6c4cbf20 [label="H", shape=none];
        interface_1_in_0x560f70f801f0 [label="s^-1*C_in", shape=none];
        interface_1_in_0x560f70f92e28 [label="H", shape=none];
    }
    {
        rank = same;
        interface_1_in_0x560f6c4cbed0;
        interface_1_in_0x560f70f802e0;
        interface_1_in_0x560f6c4cbf20;
        interface_1_in_0x560f70f801f0;
        interface_1_in_0x560f70f92e28;
    }
    // Op's.
    op_0x560f70f92e00 [label="Unfold"];
    // Dimension's.
    interface_1_in_0x560f6c4cbed0 -> interface_1_out_0x560f6c4cbed0 [label="N"];
    interface_1_in_0x560f6c4cbf20 -> interface_1_out_0x560f6c4cbf20 [label="H"];
    op_0x560f70f92e00 -> interface_1_out_0x560f6c4cbf48 [label="H"];
    interface_1_in_0x560f70f801f0 -> interface_1_out_0x560f70f801f0 [label="s^-1*C_in"];
    op_0x560f70f92e00 -> interface_1_out_0x560f70f80290 [label="k_1"];
    interface_1_in_0x560f70f802e0 -> interface_1_out_0x560f70f802e0 [label="k_1"];
    interface_1_in_0x560f70f92e28 -> op_0x560f70f92e00 [label="H"];
}

// Stage tensor.
subgraph cluster_subgraph_2 {
    label = "Subgraph 2";
    // Reductions.
    reduce_0x7f3cd0004ce8 [label="Sum", shape=box];
    // Output.
    subgraph cluster_subgraph_2_out {
        label = "";
        interface_2_out_0x560f6c4cbed0 [label="N", shape=none];
        interface_2_out_0x560f70f802e0 [label="k_1", shape=none];
        interface_2_out_0x560f6c4cbf20 [label="H", shape=none];
        interface_2_out_0x560f70f801f0 [label="s^-1*C_in", shape=none];
        interface_2_out_0x560f70f92e28 [label="H", shape=none];
    }
    {
        rank = same;
        reduce_0x7f3cd0004ce8;
        interface_2_out_0x560f6c4cbed0;
        interface_2_out_0x560f70f802e0;
        interface_2_out_0x560f6c4cbf20;
        interface_2_out_0x560f70f801f0;
        interface_2_out_0x560f70f92e28;
    }
    // Input 0.
    subgraph cluster_subgraph_2_in_0 {
        label = "";
        interface_2_in_0x560f6c4cbed0 [label="N", shape=none];
        interface_2_in_0x560f70f8b3d0 [label="C_in", shape=none];
        interface_2_in_0x560f70f92d68 [label="H", shape=none];
        interface_2_in_0x560f70f92e28 [label="H", shape=none];
    }
    {
        rank = same;
        interface_2_in_0x560f6c4cbed0;
        interface_2_in_0x560f70f8b3d0;
        interface_2_in_0x560f70f92d68;
        interface_2_in_0x560f70f92e28;
    }
    // Op's.
    op_0x560f70f80ee0 [label="Shift"];
    op_0x560f70f815a0 [label="Split"];
    op_0x560f70f88d30 [label="Merge"];
    op_0x560f70f8b390 [label="Split"];
    op_0x560f70f92d40 [label="Unfold"];
    // Dimension's.
    interface_2_in_0x560f6c4cbed0 -> interface_2_out_0x560f6c4cbed0 [label="N"];
    op_0x560f70f815a0 -> interface_2_out_0x560f6c4cbf20 [label="H"];
    op_0x560f70f8b390 -> interface_2_out_0x560f70f801f0 [label="s^-1*C_in"];
    op_0x560f70f92d40 -> interface_2_out_0x560f70f802e0 [label="k_1"];
    op_0x560f70f88d30 -> op_0x560f70f80ee0 [label="s*H"];
    op_0x560f70f80ee0 -> op_0x560f70f815a0 [label="s*H"];
    op_0x560f70f92d40 -> op_0x560f70f88d30 [label="H"];
    op_0x560f70f8b390 -> op_0x560f70f88d30 [label="s"];
    interface_2_in_0x560f70f8b3d0 -> op_0x560f70f8b390 [label="C_in"];
    interface_2_in_0x560f70f92d68 -> op_0x560f70f92d40 [label="H"];
    interface_2_in_0x560f70f92e28 -> interface_2_out_0x560f70f92e28 [label="H"];
    op_0x560f70f815a0 -> reduce_0x7f3cd0004ce8 [label="s"];
}

// Input tensor.
subgraph cluster_subgraph_3 {
    label = "Input 0";
    interface_3_out_0x560f6c4cbed0 [label="N", shape=none];
    interface_3_out_0x560f70f8b3d0 [label="C_in", shape=none];
    interface_3_out_0x560f70f92d68 [label="H", shape=none];
    interface_3_out_0x560f70f92e28 [label="H", shape=none];
}

interface_3_out_0x560f6c4cbed0 -> interface_2_in_0x560f6c4cbed0;
interface_3_out_0x560f70f8b3d0 -> interface_2_in_0x560f70f8b3d0;
interface_3_out_0x560f70f92d68 -> interface_2_in_0x560f70f92d68;
interface_3_out_0x560f70f92e28 -> interface_2_in_0x560f70f92e28;

interface_2_out_0x560f6c4cbed0 -> interface_1_in_0x560f6c4cbed0;
interface_2_out_0x560f70f802e0 -> interface_1_in_0x560f70f802e0;
interface_2_out_0x560f6c4cbf20 -> interface_1_in_0x560f6c4cbf20;
interface_2_out_0x560f70f801f0 -> interface_1_in_0x560f70f801f0;
interface_2_out_0x560f70f92e28 -> interface_1_in_0x560f70f92e28;

interface_1_out_0x560f6c4cbed0 -> interface_0_in_0x560f6c4cbed0;
interface_1_out_0x560f70f802e0 -> interface_0_in_0x560f70f802e0;
interface_1_out_0x560f6c4cbf20 -> interface_0_in_0x560f6c4cbf20;
interface_1_out_0x560f70f801f0 -> interface_0_in_0x560f70f801f0;
interface_1_out_0x560f70f80290 -> interface_0_in_0x560f70f80290;
interface_1_out_0x560f6c4cbf48 -> interface_0_in_0x560f6c4cbf48;

// Input tensor.
subgraph cluster_subgraph_4 {
    label = "Input 1";
    interface_4_out_0x560f70f801b8 [label="C_out", shape=none];
    interface_4_out_0x560f70f802f8 [label="k_1", shape=none];
    interface_4_out_0x560f70f80208 [label="s^-1*C_in", shape=none];
    interface_4_out_0x560f70f802a8 [label="k_1", shape=none];
}

interface_4_out_0x560f70f801b8 -> interface_0_in_0x560f70f801b8;
interface_4_out_0x560f70f802f8 -> interface_0_in_0x560f70f802f8;
interface_4_out_0x560f70f80208 -> interface_0_in_0x560f70f80208;
interface_4_out_0x560f70f802a8 -> interface_0_in_0x560f70f802a8;

{
    rank = same;
    interface_3_out_0x560f6c4cbed0;
    interface_3_out_0x560f70f8b3d0;
    interface_3_out_0x560f70f92d68;
    interface_3_out_0x560f70f92e28;
    interface_4_out_0x560f70f801b8;
    interface_4_out_0x560f70f802f8;
    interface_4_out_0x560f70f80208;
    interface_4_out_0x560f70f802a8;
}
subgraph cluster_subgraph_output {
    label = "Output";
    interface_5_in_0x560f6c4cbed0 [label="N", shape=none];
    interface_5_in_0x560f6c4cbef8 [label="C_out", shape=none];
    interface_5_in_0x560f6c4cbf20 [label="H", shape=none];
    interface_5_in_0x560f6c4cbf48 [label="H", shape=none];
}
interface_0_out_0x560f6c4cbed0 -> interface_5_in_0x560f6c4cbed0;
interface_0_out_0x560f6c4cbef8 -> interface_5_in_0x560f6c4cbef8;
interface_0_out_0x560f6c4cbf20 -> interface_5_in_0x560f6c4cbf20;
interface_0_out_0x560f6c4cbf48 -> interface_5_in_0x560f6c4cbf48;

}

"""
class kernel_generated_0(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([64, 3, 32, 3]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]

		# Perform contraction.
		t_2 = torch.einsum("ijkl -> ikjl", in_0)

		# [H]@Unfold5462ce2dd0c9bf76 -> [H]@Merge5f50103ea583163b, [k_1]@Share02da0a485106ab3d
		t_2 = torch.reshape(t_2, (1, 1, 56, 3584, ))
		t_2 = torch.nn.functional.unfold(t_2, (3, 1, ), padding=(1, 0, ))
		t_2 = torch.reshape(t_2, (1, 3, 56, 64, 56, ))

		# [C_in]@Splitf4535f3a98ce8ba2 -> [s]@Merge5f50103ea5831638, [s^-1*C_in]@Share8de6f167adbbf8aa
		t_2 = torch.reshape(t_2, (1, 3, 56, 2, 32, 56, ))

		# [H]@Merge5f50103ea583163b, [s]@Merge5f50103ea5831638 -> [s*H]@Shift3c9c8e9d3c84cb9b
		t_2 = torch.reshape(t_2, (1, 3, 112, 32, 56, ))

		# [s*H]@Shift3c9c8e9d3c84cb9b -> [s*H]@Splitdb1af055f999951a
		t_2 = torch.roll(t_2, self.shift_direction, 2)

		# [s*H]@Splitdb1af055f999951a -> [H]@Iterator96123ba3184da39c, [s]@Reduced95c644a3c072d9a
		t_2 = torch.reshape(t_2, (1, 3, 56, 2, 32, 56, ))

		# [s]@Reduce
		t_2 = torch.sum(t_2, dim=(3, ))

		# No contraction needed.
		t_3 = t_2

		# [H]@Unfold0063bc810b9e1e60 -> [H]@Iteratorb0a1def4ad5784ec, [k_1]@Share26cfa48d169008e4
		t_3 = torch.reshape(t_3, (1, 5376, 56, 1, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (1, 3, 56, 32, 3, 56, ))

		# Perform contraction.
		t_4 = torch.einsum("mlnjko, iljk -> mino", t_3, in_1)

		# No need to crop the output tensor.
		y = t_4

		return y

class kernel_generated_1(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([128, 3, 32, 3]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]

		# Perform contraction.
		t_2 = torch.einsum("ijkl -> ikjl", in_0)

		# [H]@Unfold5462ce2dd0c9bf76 -> [H]@Merge5f50103ea583163b, [k_1]@Share02da0a485106ab3d
		t_2 = torch.reshape(t_2, (1, 1, 28, 1792, ))
		t_2 = torch.nn.functional.unfold(t_2, (3, 1, ), padding=(1, 0, ))
		t_2 = torch.reshape(t_2, (1, 3, 28, 64, 28, ))

		# [C_in]@Splitf4535f3a98ce8ba2 -> [s]@Merge5f50103ea5831638, [s^-1*C_in]@Share8de6f167adbbf8aa
		t_2 = torch.reshape(t_2, (1, 3, 28, 2, 32, 28, ))

		# [H]@Merge5f50103ea583163b, [s]@Merge5f50103ea5831638 -> [s*H]@Shift3c9c8e9d3c84cb9b
		t_2 = torch.reshape(t_2, (1, 3, 56, 32, 28, ))

		# [s*H]@Shift3c9c8e9d3c84cb9b -> [s*H]@Splitdb1af055f999951a
		t_2 = torch.roll(t_2, self.shift_direction, 2)

		# [s*H]@Splitdb1af055f999951a -> [H]@Iterator96123ba3184da39c, [s]@Reduced95c644a3c072d9a
		t_2 = torch.reshape(t_2, (1, 3, 28, 2, 32, 28, ))

		# [s]@Reduce
		t_2 = torch.sum(t_2, dim=(3, ))

		# No contraction needed.
		t_3 = t_2

		# [H]@Unfold0063bc810b9e1e60 -> [H]@Iteratorb0a1def4ad5784ec, [k_1]@Share26cfa48d169008e4
		t_3 = torch.reshape(t_3, (1, 2688, 28, 1, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (1, 3, 28, 32, 3, 28, ))

		# Perform contraction.
		t_4 = torch.einsum("mlnjko, iljk -> mino", t_3, in_1)

		# No need to crop the output tensor.
		y = t_4

		return y

class kernel_generated_2(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([128, 3, 64, 3]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]

		# Perform contraction.
		t_2 = torch.einsum("ijkl -> ikjl", in_0)

		# [H]@Unfold5462ce2dd0c9bf76 -> [H]@Merge5f50103ea583163b, [k_1]@Share02da0a485106ab3d
		t_2 = torch.reshape(t_2, (1, 1, 28, 3584, ))
		t_2 = torch.nn.functional.unfold(t_2, (3, 1, ), padding=(1, 0, ))
		t_2 = torch.reshape(t_2, (1, 3, 28, 128, 28, ))

		# [C_in]@Splitf4535f3a98ce8ba2 -> [s]@Merge5f50103ea5831638, [s^-1*C_in]@Share8de6f167adbbf8aa
		t_2 = torch.reshape(t_2, (1, 3, 28, 2, 64, 28, ))

		# [H]@Merge5f50103ea583163b, [s]@Merge5f50103ea5831638 -> [s*H]@Shift3c9c8e9d3c84cb9b
		t_2 = torch.reshape(t_2, (1, 3, 56, 64, 28, ))

		# [s*H]@Shift3c9c8e9d3c84cb9b -> [s*H]@Splitdb1af055f999951a
		t_2 = torch.roll(t_2, self.shift_direction, 2)

		# [s*H]@Splitdb1af055f999951a -> [H]@Iterator96123ba3184da39c, [s]@Reduced95c644a3c072d9a
		t_2 = torch.reshape(t_2, (1, 3, 28, 2, 64, 28, ))

		# [s]@Reduce
		t_2 = torch.sum(t_2, dim=(3, ))

		# No contraction needed.
		t_3 = t_2

		# [H]@Unfold0063bc810b9e1e60 -> [H]@Iteratorb0a1def4ad5784ec, [k_1]@Share26cfa48d169008e4
		t_3 = torch.reshape(t_3, (1, 5376, 28, 1, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (1, 3, 28, 64, 3, 28, ))

		# Perform contraction.
		t_4 = torch.einsum("mlnjko, iljk -> mino", t_3, in_1)

		# No need to crop the output tensor.
		y = t_4

		return y

class kernel_generated_3(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([256, 3, 64, 3]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]

		# Perform contraction.
		t_2 = torch.einsum("ijkl -> ikjl", in_0)

		# [H]@Unfold5462ce2dd0c9bf76 -> [H]@Merge5f50103ea583163b, [k_1]@Share02da0a485106ab3d
		t_2 = torch.reshape(t_2, (1, 1, 14, 1792, ))
		t_2 = torch.nn.functional.unfold(t_2, (3, 1, ), padding=(1, 0, ))
		t_2 = torch.reshape(t_2, (1, 3, 14, 128, 14, ))

		# [C_in]@Splitf4535f3a98ce8ba2 -> [s]@Merge5f50103ea5831638, [s^-1*C_in]@Share8de6f167adbbf8aa
		t_2 = torch.reshape(t_2, (1, 3, 14, 2, 64, 14, ))

		# [H]@Merge5f50103ea583163b, [s]@Merge5f50103ea5831638 -> [s*H]@Shift3c9c8e9d3c84cb9b
		t_2 = torch.reshape(t_2, (1, 3, 28, 64, 14, ))

		# [s*H]@Shift3c9c8e9d3c84cb9b -> [s*H]@Splitdb1af055f999951a
		t_2 = torch.roll(t_2, self.shift_direction, 2)

		# [s*H]@Splitdb1af055f999951a -> [H]@Iterator96123ba3184da39c, [s]@Reduced95c644a3c072d9a
		t_2 = torch.reshape(t_2, (1, 3, 14, 2, 64, 14, ))

		# [s]@Reduce
		t_2 = torch.sum(t_2, dim=(3, ))

		# No contraction needed.
		t_3 = t_2

		# [H]@Unfold0063bc810b9e1e60 -> [H]@Iteratorb0a1def4ad5784ec, [k_1]@Share26cfa48d169008e4
		t_3 = torch.reshape(t_3, (1, 2688, 14, 1, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (1, 3, 14, 64, 3, 14, ))

		# Perform contraction.
		t_4 = torch.einsum("mlnjko, iljk -> mino", t_3, in_1)

		# No need to crop the output tensor.
		y = t_4

		return y

class kernel_generated_4(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([256, 3, 128, 3]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]

		# Perform contraction.
		t_2 = torch.einsum("ijkl -> ikjl", in_0)

		# [H]@Unfold5462ce2dd0c9bf76 -> [H]@Merge5f50103ea583163b, [k_1]@Share02da0a485106ab3d
		t_2 = torch.reshape(t_2, (1, 1, 14, 3584, ))
		t_2 = torch.nn.functional.unfold(t_2, (3, 1, ), padding=(1, 0, ))
		t_2 = torch.reshape(t_2, (1, 3, 14, 256, 14, ))

		# [C_in]@Splitf4535f3a98ce8ba2 -> [s]@Merge5f50103ea5831638, [s^-1*C_in]@Share8de6f167adbbf8aa
		t_2 = torch.reshape(t_2, (1, 3, 14, 2, 128, 14, ))

		# [H]@Merge5f50103ea583163b, [s]@Merge5f50103ea5831638 -> [s*H]@Shift3c9c8e9d3c84cb9b
		t_2 = torch.reshape(t_2, (1, 3, 28, 128, 14, ))

		# [s*H]@Shift3c9c8e9d3c84cb9b -> [s*H]@Splitdb1af055f999951a
		t_2 = torch.roll(t_2, self.shift_direction, 2)

		# [s*H]@Splitdb1af055f999951a -> [H]@Iterator96123ba3184da39c, [s]@Reduced95c644a3c072d9a
		t_2 = torch.reshape(t_2, (1, 3, 14, 2, 128, 14, ))

		# [s]@Reduce
		t_2 = torch.sum(t_2, dim=(3, ))

		# No contraction needed.
		t_3 = t_2

		# [H]@Unfold0063bc810b9e1e60 -> [H]@Iteratorb0a1def4ad5784ec, [k_1]@Share26cfa48d169008e4
		t_3 = torch.reshape(t_3, (1, 5376, 14, 1, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (1, 3, 14, 128, 3, 14, ))

		# Perform contraction.
		t_4 = torch.einsum("mlnjko, iljk -> mino", t_3, in_1)

		# No need to crop the output tensor.
		y = t_4

		return y

class kernel_generated_5(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([512, 3, 128, 3]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]

		# Perform contraction.
		t_2 = torch.einsum("ijkl -> ikjl", in_0)

		# [H]@Unfold5462ce2dd0c9bf76 -> [H]@Merge5f50103ea583163b, [k_1]@Share02da0a485106ab3d
		t_2 = torch.reshape(t_2, (1, 1, 7, 1792, ))
		t_2 = torch.nn.functional.unfold(t_2, (3, 1, ), padding=(1, 0, ))
		t_2 = torch.reshape(t_2, (1, 3, 7, 256, 7, ))

		# [C_in]@Splitf4535f3a98ce8ba2 -> [s]@Merge5f50103ea5831638, [s^-1*C_in]@Share8de6f167adbbf8aa
		t_2 = torch.reshape(t_2, (1, 3, 7, 2, 128, 7, ))

		# [H]@Merge5f50103ea583163b, [s]@Merge5f50103ea5831638 -> [s*H]@Shift3c9c8e9d3c84cb9b
		t_2 = torch.reshape(t_2, (1, 3, 14, 128, 7, ))

		# [s*H]@Shift3c9c8e9d3c84cb9b -> [s*H]@Splitdb1af055f999951a
		t_2 = torch.roll(t_2, self.shift_direction, 2)

		# [s*H]@Splitdb1af055f999951a -> [H]@Iterator96123ba3184da39c, [s]@Reduced95c644a3c072d9a
		t_2 = torch.reshape(t_2, (1, 3, 7, 2, 128, 7, ))

		# [s]@Reduce
		t_2 = torch.sum(t_2, dim=(3, ))

		# No contraction needed.
		t_3 = t_2

		# [H]@Unfold0063bc810b9e1e60 -> [H]@Iteratorb0a1def4ad5784ec, [k_1]@Share26cfa48d169008e4
		t_3 = torch.reshape(t_3, (1, 2688, 7, 1, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (1, 3, 7, 128, 3, 7, ))

		# Perform contraction.
		t_4 = torch.einsum("mlnjko, iljk -> mino", t_3, in_1)

		# No need to crop the output tensor.
		y = t_4

		return y

class kernel_generated_6(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([512, 3, 256, 3]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]

		# Perform contraction.
		t_2 = torch.einsum("ijkl -> ikjl", in_0)

		# [H]@Unfold5462ce2dd0c9bf76 -> [H]@Merge5f50103ea583163b, [k_1]@Share02da0a485106ab3d
		t_2 = torch.reshape(t_2, (1, 1, 7, 3584, ))
		t_2 = torch.nn.functional.unfold(t_2, (3, 1, ), padding=(1, 0, ))
		t_2 = torch.reshape(t_2, (1, 3, 7, 512, 7, ))

		# [C_in]@Splitf4535f3a98ce8ba2 -> [s]@Merge5f50103ea5831638, [s^-1*C_in]@Share8de6f167adbbf8aa
		t_2 = torch.reshape(t_2, (1, 3, 7, 2, 256, 7, ))

		# [H]@Merge5f50103ea583163b, [s]@Merge5f50103ea5831638 -> [s*H]@Shift3c9c8e9d3c84cb9b
		t_2 = torch.reshape(t_2, (1, 3, 14, 256, 7, ))

		# [s*H]@Shift3c9c8e9d3c84cb9b -> [s*H]@Splitdb1af055f999951a
		t_2 = torch.roll(t_2, self.shift_direction, 2)

		# [s*H]@Splitdb1af055f999951a -> [H]@Iterator96123ba3184da39c, [s]@Reduced95c644a3c072d9a
		t_2 = torch.reshape(t_2, (1, 3, 7, 2, 256, 7, ))

		# [s]@Reduce
		t_2 = torch.sum(t_2, dim=(3, ))

		# No contraction needed.
		t_3 = t_2

		# [H]@Unfold0063bc810b9e1e60 -> [H]@Iteratorb0a1def4ad5784ec, [k_1]@Share26cfa48d169008e4
		t_3 = torch.reshape(t_3, (1, 5376, 7, 1, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (1, 3, 7, 256, 3, 7, ))

		# Perform contraction.
		t_4 = torch.einsum("mlnjko, iljk -> mino", t_3, in_1)

		# No need to crop the output tensor.
		y = t_4

		return y

