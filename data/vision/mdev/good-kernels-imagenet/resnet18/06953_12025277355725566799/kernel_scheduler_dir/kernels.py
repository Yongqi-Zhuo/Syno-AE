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
        interface_0_in_0x5590da8a9460 [label="H", shape=none];
        interface_0_in_0x5590c9c88138 [label="H", shape=none];
    }
    {
        rank = same;
        interface_0_in_0x5590c9c880c0;
        interface_0_in_0x5590c9c880e8;
        interface_0_in_0x5590da8a9460;
        interface_0_in_0x5590c9c88138;
    }
    // Op's.
    op_0x5590da8a9440 [label="Shift"];
    // Dimension's.
    interface_0_in_0x5590c9c880c0 -> interface_0_out_0x5590c9c880c0 [label="N"];
    interface_0_in_0x5590c9c880e8 -> interface_0_out_0x5590c9c880e8 [label="C_out"];
    op_0x5590da8a9440 -> interface_0_out_0x5590c9c88110 [label="H"];
    interface_0_in_0x5590c9c88138 -> interface_0_out_0x5590c9c88138 [label="H"];
    interface_0_in_0x5590da8a9460 -> op_0x5590da8a9440 [label="H"];
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
        interface_1_out_0x5590da8a9460 [label="H", shape=none];
        interface_1_out_0x5590c9c88138 [label="H", shape=none];
    }
    {
        rank = same;
        reduce_0x7f51b0002ce8;
        interface_1_out_0x5590c9c880c0;
        interface_1_out_0x5590c9c880e8;
        interface_1_out_0x5590da8a9460;
        interface_1_out_0x5590c9c88138;
    }
    // Input 0.
    subgraph cluster_subgraph_1_in_0 {
        label = "";
        interface_1_in_0x5590c9c880c0 [label="N", shape=none];
        interface_1_in_0x5590c9c880e8 [label="C_out", shape=none];
        interface_1_in_0x5590da8ae450 [label="H", shape=none];
        interface_1_in_0x5590da8ae468 [label="s", shape=none];
        interface_1_in_0x5590c9c88138 [label="H", shape=none];
    }
    {
        rank = same;
        interface_1_in_0x5590c9c880c0;
        interface_1_in_0x5590c9c880e8;
        interface_1_in_0x5590da8ae450;
        interface_1_in_0x5590da8ae468;
        interface_1_in_0x5590c9c88138;
    }
    // Op's.
    op_0x5590da8a94a0 [label="Shift"];
    op_0x5590da8aa290 [label="Split"];
    op_0x5590da8ae410 [label="Merge"];
    // Dimension's.
    interface_1_in_0x5590c9c880c0 -> interface_1_out_0x5590c9c880c0 [label="N"];
    interface_1_in_0x5590c9c880e8 -> interface_1_out_0x5590c9c880e8 [label="C_out"];
    interface_1_in_0x5590c9c88138 -> interface_1_out_0x5590c9c88138 [label="H"];
    op_0x5590da8aa290 -> interface_1_out_0x5590da8a9460 [label="H"];
    op_0x5590da8ae410 -> op_0x5590da8a94a0 [label="s*H"];
    op_0x5590da8a94a0 -> op_0x5590da8aa290 [label="s*H"];
    interface_1_in_0x5590da8ae450 -> op_0x5590da8ae410 [label="H"];
    interface_1_in_0x5590da8ae468 -> op_0x5590da8ae410 [label="s"];
    op_0x5590da8aa290 -> reduce_0x7f51b0002ce8 [label="s"];
}

// Stage tensor.
subgraph cluster_subgraph_2 {
    label = "Subgraph 2";
    // Reductions.
    reduce_0x7f51b0005a48 [label="Sum", shape=box];
    reduce_0x7f51b0001a98 [label="Sum", shape=box];
    // Output.
    subgraph cluster_subgraph_2_out {
        label = "";
        interface_2_out_0x5590c9c880c0 [label="N", shape=none];
        interface_2_out_0x5590c9c880e8 [label="C_out", shape=none];
        interface_2_out_0x5590da8ae450 [label="H", shape=none];
        interface_2_out_0x5590da8ae468 [label="s", shape=none];
        interface_2_out_0x5590c9c88138 [label="H", shape=none];
    }
    {
        rank = same;
        reduce_0x7f51b0005a48;
        reduce_0x7f51b0001a98;
        interface_2_out_0x5590c9c880c0;
        interface_2_out_0x5590c9c880e8;
        interface_2_out_0x5590da8ae450;
        interface_2_out_0x5590da8ae468;
        interface_2_out_0x5590c9c88138;
    }
    // Input 0.
    subgraph cluster_subgraph_2_in_0 {
        label = "";
        interface_2_in_0x5590c9c880c0 [label="N", shape=none];
        interface_2_in_0x5590da8a7540 [label="C_in", shape=none];
        interface_2_in_0x5590da8ae450 [label="H", shape=none];
        interface_2_in_0x5590da8a7590 [label="k_1", shape=none];
        interface_2_in_0x5590c9c88138 [label="H", shape=none];
    }
    // Input 1.
    subgraph cluster_subgraph_2_in_1 {
        label = "";
        interface_2_in_0x5590da8a74b8 [label="C_out", shape=none];
        interface_2_in_0x5590da8a7558 [label="C_in", shape=none];
        interface_2_in_0x5590da8a75f8 [label="s", shape=none];
        interface_2_in_0x5590da8a75a8 [label="k_1", shape=none];
    }
    {
        rank = same;
        interface_2_in_0x5590c9c880c0;
        interface_2_in_0x5590da8a7540;
        interface_2_in_0x5590da8ae450;
        interface_2_in_0x5590da8a7590;
        interface_2_in_0x5590c9c88138;
        interface_2_in_0x5590da8a74b8;
        interface_2_in_0x5590da8a7558;
        interface_2_in_0x5590da8a75f8;
        interface_2_in_0x5590da8a75a8;
    }
    // Op's.
    op_0x5590da8a7480 [label="Share"];
    op_0x5590da8a7520 [label="Share"];
    op_0x5590da8a7570 [label="Share"];
    op_0x5590da8a75c0 [label="Share"];
    op_0x5590da8a7a38 [label="Expand"];
    op_0x5590da8a7a58 [label="Expand"];
    // Dimension's.
    interface_2_in_0x5590c9c880c0 -> interface_2_out_0x5590c9c880c0 [label="N"];
    op_0x5590da8a7480 -> interface_2_out_0x5590c9c880e8 [label="C_out"];
    interface_2_in_0x5590c9c88138 -> interface_2_out_0x5590c9c88138 [label="H"];
    op_0x5590da8a7a38 -> op_0x5590da8a7480 [label="C_out"];
    interface_2_in_0x5590da8a74b8 -> op_0x5590da8a7480 [label="C_out"];
    interface_2_in_0x5590da8a7540 -> op_0x5590da8a7520 [label="C_in"];
    interface_2_in_0x5590da8a7558 -> op_0x5590da8a7520 [label="C_in"];
    interface_2_in_0x5590da8a7590 -> op_0x5590da8a7570 [label="k_1"];
    interface_2_in_0x5590da8a75a8 -> op_0x5590da8a7570 [label="k_1"];
    op_0x5590da8a7a58 -> op_0x5590da8a75c0 [label="s"];
    interface_2_in_0x5590da8a75f8 -> op_0x5590da8a75c0 [label="s"];
    interface_2_in_0x5590da8ae450 -> interface_2_out_0x5590da8ae450 [label="H"];
    op_0x5590da8a75c0 -> interface_2_out_0x5590da8ae468 [label="s"];
    op_0x5590da8a7570 -> reduce_0x7f51b0001a98 [label="k_1"];
    op_0x5590da8a7520 -> reduce_0x7f51b0005a48 [label="C_in"];
}

// Stage tensor.
subgraph cluster_subgraph_3 {
    label = "Subgraph 3";
    // Reductions.
    // Output.
    subgraph cluster_subgraph_3_out {
        label = "";
        interface_3_out_0x5590c9c880c0 [label="N", shape=none];
        interface_3_out_0x5590da8a7540 [label="C_in", shape=none];
        interface_3_out_0x5590da8ae450 [label="H", shape=none];
        interface_3_out_0x5590da8a7590 [label="k_1", shape=none];
        interface_3_out_0x5590c9c88138 [label="H", shape=none];
    }
    {
        rank = same;
        interface_3_out_0x5590c9c880c0;
        interface_3_out_0x5590da8a7540;
        interface_3_out_0x5590da8ae450;
        interface_3_out_0x5590da8a7590;
        interface_3_out_0x5590c9c88138;
    }
    // Input 0.
    subgraph cluster_subgraph_3_in_0 {
        label = "";
        interface_3_in_0x5590c9c880c0 [label="N", shape=none];
        interface_3_in_0x5590da8a7540 [label="C_in", shape=none];
        interface_3_in_0x5590da8ae450 [label="H", shape=none];
        interface_3_in_0x5590da8bf028 [label="H", shape=none];
    }
    {
        rank = same;
        interface_3_in_0x5590c9c880c0;
        interface_3_in_0x5590da8a7540;
        interface_3_in_0x5590da8ae450;
        interface_3_in_0x5590da8bf028;
    }
    // Op's.
    op_0x5590da8bf000 [label="Unfold"];
    // Dimension's.
    interface_3_in_0x5590c9c880c0 -> interface_3_out_0x5590c9c880c0 [label="N"];
    op_0x5590da8bf000 -> interface_3_out_0x5590c9c88138 [label="H"];
    interface_3_in_0x5590da8a7540 -> interface_3_out_0x5590da8a7540 [label="C_in"];
    op_0x5590da8bf000 -> interface_3_out_0x5590da8a7590 [label="k_1"];
    interface_3_in_0x5590da8ae450 -> interface_3_out_0x5590da8ae450 [label="H"];
    interface_3_in_0x5590da8bf028 -> op_0x5590da8bf000 [label="H"];
}

// Input tensor.
subgraph cluster_subgraph_4 {
    label = "Input 0";
    interface_4_out_0x5590c9c880c0 [label="N", shape=none];
    interface_4_out_0x5590da8a7540 [label="C_in", shape=none];
    interface_4_out_0x5590da8ae450 [label="H", shape=none];
    interface_4_out_0x5590da8bf028 [label="H", shape=none];
}

interface_4_out_0x5590c9c880c0 -> interface_3_in_0x5590c9c880c0;
interface_4_out_0x5590da8a7540 -> interface_3_in_0x5590da8a7540;
interface_4_out_0x5590da8ae450 -> interface_3_in_0x5590da8ae450;
interface_4_out_0x5590da8bf028 -> interface_3_in_0x5590da8bf028;

interface_3_out_0x5590c9c880c0 -> interface_2_in_0x5590c9c880c0;
interface_3_out_0x5590da8a7540 -> interface_2_in_0x5590da8a7540;
interface_3_out_0x5590da8ae450 -> interface_2_in_0x5590da8ae450;
interface_3_out_0x5590da8a7590 -> interface_2_in_0x5590da8a7590;
interface_3_out_0x5590c9c88138 -> interface_2_in_0x5590c9c88138;

// Input tensor.
subgraph cluster_subgraph_5 {
    label = "Input 1";
    interface_5_out_0x5590da8a74b8 [label="C_out", shape=none];
    interface_5_out_0x5590da8a7558 [label="C_in", shape=none];
    interface_5_out_0x5590da8a75f8 [label="s", shape=none];
    interface_5_out_0x5590da8a75a8 [label="k_1", shape=none];
}

interface_5_out_0x5590da8a74b8 -> interface_2_in_0x5590da8a74b8;
interface_5_out_0x5590da8a7558 -> interface_2_in_0x5590da8a7558;
interface_5_out_0x5590da8a75f8 -> interface_2_in_0x5590da8a75f8;
interface_5_out_0x5590da8a75a8 -> interface_2_in_0x5590da8a75a8;

interface_2_out_0x5590c9c880c0 -> interface_1_in_0x5590c9c880c0;
interface_2_out_0x5590c9c880e8 -> interface_1_in_0x5590c9c880e8;
interface_2_out_0x5590da8ae450 -> interface_1_in_0x5590da8ae450;
interface_2_out_0x5590da8ae468 -> interface_1_in_0x5590da8ae468;
interface_2_out_0x5590c9c88138 -> interface_1_in_0x5590c9c88138;

interface_1_out_0x5590c9c880c0 -> interface_0_in_0x5590c9c880c0;
interface_1_out_0x5590c9c880e8 -> interface_0_in_0x5590c9c880e8;
interface_1_out_0x5590da8a9460 -> interface_0_in_0x5590da8a9460;
interface_1_out_0x5590c9c88138 -> interface_0_in_0x5590c9c88138;

{
    rank = same;
    interface_4_out_0x5590c9c880c0;
    interface_4_out_0x5590da8a7540;
    interface_4_out_0x5590da8ae450;
    interface_4_out_0x5590da8bf028;
    interface_5_out_0x5590da8a74b8;
    interface_5_out_0x5590da8a7558;
    interface_5_out_0x5590da8a75f8;
    interface_5_out_0x5590da8a75a8;
}
subgraph cluster_subgraph_output {
    label = "Output";
    interface_6_in_0x5590c9c880c0 [label="N", shape=none];
    interface_6_in_0x5590c9c880e8 [label="C_out", shape=none];
    interface_6_in_0x5590c9c88110 [label="H", shape=none];
    interface_6_in_0x5590c9c88138 [label="H", shape=none];
}
interface_0_out_0x5590c9c880c0 -> interface_6_in_0x5590c9c880c0;
interface_0_out_0x5590c9c880e8 -> interface_6_in_0x5590c9c880e8;
interface_0_out_0x5590c9c88110 -> interface_6_in_0x5590c9c88110;
interface_0_out_0x5590c9c88138 -> interface_6_in_0x5590c9c88138;

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
		t_3 = torch.einsum("mjokn, ijlk -> mioln", t_2, in_1)

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
		t_3 = torch.einsum("mjokn, ijlk -> mioln", t_2, in_1)

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
		t_3 = torch.einsum("mjokn, ijlk -> mioln", t_2, in_1)

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
		t_3 = torch.einsum("mjokn, ijlk -> mioln", t_2, in_1)

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
		t_3 = torch.einsum("mjokn, ijlk -> mioln", t_2, in_1)

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
		t_3 = torch.einsum("mjokn, ijlk -> mioln", t_2, in_1)

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
		t_3 = torch.einsum("mjokn, ijlk -> mioln", t_2, in_1)

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

