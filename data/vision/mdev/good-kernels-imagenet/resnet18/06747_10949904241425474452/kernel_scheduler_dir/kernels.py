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
        reduce_0x7f3cd0004ce8;
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
        interface_0_in_0x560f6c4cbf20 [label="H", shape=none];
        interface_0_in_0x560f70f801f0 [label="s^-1*C_in", shape=none];
        interface_0_in_0x560f70f80240 [label="s", shape=none];
        interface_0_in_0x560f70f80290 [label="k_1", shape=none];
        interface_0_in_0x560f6c4cbf48 [label="H", shape=none];
    }
    // Input 1.
    subgraph cluster_subgraph_0_in_1 {
        label = "";
        interface_0_in_0x560f70f801b8 [label="C_out", shape=none];
        interface_0_in_0x560f70f80208 [label="s^-1*C_in", shape=none];
        interface_0_in_0x560f70f80258 [label="s", shape=none];
        interface_0_in_0x560f70f802a8 [label="k_1", shape=none];
    }
    {
        rank = same;
        interface_0_in_0x560f6c4cbed0;
        interface_0_in_0x560f6c4cbf20;
        interface_0_in_0x560f70f801f0;
        interface_0_in_0x560f70f80240;
        interface_0_in_0x560f70f80290;
        interface_0_in_0x560f6c4cbf48;
        interface_0_in_0x560f70f801b8;
        interface_0_in_0x560f70f80208;
        interface_0_in_0x560f70f80258;
        interface_0_in_0x560f70f802a8;
    }
    // Op's.
    op_0x560f70f80180 [label="Share"];
    op_0x560f70f801d0 [label="Share"];
    op_0x560f70f80220 [label="Share"];
    op_0x560f70f80270 [label="Share"];
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
    interface_0_in_0x560f70f80240 -> op_0x560f70f80220 [label="s"];
    interface_0_in_0x560f70f80258 -> op_0x560f70f80220 [label="s"];
    interface_0_in_0x560f70f80290 -> op_0x560f70f80270 [label="k_1"];
    interface_0_in_0x560f70f802a8 -> op_0x560f70f80270 [label="k_1"];
    op_0x560f70f80270 -> reduce_0x7f3cd0003a98 [label="k_1"];
    op_0x560f70f80220 -> reduce_0x7f3cd0004ce8 [label="s"];
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
        interface_1_out_0x560f6c4cbf20 [label="H", shape=none];
        interface_1_out_0x560f70f801f0 [label="s^-1*C_in", shape=none];
        interface_1_out_0x560f70f80240 [label="s", shape=none];
        interface_1_out_0x560f70f80290 [label="k_1", shape=none];
        interface_1_out_0x560f6c4cbf48 [label="H", shape=none];
    }
    {
        rank = same;
        interface_1_out_0x560f6c4cbed0;
        interface_1_out_0x560f6c4cbf20;
        interface_1_out_0x560f70f801f0;
        interface_1_out_0x560f70f80240;
        interface_1_out_0x560f70f80290;
        interface_1_out_0x560f6c4cbf48;
    }
    // Input 0.
    subgraph cluster_subgraph_1_in_0 {
        label = "";
        interface_1_in_0x560f6c4cbed0 [label="N", shape=none];
        interface_1_in_0x560f70ff4150 [label="C_in", shape=none];
        interface_1_in_0x560f70f89160 [label="H", shape=none];
        interface_1_in_0x560f70f81020 [label="H", shape=none];
    }
    {
        rank = same;
        interface_1_in_0x560f6c4cbed0;
        interface_1_in_0x560f70ff4150;
        interface_1_in_0x560f70f89160;
        interface_1_in_0x560f70f81020;
    }
    // Op's.
    op_0x560f70f81000 [label="Shift"];
    op_0x560f70f811b0 [label="Shift"];
    op_0x560f70f89120 [label="Merge"];
    op_0x560f70f92e00 [label="Unfold"];
    op_0x560f70ff3b70 [label="Split"];
    op_0x560f70ff4110 [label="Split"];
    // Dimension's.
    interface_1_in_0x560f6c4cbed0 -> interface_1_out_0x560f6c4cbed0 [label="N"];
    op_0x560f70ff3b70 -> interface_1_out_0x560f6c4cbf20 [label="H"];
    op_0x560f70f92e00 -> interface_1_out_0x560f6c4cbf48 [label="H"];
    op_0x560f70ff4110 -> interface_1_out_0x560f70f801f0 [label="s^-1*C_in"];
    op_0x560f70ff3b70 -> interface_1_out_0x560f70f80240 [label="s"];
    op_0x560f70f92e00 -> interface_1_out_0x560f70f80290 [label="k_1"];
    interface_1_in_0x560f70f81020 -> op_0x560f70f81000 [label="H"];
    op_0x560f70f89120 -> op_0x560f70f811b0 [label="s*H"];
    interface_1_in_0x560f70f89160 -> op_0x560f70f89120 [label="H"];
    op_0x560f70ff4110 -> op_0x560f70f89120 [label="s"];
    op_0x560f70f81000 -> op_0x560f70f92e00 [label="H"];
    op_0x560f70f811b0 -> op_0x560f70ff3b70 [label="s*H"];
    interface_1_in_0x560f70ff4150 -> op_0x560f70ff4110 [label="C_in"];
}

// Input tensor.
subgraph cluster_subgraph_2 {
    label = "Input 0";
    interface_2_out_0x560f6c4cbed0 [label="N", shape=none];
    interface_2_out_0x560f70ff4150 [label="C_in", shape=none];
    interface_2_out_0x560f70f89160 [label="H", shape=none];
    interface_2_out_0x560f70f81020 [label="H", shape=none];
}

interface_2_out_0x560f6c4cbed0 -> interface_1_in_0x560f6c4cbed0;
interface_2_out_0x560f70ff4150 -> interface_1_in_0x560f70ff4150;
interface_2_out_0x560f70f89160 -> interface_1_in_0x560f70f89160;
interface_2_out_0x560f70f81020 -> interface_1_in_0x560f70f81020;

interface_1_out_0x560f6c4cbed0 -> interface_0_in_0x560f6c4cbed0;
interface_1_out_0x560f6c4cbf20 -> interface_0_in_0x560f6c4cbf20;
interface_1_out_0x560f70f801f0 -> interface_0_in_0x560f70f801f0;
interface_1_out_0x560f70f80240 -> interface_0_in_0x560f70f80240;
interface_1_out_0x560f70f80290 -> interface_0_in_0x560f70f80290;
interface_1_out_0x560f6c4cbf48 -> interface_0_in_0x560f6c4cbf48;

// Input tensor.
subgraph cluster_subgraph_3 {
    label = "Input 1";
    interface_3_out_0x560f70f801b8 [label="C_out", shape=none];
    interface_3_out_0x560f70f80208 [label="s^-1*C_in", shape=none];
    interface_3_out_0x560f70f80258 [label="s", shape=none];
    interface_3_out_0x560f70f802a8 [label="k_1", shape=none];
}

interface_3_out_0x560f70f801b8 -> interface_0_in_0x560f70f801b8;
interface_3_out_0x560f70f80208 -> interface_0_in_0x560f70f80208;
interface_3_out_0x560f70f80258 -> interface_0_in_0x560f70f80258;
interface_3_out_0x560f70f802a8 -> interface_0_in_0x560f70f802a8;

{
    rank = same;
    interface_2_out_0x560f6c4cbed0;
    interface_2_out_0x560f70ff4150;
    interface_2_out_0x560f70f89160;
    interface_2_out_0x560f70f81020;
    interface_3_out_0x560f70f801b8;
    interface_3_out_0x560f70f80208;
    interface_3_out_0x560f70f80258;
    interface_3_out_0x560f70f802a8;
}
subgraph cluster_subgraph_output {
    label = "Output";
    interface_4_in_0x560f6c4cbed0 [label="N", shape=none];
    interface_4_in_0x560f6c4cbef8 [label="C_out", shape=none];
    interface_4_in_0x560f6c4cbf20 [label="H", shape=none];
    interface_4_in_0x560f6c4cbf48 [label="H", shape=none];
}
interface_0_out_0x560f6c4cbed0 -> interface_4_in_0x560f6c4cbed0;
interface_0_out_0x560f6c4cbef8 -> interface_4_in_0x560f6c4cbef8;
interface_0_out_0x560f6c4cbf20 -> interface_4_in_0x560f6c4cbf20;
interface_0_out_0x560f6c4cbf48 -> interface_4_in_0x560f6c4cbf48;

}

"""
class kernel_generated_0(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([64, 32, 2, 3]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]

		# Perform contraction.
		t_2 = torch.einsum("ilkj -> iklj", in_0)

		# [C_in]@Spliteef7ce0b7703d88a -> [s]@Merge6f1a0d6b662fae85, [s^-1*C_in]@Share8de6f167adbbf8aa
		t_2 = torch.reshape(t_2, (1, 56, 2, 32, 56, ))

		# [H]@Merge6f1a0d6b662fae84, [s]@Merge6f1a0d6b662fae85 -> [s*H]@Shift594e1a6314829db7
		t_2 = torch.reshape(t_2, (1, 112, 32, 56, ))

		# [s*H]@Shift594e1a6314829db7 -> [s*H]@Split7ee86503d19bbef6
		t_2 = torch.roll(t_2, self.shift_direction, 1)

		# [s*H]@Split7ee86503d19bbef6 -> [H]@Iterator96123ba3184da39c, [s]@Shareb15a7faee0f8b868
		t_2 = torch.reshape(t_2, (1, 56, 2, 32, 56, ))

		# [H]@Shiftdbd5b2e652804221 -> [H]@Unfold0063bc810b9e1e60
		t_2 = torch.roll(t_2, self.shift_direction, 4)

		# [H]@Unfold0063bc810b9e1e60 -> [H]@Iteratorb0a1def4ad5784ec, [k_1]@Share26cfa48d169008e4
		t_2 = torch.reshape(t_2, (1, 3584, 56, 1, ))
		t_2 = torch.nn.functional.unfold(t_2, (3, 1, ), padding=(1, 0, ))
		t_2 = torch.reshape(t_2, (1, 56, 2, 32, 3, 56, ))

		# Permute to match the output of this subgraph.
		t_2 = torch.permute(t_2, (0, 1, 3, 2, 4, 5, ))

		# Perform contraction.
		t_3 = torch.einsum("mnjklo, ijkl -> mino", t_2, in_1)

		# No need to crop the output tensor.
		y = t_3

		return y

class kernel_generated_1(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([128, 32, 2, 3]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]

		# Perform contraction.
		t_2 = torch.einsum("ilkj -> iklj", in_0)

		# [C_in]@Spliteef7ce0b7703d88a -> [s]@Merge6f1a0d6b662fae85, [s^-1*C_in]@Share8de6f167adbbf8aa
		t_2 = torch.reshape(t_2, (1, 28, 2, 32, 28, ))

		# [H]@Merge6f1a0d6b662fae84, [s]@Merge6f1a0d6b662fae85 -> [s*H]@Shift594e1a6314829db7
		t_2 = torch.reshape(t_2, (1, 56, 32, 28, ))

		# [s*H]@Shift594e1a6314829db7 -> [s*H]@Split7ee86503d19bbef6
		t_2 = torch.roll(t_2, self.shift_direction, 1)

		# [s*H]@Split7ee86503d19bbef6 -> [H]@Iterator96123ba3184da39c, [s]@Shareb15a7faee0f8b868
		t_2 = torch.reshape(t_2, (1, 28, 2, 32, 28, ))

		# [H]@Shiftdbd5b2e652804221 -> [H]@Unfold0063bc810b9e1e60
		t_2 = torch.roll(t_2, self.shift_direction, 4)

		# [H]@Unfold0063bc810b9e1e60 -> [H]@Iteratorb0a1def4ad5784ec, [k_1]@Share26cfa48d169008e4
		t_2 = torch.reshape(t_2, (1, 1792, 28, 1, ))
		t_2 = torch.nn.functional.unfold(t_2, (3, 1, ), padding=(1, 0, ))
		t_2 = torch.reshape(t_2, (1, 28, 2, 32, 3, 28, ))

		# Permute to match the output of this subgraph.
		t_2 = torch.permute(t_2, (0, 1, 3, 2, 4, 5, ))

		# Perform contraction.
		t_3 = torch.einsum("mnjklo, ijkl -> mino", t_2, in_1)

		# No need to crop the output tensor.
		y = t_3

		return y

class kernel_generated_2(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([128, 64, 2, 3]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]

		# Perform contraction.
		t_2 = torch.einsum("ilkj -> iklj", in_0)

		# [C_in]@Spliteef7ce0b7703d88a -> [s]@Merge6f1a0d6b662fae85, [s^-1*C_in]@Share8de6f167adbbf8aa
		t_2 = torch.reshape(t_2, (1, 28, 2, 64, 28, ))

		# [H]@Merge6f1a0d6b662fae84, [s]@Merge6f1a0d6b662fae85 -> [s*H]@Shift594e1a6314829db7
		t_2 = torch.reshape(t_2, (1, 56, 64, 28, ))

		# [s*H]@Shift594e1a6314829db7 -> [s*H]@Split7ee86503d19bbef6
		t_2 = torch.roll(t_2, self.shift_direction, 1)

		# [s*H]@Split7ee86503d19bbef6 -> [H]@Iterator96123ba3184da39c, [s]@Shareb15a7faee0f8b868
		t_2 = torch.reshape(t_2, (1, 28, 2, 64, 28, ))

		# [H]@Shiftdbd5b2e652804221 -> [H]@Unfold0063bc810b9e1e60
		t_2 = torch.roll(t_2, self.shift_direction, 4)

		# [H]@Unfold0063bc810b9e1e60 -> [H]@Iteratorb0a1def4ad5784ec, [k_1]@Share26cfa48d169008e4
		t_2 = torch.reshape(t_2, (1, 3584, 28, 1, ))
		t_2 = torch.nn.functional.unfold(t_2, (3, 1, ), padding=(1, 0, ))
		t_2 = torch.reshape(t_2, (1, 28, 2, 64, 3, 28, ))

		# Permute to match the output of this subgraph.
		t_2 = torch.permute(t_2, (0, 1, 3, 2, 4, 5, ))

		# Perform contraction.
		t_3 = torch.einsum("mnjklo, ijkl -> mino", t_2, in_1)

		# No need to crop the output tensor.
		y = t_3

		return y

class kernel_generated_3(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([256, 64, 2, 3]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]

		# Perform contraction.
		t_2 = torch.einsum("ilkj -> iklj", in_0)

		# [C_in]@Spliteef7ce0b7703d88a -> [s]@Merge6f1a0d6b662fae85, [s^-1*C_in]@Share8de6f167adbbf8aa
		t_2 = torch.reshape(t_2, (1, 14, 2, 64, 14, ))

		# [H]@Merge6f1a0d6b662fae84, [s]@Merge6f1a0d6b662fae85 -> [s*H]@Shift594e1a6314829db7
		t_2 = torch.reshape(t_2, (1, 28, 64, 14, ))

		# [s*H]@Shift594e1a6314829db7 -> [s*H]@Split7ee86503d19bbef6
		t_2 = torch.roll(t_2, self.shift_direction, 1)

		# [s*H]@Split7ee86503d19bbef6 -> [H]@Iterator96123ba3184da39c, [s]@Shareb15a7faee0f8b868
		t_2 = torch.reshape(t_2, (1, 14, 2, 64, 14, ))

		# [H]@Shiftdbd5b2e652804221 -> [H]@Unfold0063bc810b9e1e60
		t_2 = torch.roll(t_2, self.shift_direction, 4)

		# [H]@Unfold0063bc810b9e1e60 -> [H]@Iteratorb0a1def4ad5784ec, [k_1]@Share26cfa48d169008e4
		t_2 = torch.reshape(t_2, (1, 1792, 14, 1, ))
		t_2 = torch.nn.functional.unfold(t_2, (3, 1, ), padding=(1, 0, ))
		t_2 = torch.reshape(t_2, (1, 14, 2, 64, 3, 14, ))

		# Permute to match the output of this subgraph.
		t_2 = torch.permute(t_2, (0, 1, 3, 2, 4, 5, ))

		# Perform contraction.
		t_3 = torch.einsum("mnjklo, ijkl -> mino", t_2, in_1)

		# No need to crop the output tensor.
		y = t_3

		return y

class kernel_generated_4(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([256, 128, 2, 3]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]

		# Perform contraction.
		t_2 = torch.einsum("ilkj -> iklj", in_0)

		# [C_in]@Spliteef7ce0b7703d88a -> [s]@Merge6f1a0d6b662fae85, [s^-1*C_in]@Share8de6f167adbbf8aa
		t_2 = torch.reshape(t_2, (1, 14, 2, 128, 14, ))

		# [H]@Merge6f1a0d6b662fae84, [s]@Merge6f1a0d6b662fae85 -> [s*H]@Shift594e1a6314829db7
		t_2 = torch.reshape(t_2, (1, 28, 128, 14, ))

		# [s*H]@Shift594e1a6314829db7 -> [s*H]@Split7ee86503d19bbef6
		t_2 = torch.roll(t_2, self.shift_direction, 1)

		# [s*H]@Split7ee86503d19bbef6 -> [H]@Iterator96123ba3184da39c, [s]@Shareb15a7faee0f8b868
		t_2 = torch.reshape(t_2, (1, 14, 2, 128, 14, ))

		# [H]@Shiftdbd5b2e652804221 -> [H]@Unfold0063bc810b9e1e60
		t_2 = torch.roll(t_2, self.shift_direction, 4)

		# [H]@Unfold0063bc810b9e1e60 -> [H]@Iteratorb0a1def4ad5784ec, [k_1]@Share26cfa48d169008e4
		t_2 = torch.reshape(t_2, (1, 3584, 14, 1, ))
		t_2 = torch.nn.functional.unfold(t_2, (3, 1, ), padding=(1, 0, ))
		t_2 = torch.reshape(t_2, (1, 14, 2, 128, 3, 14, ))

		# Permute to match the output of this subgraph.
		t_2 = torch.permute(t_2, (0, 1, 3, 2, 4, 5, ))

		# Perform contraction.
		t_3 = torch.einsum("mnjklo, ijkl -> mino", t_2, in_1)

		# No need to crop the output tensor.
		y = t_3

		return y

class kernel_generated_5(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([512, 128, 2, 3]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]

		# Perform contraction.
		t_2 = torch.einsum("ilkj -> iklj", in_0)

		# [C_in]@Spliteef7ce0b7703d88a -> [s]@Merge6f1a0d6b662fae85, [s^-1*C_in]@Share8de6f167adbbf8aa
		t_2 = torch.reshape(t_2, (1, 7, 2, 128, 7, ))

		# [H]@Merge6f1a0d6b662fae84, [s]@Merge6f1a0d6b662fae85 -> [s*H]@Shift594e1a6314829db7
		t_2 = torch.reshape(t_2, (1, 14, 128, 7, ))

		# [s*H]@Shift594e1a6314829db7 -> [s*H]@Split7ee86503d19bbef6
		t_2 = torch.roll(t_2, self.shift_direction, 1)

		# [s*H]@Split7ee86503d19bbef6 -> [H]@Iterator96123ba3184da39c, [s]@Shareb15a7faee0f8b868
		t_2 = torch.reshape(t_2, (1, 7, 2, 128, 7, ))

		# [H]@Shiftdbd5b2e652804221 -> [H]@Unfold0063bc810b9e1e60
		t_2 = torch.roll(t_2, self.shift_direction, 4)

		# [H]@Unfold0063bc810b9e1e60 -> [H]@Iteratorb0a1def4ad5784ec, [k_1]@Share26cfa48d169008e4
		t_2 = torch.reshape(t_2, (1, 1792, 7, 1, ))
		t_2 = torch.nn.functional.unfold(t_2, (3, 1, ), padding=(1, 0, ))
		t_2 = torch.reshape(t_2, (1, 7, 2, 128, 3, 7, ))

		# Permute to match the output of this subgraph.
		t_2 = torch.permute(t_2, (0, 1, 3, 2, 4, 5, ))

		# Perform contraction.
		t_3 = torch.einsum("mnjklo, ijkl -> mino", t_2, in_1)

		# No need to crop the output tensor.
		y = t_3

		return y

class kernel_generated_6(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([512, 256, 2, 3]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]

		# Perform contraction.
		t_2 = torch.einsum("ilkj -> iklj", in_0)

		# [C_in]@Spliteef7ce0b7703d88a -> [s]@Merge6f1a0d6b662fae85, [s^-1*C_in]@Share8de6f167adbbf8aa
		t_2 = torch.reshape(t_2, (1, 7, 2, 256, 7, ))

		# [H]@Merge6f1a0d6b662fae84, [s]@Merge6f1a0d6b662fae85 -> [s*H]@Shift594e1a6314829db7
		t_2 = torch.reshape(t_2, (1, 14, 256, 7, ))

		# [s*H]@Shift594e1a6314829db7 -> [s*H]@Split7ee86503d19bbef6
		t_2 = torch.roll(t_2, self.shift_direction, 1)

		# [s*H]@Split7ee86503d19bbef6 -> [H]@Iterator96123ba3184da39c, [s]@Shareb15a7faee0f8b868
		t_2 = torch.reshape(t_2, (1, 7, 2, 256, 7, ))

		# [H]@Shiftdbd5b2e652804221 -> [H]@Unfold0063bc810b9e1e60
		t_2 = torch.roll(t_2, self.shift_direction, 4)

		# [H]@Unfold0063bc810b9e1e60 -> [H]@Iteratorb0a1def4ad5784ec, [k_1]@Share26cfa48d169008e4
		t_2 = torch.reshape(t_2, (1, 3584, 7, 1, ))
		t_2 = torch.nn.functional.unfold(t_2, (3, 1, ), padding=(1, 0, ))
		t_2 = torch.reshape(t_2, (1, 7, 2, 256, 3, 7, ))

		# Permute to match the output of this subgraph.
		t_2 = torch.permute(t_2, (0, 1, 3, 2, 4, 5, ))

		# Perform contraction.
		t_3 = torch.einsum("mnjklo, ijkl -> mino", t_2, in_1)

		# No need to crop the output tensor.
		y = t_3

		return y

