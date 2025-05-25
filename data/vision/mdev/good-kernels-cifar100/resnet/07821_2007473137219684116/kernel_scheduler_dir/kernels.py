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
        interface_0_out_0x5617e221dd90 [label="N", shape=none];
        interface_0_out_0x5617e221ddb8 [label="C_out", shape=none];
        interface_0_out_0x5617e221dde0 [label="H", shape=none];
        interface_0_out_0x5617e221de08 [label="H", shape=none];
    }
    {
        rank = same;
        interface_0_out_0x5617e221dd90;
        interface_0_out_0x5617e221ddb8;
        interface_0_out_0x5617e221dde0;
        interface_0_out_0x5617e221de08;
    }
    // Input 0.
    subgraph cluster_subgraph_0_in_0 {
        label = "";
        interface_0_in_0x5617e221dd90 [label="N", shape=none];
        interface_0_in_0x5617e221de08 [label="H", shape=none];
        interface_0_in_0x5617e221ddb8 [label="C_out", shape=none];
        interface_0_in_0x7fdf84004160 [label="H", shape=none];
    }
    {
        rank = same;
        interface_0_in_0x5617e221dd90;
        interface_0_in_0x5617e221de08;
        interface_0_in_0x5617e221ddb8;
        interface_0_in_0x7fdf84004160;
    }
    // Op's.
    op_0x7fdf84004140 [label="Shift"];
    // Dimension's.
    interface_0_in_0x5617e221dd90 -> interface_0_out_0x5617e221dd90 [label="N"];
    interface_0_in_0x5617e221ddb8 -> interface_0_out_0x5617e221ddb8 [label="C_out"];
    op_0x7fdf84004140 -> interface_0_out_0x5617e221dde0 [label="H"];
    interface_0_in_0x5617e221de08 -> interface_0_out_0x5617e221de08 [label="H"];
    interface_0_in_0x7fdf84004160 -> op_0x7fdf84004140 [label="H"];
}

// Stage tensor.
subgraph cluster_subgraph_1 {
    label = "Subgraph 1";
    // Reductions.
    reduce_0x7fd804002de8 [label="Sum", shape=box];
    // Output.
    subgraph cluster_subgraph_1_out {
        label = "";
        interface_1_out_0x5617e221dd90 [label="N", shape=none];
        interface_1_out_0x5617e221de08 [label="H", shape=none];
        interface_1_out_0x5617e221ddb8 [label="C_out", shape=none];
        interface_1_out_0x7fdf84004160 [label="H", shape=none];
    }
    {
        rank = same;
        reduce_0x7fd804002de8;
        interface_1_out_0x5617e221dd90;
        interface_1_out_0x5617e221de08;
        interface_1_out_0x5617e221ddb8;
        interface_1_out_0x7fdf84004160;
    }
    // Input 0.
    subgraph cluster_subgraph_1_in_0 {
        label = "";
        interface_1_in_0x5617e221dd90 [label="N", shape=none];
        interface_1_in_0x7fe1cc11fb30 [label="H", shape=none];
        interface_1_in_0x5617e221de08 [label="H", shape=none];
        interface_1_in_0x5617e221ddb8 [label="C_out", shape=none];
        interface_1_in_0x7fe1cc11fb48 [label="s", shape=none];
    }
    {
        rank = same;
        interface_1_in_0x5617e221dd90;
        interface_1_in_0x7fe1cc11fb30;
        interface_1_in_0x5617e221de08;
        interface_1_in_0x5617e221ddb8;
        interface_1_in_0x7fe1cc11fb48;
    }
    // Op's.
    op_0x7fd958057310 [label="Shift"];
    op_0x7fd9b000bbc0 [label="Split"];
    op_0x7fe1cc11faf0 [label="Merge"];
    // Dimension's.
    interface_1_in_0x5617e221dd90 -> interface_1_out_0x5617e221dd90 [label="N"];
    interface_1_in_0x5617e221ddb8 -> interface_1_out_0x5617e221ddb8 [label="C_out"];
    interface_1_in_0x5617e221de08 -> interface_1_out_0x5617e221de08 [label="H"];
    op_0x7fd9b000bbc0 -> reduce_0x7fd804002de8 [label="s"];
    op_0x7fe1cc11faf0 -> op_0x7fd958057310 [label="s*H"];
    op_0x7fd958057310 -> op_0x7fd9b000bbc0 [label="s*H"];
    op_0x7fd9b000bbc0 -> interface_1_out_0x7fdf84004160 [label="H"];
    interface_1_in_0x7fe1cc11fb30 -> op_0x7fe1cc11faf0 [label="H"];
    interface_1_in_0x7fe1cc11fb48 -> op_0x7fe1cc11faf0 [label="s"];
}

// Stage tensor.
subgraph cluster_subgraph_2 {
    label = "Subgraph 2";
    // Reductions.
    reduce_0x7fd804005c48 [label="Sum", shape=box];
    reduce_0x7fd804001998 [label="Sum", shape=box];
    // Output.
    subgraph cluster_subgraph_2_out {
        label = "";
        interface_2_out_0x5617e221dd90 [label="N", shape=none];
        interface_2_out_0x7fe1cc11fb30 [label="H", shape=none];
        interface_2_out_0x5617e221de08 [label="H", shape=none];
        interface_2_out_0x5617e221ddb8 [label="C_out", shape=none];
        interface_2_out_0x7fe1cc11fb48 [label="s", shape=none];
    }
    {
        rank = same;
        reduce_0x7fd804005c48;
        reduce_0x7fd804001998;
        interface_2_out_0x5617e221dd90;
        interface_2_out_0x7fe1cc11fb30;
        interface_2_out_0x5617e221de08;
        interface_2_out_0x5617e221ddb8;
        interface_2_out_0x7fe1cc11fb48;
    }
    // Input 0.
    subgraph cluster_subgraph_2_in_0 {
        label = "";
        interface_2_in_0x5617e221dd90 [label="N", shape=none];
        interface_2_in_0x7fdef8004960 [label="C_in", shape=none];
        interface_2_in_0x7fe1cc11fb30 [label="H", shape=none];
        interface_2_in_0x5617e221de08 [label="H", shape=none];
        interface_2_in_0x7fdef8004910 [label="k_1", shape=none];
    }
    // Input 1.
    subgraph cluster_subgraph_2_in_1 {
        label = "";
        interface_2_in_0x7fdef8004978 [label="C_in", shape=none];
        interface_2_in_0x7fdef8004928 [label="k_1", shape=none];
        interface_2_in_0x7fdf58004638 [label="C_out", shape=none];
        interface_2_in_0x7fdf382f6798 [label="s", shape=none];
    }
    {
        rank = same;
        interface_2_in_0x5617e221dd90;
        interface_2_in_0x7fdef8004960;
        interface_2_in_0x7fe1cc11fb30;
        interface_2_in_0x5617e221de08;
        interface_2_in_0x7fdef8004910;
        interface_2_in_0x7fdef8004978;
        interface_2_in_0x7fdef8004928;
        interface_2_in_0x7fdf58004638;
        interface_2_in_0x7fdf382f6798;
    }
    // Op's.
    op_0x7fdc442c2f58 [label="Expand"];
    op_0x7fdef80048f0 [label="Share"];
    op_0x7fdef8004940 [label="Share"];
    op_0x7fdf382f6760 [label="Share"];
    op_0x7fdf58004600 [label="Share"];
    op_0x7fdf58004cf8 [label="Expand"];
    // Dimension's.
    interface_2_in_0x5617e221dd90 -> interface_2_out_0x5617e221dd90 [label="N"];
    op_0x7fdf58004600 -> interface_2_out_0x5617e221ddb8 [label="C_out"];
    interface_2_in_0x5617e221de08 -> interface_2_out_0x5617e221de08 [label="H"];
    op_0x7fdef80048f0 -> reduce_0x7fd804001998 [label="k_1"];
    op_0x7fdef8004940 -> reduce_0x7fd804005c48 [label="C_in"];
    interface_2_in_0x7fdef8004910 -> op_0x7fdef80048f0 [label="k_1"];
    interface_2_in_0x7fdef8004928 -> op_0x7fdef80048f0 [label="k_1"];
    interface_2_in_0x7fdef8004960 -> op_0x7fdef8004940 [label="C_in"];
    interface_2_in_0x7fdef8004978 -> op_0x7fdef8004940 [label="C_in"];
    op_0x7fdc442c2f58 -> op_0x7fdf382f6760 [label="s"];
    interface_2_in_0x7fdf382f6798 -> op_0x7fdf382f6760 [label="s"];
    op_0x7fdf58004cf8 -> op_0x7fdf58004600 [label="C_out"];
    interface_2_in_0x7fdf58004638 -> op_0x7fdf58004600 [label="C_out"];
    interface_2_in_0x7fe1cc11fb30 -> interface_2_out_0x7fe1cc11fb30 [label="H"];
    op_0x7fdf382f6760 -> interface_2_out_0x7fe1cc11fb48 [label="s"];
}

// Stage tensor.
subgraph cluster_subgraph_3 {
    label = "Subgraph 3";
    // Reductions.
    // Output.
    subgraph cluster_subgraph_3_out {
        label = "";
        interface_3_out_0x5617e221dd90 [label="N", shape=none];
        interface_3_out_0x7fdef8004960 [label="C_in", shape=none];
        interface_3_out_0x7fe1cc11fb30 [label="H", shape=none];
        interface_3_out_0x5617e221de08 [label="H", shape=none];
        interface_3_out_0x7fdef8004910 [label="k_1", shape=none];
    }
    {
        rank = same;
        interface_3_out_0x5617e221dd90;
        interface_3_out_0x7fdef8004960;
        interface_3_out_0x7fe1cc11fb30;
        interface_3_out_0x5617e221de08;
        interface_3_out_0x7fdef8004910;
    }
    // Input 0.
    subgraph cluster_subgraph_3_in_0 {
        label = "";
        interface_3_in_0x5617e221dd90 [label="N", shape=none];
        interface_3_in_0x7fdef8004960 [label="C_in", shape=none];
        interface_3_in_0x7fe1cc11fb30 [label="H", shape=none];
        interface_3_in_0x7fdf8400c8a8 [label="H", shape=none];
    }
    {
        rank = same;
        interface_3_in_0x5617e221dd90;
        interface_3_in_0x7fdef8004960;
        interface_3_in_0x7fe1cc11fb30;
        interface_3_in_0x7fdf8400c8a8;
    }
    // Op's.
    op_0x7fdf8400c880 [label="Unfold"];
    // Dimension's.
    interface_3_in_0x5617e221dd90 -> interface_3_out_0x5617e221dd90 [label="N"];
    op_0x7fdf8400c880 -> interface_3_out_0x5617e221de08 [label="H"];
    op_0x7fdf8400c880 -> interface_3_out_0x7fdef8004910 [label="k_1"];
    interface_3_in_0x7fdef8004960 -> interface_3_out_0x7fdef8004960 [label="C_in"];
    interface_3_in_0x7fdf8400c8a8 -> op_0x7fdf8400c880 [label="H"];
    interface_3_in_0x7fe1cc11fb30 -> interface_3_out_0x7fe1cc11fb30 [label="H"];
}

// Input tensor.
subgraph cluster_subgraph_4 {
    label = "Input 0";
    interface_4_out_0x5617e221dd90 [label="N", shape=none];
    interface_4_out_0x7fdef8004960 [label="C_in", shape=none];
    interface_4_out_0x7fe1cc11fb30 [label="H", shape=none];
    interface_4_out_0x7fdf8400c8a8 [label="H", shape=none];
}

interface_4_out_0x5617e221dd90 -> interface_3_in_0x5617e221dd90;
interface_4_out_0x7fdef8004960 -> interface_3_in_0x7fdef8004960;
interface_4_out_0x7fe1cc11fb30 -> interface_3_in_0x7fe1cc11fb30;
interface_4_out_0x7fdf8400c8a8 -> interface_3_in_0x7fdf8400c8a8;

interface_3_out_0x5617e221dd90 -> interface_2_in_0x5617e221dd90;
interface_3_out_0x7fdef8004960 -> interface_2_in_0x7fdef8004960;
interface_3_out_0x7fe1cc11fb30 -> interface_2_in_0x7fe1cc11fb30;
interface_3_out_0x5617e221de08 -> interface_2_in_0x5617e221de08;
interface_3_out_0x7fdef8004910 -> interface_2_in_0x7fdef8004910;

// Input tensor.
subgraph cluster_subgraph_5 {
    label = "Input 1";
    interface_5_out_0x7fdef8004978 [label="C_in", shape=none];
    interface_5_out_0x7fdef8004928 [label="k_1", shape=none];
    interface_5_out_0x7fdf58004638 [label="C_out", shape=none];
    interface_5_out_0x7fdf382f6798 [label="s", shape=none];
}

interface_5_out_0x7fdef8004978 -> interface_2_in_0x7fdef8004978;
interface_5_out_0x7fdef8004928 -> interface_2_in_0x7fdef8004928;
interface_5_out_0x7fdf58004638 -> interface_2_in_0x7fdf58004638;
interface_5_out_0x7fdf382f6798 -> interface_2_in_0x7fdf382f6798;

interface_2_out_0x5617e221dd90 -> interface_1_in_0x5617e221dd90;
interface_2_out_0x7fe1cc11fb30 -> interface_1_in_0x7fe1cc11fb30;
interface_2_out_0x5617e221de08 -> interface_1_in_0x5617e221de08;
interface_2_out_0x5617e221ddb8 -> interface_1_in_0x5617e221ddb8;
interface_2_out_0x7fe1cc11fb48 -> interface_1_in_0x7fe1cc11fb48;

interface_1_out_0x5617e221dd90 -> interface_0_in_0x5617e221dd90;
interface_1_out_0x5617e221de08 -> interface_0_in_0x5617e221de08;
interface_1_out_0x5617e221ddb8 -> interface_0_in_0x5617e221ddb8;
interface_1_out_0x7fdf84004160 -> interface_0_in_0x7fdf84004160;

{
    rank = same;
    interface_4_out_0x5617e221dd90;
    interface_4_out_0x7fdef8004960;
    interface_4_out_0x7fe1cc11fb30;
    interface_4_out_0x7fdf8400c8a8;
    interface_5_out_0x7fdef8004978;
    interface_5_out_0x7fdef8004928;
    interface_5_out_0x7fdf58004638;
    interface_5_out_0x7fdf382f6798;
}
subgraph cluster_subgraph_output {
    label = "Output";
    interface_6_in_0x5617e221dd90 [label="N", shape=none];
    interface_6_in_0x5617e221ddb8 [label="C_out", shape=none];
    interface_6_in_0x5617e221dde0 [label="H", shape=none];
    interface_6_in_0x5617e221de08 [label="H", shape=none];
}
interface_0_out_0x5617e221dd90 -> interface_6_in_0x5617e221dd90;
interface_0_out_0x5617e221ddb8 -> interface_6_in_0x5617e221ddb8;
interface_0_out_0x5617e221dde0 -> interface_6_in_0x5617e221dde0;
interface_0_out_0x5617e221de08 -> interface_6_in_0x5617e221de08;

}

"""
class kernel_generated_0(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([64, 3, 64, 2]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]

		# No contraction needed.
		t_2 = in_0

		# [H]@Unfold0063bc810b9e1e60 -> [H]@Iteratorb0a1def4ad5784ec, [k_1]@Share26cfa48d169008e4
		t_2 = torch.reshape(t_2, (128, 3584, 56, 1, ))
		t_2 = torch.nn.functional.unfold(t_2, (3, 1, ), padding=(1, 0, ))
		t_2 = torch.reshape(t_2, (128, 64, 56, 3, 56, ))

		# Permute to match the output of this subgraph.
		t_2 = torch.permute(t_2, (0, 1, 2, 4, 3, ))

		# Perform contraction.
		t_3 = torch.einsum("mjoni, jilk -> monlk", t_2, in_1)

		# No contraction needed.
		t_4 = t_3

		# [H]@Mergeb85033bfb9503997, [s]@Mergeb85033bfb9503996 -> [s*H]@Shiftf6400fb251b2477a
		t_4 = torch.permute(t_4, (0, 2, 3, 1, 4, ))
		t_4 = torch.reshape(t_4, (128, 56, 64, 112, ))

		# [s*H]@Shiftf6400fb251b2477a -> [s*H]@Split25ee6f350ecc19b9
		t_4 = torch.roll(t_4, self.shift_direction, 3)

		# [s*H]@Split25ee6f350ecc19b9 -> [H]@Shift41a433c05e30b91d, [s]@Reduced95c644a3c072d9a
		t_4 = torch.reshape(t_4, (128, 56, 64, 56, 2, ))

		# [s]@Reduce
		t_4 = torch.sum(t_4, dim=(4, ))

		# No contraction needed.
		t_5 = t_4

		# [H]@Shift41a433c05e30b91d -> [H]@Iterator96123ba3184da39c
		t_5 = torch.roll(t_5, self.shift_direction, 3)

		# Permute to match the output of this subgraph.
		t_5 = torch.permute(t_5, (0, 2, 3, 1, ))

		# No need to crop the output tensor.
		y = t_5

		return y

class kernel_generated_1(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([64, 3, 128, 2]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]

		# No contraction needed.
		t_2 = in_0

		# [H]@Unfold0063bc810b9e1e60 -> [H]@Iteratorb0a1def4ad5784ec, [k_1]@Share26cfa48d169008e4
		t_2 = torch.reshape(t_2, (128, 1792, 28, 1, ))
		t_2 = torch.nn.functional.unfold(t_2, (3, 1, ), padding=(1, 0, ))
		t_2 = torch.reshape(t_2, (128, 64, 28, 3, 28, ))

		# Permute to match the output of this subgraph.
		t_2 = torch.permute(t_2, (0, 1, 2, 4, 3, ))

		# Perform contraction.
		t_3 = torch.einsum("mjoni, jilk -> monlk", t_2, in_1)

		# No contraction needed.
		t_4 = t_3

		# [H]@Mergeb85033bfb9503997, [s]@Mergeb85033bfb9503996 -> [s*H]@Shiftf6400fb251b2477a
		t_4 = torch.permute(t_4, (0, 2, 3, 1, 4, ))
		t_4 = torch.reshape(t_4, (128, 28, 128, 56, ))

		# [s*H]@Shiftf6400fb251b2477a -> [s*H]@Split25ee6f350ecc19b9
		t_4 = torch.roll(t_4, self.shift_direction, 3)

		# [s*H]@Split25ee6f350ecc19b9 -> [H]@Shift41a433c05e30b91d, [s]@Reduced95c644a3c072d9a
		t_4 = torch.reshape(t_4, (128, 28, 128, 28, 2, ))

		# [s]@Reduce
		t_4 = torch.sum(t_4, dim=(4, ))

		# No contraction needed.
		t_5 = t_4

		# [H]@Shift41a433c05e30b91d -> [H]@Iterator96123ba3184da39c
		t_5 = torch.roll(t_5, self.shift_direction, 3)

		# Permute to match the output of this subgraph.
		t_5 = torch.permute(t_5, (0, 2, 3, 1, ))

		# No need to crop the output tensor.
		y = t_5

		return y

class kernel_generated_2(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([128, 3, 128, 2]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]

		# No contraction needed.
		t_2 = in_0

		# [H]@Unfold0063bc810b9e1e60 -> [H]@Iteratorb0a1def4ad5784ec, [k_1]@Share26cfa48d169008e4
		t_2 = torch.reshape(t_2, (128, 3584, 28, 1, ))
		t_2 = torch.nn.functional.unfold(t_2, (3, 1, ), padding=(1, 0, ))
		t_2 = torch.reshape(t_2, (128, 128, 28, 3, 28, ))

		# Permute to match the output of this subgraph.
		t_2 = torch.permute(t_2, (0, 1, 2, 4, 3, ))

		# Perform contraction.
		t_3 = torch.einsum("mjoni, jilk -> monlk", t_2, in_1)

		# No contraction needed.
		t_4 = t_3

		# [H]@Mergeb85033bfb9503997, [s]@Mergeb85033bfb9503996 -> [s*H]@Shiftf6400fb251b2477a
		t_4 = torch.permute(t_4, (0, 2, 3, 1, 4, ))
		t_4 = torch.reshape(t_4, (128, 28, 128, 56, ))

		# [s*H]@Shiftf6400fb251b2477a -> [s*H]@Split25ee6f350ecc19b9
		t_4 = torch.roll(t_4, self.shift_direction, 3)

		# [s*H]@Split25ee6f350ecc19b9 -> [H]@Shift41a433c05e30b91d, [s]@Reduced95c644a3c072d9a
		t_4 = torch.reshape(t_4, (128, 28, 128, 28, 2, ))

		# [s]@Reduce
		t_4 = torch.sum(t_4, dim=(4, ))

		# No contraction needed.
		t_5 = t_4

		# [H]@Shift41a433c05e30b91d -> [H]@Iterator96123ba3184da39c
		t_5 = torch.roll(t_5, self.shift_direction, 3)

		# Permute to match the output of this subgraph.
		t_5 = torch.permute(t_5, (0, 2, 3, 1, ))

		# No need to crop the output tensor.
		y = t_5

		return y

class kernel_generated_3(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([128, 3, 256, 2]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]

		# No contraction needed.
		t_2 = in_0

		# [H]@Unfold0063bc810b9e1e60 -> [H]@Iteratorb0a1def4ad5784ec, [k_1]@Share26cfa48d169008e4
		t_2 = torch.reshape(t_2, (128, 1792, 14, 1, ))
		t_2 = torch.nn.functional.unfold(t_2, (3, 1, ), padding=(1, 0, ))
		t_2 = torch.reshape(t_2, (128, 128, 14, 3, 14, ))

		# Permute to match the output of this subgraph.
		t_2 = torch.permute(t_2, (0, 1, 2, 4, 3, ))

		# Perform contraction.
		t_3 = torch.einsum("mjoni, jilk -> monlk", t_2, in_1)

		# No contraction needed.
		t_4 = t_3

		# [H]@Mergeb85033bfb9503997, [s]@Mergeb85033bfb9503996 -> [s*H]@Shiftf6400fb251b2477a
		t_4 = torch.permute(t_4, (0, 2, 3, 1, 4, ))
		t_4 = torch.reshape(t_4, (128, 14, 256, 28, ))

		# [s*H]@Shiftf6400fb251b2477a -> [s*H]@Split25ee6f350ecc19b9
		t_4 = torch.roll(t_4, self.shift_direction, 3)

		# [s*H]@Split25ee6f350ecc19b9 -> [H]@Shift41a433c05e30b91d, [s]@Reduced95c644a3c072d9a
		t_4 = torch.reshape(t_4, (128, 14, 256, 14, 2, ))

		# [s]@Reduce
		t_4 = torch.sum(t_4, dim=(4, ))

		# No contraction needed.
		t_5 = t_4

		# [H]@Shift41a433c05e30b91d -> [H]@Iterator96123ba3184da39c
		t_5 = torch.roll(t_5, self.shift_direction, 3)

		# Permute to match the output of this subgraph.
		t_5 = torch.permute(t_5, (0, 2, 3, 1, ))

		# No need to crop the output tensor.
		y = t_5

		return y

class kernel_generated_4(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([256, 3, 256, 2]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]

		# No contraction needed.
		t_2 = in_0

		# [H]@Unfold0063bc810b9e1e60 -> [H]@Iteratorb0a1def4ad5784ec, [k_1]@Share26cfa48d169008e4
		t_2 = torch.reshape(t_2, (128, 3584, 14, 1, ))
		t_2 = torch.nn.functional.unfold(t_2, (3, 1, ), padding=(1, 0, ))
		t_2 = torch.reshape(t_2, (128, 256, 14, 3, 14, ))

		# Permute to match the output of this subgraph.
		t_2 = torch.permute(t_2, (0, 1, 2, 4, 3, ))

		# Perform contraction.
		t_3 = torch.einsum("mjoni, jilk -> monlk", t_2, in_1)

		# No contraction needed.
		t_4 = t_3

		# [H]@Mergeb85033bfb9503997, [s]@Mergeb85033bfb9503996 -> [s*H]@Shiftf6400fb251b2477a
		t_4 = torch.permute(t_4, (0, 2, 3, 1, 4, ))
		t_4 = torch.reshape(t_4, (128, 14, 256, 28, ))

		# [s*H]@Shiftf6400fb251b2477a -> [s*H]@Split25ee6f350ecc19b9
		t_4 = torch.roll(t_4, self.shift_direction, 3)

		# [s*H]@Split25ee6f350ecc19b9 -> [H]@Shift41a433c05e30b91d, [s]@Reduced95c644a3c072d9a
		t_4 = torch.reshape(t_4, (128, 14, 256, 14, 2, ))

		# [s]@Reduce
		t_4 = torch.sum(t_4, dim=(4, ))

		# No contraction needed.
		t_5 = t_4

		# [H]@Shift41a433c05e30b91d -> [H]@Iterator96123ba3184da39c
		t_5 = torch.roll(t_5, self.shift_direction, 3)

		# Permute to match the output of this subgraph.
		t_5 = torch.permute(t_5, (0, 2, 3, 1, ))

		# No need to crop the output tensor.
		y = t_5

		return y

class kernel_generated_5(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([256, 3, 512, 2]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]

		# No contraction needed.
		t_2 = in_0

		# [H]@Unfold0063bc810b9e1e60 -> [H]@Iteratorb0a1def4ad5784ec, [k_1]@Share26cfa48d169008e4
		t_2 = torch.reshape(t_2, (128, 1792, 7, 1, ))
		t_2 = torch.nn.functional.unfold(t_2, (3, 1, ), padding=(1, 0, ))
		t_2 = torch.reshape(t_2, (128, 256, 7, 3, 7, ))

		# Permute to match the output of this subgraph.
		t_2 = torch.permute(t_2, (0, 1, 2, 4, 3, ))

		# Perform contraction.
		t_3 = torch.einsum("mjoni, jilk -> monlk", t_2, in_1)

		# No contraction needed.
		t_4 = t_3

		# [H]@Mergeb85033bfb9503997, [s]@Mergeb85033bfb9503996 -> [s*H]@Shiftf6400fb251b2477a
		t_4 = torch.permute(t_4, (0, 2, 3, 1, 4, ))
		t_4 = torch.reshape(t_4, (128, 7, 512, 14, ))

		# [s*H]@Shiftf6400fb251b2477a -> [s*H]@Split25ee6f350ecc19b9
		t_4 = torch.roll(t_4, self.shift_direction, 3)

		# [s*H]@Split25ee6f350ecc19b9 -> [H]@Shift41a433c05e30b91d, [s]@Reduced95c644a3c072d9a
		t_4 = torch.reshape(t_4, (128, 7, 512, 7, 2, ))

		# [s]@Reduce
		t_4 = torch.sum(t_4, dim=(4, ))

		# No contraction needed.
		t_5 = t_4

		# [H]@Shift41a433c05e30b91d -> [H]@Iterator96123ba3184da39c
		t_5 = torch.roll(t_5, self.shift_direction, 3)

		# Permute to match the output of this subgraph.
		t_5 = torch.permute(t_5, (0, 2, 3, 1, ))

		# No need to crop the output tensor.
		y = t_5

		return y

class kernel_generated_6(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([512, 3, 512, 2]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]

		# No contraction needed.
		t_2 = in_0

		# [H]@Unfold0063bc810b9e1e60 -> [H]@Iteratorb0a1def4ad5784ec, [k_1]@Share26cfa48d169008e4
		t_2 = torch.reshape(t_2, (128, 3584, 7, 1, ))
		t_2 = torch.nn.functional.unfold(t_2, (3, 1, ), padding=(1, 0, ))
		t_2 = torch.reshape(t_2, (128, 512, 7, 3, 7, ))

		# Permute to match the output of this subgraph.
		t_2 = torch.permute(t_2, (0, 1, 2, 4, 3, ))

		# Perform contraction.
		t_3 = torch.einsum("mjoni, jilk -> monlk", t_2, in_1)

		# No contraction needed.
		t_4 = t_3

		# [H]@Mergeb85033bfb9503997, [s]@Mergeb85033bfb9503996 -> [s*H]@Shiftf6400fb251b2477a
		t_4 = torch.permute(t_4, (0, 2, 3, 1, 4, ))
		t_4 = torch.reshape(t_4, (128, 7, 512, 14, ))

		# [s*H]@Shiftf6400fb251b2477a -> [s*H]@Split25ee6f350ecc19b9
		t_4 = torch.roll(t_4, self.shift_direction, 3)

		# [s*H]@Split25ee6f350ecc19b9 -> [H]@Shift41a433c05e30b91d, [s]@Reduced95c644a3c072d9a
		t_4 = torch.reshape(t_4, (128, 7, 512, 7, 2, ))

		# [s]@Reduce
		t_4 = torch.sum(t_4, dim=(4, ))

		# No contraction needed.
		t_5 = t_4

		# [H]@Shift41a433c05e30b91d -> [H]@Iterator96123ba3184da39c
		t_5 = torch.roll(t_5, self.shift_direction, 3)

		# Permute to match the output of this subgraph.
		t_5 = torch.permute(t_5, (0, 2, 3, 1, ))

		# No need to crop the output tensor.
		y = t_5

		return y

