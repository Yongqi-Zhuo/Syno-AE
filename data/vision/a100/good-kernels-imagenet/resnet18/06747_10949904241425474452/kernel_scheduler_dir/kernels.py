import torch
import random
"""
digraph kernel_preview {
newrank = true;

// Stage tensor.
subgraph cluster_subgraph_0 {
    label = "Subgraph 0";
    // Reductions.
    reduce_0x7f44f8004ce8 [label="Sum", shape=box];
    reduce_0x7f44f8007440 [label="Sum", shape=box];
    reduce_0x7f44f8003a98 [label="Sum", shape=box];
    // Output.
    subgraph cluster_subgraph_0_out {
        label = "";
        interface_0_out_0x5572df8cce60 [label="N", shape=none];
        interface_0_out_0x5572df8cce88 [label="C_out", shape=none];
        interface_0_out_0x5572df8cceb0 [label="H", shape=none];
        interface_0_out_0x5572df8cced8 [label="H", shape=none];
    }
    {
        rank = same;
        reduce_0x7f44f8004ce8;
        reduce_0x7f44f8007440;
        reduce_0x7f44f8003a98;
        interface_0_out_0x5572df8cce60;
        interface_0_out_0x5572df8cce88;
        interface_0_out_0x5572df8cceb0;
        interface_0_out_0x5572df8cced8;
    }
    // Input 0.
    subgraph cluster_subgraph_0_in_0 {
        label = "";
        interface_0_in_0x5572df8cce60 [label="N", shape=none];
        interface_0_in_0x5572df8cceb0 [label="H", shape=none];
        interface_0_in_0x5572e409cb70 [label="s^-1*C_in", shape=none];
        interface_0_in_0x5572e409cbc0 [label="s", shape=none];
        interface_0_in_0x5572e409cc10 [label="k_1", shape=none];
        interface_0_in_0x5572df8cced8 [label="H", shape=none];
    }
    // Input 1.
    subgraph cluster_subgraph_0_in_1 {
        label = "";
        interface_0_in_0x5572e409cb38 [label="C_out", shape=none];
        interface_0_in_0x5572e409cb88 [label="s^-1*C_in", shape=none];
        interface_0_in_0x5572e409cbd8 [label="s", shape=none];
        interface_0_in_0x5572e409cc28 [label="k_1", shape=none];
    }
    {
        rank = same;
        interface_0_in_0x5572df8cce60;
        interface_0_in_0x5572df8cceb0;
        interface_0_in_0x5572e409cb70;
        interface_0_in_0x5572e409cbc0;
        interface_0_in_0x5572e409cc10;
        interface_0_in_0x5572df8cced8;
        interface_0_in_0x5572e409cb38;
        interface_0_in_0x5572e409cb88;
        interface_0_in_0x5572e409cbd8;
        interface_0_in_0x5572e409cc28;
    }
    // Op's.
    op_0x5572e409cb00 [label="Share"];
    op_0x5572e409cb50 [label="Share"];
    op_0x5572e409cba0 [label="Share"];
    op_0x5572e409cbf0 [label="Share"];
    op_0x5572e409cfd8 [label="Expand"];
    // Dimension's.
    interface_0_in_0x5572df8cce60 -> interface_0_out_0x5572df8cce60 [label="N"];
    op_0x5572e409cb00 -> interface_0_out_0x5572df8cce88 [label="C_out"];
    interface_0_in_0x5572df8cceb0 -> interface_0_out_0x5572df8cceb0 [label="H"];
    interface_0_in_0x5572df8cced8 -> interface_0_out_0x5572df8cced8 [label="H"];
    op_0x5572e409cfd8 -> op_0x5572e409cb00 [label="C_out"];
    interface_0_in_0x5572e409cb38 -> op_0x5572e409cb00 [label="C_out"];
    interface_0_in_0x5572e409cb70 -> op_0x5572e409cb50 [label="s^-1*C_in"];
    interface_0_in_0x5572e409cb88 -> op_0x5572e409cb50 [label="s^-1*C_in"];
    interface_0_in_0x5572e409cbc0 -> op_0x5572e409cba0 [label="s"];
    interface_0_in_0x5572e409cbd8 -> op_0x5572e409cba0 [label="s"];
    interface_0_in_0x5572e409cc10 -> op_0x5572e409cbf0 [label="k_1"];
    interface_0_in_0x5572e409cc28 -> op_0x5572e409cbf0 [label="k_1"];
    op_0x5572e409cbf0 -> reduce_0x7f44f8003a98 [label="k_1"];
    op_0x5572e409cba0 -> reduce_0x7f44f8004ce8 [label="s"];
    op_0x5572e409cb50 -> reduce_0x7f44f8007440 [label="s^-1*C_in"];
}

// Stage tensor.
subgraph cluster_subgraph_1 {
    label = "Subgraph 1";
    // Reductions.
    // Output.
    subgraph cluster_subgraph_1_out {
        label = "";
        interface_1_out_0x5572df8cce60 [label="N", shape=none];
        interface_1_out_0x5572df8cceb0 [label="H", shape=none];
        interface_1_out_0x5572e409cb70 [label="s^-1*C_in", shape=none];
        interface_1_out_0x5572e409cbc0 [label="s", shape=none];
        interface_1_out_0x5572e409cc10 [label="k_1", shape=none];
        interface_1_out_0x5572df8cced8 [label="H", shape=none];
    }
    {
        rank = same;
        interface_1_out_0x5572df8cce60;
        interface_1_out_0x5572df8cceb0;
        interface_1_out_0x5572e409cb70;
        interface_1_out_0x5572e409cbc0;
        interface_1_out_0x5572e409cc10;
        interface_1_out_0x5572df8cced8;
    }
    // Input 0.
    subgraph cluster_subgraph_1_in_0 {
        label = "";
        interface_1_in_0x5572df8cce60 [label="N", shape=none];
        interface_1_in_0x5572e410cad0 [label="C_in", shape=none];
        interface_1_in_0x5572e40a54e0 [label="H", shape=none];
        interface_1_in_0x5572e409ece0 [label="H", shape=none];
    }
    {
        rank = same;
        interface_1_in_0x5572df8cce60;
        interface_1_in_0x5572e410cad0;
        interface_1_in_0x5572e40a54e0;
        interface_1_in_0x5572e409ece0;
    }
    // Op's.
    op_0x5572e409ecc0 [label="Shift"];
    op_0x5572e409ee70 [label="Shift"];
    op_0x5572e40a54a0 [label="Merge"];
    op_0x5572e40b1e40 [label="Unfold"];
    op_0x5572e410c4f0 [label="Split"];
    op_0x5572e410ca90 [label="Split"];
    // Dimension's.
    interface_1_in_0x5572df8cce60 -> interface_1_out_0x5572df8cce60 [label="N"];
    op_0x5572e410c4f0 -> interface_1_out_0x5572df8cceb0 [label="H"];
    op_0x5572e40b1e40 -> interface_1_out_0x5572df8cced8 [label="H"];
    op_0x5572e410ca90 -> interface_1_out_0x5572e409cb70 [label="s^-1*C_in"];
    op_0x5572e410c4f0 -> interface_1_out_0x5572e409cbc0 [label="s"];
    op_0x5572e40b1e40 -> interface_1_out_0x5572e409cc10 [label="k_1"];
    interface_1_in_0x5572e409ece0 -> op_0x5572e409ecc0 [label="H"];
    op_0x5572e40a54a0 -> op_0x5572e409ee70 [label="s*H"];
    interface_1_in_0x5572e40a54e0 -> op_0x5572e40a54a0 [label="H"];
    op_0x5572e410ca90 -> op_0x5572e40a54a0 [label="s"];
    op_0x5572e409ecc0 -> op_0x5572e40b1e40 [label="H"];
    op_0x5572e409ee70 -> op_0x5572e410c4f0 [label="s*H"];
    interface_1_in_0x5572e410cad0 -> op_0x5572e410ca90 [label="C_in"];
}

// Input tensor.
subgraph cluster_subgraph_2 {
    label = "Input 0";
    interface_2_out_0x5572df8cce60 [label="N", shape=none];
    interface_2_out_0x5572e410cad0 [label="C_in", shape=none];
    interface_2_out_0x5572e40a54e0 [label="H", shape=none];
    interface_2_out_0x5572e409ece0 [label="H", shape=none];
}

interface_2_out_0x5572df8cce60 -> interface_1_in_0x5572df8cce60;
interface_2_out_0x5572e410cad0 -> interface_1_in_0x5572e410cad0;
interface_2_out_0x5572e40a54e0 -> interface_1_in_0x5572e40a54e0;
interface_2_out_0x5572e409ece0 -> interface_1_in_0x5572e409ece0;

interface_1_out_0x5572df8cce60 -> interface_0_in_0x5572df8cce60;
interface_1_out_0x5572df8cceb0 -> interface_0_in_0x5572df8cceb0;
interface_1_out_0x5572e409cb70 -> interface_0_in_0x5572e409cb70;
interface_1_out_0x5572e409cbc0 -> interface_0_in_0x5572e409cbc0;
interface_1_out_0x5572e409cc10 -> interface_0_in_0x5572e409cc10;
interface_1_out_0x5572df8cced8 -> interface_0_in_0x5572df8cced8;

// Input tensor.
subgraph cluster_subgraph_3 {
    label = "Input 1";
    interface_3_out_0x5572e409cb38 [label="C_out", shape=none];
    interface_3_out_0x5572e409cb88 [label="s^-1*C_in", shape=none];
    interface_3_out_0x5572e409cbd8 [label="s", shape=none];
    interface_3_out_0x5572e409cc28 [label="k_1", shape=none];
}

interface_3_out_0x5572e409cb38 -> interface_0_in_0x5572e409cb38;
interface_3_out_0x5572e409cb88 -> interface_0_in_0x5572e409cb88;
interface_3_out_0x5572e409cbd8 -> interface_0_in_0x5572e409cbd8;
interface_3_out_0x5572e409cc28 -> interface_0_in_0x5572e409cc28;

{
    rank = same;
    interface_2_out_0x5572df8cce60;
    interface_2_out_0x5572e410cad0;
    interface_2_out_0x5572e40a54e0;
    interface_2_out_0x5572e409ece0;
    interface_3_out_0x5572e409cb38;
    interface_3_out_0x5572e409cb88;
    interface_3_out_0x5572e409cbd8;
    interface_3_out_0x5572e409cc28;
}
subgraph cluster_subgraph_output {
    label = "Output";
    interface_4_in_0x5572df8cce60 [label="N", shape=none];
    interface_4_in_0x5572df8cce88 [label="C_out", shape=none];
    interface_4_in_0x5572df8cceb0 [label="H", shape=none];
    interface_4_in_0x5572df8cced8 [label="H", shape=none];
}
interface_0_out_0x5572df8cce60 -> interface_4_in_0x5572df8cce60;
interface_0_out_0x5572df8cce88 -> interface_4_in_0x5572df8cce88;
interface_0_out_0x5572df8cceb0 -> interface_4_in_0x5572df8cceb0;
interface_0_out_0x5572df8cced8 -> interface_4_in_0x5572df8cced8;

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

