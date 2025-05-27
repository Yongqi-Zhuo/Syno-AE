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
        interface_0_out_0x560f6c4cbed0 [label="N", shape=none];
        interface_0_out_0x560f6c4cbef8 [label="C_out", shape=none];
        interface_0_out_0x560f6c4cbf20 [label="H", shape=none];
        interface_0_out_0x560f6c4cbf48 [label="H", shape=none];
    }
    {
        rank = same;
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
        interface_0_in_0x560f70f80ea0 [label="H", shape=none];
        interface_0_in_0x560f6c4cbf48 [label="H", shape=none];
    }
    {
        rank = same;
        interface_0_in_0x560f6c4cbed0;
        interface_0_in_0x560f6c4cbef8;
        interface_0_in_0x560f70f80ea0;
        interface_0_in_0x560f6c4cbf48;
    }
    // Op's.
    op_0x560f70f80e80 [label="Shift"];
    // Dimension's.
    interface_0_in_0x560f6c4cbed0 -> interface_0_out_0x560f6c4cbed0 [label="N"];
    interface_0_in_0x560f6c4cbef8 -> interface_0_out_0x560f6c4cbef8 [label="C_out"];
    op_0x560f70f80e80 -> interface_0_out_0x560f6c4cbf20 [label="H"];
    interface_0_in_0x560f6c4cbf48 -> interface_0_out_0x560f6c4cbf48 [label="H"];
    interface_0_in_0x560f70f80ea0 -> op_0x560f70f80e80 [label="H"];
}

// Stage tensor.
subgraph cluster_subgraph_1 {
    label = "Subgraph 1";
    // Reductions.
    reduce_0x7f3cd0004ce8 [label="Sum", shape=box];
    // Output.
    subgraph cluster_subgraph_1_out {
        label = "";
        interface_1_out_0x560f6c4cbed0 [label="N", shape=none];
        interface_1_out_0x560f6c4cbef8 [label="C_out", shape=none];
        interface_1_out_0x560f70f80ea0 [label="H", shape=none];
        interface_1_out_0x560f6c4cbf48 [label="H", shape=none];
    }
    {
        rank = same;
        reduce_0x7f3cd0004ce8;
        interface_1_out_0x560f6c4cbed0;
        interface_1_out_0x560f6c4cbef8;
        interface_1_out_0x560f70f80ea0;
        interface_1_out_0x560f6c4cbf48;
    }
    // Input 0.
    subgraph cluster_subgraph_1_in_0 {
        label = "";
        interface_1_in_0x560f6c4cbed0 [label="N", shape=none];
        interface_1_in_0x560f6c4cbef8 [label="C_out", shape=none];
        interface_1_in_0x560f71035130 [label="H", shape=none];
        interface_1_in_0x560f71035148 [label="s", shape=none];
        interface_1_in_0x560f6c4cbf48 [label="H", shape=none];
    }
    {
        rank = same;
        interface_1_in_0x560f6c4cbed0;
        interface_1_in_0x560f6c4cbef8;
        interface_1_in_0x560f71035130;
        interface_1_in_0x560f71035148;
        interface_1_in_0x560f6c4cbf48;
    }
    // Op's.
    op_0x560f70f811e0 [label="Shift"];
    op_0x560f70ff4610 [label="Split"];
    op_0x560f710350f0 [label="Merge"];
    // Dimension's.
    interface_1_in_0x560f6c4cbed0 -> interface_1_out_0x560f6c4cbed0 [label="N"];
    interface_1_in_0x560f6c4cbef8 -> interface_1_out_0x560f6c4cbef8 [label="C_out"];
    interface_1_in_0x560f6c4cbf48 -> interface_1_out_0x560f6c4cbf48 [label="H"];
    op_0x560f70ff4610 -> interface_1_out_0x560f70f80ea0 [label="H"];
    op_0x560f710350f0 -> op_0x560f70f811e0 [label="s*H"];
    op_0x560f70f811e0 -> op_0x560f70ff4610 [label="s*H"];
    interface_1_in_0x560f71035130 -> op_0x560f710350f0 [label="H"];
    interface_1_in_0x560f71035148 -> op_0x560f710350f0 [label="s"];
    op_0x560f70ff4610 -> reduce_0x7f3cd0004ce8 [label="s"];
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
        interface_2_out_0x560f6c4cbef8 [label="C_out", shape=none];
        interface_2_out_0x560f71035130 [label="H", shape=none];
        interface_2_out_0x560f71035148 [label="s", shape=none];
        interface_2_out_0x560f6c4cbf48 [label="H", shape=none];
    }
    {
        rank = same;
        reduce_0x7f3cd0007948;
        reduce_0x7f3cd0003a98;
        interface_2_out_0x560f6c4cbed0;
        interface_2_out_0x560f6c4cbef8;
        interface_2_out_0x560f71035130;
        interface_2_out_0x560f71035148;
        interface_2_out_0x560f6c4cbf48;
    }
    // Input 0.
    subgraph cluster_subgraph_2_in_0 {
        label = "";
        interface_2_in_0x560f6c4cbed0 [label="N", shape=none];
        interface_2_in_0x560f70faccc0 [label="C_in", shape=none];
        interface_2_in_0x560f71035130 [label="H", shape=none];
        interface_2_in_0x560f70f80290 [label="k_1", shape=none];
        interface_2_in_0x560f6c4cbf48 [label="H", shape=none];
    }
    // Input 1.
    subgraph cluster_subgraph_2_in_1 {
        label = "";
        interface_2_in_0x560f70f801b8 [label="C_out", shape=none];
        interface_2_in_0x560f70faccd8 [label="C_in", shape=none];
        interface_2_in_0x560f70facd28 [label="s", shape=none];
        interface_2_in_0x560f70f802a8 [label="k_1", shape=none];
    }
    {
        rank = same;
        interface_2_in_0x560f6c4cbed0;
        interface_2_in_0x560f70faccc0;
        interface_2_in_0x560f71035130;
        interface_2_in_0x560f70f80290;
        interface_2_in_0x560f6c4cbf48;
        interface_2_in_0x560f70f801b8;
        interface_2_in_0x560f70faccd8;
        interface_2_in_0x560f70facd28;
        interface_2_in_0x560f70f802a8;
    }
    // Op's.
    op_0x560f70f80180 [label="Share"];
    op_0x560f70f80270 [label="Share"];
    op_0x560f70f80658 [label="Expand"];
    op_0x560f70f806d8 [label="Expand"];
    op_0x560f70facca0 [label="Share"];
    op_0x560f70faccf0 [label="Share"];
    // Dimension's.
    interface_2_in_0x560f6c4cbed0 -> interface_2_out_0x560f6c4cbed0 [label="N"];
    op_0x560f70f80180 -> interface_2_out_0x560f6c4cbef8 [label="C_out"];
    interface_2_in_0x560f6c4cbf48 -> interface_2_out_0x560f6c4cbf48 [label="H"];
    op_0x560f70f80658 -> op_0x560f70f80180 [label="C_out"];
    interface_2_in_0x560f70f801b8 -> op_0x560f70f80180 [label="C_out"];
    interface_2_in_0x560f70f80290 -> op_0x560f70f80270 [label="k_1"];
    interface_2_in_0x560f70f802a8 -> op_0x560f70f80270 [label="k_1"];
    interface_2_in_0x560f70faccc0 -> op_0x560f70facca0 [label="C_in"];
    interface_2_in_0x560f70faccd8 -> op_0x560f70facca0 [label="C_in"];
    op_0x560f70f806d8 -> op_0x560f70faccf0 [label="s"];
    interface_2_in_0x560f70facd28 -> op_0x560f70faccf0 [label="s"];
    interface_2_in_0x560f71035130 -> interface_2_out_0x560f71035130 [label="H"];
    op_0x560f70faccf0 -> interface_2_out_0x560f71035148 [label="s"];
    op_0x560f70f80270 -> reduce_0x7f3cd0003a98 [label="k_1"];
    op_0x560f70facca0 -> reduce_0x7f3cd0007948 [label="C_in"];
}

// Stage tensor.
subgraph cluster_subgraph_3 {
    label = "Subgraph 3";
    // Reductions.
    // Output.
    subgraph cluster_subgraph_3_out {
        label = "";
        interface_3_out_0x560f6c4cbed0 [label="N", shape=none];
        interface_3_out_0x560f70faccc0 [label="C_in", shape=none];
        interface_3_out_0x560f71035130 [label="H", shape=none];
        interface_3_out_0x560f70f80290 [label="k_1", shape=none];
        interface_3_out_0x560f6c4cbf48 [label="H", shape=none];
    }
    {
        rank = same;
        interface_3_out_0x560f6c4cbed0;
        interface_3_out_0x560f70faccc0;
        interface_3_out_0x560f71035130;
        interface_3_out_0x560f70f80290;
        interface_3_out_0x560f6c4cbf48;
    }
    // Input 0.
    subgraph cluster_subgraph_3_in_0 {
        label = "";
        interface_3_in_0x560f6c4cbed0 [label="N", shape=none];
        interface_3_in_0x560f70faccc0 [label="C_in", shape=none];
        interface_3_in_0x560f71035130 [label="H", shape=none];
        interface_3_in_0x560f70f92e28 [label="H", shape=none];
    }
    {
        rank = same;
        interface_3_in_0x560f6c4cbed0;
        interface_3_in_0x560f70faccc0;
        interface_3_in_0x560f71035130;
        interface_3_in_0x560f70f92e28;
    }
    // Op's.
    op_0x560f70f92e00 [label="Unfold"];
    // Dimension's.
    interface_3_in_0x560f6c4cbed0 -> interface_3_out_0x560f6c4cbed0 [label="N"];
    op_0x560f70f92e00 -> interface_3_out_0x560f6c4cbf48 [label="H"];
    op_0x560f70f92e00 -> interface_3_out_0x560f70f80290 [label="k_1"];
    interface_3_in_0x560f70f92e28 -> op_0x560f70f92e00 [label="H"];
    interface_3_in_0x560f70faccc0 -> interface_3_out_0x560f70faccc0 [label="C_in"];
    interface_3_in_0x560f71035130 -> interface_3_out_0x560f71035130 [label="H"];
}

// Input tensor.
subgraph cluster_subgraph_4 {
    label = "Input 0";
    interface_4_out_0x560f6c4cbed0 [label="N", shape=none];
    interface_4_out_0x560f70faccc0 [label="C_in", shape=none];
    interface_4_out_0x560f71035130 [label="H", shape=none];
    interface_4_out_0x560f70f92e28 [label="H", shape=none];
}

interface_4_out_0x560f6c4cbed0 -> interface_3_in_0x560f6c4cbed0;
interface_4_out_0x560f70faccc0 -> interface_3_in_0x560f70faccc0;
interface_4_out_0x560f71035130 -> interface_3_in_0x560f71035130;
interface_4_out_0x560f70f92e28 -> interface_3_in_0x560f70f92e28;

interface_3_out_0x560f6c4cbed0 -> interface_2_in_0x560f6c4cbed0;
interface_3_out_0x560f70faccc0 -> interface_2_in_0x560f70faccc0;
interface_3_out_0x560f71035130 -> interface_2_in_0x560f71035130;
interface_3_out_0x560f70f80290 -> interface_2_in_0x560f70f80290;
interface_3_out_0x560f6c4cbf48 -> interface_2_in_0x560f6c4cbf48;

// Input tensor.
subgraph cluster_subgraph_5 {
    label = "Input 1";
    interface_5_out_0x560f70f801b8 [label="C_out", shape=none];
    interface_5_out_0x560f70faccd8 [label="C_in", shape=none];
    interface_5_out_0x560f70facd28 [label="s", shape=none];
    interface_5_out_0x560f70f802a8 [label="k_1", shape=none];
}

interface_5_out_0x560f70f801b8 -> interface_2_in_0x560f70f801b8;
interface_5_out_0x560f70faccd8 -> interface_2_in_0x560f70faccd8;
interface_5_out_0x560f70facd28 -> interface_2_in_0x560f70facd28;
interface_5_out_0x560f70f802a8 -> interface_2_in_0x560f70f802a8;

interface_2_out_0x560f6c4cbed0 -> interface_1_in_0x560f6c4cbed0;
interface_2_out_0x560f6c4cbef8 -> interface_1_in_0x560f6c4cbef8;
interface_2_out_0x560f71035130 -> interface_1_in_0x560f71035130;
interface_2_out_0x560f71035148 -> interface_1_in_0x560f71035148;
interface_2_out_0x560f6c4cbf48 -> interface_1_in_0x560f6c4cbf48;

interface_1_out_0x560f6c4cbed0 -> interface_0_in_0x560f6c4cbed0;
interface_1_out_0x560f6c4cbef8 -> interface_0_in_0x560f6c4cbef8;
interface_1_out_0x560f70f80ea0 -> interface_0_in_0x560f70f80ea0;
interface_1_out_0x560f6c4cbf48 -> interface_0_in_0x560f6c4cbf48;

{
    rank = same;
    interface_4_out_0x560f6c4cbed0;
    interface_4_out_0x560f70faccc0;
    interface_4_out_0x560f71035130;
    interface_4_out_0x560f70f92e28;
    interface_5_out_0x560f70f801b8;
    interface_5_out_0x560f70faccd8;
    interface_5_out_0x560f70facd28;
    interface_5_out_0x560f70f802a8;
}
subgraph cluster_subgraph_output {
    label = "Output";
    interface_6_in_0x560f6c4cbed0 [label="N", shape=none];
    interface_6_in_0x560f6c4cbef8 [label="C_out", shape=none];
    interface_6_in_0x560f6c4cbf20 [label="H", shape=none];
    interface_6_in_0x560f6c4cbf48 [label="H", shape=none];
}
interface_0_out_0x560f6c4cbed0 -> interface_6_in_0x560f6c4cbed0;
interface_0_out_0x560f6c4cbef8 -> interface_6_in_0x560f6c4cbef8;
interface_0_out_0x560f6c4cbf20 -> interface_6_in_0x560f6c4cbf20;
interface_0_out_0x560f6c4cbf48 -> interface_6_in_0x560f6c4cbf48;

}

"""
class kernel_generated_0(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([64, 64, 2, 3]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]

		# No contraction needed.
		t_2 = in_0

		# [H]@Unfold0063bc810b9e1e60 -> [H]@Iteratorb0a1def4ad5784ec, [k_1]@Share26cfa48d169008e4
		t_2 = torch.reshape(t_2, (1, 3584, 56, 1, ))
		t_2 = torch.nn.functional.unfold(t_2, (3, 1, ), padding=(1, 0, ))
		t_2 = torch.reshape(t_2, (1, 64, 56, 3, 56, ))

		# Perform contraction.
		t_3 = torch.einsum("mkojn, iklj -> mioln", t_2, in_1)

		# No contraction needed.
		t_4 = t_3

		# [H]@Mergeb85033bfb9503997, [s]@Mergeb85033bfb9503996 -> [s*H]@Shiftf6400fb251b2477a
		t_4 = torch.reshape(t_4, (1, 64, 112, 56, ))

		# [s*H]@Shiftf6400fb251b2477a -> [s*H]@Split25ee6f350ecc19b9
		t_4 = torch.roll(t_4, self.shift_direction, 2)

		# [s*H]@Split25ee6f350ecc19b9 -> [H]@Shift41a433c05e30b91d, [s]@Reduced95c644a3c072d9a
		t_4 = torch.reshape(t_4, (1, 64, 56, 2, 56, ))

		# [s]@Reduce
		t_4 = torch.sum(t_4, dim=(3, ))

		# No contraction needed.
		t_5 = t_4

		# [H]@Shift41a433c05e30b91d -> [H]@Iterator96123ba3184da39c
		t_5 = torch.roll(t_5, self.shift_direction, 2)

		# No need to crop the output tensor.
		y = t_5

		return y

class kernel_generated_1(torch.nn.Module):
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

		# No contraction needed.
		t_2 = in_0

		# [H]@Unfold0063bc810b9e1e60 -> [H]@Iteratorb0a1def4ad5784ec, [k_1]@Share26cfa48d169008e4
		t_2 = torch.reshape(t_2, (1, 1792, 28, 1, ))
		t_2 = torch.nn.functional.unfold(t_2, (3, 1, ), padding=(1, 0, ))
		t_2 = torch.reshape(t_2, (1, 64, 28, 3, 28, ))

		# Perform contraction.
		t_3 = torch.einsum("mkojn, iklj -> mioln", t_2, in_1)

		# No contraction needed.
		t_4 = t_3

		# [H]@Mergeb85033bfb9503997, [s]@Mergeb85033bfb9503996 -> [s*H]@Shiftf6400fb251b2477a
		t_4 = torch.reshape(t_4, (1, 128, 56, 28, ))

		# [s*H]@Shiftf6400fb251b2477a -> [s*H]@Split25ee6f350ecc19b9
		t_4 = torch.roll(t_4, self.shift_direction, 2)

		# [s*H]@Split25ee6f350ecc19b9 -> [H]@Shift41a433c05e30b91d, [s]@Reduced95c644a3c072d9a
		t_4 = torch.reshape(t_4, (1, 128, 28, 2, 28, ))

		# [s]@Reduce
		t_4 = torch.sum(t_4, dim=(3, ))

		# No contraction needed.
		t_5 = t_4

		# [H]@Shift41a433c05e30b91d -> [H]@Iterator96123ba3184da39c
		t_5 = torch.roll(t_5, self.shift_direction, 2)

		# No need to crop the output tensor.
		y = t_5

		return y

class kernel_generated_2(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([128, 128, 2, 3]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]

		# No contraction needed.
		t_2 = in_0

		# [H]@Unfold0063bc810b9e1e60 -> [H]@Iteratorb0a1def4ad5784ec, [k_1]@Share26cfa48d169008e4
		t_2 = torch.reshape(t_2, (1, 3584, 28, 1, ))
		t_2 = torch.nn.functional.unfold(t_2, (3, 1, ), padding=(1, 0, ))
		t_2 = torch.reshape(t_2, (1, 128, 28, 3, 28, ))

		# Perform contraction.
		t_3 = torch.einsum("mkojn, iklj -> mioln", t_2, in_1)

		# No contraction needed.
		t_4 = t_3

		# [H]@Mergeb85033bfb9503997, [s]@Mergeb85033bfb9503996 -> [s*H]@Shiftf6400fb251b2477a
		t_4 = torch.reshape(t_4, (1, 128, 56, 28, ))

		# [s*H]@Shiftf6400fb251b2477a -> [s*H]@Split25ee6f350ecc19b9
		t_4 = torch.roll(t_4, self.shift_direction, 2)

		# [s*H]@Split25ee6f350ecc19b9 -> [H]@Shift41a433c05e30b91d, [s]@Reduced95c644a3c072d9a
		t_4 = torch.reshape(t_4, (1, 128, 28, 2, 28, ))

		# [s]@Reduce
		t_4 = torch.sum(t_4, dim=(3, ))

		# No contraction needed.
		t_5 = t_4

		# [H]@Shift41a433c05e30b91d -> [H]@Iterator96123ba3184da39c
		t_5 = torch.roll(t_5, self.shift_direction, 2)

		# No need to crop the output tensor.
		y = t_5

		return y

class kernel_generated_3(torch.nn.Module):
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

		# No contraction needed.
		t_2 = in_0

		# [H]@Unfold0063bc810b9e1e60 -> [H]@Iteratorb0a1def4ad5784ec, [k_1]@Share26cfa48d169008e4
		t_2 = torch.reshape(t_2, (1, 1792, 14, 1, ))
		t_2 = torch.nn.functional.unfold(t_2, (3, 1, ), padding=(1, 0, ))
		t_2 = torch.reshape(t_2, (1, 128, 14, 3, 14, ))

		# Perform contraction.
		t_3 = torch.einsum("mkojn, iklj -> mioln", t_2, in_1)

		# No contraction needed.
		t_4 = t_3

		# [H]@Mergeb85033bfb9503997, [s]@Mergeb85033bfb9503996 -> [s*H]@Shiftf6400fb251b2477a
		t_4 = torch.reshape(t_4, (1, 256, 28, 14, ))

		# [s*H]@Shiftf6400fb251b2477a -> [s*H]@Split25ee6f350ecc19b9
		t_4 = torch.roll(t_4, self.shift_direction, 2)

		# [s*H]@Split25ee6f350ecc19b9 -> [H]@Shift41a433c05e30b91d, [s]@Reduced95c644a3c072d9a
		t_4 = torch.reshape(t_4, (1, 256, 14, 2, 14, ))

		# [s]@Reduce
		t_4 = torch.sum(t_4, dim=(3, ))

		# No contraction needed.
		t_5 = t_4

		# [H]@Shift41a433c05e30b91d -> [H]@Iterator96123ba3184da39c
		t_5 = torch.roll(t_5, self.shift_direction, 2)

		# No need to crop the output tensor.
		y = t_5

		return y

class kernel_generated_4(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([256, 256, 2, 3]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]

		# No contraction needed.
		t_2 = in_0

		# [H]@Unfold0063bc810b9e1e60 -> [H]@Iteratorb0a1def4ad5784ec, [k_1]@Share26cfa48d169008e4
		t_2 = torch.reshape(t_2, (1, 3584, 14, 1, ))
		t_2 = torch.nn.functional.unfold(t_2, (3, 1, ), padding=(1, 0, ))
		t_2 = torch.reshape(t_2, (1, 256, 14, 3, 14, ))

		# Perform contraction.
		t_3 = torch.einsum("mkojn, iklj -> mioln", t_2, in_1)

		# No contraction needed.
		t_4 = t_3

		# [H]@Mergeb85033bfb9503997, [s]@Mergeb85033bfb9503996 -> [s*H]@Shiftf6400fb251b2477a
		t_4 = torch.reshape(t_4, (1, 256, 28, 14, ))

		# [s*H]@Shiftf6400fb251b2477a -> [s*H]@Split25ee6f350ecc19b9
		t_4 = torch.roll(t_4, self.shift_direction, 2)

		# [s*H]@Split25ee6f350ecc19b9 -> [H]@Shift41a433c05e30b91d, [s]@Reduced95c644a3c072d9a
		t_4 = torch.reshape(t_4, (1, 256, 14, 2, 14, ))

		# [s]@Reduce
		t_4 = torch.sum(t_4, dim=(3, ))

		# No contraction needed.
		t_5 = t_4

		# [H]@Shift41a433c05e30b91d -> [H]@Iterator96123ba3184da39c
		t_5 = torch.roll(t_5, self.shift_direction, 2)

		# No need to crop the output tensor.
		y = t_5

		return y

class kernel_generated_5(torch.nn.Module):
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

		# No contraction needed.
		t_2 = in_0

		# [H]@Unfold0063bc810b9e1e60 -> [H]@Iteratorb0a1def4ad5784ec, [k_1]@Share26cfa48d169008e4
		t_2 = torch.reshape(t_2, (1, 1792, 7, 1, ))
		t_2 = torch.nn.functional.unfold(t_2, (3, 1, ), padding=(1, 0, ))
		t_2 = torch.reshape(t_2, (1, 256, 7, 3, 7, ))

		# Perform contraction.
		t_3 = torch.einsum("mkojn, iklj -> mioln", t_2, in_1)

		# No contraction needed.
		t_4 = t_3

		# [H]@Mergeb85033bfb9503997, [s]@Mergeb85033bfb9503996 -> [s*H]@Shiftf6400fb251b2477a
		t_4 = torch.reshape(t_4, (1, 512, 14, 7, ))

		# [s*H]@Shiftf6400fb251b2477a -> [s*H]@Split25ee6f350ecc19b9
		t_4 = torch.roll(t_4, self.shift_direction, 2)

		# [s*H]@Split25ee6f350ecc19b9 -> [H]@Shift41a433c05e30b91d, [s]@Reduced95c644a3c072d9a
		t_4 = torch.reshape(t_4, (1, 512, 7, 2, 7, ))

		# [s]@Reduce
		t_4 = torch.sum(t_4, dim=(3, ))

		# No contraction needed.
		t_5 = t_4

		# [H]@Shift41a433c05e30b91d -> [H]@Iterator96123ba3184da39c
		t_5 = torch.roll(t_5, self.shift_direction, 2)

		# No need to crop the output tensor.
		y = t_5

		return y

class kernel_generated_6(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([512, 512, 2, 3]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]

		# No contraction needed.
		t_2 = in_0

		# [H]@Unfold0063bc810b9e1e60 -> [H]@Iteratorb0a1def4ad5784ec, [k_1]@Share26cfa48d169008e4
		t_2 = torch.reshape(t_2, (1, 3584, 7, 1, ))
		t_2 = torch.nn.functional.unfold(t_2, (3, 1, ), padding=(1, 0, ))
		t_2 = torch.reshape(t_2, (1, 512, 7, 3, 7, ))

		# Perform contraction.
		t_3 = torch.einsum("mkojn, iklj -> mioln", t_2, in_1)

		# No contraction needed.
		t_4 = t_3

		# [H]@Mergeb85033bfb9503997, [s]@Mergeb85033bfb9503996 -> [s*H]@Shiftf6400fb251b2477a
		t_4 = torch.reshape(t_4, (1, 512, 14, 7, ))

		# [s*H]@Shiftf6400fb251b2477a -> [s*H]@Split25ee6f350ecc19b9
		t_4 = torch.roll(t_4, self.shift_direction, 2)

		# [s*H]@Split25ee6f350ecc19b9 -> [H]@Shift41a433c05e30b91d, [s]@Reduced95c644a3c072d9a
		t_4 = torch.reshape(t_4, (1, 512, 7, 2, 7, ))

		# [s]@Reduce
		t_4 = torch.sum(t_4, dim=(3, ))

		# No contraction needed.
		t_5 = t_4

		# [H]@Shift41a433c05e30b91d -> [H]@Iterator96123ba3184da39c
		t_5 = torch.roll(t_5, self.shift_direction, 2)

		# No need to crop the output tensor.
		y = t_5

		return y

