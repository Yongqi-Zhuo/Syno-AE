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
        interface_0_out_0x55ceeb214920 [label="N", shape=none];
        interface_0_out_0x55ceeb214948 [label="C_out", shape=none];
        interface_0_out_0x55ceeb214970 [label="H", shape=none];
        interface_0_out_0x55ceeb214998 [label="H", shape=none];
    }
    {
        rank = same;
        interface_0_out_0x55ceeb214920;
        interface_0_out_0x55ceeb214948;
        interface_0_out_0x55ceeb214970;
        interface_0_out_0x55ceeb214998;
    }
    // Input 0.
    subgraph cluster_subgraph_0_in_0 {
        label = "";
        interface_0_in_0x55ceeb214920 [label="N", shape=none];
        interface_0_in_0x55ceeec84fe0 [label="g", shape=none];
        interface_0_in_0x55ceeec84ff8 [label="g^-1*C_out", shape=none];
        interface_0_in_0x55ceeec839e0 [label="H", shape=none];
        interface_0_in_0x55ceeb214998 [label="H", shape=none];
    }
    {
        rank = same;
        interface_0_in_0x55ceeb214920;
        interface_0_in_0x55ceeec84fe0;
        interface_0_in_0x55ceeec84ff8;
        interface_0_in_0x55ceeec839e0;
        interface_0_in_0x55ceeb214998;
    }
    // Op's.
    op_0x55ceeec839c0 [label="Shift"];
    op_0x55ceeec84fa0 [label="Merge"];
    // Dimension's.
    interface_0_in_0x55ceeb214920 -> interface_0_out_0x55ceeb214920 [label="N"];
    op_0x55ceeec84fa0 -> interface_0_out_0x55ceeb214948 [label="C_out"];
    op_0x55ceeec839c0 -> interface_0_out_0x55ceeb214970 [label="H"];
    interface_0_in_0x55ceeb214998 -> interface_0_out_0x55ceeb214998 [label="H"];
    interface_0_in_0x55ceeec839e0 -> op_0x55ceeec839c0 [label="H"];
    interface_0_in_0x55ceeec84fe0 -> op_0x55ceeec84fa0 [label="g"];
    interface_0_in_0x55ceeec84ff8 -> op_0x55ceeec84fa0 [label="g^-1*C_out"];
}

// Stage tensor.
subgraph cluster_subgraph_1 {
    label = "Subgraph 1";
    // Reductions.
    reduce_0x7f854c001ab0 [label="Sum", shape=box];
    reduce_0x7f854c005820 [label="Sum", shape=box];
    reduce_0x7f854c001a98 [label="Sum", shape=box];
    // Output.
    subgraph cluster_subgraph_1_out {
        label = "";
        interface_1_out_0x55ceeb214920 [label="N", shape=none];
        interface_1_out_0x55ceeec84fe0 [label="g", shape=none];
        interface_1_out_0x55ceeec84ff8 [label="g^-1*C_out", shape=none];
        interface_1_out_0x55ceeec839e0 [label="H", shape=none];
        interface_1_out_0x55ceeb214998 [label="H", shape=none];
    }
    {
        rank = same;
        reduce_0x7f854c001ab0;
        reduce_0x7f854c005820;
        reduce_0x7f854c001a98;
        interface_1_out_0x55ceeb214920;
        interface_1_out_0x55ceeec84fe0;
        interface_1_out_0x55ceeec84ff8;
        interface_1_out_0x55ceeec839e0;
        interface_1_out_0x55ceeb214998;
    }
    // Input 0.
    subgraph cluster_subgraph_1_in_0 {
        label = "";
        interface_1_in_0x55ceeb214920 [label="N", shape=none];
        interface_1_in_0x55ceeec82dd0 [label="k_1", shape=none];
        interface_1_in_0x55ceeec82e20 [label="g", shape=none];
        interface_1_in_0x55ceeec82d30 [label="g^-1*s^-1*C_in", shape=none];
        interface_1_in_0x55ceeec839e0 [label="H", shape=none];
        interface_1_in_0x55ceeec82c40 [label="k_1", shape=none];
        interface_1_in_0x55ceeb214998 [label="H", shape=none];
    }
    // Input 1.
    subgraph cluster_subgraph_1_in_1 {
        label = "";
        interface_1_in_0x55ceeec82de8 [label="k_1", shape=none];
        interface_1_in_0x55ceeec82d48 [label="g^-1*s^-1*C_in", shape=none];
        interface_1_in_0x55ceeec82e38 [label="g", shape=none];
        interface_1_in_0x55ceeec82e88 [label="g^-1*C_out", shape=none];
        interface_1_in_0x55ceeec82c58 [label="k_1", shape=none];
    }
    {
        rank = same;
        interface_1_in_0x55ceeb214920;
        interface_1_in_0x55ceeec82dd0;
        interface_1_in_0x55ceeec82e20;
        interface_1_in_0x55ceeec82d30;
        interface_1_in_0x55ceeec839e0;
        interface_1_in_0x55ceeec82c40;
        interface_1_in_0x55ceeb214998;
        interface_1_in_0x55ceeec82de8;
        interface_1_in_0x55ceeec82d48;
        interface_1_in_0x55ceeec82e38;
        interface_1_in_0x55ceeec82e88;
        interface_1_in_0x55ceeec82c58;
    }
    // Op's.
    op_0x55ceeec82c20 [label="Share"];
    op_0x55ceeec82d10 [label="Share"];
    op_0x55ceeec82db0 [label="Share"];
    op_0x55ceeec82e00 [label="Share"];
    op_0x55ceeec82e50 [label="Share"];
    op_0x55ceeec831b8 [label="Expand"];
    // Dimension's.
    interface_1_in_0x55ceeb214920 -> interface_1_out_0x55ceeb214920 [label="N"];
    interface_1_in_0x55ceeb214998 -> interface_1_out_0x55ceeb214998 [label="H"];
    interface_1_in_0x55ceeec82c40 -> op_0x55ceeec82c20 [label="k_1"];
    interface_1_in_0x55ceeec82c58 -> op_0x55ceeec82c20 [label="k_1"];
    interface_1_in_0x55ceeec82d30 -> op_0x55ceeec82d10 [label="g^-1*s^-1*C_in"];
    interface_1_in_0x55ceeec82d48 -> op_0x55ceeec82d10 [label="g^-1*s^-1*C_in"];
    interface_1_in_0x55ceeec82dd0 -> op_0x55ceeec82db0 [label="k_1"];
    interface_1_in_0x55ceeec82de8 -> op_0x55ceeec82db0 [label="k_1"];
    interface_1_in_0x55ceeec82e20 -> op_0x55ceeec82e00 [label="g"];
    interface_1_in_0x55ceeec82e38 -> op_0x55ceeec82e00 [label="g"];
    op_0x55ceeec831b8 -> op_0x55ceeec82e50 [label="g^-1*C_out"];
    interface_1_in_0x55ceeec82e88 -> op_0x55ceeec82e50 [label="g^-1*C_out"];
    interface_1_in_0x55ceeec839e0 -> interface_1_out_0x55ceeec839e0 [label="H"];
    op_0x55ceeec82e00 -> interface_1_out_0x55ceeec84fe0 [label="g"];
    op_0x55ceeec82e50 -> interface_1_out_0x55ceeec84ff8 [label="g^-1*C_out"];
    op_0x55ceeec82c20 -> reduce_0x7f854c001a98 [label="k_1"];
    op_0x55ceeec82db0 -> reduce_0x7f854c001ab0 [label="k_1"];
    op_0x55ceeec82d10 -> reduce_0x7f854c005820 [label="g^-1*s^-1*C_in"];
}

// Stage tensor.
subgraph cluster_subgraph_2 {
    label = "Subgraph 2";
    // Reductions.
    // Output.
    subgraph cluster_subgraph_2_out {
        label = "";
        interface_2_out_0x55ceeb214920 [label="N", shape=none];
        interface_2_out_0x55ceeec82dd0 [label="k_1", shape=none];
        interface_2_out_0x55ceeec82e20 [label="g", shape=none];
        interface_2_out_0x55ceeec82d30 [label="g^-1*s^-1*C_in", shape=none];
        interface_2_out_0x55ceeec839e0 [label="H", shape=none];
        interface_2_out_0x55ceeec82c40 [label="k_1", shape=none];
        interface_2_out_0x55ceeb214998 [label="H", shape=none];
    }
    {
        rank = same;
        interface_2_out_0x55ceeb214920;
        interface_2_out_0x55ceeec82dd0;
        interface_2_out_0x55ceeec82e20;
        interface_2_out_0x55ceeec82d30;
        interface_2_out_0x55ceeec839e0;
        interface_2_out_0x55ceeec82c40;
        interface_2_out_0x55ceeb214998;
    }
    // Input 0.
    subgraph cluster_subgraph_2_in_0 {
        label = "";
        interface_2_in_0x55ceeb214920 [label="N", shape=none];
        interface_2_in_0x55ceeed1e1c0 [label="s^-1*C_in", shape=none];
        interface_2_in_0x55ceeec839e0 [label="H", shape=none];
        interface_2_in_0x55ceeec83a40 [label="H", shape=none];
    }
    {
        rank = same;
        interface_2_in_0x55ceeb214920;
        interface_2_in_0x55ceeed1e1c0;
        interface_2_in_0x55ceeec839e0;
        interface_2_in_0x55ceeec83a40;
    }
    // Op's.
    op_0x55ceeec83a20 [label="Shift"];
    op_0x55ceeec91700 [label="Unfold"];
    op_0x55ceeec91980 [label="Unfold"];
    op_0x55ceeed1e180 [label="Split"];
    // Dimension's.
    interface_2_in_0x55ceeb214920 -> interface_2_out_0x55ceeb214920 [label="N"];
    op_0x55ceeec91700 -> interface_2_out_0x55ceeb214998 [label="H"];
    op_0x55ceeec91700 -> interface_2_out_0x55ceeec82c40 [label="k_1"];
    op_0x55ceeed1e180 -> interface_2_out_0x55ceeec82d30 [label="g^-1*s^-1*C_in"];
    op_0x55ceeec91980 -> interface_2_out_0x55ceeec82dd0 [label="k_1"];
    op_0x55ceeec91980 -> interface_2_out_0x55ceeec82e20 [label="g"];
    interface_2_in_0x55ceeec839e0 -> interface_2_out_0x55ceeec839e0 [label="H"];
    interface_2_in_0x55ceeec83a40 -> op_0x55ceeec83a20 [label="H"];
    op_0x55ceeec83a20 -> op_0x55ceeec91700 [label="H"];
    op_0x55ceeed1e180 -> op_0x55ceeec91980 [label="g"];
    interface_2_in_0x55ceeed1e1c0 -> op_0x55ceeed1e180 [label="s^-1*C_in"];
}

// Stage tensor.
subgraph cluster_subgraph_3 {
    label = "Subgraph 3";
    // Reductions.
    reduce_0x7f854c002e58 [label="Sum", shape=box];
    // Output.
    subgraph cluster_subgraph_3_out {
        label = "";
        interface_3_out_0x55ceeb214920 [label="N", shape=none];
        interface_3_out_0x55ceeed1e1c0 [label="s^-1*C_in", shape=none];
        interface_3_out_0x55ceeec839e0 [label="H", shape=none];
        interface_3_out_0x55ceeec83a40 [label="H", shape=none];
    }
    {
        rank = same;
        reduce_0x7f854c002e58;
        interface_3_out_0x55ceeb214920;
        interface_3_out_0x55ceeed1e1c0;
        interface_3_out_0x55ceeec839e0;
        interface_3_out_0x55ceeec83a40;
    }
    // Input 0.
    subgraph cluster_subgraph_3_in_0 {
        label = "";
        interface_3_in_0x55ceeb214920 [label="N", shape=none];
        interface_3_in_0x55ceeed1e4e0 [label="C_in", shape=none];
        interface_3_in_0x55ceeec839e0 [label="H", shape=none];
        interface_3_in_0x55ceeec83a40 [label="H", shape=none];
    }
    {
        rank = same;
        interface_3_in_0x55ceeb214920;
        interface_3_in_0x55ceeed1e4e0;
        interface_3_in_0x55ceeec839e0;
        interface_3_in_0x55ceeec83a40;
    }
    // Op's.
    op_0x55ceeed1e4a0 [label="Split"];
    // Dimension's.
    interface_3_in_0x55ceeb214920 -> interface_3_out_0x55ceeb214920 [label="N"];
    interface_3_in_0x55ceeec839e0 -> interface_3_out_0x55ceeec839e0 [label="H"];
    interface_3_in_0x55ceeec83a40 -> interface_3_out_0x55ceeec83a40 [label="H"];
    op_0x55ceeed1e4a0 -> interface_3_out_0x55ceeed1e1c0 [label="s^-1*C_in"];
    interface_3_in_0x55ceeed1e4e0 -> op_0x55ceeed1e4a0 [label="C_in"];
    op_0x55ceeed1e4a0 -> reduce_0x7f854c002e58 [label="s"];
}

// Input tensor.
subgraph cluster_subgraph_4 {
    label = "Input 0";
    interface_4_out_0x55ceeb214920 [label="N", shape=none];
    interface_4_out_0x55ceeed1e4e0 [label="C_in", shape=none];
    interface_4_out_0x55ceeec839e0 [label="H", shape=none];
    interface_4_out_0x55ceeec83a40 [label="H", shape=none];
}

interface_4_out_0x55ceeb214920 -> interface_3_in_0x55ceeb214920;
interface_4_out_0x55ceeed1e4e0 -> interface_3_in_0x55ceeed1e4e0;
interface_4_out_0x55ceeec839e0 -> interface_3_in_0x55ceeec839e0;
interface_4_out_0x55ceeec83a40 -> interface_3_in_0x55ceeec83a40;

interface_3_out_0x55ceeb214920 -> interface_2_in_0x55ceeb214920;
interface_3_out_0x55ceeed1e1c0 -> interface_2_in_0x55ceeed1e1c0;
interface_3_out_0x55ceeec839e0 -> interface_2_in_0x55ceeec839e0;
interface_3_out_0x55ceeec83a40 -> interface_2_in_0x55ceeec83a40;

interface_2_out_0x55ceeb214920 -> interface_1_in_0x55ceeb214920;
interface_2_out_0x55ceeec82dd0 -> interface_1_in_0x55ceeec82dd0;
interface_2_out_0x55ceeec82e20 -> interface_1_in_0x55ceeec82e20;
interface_2_out_0x55ceeec82d30 -> interface_1_in_0x55ceeec82d30;
interface_2_out_0x55ceeec839e0 -> interface_1_in_0x55ceeec839e0;
interface_2_out_0x55ceeec82c40 -> interface_1_in_0x55ceeec82c40;
interface_2_out_0x55ceeb214998 -> interface_1_in_0x55ceeb214998;

// Input tensor.
subgraph cluster_subgraph_5 {
    label = "Input 1";
    interface_5_out_0x55ceeec82de8 [label="k_1", shape=none];
    interface_5_out_0x55ceeec82d48 [label="g^-1*s^-1*C_in", shape=none];
    interface_5_out_0x55ceeec82e38 [label="g", shape=none];
    interface_5_out_0x55ceeec82e88 [label="g^-1*C_out", shape=none];
    interface_5_out_0x55ceeec82c58 [label="k_1", shape=none];
}

interface_5_out_0x55ceeec82de8 -> interface_1_in_0x55ceeec82de8;
interface_5_out_0x55ceeec82d48 -> interface_1_in_0x55ceeec82d48;
interface_5_out_0x55ceeec82e38 -> interface_1_in_0x55ceeec82e38;
interface_5_out_0x55ceeec82e88 -> interface_1_in_0x55ceeec82e88;
interface_5_out_0x55ceeec82c58 -> interface_1_in_0x55ceeec82c58;

interface_1_out_0x55ceeb214920 -> interface_0_in_0x55ceeb214920;
interface_1_out_0x55ceeec84fe0 -> interface_0_in_0x55ceeec84fe0;
interface_1_out_0x55ceeec84ff8 -> interface_0_in_0x55ceeec84ff8;
interface_1_out_0x55ceeec839e0 -> interface_0_in_0x55ceeec839e0;
interface_1_out_0x55ceeb214998 -> interface_0_in_0x55ceeb214998;

{
    rank = same;
    interface_4_out_0x55ceeb214920;
    interface_4_out_0x55ceeed1e4e0;
    interface_4_out_0x55ceeec839e0;
    interface_4_out_0x55ceeec83a40;
    interface_5_out_0x55ceeec82de8;
    interface_5_out_0x55ceeec82d48;
    interface_5_out_0x55ceeec82e38;
    interface_5_out_0x55ceeec82e88;
    interface_5_out_0x55ceeec82c58;
}
subgraph cluster_subgraph_output {
    label = "Output";
    interface_6_in_0x55ceeb214920 [label="N", shape=none];
    interface_6_in_0x55ceeb214948 [label="C_out", shape=none];
    interface_6_in_0x55ceeb214970 [label="H", shape=none];
    interface_6_in_0x55ceeb214998 [label="H", shape=none];
}
interface_0_out_0x55ceeb214920 -> interface_6_in_0x55ceeb214920;
interface_0_out_0x55ceeb214948 -> interface_6_in_0x55ceeb214948;
interface_0_out_0x55ceeb214970 -> interface_6_in_0x55ceeb214970;
interface_0_out_0x55ceeb214998 -> interface_6_in_0x55ceeb214998;

}

"""
class kernel_generated_0(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([3, 2, 32, 4, 3]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]

		# No contraction needed.
		t_2 = in_0

		# [C_in]@Splita06ce4f8f1aa614a -> [s]@Reduced95c644a3c072d9a, [s^-1*C_in]@Split313fe4f50bf9d419
		t_2 = torch.reshape(t_2, (1, 2, 64, 56, 56, ))

		# [s]@Reduce
		t_2 = torch.sum(t_2, dim=(1, ))

		# No contraction needed.
		t_3 = t_2

		# [s^-1*C_in]@Split313fe4f50bf9d419 -> [g]@Unfold00a2b12a52289aa2, [g^-1*s^-1*C_in]@Share77b21cfebfb4fc10
		t_3 = torch.reshape(t_3, (1, 32, 2, 56, 56, ))

		# [g]@Unfold00a2b12a52289aa2 -> [g]@Share3ccf867b1ad85e4e, [k_1]@Share02da0a485106ab3d
		t_3 = torch.reshape(t_3, (1, 1, 32, 6272, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (1, 3, 32, 2, 56, 56, ))

		# [H]@Shiftdbd5b2e652804221 -> [H]@Unfold0063bc810b9e1e60
		t_3 = torch.roll(t_3, self.shift_direction, 5)

		# [H]@Unfold0063bc810b9e1e60 -> [H]@Iteratorb0a1def4ad5784ec, [k_1]@Share26cfa48d169008e4
		t_3 = torch.reshape(t_3, (1, 10752, 56, 1, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (1, 3, 32, 2, 56, 3, 56, ))

		# Perform contraction.
		t_4 = torch.einsum("nkljpio, kjlmi -> nlmpo", t_3, in_1)

		# No contraction needed.
		t_5 = t_4

		# [g]@Merge402ce7fe20a0a5fb, [g^-1*C_out]@Merge402ce7fe20a0a5f8 -> [C_out]@Iteratorc7f8eb87a5a0a9e0
		t_5 = torch.reshape(t_5, (1, 128, 56, 56, ))

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
			torch.randn([3, 4, 32, 8, 3]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]

		# No contraction needed.
		t_2 = in_0

		# [C_in]@Splita06ce4f8f1aa614a -> [s]@Reduced95c644a3c072d9a, [s^-1*C_in]@Split313fe4f50bf9d419
		t_2 = torch.reshape(t_2, (1, 2, 128, 28, 28, ))

		# [s]@Reduce
		t_2 = torch.sum(t_2, dim=(1, ))

		# No contraction needed.
		t_3 = t_2

		# [s^-1*C_in]@Split313fe4f50bf9d419 -> [g]@Unfold00a2b12a52289aa2, [g^-1*s^-1*C_in]@Share77b21cfebfb4fc10
		t_3 = torch.reshape(t_3, (1, 32, 4, 28, 28, ))

		# [g]@Unfold00a2b12a52289aa2 -> [g]@Share3ccf867b1ad85e4e, [k_1]@Share02da0a485106ab3d
		t_3 = torch.reshape(t_3, (1, 1, 32, 3136, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (1, 3, 32, 4, 28, 28, ))

		# [H]@Shiftdbd5b2e652804221 -> [H]@Unfold0063bc810b9e1e60
		t_3 = torch.roll(t_3, self.shift_direction, 5)

		# [H]@Unfold0063bc810b9e1e60 -> [H]@Iteratorb0a1def4ad5784ec, [k_1]@Share26cfa48d169008e4
		t_3 = torch.reshape(t_3, (1, 10752, 28, 1, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (1, 3, 32, 4, 28, 3, 28, ))

		# Perform contraction.
		t_4 = torch.einsum("nkljpio, kjlmi -> nlmpo", t_3, in_1)

		# No contraction needed.
		t_5 = t_4

		# [g]@Merge402ce7fe20a0a5fb, [g^-1*C_out]@Merge402ce7fe20a0a5f8 -> [C_out]@Iteratorc7f8eb87a5a0a9e0
		t_5 = torch.reshape(t_5, (1, 256, 28, 28, ))

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
			torch.randn([3, 8, 32, 16, 3]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]

		# No contraction needed.
		t_2 = in_0

		# [C_in]@Splita06ce4f8f1aa614a -> [s]@Reduced95c644a3c072d9a, [s^-1*C_in]@Split313fe4f50bf9d419
		t_2 = torch.reshape(t_2, (1, 2, 256, 14, 14, ))

		# [s]@Reduce
		t_2 = torch.sum(t_2, dim=(1, ))

		# No contraction needed.
		t_3 = t_2

		# [s^-1*C_in]@Split313fe4f50bf9d419 -> [g]@Unfold00a2b12a52289aa2, [g^-1*s^-1*C_in]@Share77b21cfebfb4fc10
		t_3 = torch.reshape(t_3, (1, 32, 8, 14, 14, ))

		# [g]@Unfold00a2b12a52289aa2 -> [g]@Share3ccf867b1ad85e4e, [k_1]@Share02da0a485106ab3d
		t_3 = torch.reshape(t_3, (1, 1, 32, 1568, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (1, 3, 32, 8, 14, 14, ))

		# [H]@Shiftdbd5b2e652804221 -> [H]@Unfold0063bc810b9e1e60
		t_3 = torch.roll(t_3, self.shift_direction, 5)

		# [H]@Unfold0063bc810b9e1e60 -> [H]@Iteratorb0a1def4ad5784ec, [k_1]@Share26cfa48d169008e4
		t_3 = torch.reshape(t_3, (1, 10752, 14, 1, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (1, 3, 32, 8, 14, 3, 14, ))

		# Perform contraction.
		t_4 = torch.einsum("nkljpio, kjlmi -> nlmpo", t_3, in_1)

		# No contraction needed.
		t_5 = t_4

		# [g]@Merge402ce7fe20a0a5fb, [g^-1*C_out]@Merge402ce7fe20a0a5f8 -> [C_out]@Iteratorc7f8eb87a5a0a9e0
		t_5 = torch.reshape(t_5, (1, 512, 14, 14, ))

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
			torch.randn([3, 16, 32, 32, 3]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]

		# No contraction needed.
		t_2 = in_0

		# [C_in]@Splita06ce4f8f1aa614a -> [s]@Reduced95c644a3c072d9a, [s^-1*C_in]@Split313fe4f50bf9d419
		t_2 = torch.reshape(t_2, (1, 2, 512, 7, 7, ))

		# [s]@Reduce
		t_2 = torch.sum(t_2, dim=(1, ))

		# No contraction needed.
		t_3 = t_2

		# [s^-1*C_in]@Split313fe4f50bf9d419 -> [g]@Unfold00a2b12a52289aa2, [g^-1*s^-1*C_in]@Share77b21cfebfb4fc10
		t_3 = torch.reshape(t_3, (1, 32, 16, 7, 7, ))

		# [g]@Unfold00a2b12a52289aa2 -> [g]@Share3ccf867b1ad85e4e, [k_1]@Share02da0a485106ab3d
		t_3 = torch.reshape(t_3, (1, 1, 32, 784, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (1, 3, 32, 16, 7, 7, ))

		# [H]@Shiftdbd5b2e652804221 -> [H]@Unfold0063bc810b9e1e60
		t_3 = torch.roll(t_3, self.shift_direction, 5)

		# [H]@Unfold0063bc810b9e1e60 -> [H]@Iteratorb0a1def4ad5784ec, [k_1]@Share26cfa48d169008e4
		t_3 = torch.reshape(t_3, (1, 10752, 7, 1, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (1, 3, 32, 16, 7, 3, 7, ))

		# Perform contraction.
		t_4 = torch.einsum("nkljpio, kjlmi -> nlmpo", t_3, in_1)

		# No contraction needed.
		t_5 = t_4

		# [g]@Merge402ce7fe20a0a5fb, [g^-1*C_out]@Merge402ce7fe20a0a5f8 -> [C_out]@Iteratorc7f8eb87a5a0a9e0
		t_5 = torch.reshape(t_5, (1, 1024, 7, 7, ))

		# [H]@Shift41a433c05e30b91d -> [H]@Iterator96123ba3184da39c
		t_5 = torch.roll(t_5, self.shift_direction, 2)

		# No need to crop the output tensor.
		y = t_5

		return y

