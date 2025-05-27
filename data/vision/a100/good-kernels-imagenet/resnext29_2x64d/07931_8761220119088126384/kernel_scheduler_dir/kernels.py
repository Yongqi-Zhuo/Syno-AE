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
        interface_0_out_0x55b738631280 [label="N", shape=none];
        interface_0_out_0x55b7386312a8 [label="C_out", shape=none];
        interface_0_out_0x55b7386312d0 [label="H", shape=none];
        interface_0_out_0x55b7386312f8 [label="H", shape=none];
    }
    {
        rank = same;
        interface_0_out_0x55b738631280;
        interface_0_out_0x55b7386312a8;
        interface_0_out_0x55b7386312d0;
        interface_0_out_0x55b7386312f8;
    }
    // Input 0.
    subgraph cluster_subgraph_0_in_0 {
        label = "";
        interface_0_in_0x55b738631280 [label="N", shape=none];
        interface_0_in_0x55b7501bae80 [label="g", shape=none];
        interface_0_in_0x55b7501bae98 [label="g^-1*C_out", shape=none];
        interface_0_in_0x55b7501b6ea0 [label="H", shape=none];
        interface_0_in_0x55b7386312f8 [label="H", shape=none];
    }
    {
        rank = same;
        interface_0_in_0x55b738631280;
        interface_0_in_0x55b7501bae80;
        interface_0_in_0x55b7501bae98;
        interface_0_in_0x55b7501b6ea0;
        interface_0_in_0x55b7386312f8;
    }
    // Op's.
    op_0x55b7501b6e80 [label="Shift"];
    op_0x55b7501bae40 [label="Merge"];
    // Dimension's.
    interface_0_in_0x55b738631280 -> interface_0_out_0x55b738631280 [label="N"];
    op_0x55b7501bae40 -> interface_0_out_0x55b7386312a8 [label="C_out"];
    op_0x55b7501b6e80 -> interface_0_out_0x55b7386312d0 [label="H"];
    interface_0_in_0x55b7386312f8 -> interface_0_out_0x55b7386312f8 [label="H"];
    interface_0_in_0x55b7501b6ea0 -> op_0x55b7501b6e80 [label="H"];
    interface_0_in_0x55b7501bae80 -> op_0x55b7501bae40 [label="g"];
    interface_0_in_0x55b7501bae98 -> op_0x55b7501bae40 [label="g^-1*C_out"];
}

// Stage tensor.
subgraph cluster_subgraph_1 {
    label = "Subgraph 1";
    // Reductions.
    reduce_0x7f6f60003ab0 [label="Sum", shape=box];
    reduce_0x7f6f60007720 [label="Sum", shape=box];
    reduce_0x7f6f60003a98 [label="Sum", shape=box];
    // Output.
    subgraph cluster_subgraph_1_out {
        label = "";
        interface_1_out_0x55b738631280 [label="N", shape=none];
        interface_1_out_0x55b7501bae80 [label="g", shape=none];
        interface_1_out_0x55b7501bae98 [label="g^-1*C_out", shape=none];
        interface_1_out_0x55b7501b6ea0 [label="H", shape=none];
        interface_1_out_0x55b7386312f8 [label="H", shape=none];
    }
    {
        rank = same;
        reduce_0x7f6f60003ab0;
        reduce_0x7f6f60007720;
        reduce_0x7f6f60003a98;
        interface_1_out_0x55b738631280;
        interface_1_out_0x55b7501bae80;
        interface_1_out_0x55b7501bae98;
        interface_1_out_0x55b7501b6ea0;
        interface_1_out_0x55b7386312f8;
    }
    // Input 0.
    subgraph cluster_subgraph_1_in_0 {
        label = "";
        interface_1_in_0x55b738631280 [label="N", shape=none];
        interface_1_in_0x55b7501b62e0 [label="k_1", shape=none];
        interface_1_in_0x55b7501b6330 [label="g", shape=none];
        interface_1_in_0x55b7501b61f0 [label="g^-1*s^-1*C_in", shape=none];
        interface_1_in_0x55b7501b6ea0 [label="H", shape=none];
        interface_1_in_0x55b7501b6290 [label="k_1", shape=none];
        interface_1_in_0x55b7386312f8 [label="H", shape=none];
    }
    // Input 1.
    subgraph cluster_subgraph_1_in_1 {
        label = "";
        interface_1_in_0x55b7501b62f8 [label="k_1", shape=none];
        interface_1_in_0x55b7501b6208 [label="g^-1*s^-1*C_in", shape=none];
        interface_1_in_0x55b7501b6348 [label="g", shape=none];
        interface_1_in_0x55b7501b6398 [label="g^-1*C_out", shape=none];
        interface_1_in_0x55b7501b62a8 [label="k_1", shape=none];
    }
    {
        rank = same;
        interface_1_in_0x55b738631280;
        interface_1_in_0x55b7501b62e0;
        interface_1_in_0x55b7501b6330;
        interface_1_in_0x55b7501b61f0;
        interface_1_in_0x55b7501b6ea0;
        interface_1_in_0x55b7501b6290;
        interface_1_in_0x55b7386312f8;
        interface_1_in_0x55b7501b62f8;
        interface_1_in_0x55b7501b6208;
        interface_1_in_0x55b7501b6348;
        interface_1_in_0x55b7501b6398;
        interface_1_in_0x55b7501b62a8;
    }
    // Op's.
    op_0x55b7501b61d0 [label="Share"];
    op_0x55b7501b6270 [label="Share"];
    op_0x55b7501b62c0 [label="Share"];
    op_0x55b7501b6310 [label="Share"];
    op_0x55b7501b6360 [label="Share"];
    op_0x55b7501b6698 [label="Expand"];
    // Dimension's.
    interface_1_in_0x55b738631280 -> interface_1_out_0x55b738631280 [label="N"];
    interface_1_in_0x55b7386312f8 -> interface_1_out_0x55b7386312f8 [label="H"];
    interface_1_in_0x55b7501b61f0 -> op_0x55b7501b61d0 [label="g^-1*s^-1*C_in"];
    interface_1_in_0x55b7501b6208 -> op_0x55b7501b61d0 [label="g^-1*s^-1*C_in"];
    interface_1_in_0x55b7501b6290 -> op_0x55b7501b6270 [label="k_1"];
    interface_1_in_0x55b7501b62a8 -> op_0x55b7501b6270 [label="k_1"];
    interface_1_in_0x55b7501b62e0 -> op_0x55b7501b62c0 [label="k_1"];
    interface_1_in_0x55b7501b62f8 -> op_0x55b7501b62c0 [label="k_1"];
    interface_1_in_0x55b7501b6330 -> op_0x55b7501b6310 [label="g"];
    interface_1_in_0x55b7501b6348 -> op_0x55b7501b6310 [label="g"];
    op_0x55b7501b6698 -> op_0x55b7501b6360 [label="g^-1*C_out"];
    interface_1_in_0x55b7501b6398 -> op_0x55b7501b6360 [label="g^-1*C_out"];
    interface_1_in_0x55b7501b6ea0 -> interface_1_out_0x55b7501b6ea0 [label="H"];
    op_0x55b7501b6310 -> interface_1_out_0x55b7501bae80 [label="g"];
    op_0x55b7501b6360 -> interface_1_out_0x55b7501bae98 [label="g^-1*C_out"];
    op_0x55b7501b6270 -> reduce_0x7f6f60003a98 [label="k_1"];
    op_0x55b7501b62c0 -> reduce_0x7f6f60003ab0 [label="k_1"];
    op_0x55b7501b61d0 -> reduce_0x7f6f60007720 [label="g^-1*s^-1*C_in"];
}

// Stage tensor.
subgraph cluster_subgraph_2 {
    label = "Subgraph 2";
    // Reductions.
    // Output.
    subgraph cluster_subgraph_2_out {
        label = "";
        interface_2_out_0x55b738631280 [label="N", shape=none];
        interface_2_out_0x55b7501b62e0 [label="k_1", shape=none];
        interface_2_out_0x55b7501b6330 [label="g", shape=none];
        interface_2_out_0x55b7501b61f0 [label="g^-1*s^-1*C_in", shape=none];
        interface_2_out_0x55b7501b6ea0 [label="H", shape=none];
        interface_2_out_0x55b7501b6290 [label="k_1", shape=none];
        interface_2_out_0x55b7386312f8 [label="H", shape=none];
    }
    {
        rank = same;
        interface_2_out_0x55b738631280;
        interface_2_out_0x55b7501b62e0;
        interface_2_out_0x55b7501b6330;
        interface_2_out_0x55b7501b61f0;
        interface_2_out_0x55b7501b6ea0;
        interface_2_out_0x55b7501b6290;
        interface_2_out_0x55b7386312f8;
    }
    // Input 0.
    subgraph cluster_subgraph_2_in_0 {
        label = "";
        interface_2_in_0x55b738631280 [label="N", shape=none];
        interface_2_in_0x55b750263140 [label="s^-1*C_in", shape=none];
        interface_2_in_0x55b7501b6ea0 [label="H", shape=none];
        interface_2_in_0x55b7501b6f60 [label="H", shape=none];
    }
    {
        rank = same;
        interface_2_in_0x55b738631280;
        interface_2_in_0x55b750263140;
        interface_2_in_0x55b7501b6ea0;
        interface_2_in_0x55b7501b6f60;
    }
    // Op's.
    op_0x55b7501b6f40 [label="Shift"];
    op_0x55b7501d45c0 [label="Unfold"];
    op_0x55b7501d4740 [label="Unfold"];
    op_0x55b750263100 [label="Split"];
    // Dimension's.
    interface_2_in_0x55b738631280 -> interface_2_out_0x55b738631280 [label="N"];
    op_0x55b7501d45c0 -> interface_2_out_0x55b7386312f8 [label="H"];
    op_0x55b750263100 -> interface_2_out_0x55b7501b61f0 [label="g^-1*s^-1*C_in"];
    op_0x55b7501d45c0 -> interface_2_out_0x55b7501b6290 [label="k_1"];
    op_0x55b7501d4740 -> interface_2_out_0x55b7501b62e0 [label="k_1"];
    op_0x55b7501d4740 -> interface_2_out_0x55b7501b6330 [label="g"];
    interface_2_in_0x55b7501b6ea0 -> interface_2_out_0x55b7501b6ea0 [label="H"];
    interface_2_in_0x55b7501b6f60 -> op_0x55b7501b6f40 [label="H"];
    op_0x55b7501b6f40 -> op_0x55b7501d45c0 [label="H"];
    op_0x55b750263100 -> op_0x55b7501d4740 [label="g"];
    interface_2_in_0x55b750263140 -> op_0x55b750263100 [label="s^-1*C_in"];
}

// Stage tensor.
subgraph cluster_subgraph_3 {
    label = "Subgraph 3";
    // Reductions.
    reduce_0x7f6f60004e58 [label="Sum", shape=box];
    // Output.
    subgraph cluster_subgraph_3_out {
        label = "";
        interface_3_out_0x55b738631280 [label="N", shape=none];
        interface_3_out_0x55b750263140 [label="s^-1*C_in", shape=none];
        interface_3_out_0x55b7501b6ea0 [label="H", shape=none];
        interface_3_out_0x55b7501b6f60 [label="H", shape=none];
    }
    {
        rank = same;
        reduce_0x7f6f60004e58;
        interface_3_out_0x55b738631280;
        interface_3_out_0x55b750263140;
        interface_3_out_0x55b7501b6ea0;
        interface_3_out_0x55b7501b6f60;
    }
    // Input 0.
    subgraph cluster_subgraph_3_in_0 {
        label = "";
        interface_3_in_0x55b738631280 [label="N", shape=none];
        interface_3_in_0x55b750263460 [label="C_in", shape=none];
        interface_3_in_0x55b7501b6ea0 [label="H", shape=none];
        interface_3_in_0x55b7501b6f60 [label="H", shape=none];
    }
    {
        rank = same;
        interface_3_in_0x55b738631280;
        interface_3_in_0x55b750263460;
        interface_3_in_0x55b7501b6ea0;
        interface_3_in_0x55b7501b6f60;
    }
    // Op's.
    op_0x55b750263420 [label="Split"];
    // Dimension's.
    interface_3_in_0x55b738631280 -> interface_3_out_0x55b738631280 [label="N"];
    interface_3_in_0x55b7501b6ea0 -> interface_3_out_0x55b7501b6ea0 [label="H"];
    interface_3_in_0x55b7501b6f60 -> interface_3_out_0x55b7501b6f60 [label="H"];
    op_0x55b750263420 -> interface_3_out_0x55b750263140 [label="s^-1*C_in"];
    interface_3_in_0x55b750263460 -> op_0x55b750263420 [label="C_in"];
    op_0x55b750263420 -> reduce_0x7f6f60004e58 [label="s"];
}

// Input tensor.
subgraph cluster_subgraph_4 {
    label = "Input 0";
    interface_4_out_0x55b738631280 [label="N", shape=none];
    interface_4_out_0x55b750263460 [label="C_in", shape=none];
    interface_4_out_0x55b7501b6ea0 [label="H", shape=none];
    interface_4_out_0x55b7501b6f60 [label="H", shape=none];
}

interface_4_out_0x55b738631280 -> interface_3_in_0x55b738631280;
interface_4_out_0x55b750263460 -> interface_3_in_0x55b750263460;
interface_4_out_0x55b7501b6ea0 -> interface_3_in_0x55b7501b6ea0;
interface_4_out_0x55b7501b6f60 -> interface_3_in_0x55b7501b6f60;

interface_3_out_0x55b738631280 -> interface_2_in_0x55b738631280;
interface_3_out_0x55b750263140 -> interface_2_in_0x55b750263140;
interface_3_out_0x55b7501b6ea0 -> interface_2_in_0x55b7501b6ea0;
interface_3_out_0x55b7501b6f60 -> interface_2_in_0x55b7501b6f60;

interface_2_out_0x55b738631280 -> interface_1_in_0x55b738631280;
interface_2_out_0x55b7501b62e0 -> interface_1_in_0x55b7501b62e0;
interface_2_out_0x55b7501b6330 -> interface_1_in_0x55b7501b6330;
interface_2_out_0x55b7501b61f0 -> interface_1_in_0x55b7501b61f0;
interface_2_out_0x55b7501b6ea0 -> interface_1_in_0x55b7501b6ea0;
interface_2_out_0x55b7501b6290 -> interface_1_in_0x55b7501b6290;
interface_2_out_0x55b7386312f8 -> interface_1_in_0x55b7386312f8;

// Input tensor.
subgraph cluster_subgraph_5 {
    label = "Input 1";
    interface_5_out_0x55b7501b62f8 [label="k_1", shape=none];
    interface_5_out_0x55b7501b6208 [label="g^-1*s^-1*C_in", shape=none];
    interface_5_out_0x55b7501b6348 [label="g", shape=none];
    interface_5_out_0x55b7501b6398 [label="g^-1*C_out", shape=none];
    interface_5_out_0x55b7501b62a8 [label="k_1", shape=none];
}

interface_5_out_0x55b7501b62f8 -> interface_1_in_0x55b7501b62f8;
interface_5_out_0x55b7501b6208 -> interface_1_in_0x55b7501b6208;
interface_5_out_0x55b7501b6348 -> interface_1_in_0x55b7501b6348;
interface_5_out_0x55b7501b6398 -> interface_1_in_0x55b7501b6398;
interface_5_out_0x55b7501b62a8 -> interface_1_in_0x55b7501b62a8;

interface_1_out_0x55b738631280 -> interface_0_in_0x55b738631280;
interface_1_out_0x55b7501bae80 -> interface_0_in_0x55b7501bae80;
interface_1_out_0x55b7501bae98 -> interface_0_in_0x55b7501bae98;
interface_1_out_0x55b7501b6ea0 -> interface_0_in_0x55b7501b6ea0;
interface_1_out_0x55b7386312f8 -> interface_0_in_0x55b7386312f8;

{
    rank = same;
    interface_4_out_0x55b738631280;
    interface_4_out_0x55b750263460;
    interface_4_out_0x55b7501b6ea0;
    interface_4_out_0x55b7501b6f60;
    interface_5_out_0x55b7501b62f8;
    interface_5_out_0x55b7501b6208;
    interface_5_out_0x55b7501b6348;
    interface_5_out_0x55b7501b6398;
    interface_5_out_0x55b7501b62a8;
}
subgraph cluster_subgraph_output {
    label = "Output";
    interface_6_in_0x55b738631280 [label="N", shape=none];
    interface_6_in_0x55b7386312a8 [label="C_out", shape=none];
    interface_6_in_0x55b7386312d0 [label="H", shape=none];
    interface_6_in_0x55b7386312f8 [label="H", shape=none];
}
interface_0_out_0x55b738631280 -> interface_6_in_0x55b738631280;
interface_0_out_0x55b7386312a8 -> interface_6_in_0x55b7386312a8;
interface_0_out_0x55b7386312d0 -> interface_6_in_0x55b7386312d0;
interface_0_out_0x55b7386312f8 -> interface_6_in_0x55b7386312f8;

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

