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
        interface_0_out_0x5566a5448560 [label="N", shape=none];
        interface_0_out_0x5566a5448588 [label="C_out", shape=none];
        interface_0_out_0x5566a54485b0 [label="H", shape=none];
        interface_0_out_0x5566a54485d8 [label="H", shape=none];
    }
    {
        rank = same;
        interface_0_out_0x5566a5448560;
        interface_0_out_0x5566a5448588;
        interface_0_out_0x5566a54485b0;
        interface_0_out_0x5566a54485d8;
    }
    // Input 0.
    subgraph cluster_subgraph_0_in_0 {
        label = "";
        interface_0_in_0x5566a5448560 [label="N", shape=none];
        interface_0_in_0x5566a54485d8 [label="H", shape=none];
        interface_0_in_0x5566a5448588 [label="C_out", shape=none];
        interface_0_in_0x5566a540f3a0 [label="H", shape=none];
    }
    {
        rank = same;
        interface_0_in_0x5566a5448560;
        interface_0_in_0x5566a54485d8;
        interface_0_in_0x5566a5448588;
        interface_0_in_0x5566a540f3a0;
    }
    // Op's.
    op_0x5566a540f380 [label="Shift"];
    // Dimension's.
    interface_0_in_0x5566a540f3a0 -> op_0x5566a540f380 [label="H"];
    interface_0_in_0x5566a5448560 -> interface_0_out_0x5566a5448560 [label="N"];
    interface_0_in_0x5566a5448588 -> interface_0_out_0x5566a5448588 [label="C_out"];
    op_0x5566a540f380 -> interface_0_out_0x5566a54485b0 [label="H"];
    interface_0_in_0x5566a54485d8 -> interface_0_out_0x5566a54485d8 [label="H"];
}

// Stage tensor.
subgraph cluster_subgraph_1 {
    label = "Subgraph 1";
    // Reductions.
    reduce_0x7f23c0002ce8 [label="Sum", shape=box];
    // Output.
    subgraph cluster_subgraph_1_out {
        label = "";
        interface_1_out_0x5566a5448560 [label="N", shape=none];
        interface_1_out_0x5566a54485d8 [label="H", shape=none];
        interface_1_out_0x5566a5448588 [label="C_out", shape=none];
        interface_1_out_0x5566a540f3a0 [label="H", shape=none];
    }
    {
        rank = same;
        reduce_0x7f23c0002ce8;
        interface_1_out_0x5566a5448560;
        interface_1_out_0x5566a54485d8;
        interface_1_out_0x5566a5448588;
        interface_1_out_0x5566a540f3a0;
    }
    // Input 0.
    subgraph cluster_subgraph_1_in_0 {
        label = "";
        interface_1_in_0x5566a5448560 [label="N", shape=none];
        interface_1_in_0x5566a755a5a0 [label="H", shape=none];
        interface_1_in_0x5566a54485d8 [label="H", shape=none];
        interface_1_in_0x5566a5448588 [label="C_out", shape=none];
        interface_1_in_0x5566a755a5b8 [label="s", shape=none];
    }
    {
        rank = same;
        interface_1_in_0x5566a5448560;
        interface_1_in_0x5566a755a5a0;
        interface_1_in_0x5566a54485d8;
        interface_1_in_0x5566a5448588;
        interface_1_in_0x5566a755a5b8;
    }
    // Op's.
    op_0x5566a540f710 [label="Shift"];
    op_0x5566a5490e00 [label="Split"];
    op_0x5566a755a560 [label="Merge"];
    // Dimension's.
    op_0x5566a5490e00 -> interface_1_out_0x5566a540f3a0 [label="H"];
    op_0x5566a755a560 -> op_0x5566a540f710 [label="s*H"];
    interface_1_in_0x5566a5448560 -> interface_1_out_0x5566a5448560 [label="N"];
    interface_1_in_0x5566a5448588 -> interface_1_out_0x5566a5448588 [label="C_out"];
    interface_1_in_0x5566a54485d8 -> interface_1_out_0x5566a54485d8 [label="H"];
    op_0x5566a540f710 -> op_0x5566a5490e00 [label="s*H"];
    interface_1_in_0x5566a755a5a0 -> op_0x5566a755a560 [label="H"];
    interface_1_in_0x5566a755a5b8 -> op_0x5566a755a560 [label="s"];
    op_0x5566a5490e00 -> reduce_0x7f23c0002ce8 [label="s"];
}

// Stage tensor.
subgraph cluster_subgraph_2 {
    label = "Subgraph 2";
    // Reductions.
    reduce_0x7f23c0005b48 [label="Sum", shape=box];
    reduce_0x7f23c0001a98 [label="Sum", shape=box];
    // Output.
    subgraph cluster_subgraph_2_out {
        label = "";
        interface_2_out_0x5566a5448560 [label="N", shape=none];
        interface_2_out_0x5566a755a5a0 [label="H", shape=none];
        interface_2_out_0x5566a54485d8 [label="H", shape=none];
        interface_2_out_0x5566a5448588 [label="C_out", shape=none];
        interface_2_out_0x5566a755a5b8 [label="s", shape=none];
    }
    {
        rank = same;
        reduce_0x7f23c0005b48;
        reduce_0x7f23c0001a98;
        interface_2_out_0x5566a5448560;
        interface_2_out_0x5566a755a5a0;
        interface_2_out_0x5566a54485d8;
        interface_2_out_0x5566a5448588;
        interface_2_out_0x5566a755a5b8;
    }
    // Input 0.
    subgraph cluster_subgraph_2_in_0 {
        label = "";
        interface_2_in_0x5566a5448560 [label="N", shape=none];
        interface_2_in_0x5566a540e930 [label="C_in", shape=none];
        interface_2_in_0x5566a755a5a0 [label="H", shape=none];
        interface_2_in_0x5566a54485d8 [label="H", shape=none];
        interface_2_in_0x5566a540e610 [label="k_1", shape=none];
    }
    // Input 1.
    subgraph cluster_subgraph_2_in_1 {
        label = "";
        interface_2_in_0x5566a540e948 [label="C_in", shape=none];
        interface_2_in_0x5566a540e628 [label="k_1", shape=none];
        interface_2_in_0x5566a540e538 [label="C_out", shape=none];
        interface_2_in_0x5566a54cb318 [label="s", shape=none];
    }
    {
        rank = same;
        interface_2_in_0x5566a5448560;
        interface_2_in_0x5566a540e930;
        interface_2_in_0x5566a755a5a0;
        interface_2_in_0x5566a54485d8;
        interface_2_in_0x5566a540e610;
        interface_2_in_0x5566a540e948;
        interface_2_in_0x5566a540e628;
        interface_2_in_0x5566a540e538;
        interface_2_in_0x5566a54cb318;
    }
    // Op's.
    op_0x5566a540e500 [label="Share"];
    op_0x5566a540e5f0 [label="Share"];
    op_0x5566a540e910 [label="Share"];
    op_0x5566a540eab8 [label="Expand"];
    op_0x5566a540eb58 [label="Expand"];
    op_0x5566a54cb2e0 [label="Share"];
    // Dimension's.
    op_0x5566a540eab8 -> op_0x5566a540e500 [label="C_out"];
    interface_2_in_0x5566a540e538 -> op_0x5566a540e500 [label="C_out"];
    interface_2_in_0x5566a540e610 -> op_0x5566a540e5f0 [label="k_1"];
    interface_2_in_0x5566a540e628 -> op_0x5566a540e5f0 [label="k_1"];
    interface_2_in_0x5566a540e930 -> op_0x5566a540e910 [label="C_in"];
    interface_2_in_0x5566a540e948 -> op_0x5566a540e910 [label="C_in"];
    interface_2_in_0x5566a5448560 -> interface_2_out_0x5566a5448560 [label="N"];
    op_0x5566a540e500 -> interface_2_out_0x5566a5448588 [label="C_out"];
    interface_2_in_0x5566a54485d8 -> interface_2_out_0x5566a54485d8 [label="H"];
    op_0x5566a540eb58 -> op_0x5566a54cb2e0 [label="s"];
    interface_2_in_0x5566a54cb318 -> op_0x5566a54cb2e0 [label="s"];
    interface_2_in_0x5566a755a5a0 -> interface_2_out_0x5566a755a5a0 [label="H"];
    op_0x5566a54cb2e0 -> interface_2_out_0x5566a755a5b8 [label="s"];
    op_0x5566a540e5f0 -> reduce_0x7f23c0001a98 [label="k_1"];
    op_0x5566a540e910 -> reduce_0x7f23c0005b48 [label="C_in"];
}

// Stage tensor.
subgraph cluster_subgraph_3 {
    label = "Subgraph 3";
    // Reductions.
    // Output.
    subgraph cluster_subgraph_3_out {
        label = "";
        interface_3_out_0x5566a5448560 [label="N", shape=none];
        interface_3_out_0x5566a540e930 [label="C_in", shape=none];
        interface_3_out_0x5566a755a5a0 [label="H", shape=none];
        interface_3_out_0x5566a54485d8 [label="H", shape=none];
        interface_3_out_0x5566a540e610 [label="k_1", shape=none];
    }
    {
        rank = same;
        interface_3_out_0x5566a5448560;
        interface_3_out_0x5566a540e930;
        interface_3_out_0x5566a755a5a0;
        interface_3_out_0x5566a54485d8;
        interface_3_out_0x5566a540e610;
    }
    // Input 0.
    subgraph cluster_subgraph_3_in_0 {
        label = "";
        interface_3_in_0x5566a5448560 [label="N", shape=none];
        interface_3_in_0x5566a540e930 [label="C_in", shape=none];
        interface_3_in_0x5566a755a5a0 [label="H", shape=none];
        interface_3_in_0x5566a75445e8 [label="H", shape=none];
    }
    {
        rank = same;
        interface_3_in_0x5566a5448560;
        interface_3_in_0x5566a540e930;
        interface_3_in_0x5566a755a5a0;
        interface_3_in_0x5566a75445e8;
    }
    // Op's.
    op_0x5566a75445c0 [label="Unfold"];
    // Dimension's.
    op_0x5566a75445c0 -> interface_3_out_0x5566a540e610 [label="k_1"];
    interface_3_in_0x5566a540e930 -> interface_3_out_0x5566a540e930 [label="C_in"];
    interface_3_in_0x5566a5448560 -> interface_3_out_0x5566a5448560 [label="N"];
    op_0x5566a75445c0 -> interface_3_out_0x5566a54485d8 [label="H"];
    interface_3_in_0x5566a75445e8 -> op_0x5566a75445c0 [label="H"];
    interface_3_in_0x5566a755a5a0 -> interface_3_out_0x5566a755a5a0 [label="H"];
}

// Input tensor.
subgraph cluster_subgraph_4 {
    label = "Input 0";
    interface_4_out_0x5566a5448560 [label="N", shape=none];
    interface_4_out_0x5566a540e930 [label="C_in", shape=none];
    interface_4_out_0x5566a755a5a0 [label="H", shape=none];
    interface_4_out_0x5566a75445e8 [label="H", shape=none];
}

interface_4_out_0x5566a5448560 -> interface_3_in_0x5566a5448560;
interface_4_out_0x5566a540e930 -> interface_3_in_0x5566a540e930;
interface_4_out_0x5566a755a5a0 -> interface_3_in_0x5566a755a5a0;
interface_4_out_0x5566a75445e8 -> interface_3_in_0x5566a75445e8;

interface_3_out_0x5566a5448560 -> interface_2_in_0x5566a5448560;
interface_3_out_0x5566a540e930 -> interface_2_in_0x5566a540e930;
interface_3_out_0x5566a755a5a0 -> interface_2_in_0x5566a755a5a0;
interface_3_out_0x5566a54485d8 -> interface_2_in_0x5566a54485d8;
interface_3_out_0x5566a540e610 -> interface_2_in_0x5566a540e610;

// Input tensor.
subgraph cluster_subgraph_5 {
    label = "Input 1";
    interface_5_out_0x5566a540e948 [label="C_in", shape=none];
    interface_5_out_0x5566a540e628 [label="k_1", shape=none];
    interface_5_out_0x5566a540e538 [label="C_out", shape=none];
    interface_5_out_0x5566a54cb318 [label="s", shape=none];
}

interface_5_out_0x5566a540e948 -> interface_2_in_0x5566a540e948;
interface_5_out_0x5566a540e628 -> interface_2_in_0x5566a540e628;
interface_5_out_0x5566a540e538 -> interface_2_in_0x5566a540e538;
interface_5_out_0x5566a54cb318 -> interface_2_in_0x5566a54cb318;

interface_2_out_0x5566a5448560 -> interface_1_in_0x5566a5448560;
interface_2_out_0x5566a755a5a0 -> interface_1_in_0x5566a755a5a0;
interface_2_out_0x5566a54485d8 -> interface_1_in_0x5566a54485d8;
interface_2_out_0x5566a5448588 -> interface_1_in_0x5566a5448588;
interface_2_out_0x5566a755a5b8 -> interface_1_in_0x5566a755a5b8;

interface_1_out_0x5566a5448560 -> interface_0_in_0x5566a5448560;
interface_1_out_0x5566a54485d8 -> interface_0_in_0x5566a54485d8;
interface_1_out_0x5566a5448588 -> interface_0_in_0x5566a5448588;
interface_1_out_0x5566a540f3a0 -> interface_0_in_0x5566a540f3a0;

{
    rank = same;
    interface_4_out_0x5566a5448560;
    interface_4_out_0x5566a540e930;
    interface_4_out_0x5566a755a5a0;
    interface_4_out_0x5566a75445e8;
    interface_5_out_0x5566a540e948;
    interface_5_out_0x5566a540e628;
    interface_5_out_0x5566a540e538;
    interface_5_out_0x5566a54cb318;
}
subgraph cluster_subgraph_output {
    label = "Output";
    interface_6_in_0x5566a5448560 [label="N", shape=none];
    interface_6_in_0x5566a5448588 [label="C_out", shape=none];
    interface_6_in_0x5566a54485b0 [label="H", shape=none];
    interface_6_in_0x5566a54485d8 [label="H", shape=none];
}
interface_0_out_0x5566a5448560 -> interface_6_in_0x5566a5448560;
interface_0_out_0x5566a5448588 -> interface_6_in_0x5566a5448588;
interface_0_out_0x5566a54485b0 -> interface_6_in_0x5566a54485b0;
interface_0_out_0x5566a54485d8 -> interface_6_in_0x5566a54485d8;

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
		t_2 = torch.reshape(t_2, (1024, 3584, 56, 1, ))
		t_2 = torch.nn.functional.unfold(t_2, (3, 1, ), padding=(1, 0, ))
		t_2 = torch.reshape(t_2, (1024, 64, 56, 3, 56, ))

		# Permute to match the output of this subgraph.
		t_2 = torch.permute(t_2, (0, 1, 2, 4, 3, ))

		# Perform contraction.
		t_3 = torch.einsum("mkonj, kjil -> monil", t_2, in_1)

		# No contraction needed.
		t_4 = t_3

		# [H]@Mergeb85033bfb9503997, [s]@Mergeb85033bfb9503996 -> [s*H]@Shiftf6400fb251b2477a
		t_4 = torch.permute(t_4, (0, 2, 3, 1, 4, ))
		t_4 = torch.reshape(t_4, (1024, 56, 64, 112, ))

		# [s*H]@Shiftf6400fb251b2477a -> [s*H]@Split25ee6f350ecc19b9
		t_4 = torch.roll(t_4, self.shift_direction, 3)

		# [s*H]@Split25ee6f350ecc19b9 -> [H]@Shift41a433c05e30b91d, [s]@Reduced95c644a3c072d9a
		t_4 = torch.reshape(t_4, (1024, 56, 64, 56, 2, ))

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
		t_2 = torch.reshape(t_2, (1024, 1792, 28, 1, ))
		t_2 = torch.nn.functional.unfold(t_2, (3, 1, ), padding=(1, 0, ))
		t_2 = torch.reshape(t_2, (1024, 64, 28, 3, 28, ))

		# Permute to match the output of this subgraph.
		t_2 = torch.permute(t_2, (0, 1, 2, 4, 3, ))

		# Perform contraction.
		t_3 = torch.einsum("mkonj, kjil -> monil", t_2, in_1)

		# No contraction needed.
		t_4 = t_3

		# [H]@Mergeb85033bfb9503997, [s]@Mergeb85033bfb9503996 -> [s*H]@Shiftf6400fb251b2477a
		t_4 = torch.permute(t_4, (0, 2, 3, 1, 4, ))
		t_4 = torch.reshape(t_4, (1024, 28, 128, 56, ))

		# [s*H]@Shiftf6400fb251b2477a -> [s*H]@Split25ee6f350ecc19b9
		t_4 = torch.roll(t_4, self.shift_direction, 3)

		# [s*H]@Split25ee6f350ecc19b9 -> [H]@Shift41a433c05e30b91d, [s]@Reduced95c644a3c072d9a
		t_4 = torch.reshape(t_4, (1024, 28, 128, 28, 2, ))

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
		t_2 = torch.reshape(t_2, (1024, 3584, 28, 1, ))
		t_2 = torch.nn.functional.unfold(t_2, (3, 1, ), padding=(1, 0, ))
		t_2 = torch.reshape(t_2, (1024, 128, 28, 3, 28, ))

		# Permute to match the output of this subgraph.
		t_2 = torch.permute(t_2, (0, 1, 2, 4, 3, ))

		# Perform contraction.
		t_3 = torch.einsum("mkonj, kjil -> monil", t_2, in_1)

		# No contraction needed.
		t_4 = t_3

		# [H]@Mergeb85033bfb9503997, [s]@Mergeb85033bfb9503996 -> [s*H]@Shiftf6400fb251b2477a
		t_4 = torch.permute(t_4, (0, 2, 3, 1, 4, ))
		t_4 = torch.reshape(t_4, (1024, 28, 128, 56, ))

		# [s*H]@Shiftf6400fb251b2477a -> [s*H]@Split25ee6f350ecc19b9
		t_4 = torch.roll(t_4, self.shift_direction, 3)

		# [s*H]@Split25ee6f350ecc19b9 -> [H]@Shift41a433c05e30b91d, [s]@Reduced95c644a3c072d9a
		t_4 = torch.reshape(t_4, (1024, 28, 128, 28, 2, ))

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
		t_2 = torch.reshape(t_2, (1024, 1792, 14, 1, ))
		t_2 = torch.nn.functional.unfold(t_2, (3, 1, ), padding=(1, 0, ))
		t_2 = torch.reshape(t_2, (1024, 128, 14, 3, 14, ))

		# Permute to match the output of this subgraph.
		t_2 = torch.permute(t_2, (0, 1, 2, 4, 3, ))

		# Perform contraction.
		t_3 = torch.einsum("mkonj, kjil -> monil", t_2, in_1)

		# No contraction needed.
		t_4 = t_3

		# [H]@Mergeb85033bfb9503997, [s]@Mergeb85033bfb9503996 -> [s*H]@Shiftf6400fb251b2477a
		t_4 = torch.permute(t_4, (0, 2, 3, 1, 4, ))
		t_4 = torch.reshape(t_4, (1024, 14, 256, 28, ))

		# [s*H]@Shiftf6400fb251b2477a -> [s*H]@Split25ee6f350ecc19b9
		t_4 = torch.roll(t_4, self.shift_direction, 3)

		# [s*H]@Split25ee6f350ecc19b9 -> [H]@Shift41a433c05e30b91d, [s]@Reduced95c644a3c072d9a
		t_4 = torch.reshape(t_4, (1024, 14, 256, 14, 2, ))

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
		t_2 = torch.reshape(t_2, (1024, 3584, 14, 1, ))
		t_2 = torch.nn.functional.unfold(t_2, (3, 1, ), padding=(1, 0, ))
		t_2 = torch.reshape(t_2, (1024, 256, 14, 3, 14, ))

		# Permute to match the output of this subgraph.
		t_2 = torch.permute(t_2, (0, 1, 2, 4, 3, ))

		# Perform contraction.
		t_3 = torch.einsum("mkonj, kjil -> monil", t_2, in_1)

		# No contraction needed.
		t_4 = t_3

		# [H]@Mergeb85033bfb9503997, [s]@Mergeb85033bfb9503996 -> [s*H]@Shiftf6400fb251b2477a
		t_4 = torch.permute(t_4, (0, 2, 3, 1, 4, ))
		t_4 = torch.reshape(t_4, (1024, 14, 256, 28, ))

		# [s*H]@Shiftf6400fb251b2477a -> [s*H]@Split25ee6f350ecc19b9
		t_4 = torch.roll(t_4, self.shift_direction, 3)

		# [s*H]@Split25ee6f350ecc19b9 -> [H]@Shift41a433c05e30b91d, [s]@Reduced95c644a3c072d9a
		t_4 = torch.reshape(t_4, (1024, 14, 256, 14, 2, ))

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
		t_2 = torch.reshape(t_2, (1024, 1792, 7, 1, ))
		t_2 = torch.nn.functional.unfold(t_2, (3, 1, ), padding=(1, 0, ))
		t_2 = torch.reshape(t_2, (1024, 256, 7, 3, 7, ))

		# Permute to match the output of this subgraph.
		t_2 = torch.permute(t_2, (0, 1, 2, 4, 3, ))

		# Perform contraction.
		t_3 = torch.einsum("mkonj, kjil -> monil", t_2, in_1)

		# No contraction needed.
		t_4 = t_3

		# [H]@Mergeb85033bfb9503997, [s]@Mergeb85033bfb9503996 -> [s*H]@Shiftf6400fb251b2477a
		t_4 = torch.permute(t_4, (0, 2, 3, 1, 4, ))
		t_4 = torch.reshape(t_4, (1024, 7, 512, 14, ))

		# [s*H]@Shiftf6400fb251b2477a -> [s*H]@Split25ee6f350ecc19b9
		t_4 = torch.roll(t_4, self.shift_direction, 3)

		# [s*H]@Split25ee6f350ecc19b9 -> [H]@Shift41a433c05e30b91d, [s]@Reduced95c644a3c072d9a
		t_4 = torch.reshape(t_4, (1024, 7, 512, 7, 2, ))

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
		t_2 = torch.reshape(t_2, (1024, 3584, 7, 1, ))
		t_2 = torch.nn.functional.unfold(t_2, (3, 1, ), padding=(1, 0, ))
		t_2 = torch.reshape(t_2, (1024, 512, 7, 3, 7, ))

		# Permute to match the output of this subgraph.
		t_2 = torch.permute(t_2, (0, 1, 2, 4, 3, ))

		# Perform contraction.
		t_3 = torch.einsum("mkonj, kjil -> monil", t_2, in_1)

		# No contraction needed.
		t_4 = t_3

		# [H]@Mergeb85033bfb9503997, [s]@Mergeb85033bfb9503996 -> [s*H]@Shiftf6400fb251b2477a
		t_4 = torch.permute(t_4, (0, 2, 3, 1, 4, ))
		t_4 = torch.reshape(t_4, (1024, 7, 512, 14, ))

		# [s*H]@Shiftf6400fb251b2477a -> [s*H]@Split25ee6f350ecc19b9
		t_4 = torch.roll(t_4, self.shift_direction, 3)

		# [s*H]@Split25ee6f350ecc19b9 -> [H]@Shift41a433c05e30b91d, [s]@Reduced95c644a3c072d9a
		t_4 = torch.reshape(t_4, (1024, 7, 512, 7, 2, ))

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

