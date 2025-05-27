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
        interface_0_out_0x55d1b69697c0 [label="N", shape=none];
        interface_0_out_0x55d1b69697e8 [label="C_out", shape=none];
        interface_0_out_0x55d1b6969810 [label="H", shape=none];
        interface_0_out_0x55d1b6969838 [label="H", shape=none];
    }
    {
        rank = same;
        interface_0_out_0x55d1b69697c0;
        interface_0_out_0x55d1b69697e8;
        interface_0_out_0x55d1b6969810;
        interface_0_out_0x55d1b6969838;
    }
    // Input 0.
    subgraph cluster_subgraph_0_in_0 {
        label = "";
        interface_0_in_0x55d1b69697c0 [label="N", shape=none];
        interface_0_in_0x55d1ce270300 [label="g", shape=none];
        interface_0_in_0x55d1ce270318 [label="g^-1*C_out", shape=none];
        interface_0_in_0x55d1ce266c20 [label="H", shape=none];
        interface_0_in_0x55d1b6969838 [label="H", shape=none];
    }
    {
        rank = same;
        interface_0_in_0x55d1b69697c0;
        interface_0_in_0x55d1ce270300;
        interface_0_in_0x55d1ce270318;
        interface_0_in_0x55d1ce266c20;
        interface_0_in_0x55d1b6969838;
    }
    // Op's.
    op_0x55d1ce266c00 [label="Shift"];
    op_0x55d1ce2702c0 [label="Merge"];
    // Dimension's.
    interface_0_in_0x55d1b69697c0 -> interface_0_out_0x55d1b69697c0 [label="N"];
    op_0x55d1ce2702c0 -> interface_0_out_0x55d1b69697e8 [label="C_out"];
    op_0x55d1ce266c00 -> interface_0_out_0x55d1b6969810 [label="H"];
    interface_0_in_0x55d1b6969838 -> interface_0_out_0x55d1b6969838 [label="H"];
    interface_0_in_0x55d1ce266c20 -> op_0x55d1ce266c00 [label="H"];
    interface_0_in_0x55d1ce270300 -> op_0x55d1ce2702c0 [label="g"];
    interface_0_in_0x55d1ce270318 -> op_0x55d1ce2702c0 [label="g^-1*C_out"];
}

// Stage tensor.
subgraph cluster_subgraph_1 {
    label = "Subgraph 1";
    // Reductions.
    reduce_0x7f2690003ab0 [label="Sum", shape=box];
    reduce_0x7f2690007720 [label="Sum", shape=box];
    reduce_0x7f2690003a98 [label="Sum", shape=box];
    // Output.
    subgraph cluster_subgraph_1_out {
        label = "";
        interface_1_out_0x55d1b69697c0 [label="N", shape=none];
        interface_1_out_0x55d1ce270300 [label="g", shape=none];
        interface_1_out_0x55d1ce270318 [label="g^-1*C_out", shape=none];
        interface_1_out_0x55d1ce266c20 [label="H", shape=none];
        interface_1_out_0x55d1b6969838 [label="H", shape=none];
    }
    {
        rank = same;
        reduce_0x7f2690003ab0;
        reduce_0x7f2690007720;
        reduce_0x7f2690003a98;
        interface_1_out_0x55d1b69697c0;
        interface_1_out_0x55d1ce270300;
        interface_1_out_0x55d1ce270318;
        interface_1_out_0x55d1ce266c20;
        interface_1_out_0x55d1b6969838;
    }
    // Input 0.
    subgraph cluster_subgraph_1_in_0 {
        label = "";
        interface_1_in_0x55d1b69697c0 [label="N", shape=none];
        interface_1_in_0x55d1ce264de0 [label="k_1", shape=none];
        interface_1_in_0x55d1ce264e30 [label="g", shape=none];
        interface_1_in_0x55d1ce264cf0 [label="g^-1*s^-1*C_in", shape=none];
        interface_1_in_0x55d1ce266c20 [label="H", shape=none];
        interface_1_in_0x55d1ce264d90 [label="k_1", shape=none];
        interface_1_in_0x55d1b6969838 [label="H", shape=none];
    }
    // Input 1.
    subgraph cluster_subgraph_1_in_1 {
        label = "";
        interface_1_in_0x55d1ce264df8 [label="k_1", shape=none];
        interface_1_in_0x55d1ce264d08 [label="g^-1*s^-1*C_in", shape=none];
        interface_1_in_0x55d1ce264e48 [label="g", shape=none];
        interface_1_in_0x55d1ce264e98 [label="g^-1*C_out", shape=none];
        interface_1_in_0x55d1ce264da8 [label="k_1", shape=none];
    }
    {
        rank = same;
        interface_1_in_0x55d1b69697c0;
        interface_1_in_0x55d1ce264de0;
        interface_1_in_0x55d1ce264e30;
        interface_1_in_0x55d1ce264cf0;
        interface_1_in_0x55d1ce266c20;
        interface_1_in_0x55d1ce264d90;
        interface_1_in_0x55d1b6969838;
        interface_1_in_0x55d1ce264df8;
        interface_1_in_0x55d1ce264d08;
        interface_1_in_0x55d1ce264e48;
        interface_1_in_0x55d1ce264e98;
        interface_1_in_0x55d1ce264da8;
    }
    // Op's.
    op_0x55d1ce264cd0 [label="Share"];
    op_0x55d1ce264d70 [label="Share"];
    op_0x55d1ce264dc0 [label="Share"];
    op_0x55d1ce264e10 [label="Share"];
    op_0x55d1ce264e60 [label="Share"];
    op_0x55d1ce265198 [label="Expand"];
    // Dimension's.
    interface_1_in_0x55d1b69697c0 -> interface_1_out_0x55d1b69697c0 [label="N"];
    interface_1_in_0x55d1b6969838 -> interface_1_out_0x55d1b6969838 [label="H"];
    interface_1_in_0x55d1ce264cf0 -> op_0x55d1ce264cd0 [label="g^-1*s^-1*C_in"];
    interface_1_in_0x55d1ce264d08 -> op_0x55d1ce264cd0 [label="g^-1*s^-1*C_in"];
    interface_1_in_0x55d1ce264d90 -> op_0x55d1ce264d70 [label="k_1"];
    interface_1_in_0x55d1ce264da8 -> op_0x55d1ce264d70 [label="k_1"];
    interface_1_in_0x55d1ce264de0 -> op_0x55d1ce264dc0 [label="k_1"];
    interface_1_in_0x55d1ce264df8 -> op_0x55d1ce264dc0 [label="k_1"];
    interface_1_in_0x55d1ce264e30 -> op_0x55d1ce264e10 [label="g"];
    interface_1_in_0x55d1ce264e48 -> op_0x55d1ce264e10 [label="g"];
    op_0x55d1ce265198 -> op_0x55d1ce264e60 [label="g^-1*C_out"];
    interface_1_in_0x55d1ce264e98 -> op_0x55d1ce264e60 [label="g^-1*C_out"];
    interface_1_in_0x55d1ce266c20 -> interface_1_out_0x55d1ce266c20 [label="H"];
    op_0x55d1ce264e10 -> interface_1_out_0x55d1ce270300 [label="g"];
    op_0x55d1ce264e60 -> interface_1_out_0x55d1ce270318 [label="g^-1*C_out"];
    op_0x55d1ce264d70 -> reduce_0x7f2690003a98 [label="k_1"];
    op_0x55d1ce264dc0 -> reduce_0x7f2690003ab0 [label="k_1"];
    op_0x55d1ce264cd0 -> reduce_0x7f2690007720 [label="g^-1*s^-1*C_in"];
}

// Stage tensor.
subgraph cluster_subgraph_2 {
    label = "Subgraph 2";
    // Reductions.
    // Output.
    subgraph cluster_subgraph_2_out {
        label = "";
        interface_2_out_0x55d1b69697c0 [label="N", shape=none];
        interface_2_out_0x55d1ce264de0 [label="k_1", shape=none];
        interface_2_out_0x55d1ce264e30 [label="g", shape=none];
        interface_2_out_0x55d1ce264cf0 [label="g^-1*s^-1*C_in", shape=none];
        interface_2_out_0x55d1ce266c20 [label="H", shape=none];
        interface_2_out_0x55d1ce264d90 [label="k_1", shape=none];
        interface_2_out_0x55d1b6969838 [label="H", shape=none];
    }
    {
        rank = same;
        interface_2_out_0x55d1b69697c0;
        interface_2_out_0x55d1ce264de0;
        interface_2_out_0x55d1ce264e30;
        interface_2_out_0x55d1ce264cf0;
        interface_2_out_0x55d1ce266c20;
        interface_2_out_0x55d1ce264d90;
        interface_2_out_0x55d1b6969838;
    }
    // Input 0.
    subgraph cluster_subgraph_2_in_0 {
        label = "";
        interface_2_in_0x55d1b69697c0 [label="N", shape=none];
        interface_2_in_0x55d1ce30f640 [label="s^-1*C_in", shape=none];
        interface_2_in_0x55d1ce266c20 [label="H", shape=none];
        interface_2_in_0x55d1ce266ce0 [label="H", shape=none];
    }
    {
        rank = same;
        interface_2_in_0x55d1b69697c0;
        interface_2_in_0x55d1ce30f640;
        interface_2_in_0x55d1ce266c20;
        interface_2_in_0x55d1ce266ce0;
    }
    // Op's.
    op_0x55d1ce266cc0 [label="Shift"];
    op_0x55d1ce2864c0 [label="Unfold"];
    op_0x55d1ce286640 [label="Unfold"];
    op_0x55d1ce30f600 [label="Split"];
    // Dimension's.
    interface_2_in_0x55d1b69697c0 -> interface_2_out_0x55d1b69697c0 [label="N"];
    op_0x55d1ce2864c0 -> interface_2_out_0x55d1b6969838 [label="H"];
    op_0x55d1ce30f600 -> interface_2_out_0x55d1ce264cf0 [label="g^-1*s^-1*C_in"];
    op_0x55d1ce2864c0 -> interface_2_out_0x55d1ce264d90 [label="k_1"];
    op_0x55d1ce286640 -> interface_2_out_0x55d1ce264de0 [label="k_1"];
    op_0x55d1ce286640 -> interface_2_out_0x55d1ce264e30 [label="g"];
    interface_2_in_0x55d1ce266c20 -> interface_2_out_0x55d1ce266c20 [label="H"];
    interface_2_in_0x55d1ce266ce0 -> op_0x55d1ce266cc0 [label="H"];
    op_0x55d1ce266cc0 -> op_0x55d1ce2864c0 [label="H"];
    op_0x55d1ce30f600 -> op_0x55d1ce286640 [label="g"];
    interface_2_in_0x55d1ce30f640 -> op_0x55d1ce30f600 [label="s^-1*C_in"];
}

// Stage tensor.
subgraph cluster_subgraph_3 {
    label = "Subgraph 3";
    // Reductions.
    reduce_0x7f2690004e58 [label="Sum", shape=box];
    // Output.
    subgraph cluster_subgraph_3_out {
        label = "";
        interface_3_out_0x55d1b69697c0 [label="N", shape=none];
        interface_3_out_0x55d1ce30f640 [label="s^-1*C_in", shape=none];
        interface_3_out_0x55d1ce266c20 [label="H", shape=none];
        interface_3_out_0x55d1ce266ce0 [label="H", shape=none];
    }
    {
        rank = same;
        reduce_0x7f2690004e58;
        interface_3_out_0x55d1b69697c0;
        interface_3_out_0x55d1ce30f640;
        interface_3_out_0x55d1ce266c20;
        interface_3_out_0x55d1ce266ce0;
    }
    // Input 0.
    subgraph cluster_subgraph_3_in_0 {
        label = "";
        interface_3_in_0x55d1b69697c0 [label="N", shape=none];
        interface_3_in_0x55d1ce30f960 [label="C_in", shape=none];
        interface_3_in_0x55d1ce266c20 [label="H", shape=none];
        interface_3_in_0x55d1ce266ce0 [label="H", shape=none];
    }
    {
        rank = same;
        interface_3_in_0x55d1b69697c0;
        interface_3_in_0x55d1ce30f960;
        interface_3_in_0x55d1ce266c20;
        interface_3_in_0x55d1ce266ce0;
    }
    // Op's.
    op_0x55d1ce30f920 [label="Split"];
    // Dimension's.
    interface_3_in_0x55d1b69697c0 -> interface_3_out_0x55d1b69697c0 [label="N"];
    interface_3_in_0x55d1ce266c20 -> interface_3_out_0x55d1ce266c20 [label="H"];
    interface_3_in_0x55d1ce266ce0 -> interface_3_out_0x55d1ce266ce0 [label="H"];
    op_0x55d1ce30f920 -> interface_3_out_0x55d1ce30f640 [label="s^-1*C_in"];
    interface_3_in_0x55d1ce30f960 -> op_0x55d1ce30f920 [label="C_in"];
    op_0x55d1ce30f920 -> reduce_0x7f2690004e58 [label="s"];
}

// Input tensor.
subgraph cluster_subgraph_4 {
    label = "Input 0";
    interface_4_out_0x55d1b69697c0 [label="N", shape=none];
    interface_4_out_0x55d1ce30f960 [label="C_in", shape=none];
    interface_4_out_0x55d1ce266c20 [label="H", shape=none];
    interface_4_out_0x55d1ce266ce0 [label="H", shape=none];
}

interface_4_out_0x55d1b69697c0 -> interface_3_in_0x55d1b69697c0;
interface_4_out_0x55d1ce30f960 -> interface_3_in_0x55d1ce30f960;
interface_4_out_0x55d1ce266c20 -> interface_3_in_0x55d1ce266c20;
interface_4_out_0x55d1ce266ce0 -> interface_3_in_0x55d1ce266ce0;

interface_3_out_0x55d1b69697c0 -> interface_2_in_0x55d1b69697c0;
interface_3_out_0x55d1ce30f640 -> interface_2_in_0x55d1ce30f640;
interface_3_out_0x55d1ce266c20 -> interface_2_in_0x55d1ce266c20;
interface_3_out_0x55d1ce266ce0 -> interface_2_in_0x55d1ce266ce0;

interface_2_out_0x55d1b69697c0 -> interface_1_in_0x55d1b69697c0;
interface_2_out_0x55d1ce264de0 -> interface_1_in_0x55d1ce264de0;
interface_2_out_0x55d1ce264e30 -> interface_1_in_0x55d1ce264e30;
interface_2_out_0x55d1ce264cf0 -> interface_1_in_0x55d1ce264cf0;
interface_2_out_0x55d1ce266c20 -> interface_1_in_0x55d1ce266c20;
interface_2_out_0x55d1ce264d90 -> interface_1_in_0x55d1ce264d90;
interface_2_out_0x55d1b6969838 -> interface_1_in_0x55d1b6969838;

// Input tensor.
subgraph cluster_subgraph_5 {
    label = "Input 1";
    interface_5_out_0x55d1ce264df8 [label="k_1", shape=none];
    interface_5_out_0x55d1ce264d08 [label="g^-1*s^-1*C_in", shape=none];
    interface_5_out_0x55d1ce264e48 [label="g", shape=none];
    interface_5_out_0x55d1ce264e98 [label="g^-1*C_out", shape=none];
    interface_5_out_0x55d1ce264da8 [label="k_1", shape=none];
}

interface_5_out_0x55d1ce264df8 -> interface_1_in_0x55d1ce264df8;
interface_5_out_0x55d1ce264d08 -> interface_1_in_0x55d1ce264d08;
interface_5_out_0x55d1ce264e48 -> interface_1_in_0x55d1ce264e48;
interface_5_out_0x55d1ce264e98 -> interface_1_in_0x55d1ce264e98;
interface_5_out_0x55d1ce264da8 -> interface_1_in_0x55d1ce264da8;

interface_1_out_0x55d1b69697c0 -> interface_0_in_0x55d1b69697c0;
interface_1_out_0x55d1ce270300 -> interface_0_in_0x55d1ce270300;
interface_1_out_0x55d1ce270318 -> interface_0_in_0x55d1ce270318;
interface_1_out_0x55d1ce266c20 -> interface_0_in_0x55d1ce266c20;
interface_1_out_0x55d1b6969838 -> interface_0_in_0x55d1b6969838;

{
    rank = same;
    interface_4_out_0x55d1b69697c0;
    interface_4_out_0x55d1ce30f960;
    interface_4_out_0x55d1ce266c20;
    interface_4_out_0x55d1ce266ce0;
    interface_5_out_0x55d1ce264df8;
    interface_5_out_0x55d1ce264d08;
    interface_5_out_0x55d1ce264e48;
    interface_5_out_0x55d1ce264e98;
    interface_5_out_0x55d1ce264da8;
}
subgraph cluster_subgraph_output {
    label = "Output";
    interface_6_in_0x55d1b69697c0 [label="N", shape=none];
    interface_6_in_0x55d1b69697e8 [label="C_out", shape=none];
    interface_6_in_0x55d1b6969810 [label="H", shape=none];
    interface_6_in_0x55d1b6969838 [label="H", shape=none];
}
interface_0_out_0x55d1b69697c0 -> interface_6_in_0x55d1b69697c0;
interface_0_out_0x55d1b69697e8 -> interface_6_in_0x55d1b69697e8;
interface_0_out_0x55d1b6969810 -> interface_6_in_0x55d1b6969810;
interface_0_out_0x55d1b6969838 -> interface_6_in_0x55d1b6969838;

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
		t_4 = torch.einsum("nklipjo, kilmj -> nlmpo", t_3, in_1)

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
		t_4 = torch.einsum("nklipjo, kilmj -> nlmpo", t_3, in_1)

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
		t_4 = torch.einsum("nklipjo, kilmj -> nlmpo", t_3, in_1)

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
		t_4 = torch.einsum("nklipjo, kilmj -> nlmpo", t_3, in_1)

		# No contraction needed.
		t_5 = t_4

		# [g]@Merge402ce7fe20a0a5fb, [g^-1*C_out]@Merge402ce7fe20a0a5f8 -> [C_out]@Iteratorc7f8eb87a5a0a9e0
		t_5 = torch.reshape(t_5, (1, 1024, 7, 7, ))

		# [H]@Shift41a433c05e30b91d -> [H]@Iterator96123ba3184da39c
		t_5 = torch.roll(t_5, self.shift_direction, 2)

		# No need to crop the output tensor.
		y = t_5

		return y

