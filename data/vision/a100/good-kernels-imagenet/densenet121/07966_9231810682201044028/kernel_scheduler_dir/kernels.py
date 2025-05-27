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
        interface_0_out_0x55e3a880e020 [label="N", shape=none];
        interface_0_out_0x55e3a880e048 [label="C_out", shape=none];
        interface_0_out_0x55e3a880e070 [label="H", shape=none];
        interface_0_out_0x55e3a880e098 [label="H", shape=none];
    }
    {
        rank = same;
        interface_0_out_0x55e3a880e020;
        interface_0_out_0x55e3a880e048;
        interface_0_out_0x55e3a880e070;
        interface_0_out_0x55e3a880e098;
    }
    // Input 0.
    subgraph cluster_subgraph_0_in_0 {
        label = "";
        interface_0_in_0x55e3a880e020 [label="N", shape=none];
        interface_0_in_0x55e3a880e048 [label="C_out", shape=none];
        interface_0_in_0x55e3a880e070 [label="H", shape=none];
        interface_0_in_0x55e39eb54310 [label="H", shape=none];
    }
    {
        rank = same;
        interface_0_in_0x55e3a880e020;
        interface_0_in_0x55e3a880e048;
        interface_0_in_0x55e3a880e070;
        interface_0_in_0x55e39eb54310;
    }
    // Op's.
    op_0x55e39eb542f0 [label="Shift"];
    // Dimension's.
    interface_0_in_0x55e39eb54310 -> op_0x55e39eb542f0 [label="H"];
    interface_0_in_0x55e3a880e020 -> interface_0_out_0x55e3a880e020 [label="N"];
    interface_0_in_0x55e3a880e048 -> interface_0_out_0x55e3a880e048 [label="C_out"];
    interface_0_in_0x55e3a880e070 -> interface_0_out_0x55e3a880e070 [label="H"];
    op_0x55e39eb542f0 -> interface_0_out_0x55e3a880e098 [label="H"];
}

// Stage tensor.
subgraph cluster_subgraph_1 {
    label = "Subgraph 1";
    // Reductions.
    reduce_0x7fb2b80072d0 [label="Sum", shape=box];
    reduce_0x7fb2b8003a98 [label="Sum", shape=box];
    // Output.
    subgraph cluster_subgraph_1_out {
        label = "";
        interface_1_out_0x55e3a880e020 [label="N", shape=none];
        interface_1_out_0x55e3a880e048 [label="C_out", shape=none];
        interface_1_out_0x55e3a880e070 [label="H", shape=none];
        interface_1_out_0x55e39eb54310 [label="H", shape=none];
    }
    {
        rank = same;
        reduce_0x7fb2b80072d0;
        reduce_0x7fb2b8003a98;
        interface_1_out_0x55e3a880e020;
        interface_1_out_0x55e3a880e048;
        interface_1_out_0x55e3a880e070;
        interface_1_out_0x55e39eb54310;
    }
    // Input 0.
    subgraph cluster_subgraph_1_in_0 {
        label = "";
        interface_1_in_0x55e3a880e020 [label="N", shape=none];
        interface_1_in_0x55e3a8934470 [label="s^-1*C_in", shape=none];
        interface_1_in_0x55e3a89346f0 [label="k_1", shape=none];
        interface_1_in_0x55e3a880e070 [label="H", shape=none];
        interface_1_in_0x55e39eb54310 [label="H", shape=none];
    }
    // Input 1.
    subgraph cluster_subgraph_1_in_1 {
        label = "";
        interface_1_in_0x55e3a8934438 [label="C_out", shape=none];
        interface_1_in_0x55e3a8934488 [label="s^-1*C_in", shape=none];
        interface_1_in_0x55e3a8934708 [label="k_1", shape=none];
    }
    {
        rank = same;
        interface_1_in_0x55e3a880e020;
        interface_1_in_0x55e3a8934470;
        interface_1_in_0x55e3a89346f0;
        interface_1_in_0x55e3a880e070;
        interface_1_in_0x55e39eb54310;
        interface_1_in_0x55e3a8934438;
        interface_1_in_0x55e3a8934488;
        interface_1_in_0x55e3a8934708;
    }
    // Op's.
    op_0x55e3a8934400 [label="Share"];
    op_0x55e3a8934450 [label="Share"];
    op_0x55e3a89346d0 [label="Share"];
    op_0x55e3a89348d8 [label="Expand"];
    // Dimension's.
    interface_1_in_0x55e39eb54310 -> interface_1_out_0x55e39eb54310 [label="H"];
    interface_1_in_0x55e3a880e020 -> interface_1_out_0x55e3a880e020 [label="N"];
    op_0x55e3a8934400 -> interface_1_out_0x55e3a880e048 [label="C_out"];
    interface_1_in_0x55e3a880e070 -> interface_1_out_0x55e3a880e070 [label="H"];
    op_0x55e3a89348d8 -> op_0x55e3a8934400 [label="C_out"];
    interface_1_in_0x55e3a8934438 -> op_0x55e3a8934400 [label="C_out"];
    interface_1_in_0x55e3a8934470 -> op_0x55e3a8934450 [label="s^-1*C_in"];
    interface_1_in_0x55e3a8934488 -> op_0x55e3a8934450 [label="s^-1*C_in"];
    interface_1_in_0x55e3a89346f0 -> op_0x55e3a89346d0 [label="k_1"];
    interface_1_in_0x55e3a8934708 -> op_0x55e3a89346d0 [label="k_1"];
    op_0x55e3a89346d0 -> reduce_0x7fb2b8003a98 [label="k_1"];
    op_0x55e3a8934450 -> reduce_0x7fb2b80072d0 [label="s^-1*C_in"];
}

// Stage tensor.
subgraph cluster_subgraph_2 {
    label = "Subgraph 2";
    // Reductions.
    reduce_0x7fb2b800deb0 [label="Sum", shape=box];
    // Output.
    subgraph cluster_subgraph_2_out {
        label = "";
        interface_2_out_0x55e3a880e020 [label="N", shape=none];
        interface_2_out_0x55e3a8934470 [label="s^-1*C_in", shape=none];
        interface_2_out_0x55e3a89346f0 [label="k_1", shape=none];
        interface_2_out_0x55e3a880e070 [label="H", shape=none];
        interface_2_out_0x55e39eb54310 [label="H", shape=none];
    }
    {
        rank = same;
        reduce_0x7fb2b800deb0;
        interface_2_out_0x55e3a880e020;
        interface_2_out_0x55e3a8934470;
        interface_2_out_0x55e3a89346f0;
        interface_2_out_0x55e3a880e070;
        interface_2_out_0x55e39eb54310;
    }
    // Input 0.
    subgraph cluster_subgraph_2_in_0 {
        label = "";
        interface_2_in_0x55e3a880e020 [label="N", shape=none];
        interface_2_in_0x55e3a8934470 [label="s^-1*C_in", shape=none];
        interface_2_in_0x55e3a89548d0 [label="g^-2*k_1*C_out^2", shape=none];
        interface_2_in_0x55e3a880e070 [label="H", shape=none];
        interface_2_in_0x55e39eb54310 [label="H", shape=none];
    }
    {
        rank = same;
        interface_2_in_0x55e3a880e020;
        interface_2_in_0x55e3a8934470;
        interface_2_in_0x55e3a89548d0;
        interface_2_in_0x55e3a880e070;
        interface_2_in_0x55e39eb54310;
    }
    // Op's.
    op_0x55e3a8954890 [label="Split"];
    // Dimension's.
    interface_2_in_0x55e39eb54310 -> interface_2_out_0x55e39eb54310 [label="H"];
    interface_2_in_0x55e3a880e020 -> interface_2_out_0x55e3a880e020 [label="N"];
    interface_2_in_0x55e3a880e070 -> interface_2_out_0x55e3a880e070 [label="H"];
    interface_2_in_0x55e3a8934470 -> interface_2_out_0x55e3a8934470 [label="s^-1*C_in"];
    op_0x55e3a8954890 -> interface_2_out_0x55e3a89346f0 [label="k_1"];
    interface_2_in_0x55e3a89548d0 -> op_0x55e3a8954890 [label="g^-2*k_1*C_out^2"];
    op_0x55e3a8954890 -> reduce_0x7fb2b800deb0 [label="g^-2*C_out^2"];
}

// Stage tensor.
subgraph cluster_subgraph_3 {
    label = "Subgraph 3";
    // Reductions.
    reduce_0x7fb2b800b670 [label="Sum", shape=box];
    // Output.
    subgraph cluster_subgraph_3_out {
        label = "";
        interface_3_out_0x55e3a880e020 [label="N", shape=none];
        interface_3_out_0x55e3a8934470 [label="s^-1*C_in", shape=none];
        interface_3_out_0x55e3a89548d0 [label="g^-2*k_1*C_out^2", shape=none];
        interface_3_out_0x55e3a880e070 [label="H", shape=none];
        interface_3_out_0x55e39eb54310 [label="H", shape=none];
    }
    {
        rank = same;
        reduce_0x7fb2b800b670;
        interface_3_out_0x55e3a880e020;
        interface_3_out_0x55e3a8934470;
        interface_3_out_0x55e3a89548d0;
        interface_3_out_0x55e3a880e070;
        interface_3_out_0x55e39eb54310;
    }
    // Input 0.
    subgraph cluster_subgraph_3_in_0 {
        label = "";
        interface_3_in_0x55e3a880e020 [label="N", shape=none];
        interface_3_in_0x55e3a8934470 [label="s^-1*C_in", shape=none];
        interface_3_in_0x55e3a89369a8 [label="H", shape=none];
        interface_3_in_0x55e39eb54310 [label="H", shape=none];
    }
    {
        rank = same;
        interface_3_in_0x55e3a880e020;
        interface_3_in_0x55e3a8934470;
        interface_3_in_0x55e3a89369a8;
        interface_3_in_0x55e39eb54310;
    }
    // Op's.
    op_0x55e3a8936980 [label="Unfold"];
    op_0x55e3a8955970 [label="Split"];
    // Dimension's.
    interface_3_in_0x55e39eb54310 -> interface_3_out_0x55e39eb54310 [label="H"];
    interface_3_in_0x55e3a880e020 -> interface_3_out_0x55e3a880e020 [label="N"];
    op_0x55e3a8936980 -> interface_3_out_0x55e3a880e070 [label="H"];
    interface_3_in_0x55e3a8934470 -> interface_3_out_0x55e3a8934470 [label="s^-1*C_in"];
    interface_3_in_0x55e3a89369a8 -> op_0x55e3a8936980 [label="H"];
    op_0x55e3a8955970 -> interface_3_out_0x55e3a89548d0 [label="g^-2*k_1*C_out^2"];
    op_0x55e3a8936980 -> op_0x55e3a8955970 [label="g^-3*k_1*C_out^3"];
    op_0x55e3a8955970 -> reduce_0x7fb2b800b670 [label="g^-1*C_out"];
}

// Stage tensor.
subgraph cluster_subgraph_4 {
    label = "Subgraph 4";
    // Reductions.
    reduce_0x7fb2b8004c30 [label="Sum", shape=box];
    // Output.
    subgraph cluster_subgraph_4_out {
        label = "";
        interface_4_out_0x55e3a880e020 [label="N", shape=none];
        interface_4_out_0x55e3a8934470 [label="s^-1*C_in", shape=none];
        interface_4_out_0x55e3a89369a8 [label="H", shape=none];
        interface_4_out_0x55e39eb54310 [label="H", shape=none];
    }
    {
        rank = same;
        reduce_0x7fb2b8004c30;
        interface_4_out_0x55e3a880e020;
        interface_4_out_0x55e3a8934470;
        interface_4_out_0x55e3a89369a8;
        interface_4_out_0x55e39eb54310;
    }
    // Input 0.
    subgraph cluster_subgraph_4_in_0 {
        label = "";
        interface_4_in_0x55e3a880e020 [label="N", shape=none];
        interface_4_in_0x55e3a89558c0 [label="C_in", shape=none];
        interface_4_in_0x55e3a89369a8 [label="H", shape=none];
        interface_4_in_0x55e39eb54310 [label="H", shape=none];
    }
    {
        rank = same;
        interface_4_in_0x55e3a880e020;
        interface_4_in_0x55e3a89558c0;
        interface_4_in_0x55e3a89369a8;
        interface_4_in_0x55e39eb54310;
    }
    // Op's.
    op_0x55e3a8955880 [label="Split"];
    // Dimension's.
    interface_4_in_0x55e39eb54310 -> interface_4_out_0x55e39eb54310 [label="H"];
    interface_4_in_0x55e3a880e020 -> interface_4_out_0x55e3a880e020 [label="N"];
    op_0x55e3a8955880 -> interface_4_out_0x55e3a8934470 [label="s^-1*C_in"];
    interface_4_in_0x55e3a89369a8 -> interface_4_out_0x55e3a89369a8 [label="H"];
    interface_4_in_0x55e3a89558c0 -> op_0x55e3a8955880 [label="C_in"];
    op_0x55e3a8955880 -> reduce_0x7fb2b8004c30 [label="s"];
}

// Input tensor.
subgraph cluster_subgraph_5 {
    label = "Input 0";
    interface_5_out_0x55e3a880e020 [label="N", shape=none];
    interface_5_out_0x55e3a89558c0 [label="C_in", shape=none];
    interface_5_out_0x55e3a89369a8 [label="H", shape=none];
    interface_5_out_0x55e39eb54310 [label="H", shape=none];
}

interface_5_out_0x55e3a880e020 -> interface_4_in_0x55e3a880e020;
interface_5_out_0x55e3a89558c0 -> interface_4_in_0x55e3a89558c0;
interface_5_out_0x55e3a89369a8 -> interface_4_in_0x55e3a89369a8;
interface_5_out_0x55e39eb54310 -> interface_4_in_0x55e39eb54310;

interface_4_out_0x55e3a880e020 -> interface_3_in_0x55e3a880e020;
interface_4_out_0x55e3a8934470 -> interface_3_in_0x55e3a8934470;
interface_4_out_0x55e3a89369a8 -> interface_3_in_0x55e3a89369a8;
interface_4_out_0x55e39eb54310 -> interface_3_in_0x55e39eb54310;

interface_3_out_0x55e3a880e020 -> interface_2_in_0x55e3a880e020;
interface_3_out_0x55e3a8934470 -> interface_2_in_0x55e3a8934470;
interface_3_out_0x55e3a89548d0 -> interface_2_in_0x55e3a89548d0;
interface_3_out_0x55e3a880e070 -> interface_2_in_0x55e3a880e070;
interface_3_out_0x55e39eb54310 -> interface_2_in_0x55e39eb54310;

interface_2_out_0x55e3a880e020 -> interface_1_in_0x55e3a880e020;
interface_2_out_0x55e3a8934470 -> interface_1_in_0x55e3a8934470;
interface_2_out_0x55e3a89346f0 -> interface_1_in_0x55e3a89346f0;
interface_2_out_0x55e3a880e070 -> interface_1_in_0x55e3a880e070;
interface_2_out_0x55e39eb54310 -> interface_1_in_0x55e39eb54310;

// Input tensor.
subgraph cluster_subgraph_6 {
    label = "Input 1";
    interface_6_out_0x55e3a8934438 [label="C_out", shape=none];
    interface_6_out_0x55e3a8934488 [label="s^-1*C_in", shape=none];
    interface_6_out_0x55e3a8934708 [label="k_1", shape=none];
}

interface_6_out_0x55e3a8934438 -> interface_1_in_0x55e3a8934438;
interface_6_out_0x55e3a8934488 -> interface_1_in_0x55e3a8934488;
interface_6_out_0x55e3a8934708 -> interface_1_in_0x55e3a8934708;

interface_1_out_0x55e3a880e020 -> interface_0_in_0x55e3a880e020;
interface_1_out_0x55e3a880e048 -> interface_0_in_0x55e3a880e048;
interface_1_out_0x55e3a880e070 -> interface_0_in_0x55e3a880e070;
interface_1_out_0x55e39eb54310 -> interface_0_in_0x55e39eb54310;

{
    rank = same;
    interface_5_out_0x55e3a880e020;
    interface_5_out_0x55e3a89558c0;
    interface_5_out_0x55e3a89369a8;
    interface_5_out_0x55e39eb54310;
    interface_6_out_0x55e3a8934438;
    interface_6_out_0x55e3a8934488;
    interface_6_out_0x55e3a8934708;
}
subgraph cluster_subgraph_output {
    label = "Output";
    interface_7_in_0x55e3a880e020 [label="N", shape=none];
    interface_7_in_0x55e3a880e048 [label="C_out", shape=none];
    interface_7_in_0x55e3a880e070 [label="H", shape=none];
    interface_7_in_0x55e3a880e098 [label="H", shape=none];
}
interface_0_out_0x55e3a880e020 -> interface_7_in_0x55e3a880e020;
interface_0_out_0x55e3a880e048 -> interface_7_in_0x55e3a880e048;
interface_0_out_0x55e3a880e070 -> interface_7_in_0x55e3a880e070;
interface_0_out_0x55e3a880e098 -> interface_7_in_0x55e3a880e098;

}

"""
class kernel_generated_0(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([32, 64, 3]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]

		# No contraction needed.
		t_2 = in_0

		# [C_in]@Splitcfaed9699d036d38 -> [s]@Reduced95c644a3c072d9a, [s^-1*C_in]@Share8de6f167adbbf8aa
		t_2 = torch.reshape(t_2, (1, 2, 64, 56, 56, ))

		# [s]@Reduce
		t_2 = torch.sum(t_2, dim=(1, ))

		# No contraction needed.
		t_3 = t_2

		# [H]@Unfold4aa57e8190ebe608 -> [H]@Iterator96123ba3184da39c, [g^-3*k_1*C_out^3]@Splite17fc0c11dbe5a05
		t_3 = torch.reshape(t_3, (1, 64, 56, 56, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (1, 64, 3, 56, 56, ))

		# [g^-3*k_1*C_out^3]@Splite17fc0c11dbe5a05 -> [g^-1*C_out]@Reduce28c4f9e5abf023cf, [g^-2*k_1*C_out^2]@Split5f8295cb2a9219e3
		t_3 = torch.reshape(t_3, (1, 64, 1, 3, 56, 56, ))

		# [g^-1*C_out]@Reduce
		t_3 = torch.sum(t_3, dim=(2, ))

		# No contraction needed.
		t_4 = t_3

		# [g^-2*k_1*C_out^2]@Split5f8295cb2a9219e3 -> [k_1]@Share26cfa48d169008e4, [g^-2*C_out^2]@Reduce159437b921f023cf
		t_4 = torch.reshape(t_4, (1, 64, 3, 1, 56, 56, ))

		# [g^-2*C_out^2]@Reduce
		t_4 = torch.sum(t_4, dim=(3, ))

		# Perform contraction.
		t_5 = torch.einsum("mjknl, ijk -> minl", t_4, in_1)

		# No contraction needed.
		t_6 = t_5

		# [H]@Shift6b179c72f0c6dbad -> [H]@Iteratorb0a1def4ad5784ec
		t_6 = torch.roll(t_6, self.shift_direction, 3)

		# No need to crop the output tensor.
		y = t_6

		return y

class kernel_generated_1(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([32, 64, 3]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]

		# No contraction needed.
		t_2 = in_0

		# [C_in]@Splitcfaed9699d036d38 -> [s]@Reduced95c644a3c072d9a, [s^-1*C_in]@Share8de6f167adbbf8aa
		t_2 = torch.reshape(t_2, (1, 2, 64, 28, 28, ))

		# [s]@Reduce
		t_2 = torch.sum(t_2, dim=(1, ))

		# No contraction needed.
		t_3 = t_2

		# [H]@Unfold4aa57e8190ebe608 -> [H]@Iterator96123ba3184da39c, [g^-3*k_1*C_out^3]@Splite17fc0c11dbe5a05
		t_3 = torch.reshape(t_3, (1, 64, 28, 28, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (1, 64, 3, 28, 28, ))

		# [g^-3*k_1*C_out^3]@Splite17fc0c11dbe5a05 -> [g^-1*C_out]@Reduce28c4f9e5abf023cf, [g^-2*k_1*C_out^2]@Split5f8295cb2a9219e3
		t_3 = torch.reshape(t_3, (1, 64, 1, 3, 28, 28, ))

		# [g^-1*C_out]@Reduce
		t_3 = torch.sum(t_3, dim=(2, ))

		# No contraction needed.
		t_4 = t_3

		# [g^-2*k_1*C_out^2]@Split5f8295cb2a9219e3 -> [k_1]@Share26cfa48d169008e4, [g^-2*C_out^2]@Reduce159437b921f023cf
		t_4 = torch.reshape(t_4, (1, 64, 3, 1, 28, 28, ))

		# [g^-2*C_out^2]@Reduce
		t_4 = torch.sum(t_4, dim=(3, ))

		# Perform contraction.
		t_5 = torch.einsum("mjknl, ijk -> minl", t_4, in_1)

		# No contraction needed.
		t_6 = t_5

		# [H]@Shift6b179c72f0c6dbad -> [H]@Iteratorb0a1def4ad5784ec
		t_6 = torch.roll(t_6, self.shift_direction, 3)

		# No need to crop the output tensor.
		y = t_6

		return y

class kernel_generated_2(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([32, 64, 3]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]

		# No contraction needed.
		t_2 = in_0

		# [C_in]@Splitcfaed9699d036d38 -> [s]@Reduced95c644a3c072d9a, [s^-1*C_in]@Share8de6f167adbbf8aa
		t_2 = torch.reshape(t_2, (1, 2, 64, 14, 14, ))

		# [s]@Reduce
		t_2 = torch.sum(t_2, dim=(1, ))

		# No contraction needed.
		t_3 = t_2

		# [H]@Unfold4aa57e8190ebe608 -> [H]@Iterator96123ba3184da39c, [g^-3*k_1*C_out^3]@Splite17fc0c11dbe5a05
		t_3 = torch.reshape(t_3, (1, 64, 14, 14, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (1, 64, 3, 14, 14, ))

		# [g^-3*k_1*C_out^3]@Splite17fc0c11dbe5a05 -> [g^-1*C_out]@Reduce28c4f9e5abf023cf, [g^-2*k_1*C_out^2]@Split5f8295cb2a9219e3
		t_3 = torch.reshape(t_3, (1, 64, 1, 3, 14, 14, ))

		# [g^-1*C_out]@Reduce
		t_3 = torch.sum(t_3, dim=(2, ))

		# No contraction needed.
		t_4 = t_3

		# [g^-2*k_1*C_out^2]@Split5f8295cb2a9219e3 -> [k_1]@Share26cfa48d169008e4, [g^-2*C_out^2]@Reduce159437b921f023cf
		t_4 = torch.reshape(t_4, (1, 64, 3, 1, 14, 14, ))

		# [g^-2*C_out^2]@Reduce
		t_4 = torch.sum(t_4, dim=(3, ))

		# Perform contraction.
		t_5 = torch.einsum("mjknl, ijk -> minl", t_4, in_1)

		# No contraction needed.
		t_6 = t_5

		# [H]@Shift6b179c72f0c6dbad -> [H]@Iteratorb0a1def4ad5784ec
		t_6 = torch.roll(t_6, self.shift_direction, 3)

		# No need to crop the output tensor.
		y = t_6

		return y

class kernel_generated_3(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([32, 64, 3]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]

		# No contraction needed.
		t_2 = in_0

		# [C_in]@Splitcfaed9699d036d38 -> [s]@Reduced95c644a3c072d9a, [s^-1*C_in]@Share8de6f167adbbf8aa
		t_2 = torch.reshape(t_2, (1, 2, 64, 7, 7, ))

		# [s]@Reduce
		t_2 = torch.sum(t_2, dim=(1, ))

		# No contraction needed.
		t_3 = t_2

		# [H]@Unfold4aa57e8190ebe608 -> [H]@Iterator96123ba3184da39c, [g^-3*k_1*C_out^3]@Splite17fc0c11dbe5a05
		t_3 = torch.reshape(t_3, (1, 64, 7, 7, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (1, 64, 3, 7, 7, ))

		# [g^-3*k_1*C_out^3]@Splite17fc0c11dbe5a05 -> [g^-1*C_out]@Reduce28c4f9e5abf023cf, [g^-2*k_1*C_out^2]@Split5f8295cb2a9219e3
		t_3 = torch.reshape(t_3, (1, 64, 1, 3, 7, 7, ))

		# [g^-1*C_out]@Reduce
		t_3 = torch.sum(t_3, dim=(2, ))

		# No contraction needed.
		t_4 = t_3

		# [g^-2*k_1*C_out^2]@Split5f8295cb2a9219e3 -> [k_1]@Share26cfa48d169008e4, [g^-2*C_out^2]@Reduce159437b921f023cf
		t_4 = torch.reshape(t_4, (1, 64, 3, 1, 7, 7, ))

		# [g^-2*C_out^2]@Reduce
		t_4 = torch.sum(t_4, dim=(3, ))

		# Perform contraction.
		t_5 = torch.einsum("mjknl, ijk -> minl", t_4, in_1)

		# No contraction needed.
		t_6 = t_5

		# [H]@Shift6b179c72f0c6dbad -> [H]@Iteratorb0a1def4ad5784ec
		t_6 = torch.roll(t_6, self.shift_direction, 3)

		# No need to crop the output tensor.
		y = t_6

		return y

