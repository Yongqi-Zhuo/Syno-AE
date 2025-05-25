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
        interface_0_out_0x5611d2dde4e0 [label="N", shape=none];
        interface_0_out_0x5611d2dde508 [label="C_out", shape=none];
        interface_0_out_0x5611d2dde530 [label="H", shape=none];
        interface_0_out_0x5611d2dde558 [label="H", shape=none];
    }
    {
        rank = same;
        interface_0_out_0x5611d2dde4e0;
        interface_0_out_0x5611d2dde508;
        interface_0_out_0x5611d2dde530;
        interface_0_out_0x5611d2dde558;
    }
    // Input 0.
    subgraph cluster_subgraph_0_in_0 {
        label = "";
        interface_0_in_0x5611d2dde4e0 [label="N", shape=none];
        interface_0_in_0x5611d2dde508 [label="C_out", shape=none];
        interface_0_in_0x5611d2dde530 [label="H", shape=none];
        interface_0_in_0x5611d2d29910 [label="H", shape=none];
    }
    {
        rank = same;
        interface_0_in_0x5611d2dde4e0;
        interface_0_in_0x5611d2dde508;
        interface_0_in_0x5611d2dde530;
        interface_0_in_0x5611d2d29910;
    }
    // Op's.
    op_0x5611d2d298f0 [label="Shift"];
    // Dimension's.
    interface_0_in_0x5611d2d29910 -> op_0x5611d2d298f0 [label="H"];
    interface_0_in_0x5611d2dde4e0 -> interface_0_out_0x5611d2dde4e0 [label="N"];
    interface_0_in_0x5611d2dde508 -> interface_0_out_0x5611d2dde508 [label="C_out"];
    interface_0_in_0x5611d2dde530 -> interface_0_out_0x5611d2dde530 [label="H"];
    op_0x5611d2d298f0 -> interface_0_out_0x5611d2dde558 [label="H"];
}

// Stage tensor.
subgraph cluster_subgraph_1 {
    label = "Subgraph 1";
    // Reductions.
    reduce_0x7f9448002ce8 [label="Sum", shape=box];
    // Output.
    subgraph cluster_subgraph_1_out {
        label = "";
        interface_1_out_0x5611d2dde4e0 [label="N", shape=none];
        interface_1_out_0x5611d2dde508 [label="C_out", shape=none];
        interface_1_out_0x5611d2dde530 [label="H", shape=none];
        interface_1_out_0x5611d2d29910 [label="H", shape=none];
    }
    {
        rank = same;
        reduce_0x7f9448002ce8;
        interface_1_out_0x5611d2dde4e0;
        interface_1_out_0x5611d2dde508;
        interface_1_out_0x5611d2dde530;
        interface_1_out_0x5611d2d29910;
    }
    // Input 0.
    subgraph cluster_subgraph_1_in_0 {
        label = "";
        interface_1_in_0x5611d2dde4e0 [label="N", shape=none];
        interface_1_in_0x5611d2dde508 [label="C_out", shape=none];
        interface_1_in_0x5611d2d27a50 [label="H", shape=none];
        interface_1_in_0x5611d2d27a68 [label="s", shape=none];
        interface_1_in_0x5611d2d29910 [label="H", shape=none];
    }
    {
        rank = same;
        interface_1_in_0x5611d2dde4e0;
        interface_1_in_0x5611d2dde508;
        interface_1_in_0x5611d2d27a50;
        interface_1_in_0x5611d2d27a68;
        interface_1_in_0x5611d2d29910;
    }
    // Op's.
    op_0x5611d2d27a10 [label="Merge"];
    op_0x5611d2d29920 [label="Shift"];
    op_0x5611d2d2a0a0 [label="Split"];
    // Dimension's.
    interface_1_in_0x5611d2d27a50 -> op_0x5611d2d27a10 [label="H"];
    interface_1_in_0x5611d2d27a68 -> op_0x5611d2d27a10 [label="s"];
    interface_1_in_0x5611d2d29910 -> interface_1_out_0x5611d2d29910 [label="H"];
    op_0x5611d2d27a10 -> op_0x5611d2d29920 [label="s*H"];
    op_0x5611d2d29920 -> op_0x5611d2d2a0a0 [label="s*H"];
    interface_1_in_0x5611d2dde4e0 -> interface_1_out_0x5611d2dde4e0 [label="N"];
    interface_1_in_0x5611d2dde508 -> interface_1_out_0x5611d2dde508 [label="C_out"];
    op_0x5611d2d2a0a0 -> interface_1_out_0x5611d2dde530 [label="H"];
    op_0x5611d2d2a0a0 -> reduce_0x7f9448002ce8 [label="s"];
}

// Stage tensor.
subgraph cluster_subgraph_2 {
    label = "Subgraph 2";
    // Reductions.
    reduce_0x7f9448001a98 [label="Sum", shape=box];
    reduce_0x7f9448005b48 [label="Sum", shape=box];
    // Output.
    subgraph cluster_subgraph_2_out {
        label = "";
        interface_2_out_0x5611d2dde4e0 [label="N", shape=none];
        interface_2_out_0x5611d2dde508 [label="C_out", shape=none];
        interface_2_out_0x5611d2d27a50 [label="H", shape=none];
        interface_2_out_0x5611d2d27a68 [label="s", shape=none];
        interface_2_out_0x5611d2d29910 [label="H", shape=none];
    }
    {
        rank = same;
        reduce_0x7f9448001a98;
        reduce_0x7f9448005b48;
        interface_2_out_0x5611d2dde4e0;
        interface_2_out_0x5611d2dde508;
        interface_2_out_0x5611d2d27a50;
        interface_2_out_0x5611d2d27a68;
        interface_2_out_0x5611d2d29910;
    }
    // Input 0.
    subgraph cluster_subgraph_2_in_0 {
        label = "";
        interface_2_in_0x5611d2dde4e0 [label="N", shape=none];
        interface_2_in_0x5611d4495290 [label="k_1", shape=none];
        interface_2_in_0x5611d2d27a50 [label="H", shape=none];
        interface_2_in_0x5611d4495240 [label="C_in", shape=none];
        interface_2_in_0x5611d2d29910 [label="H", shape=none];
    }
    // Input 1.
    subgraph cluster_subgraph_2_in_1 {
        label = "";
        interface_2_in_0x5611d44951b8 [label="C_out", shape=none];
        interface_2_in_0x5611d44952a8 [label="k_1", shape=none];
        interface_2_in_0x5611d44952f8 [label="s", shape=none];
        interface_2_in_0x5611d4495258 [label="C_in", shape=none];
    }
    {
        rank = same;
        interface_2_in_0x5611d2dde4e0;
        interface_2_in_0x5611d4495290;
        interface_2_in_0x5611d2d27a50;
        interface_2_in_0x5611d4495240;
        interface_2_in_0x5611d2d29910;
        interface_2_in_0x5611d44951b8;
        interface_2_in_0x5611d44952a8;
        interface_2_in_0x5611d44952f8;
        interface_2_in_0x5611d4495258;
    }
    // Op's.
    op_0x5611d2c9c698 [label="Expand"];
    op_0x5611d2c9c6b8 [label="Expand"];
    op_0x5611d4495180 [label="Share"];
    op_0x5611d4495220 [label="Share"];
    op_0x5611d4495270 [label="Share"];
    op_0x5611d44952c0 [label="Share"];
    // Dimension's.
    interface_2_in_0x5611d2d27a50 -> interface_2_out_0x5611d2d27a50 [label="H"];
    op_0x5611d44952c0 -> interface_2_out_0x5611d2d27a68 [label="s"];
    interface_2_in_0x5611d2d29910 -> interface_2_out_0x5611d2d29910 [label="H"];
    interface_2_in_0x5611d2dde4e0 -> interface_2_out_0x5611d2dde4e0 [label="N"];
    op_0x5611d4495180 -> interface_2_out_0x5611d2dde508 [label="C_out"];
    op_0x5611d2c9c698 -> op_0x5611d4495180 [label="C_out"];
    interface_2_in_0x5611d44951b8 -> op_0x5611d4495180 [label="C_out"];
    interface_2_in_0x5611d4495240 -> op_0x5611d4495220 [label="C_in"];
    interface_2_in_0x5611d4495258 -> op_0x5611d4495220 [label="C_in"];
    interface_2_in_0x5611d4495290 -> op_0x5611d4495270 [label="k_1"];
    interface_2_in_0x5611d44952a8 -> op_0x5611d4495270 [label="k_1"];
    op_0x5611d2c9c6b8 -> op_0x5611d44952c0 [label="s"];
    interface_2_in_0x5611d44952f8 -> op_0x5611d44952c0 [label="s"];
    op_0x5611d4495270 -> reduce_0x7f9448001a98 [label="k_1"];
    op_0x5611d4495220 -> reduce_0x7f9448005b48 [label="C_in"];
}

// Stage tensor.
subgraph cluster_subgraph_3 {
    label = "Subgraph 3";
    // Reductions.
    // Output.
    subgraph cluster_subgraph_3_out {
        label = "";
        interface_3_out_0x5611d2dde4e0 [label="N", shape=none];
        interface_3_out_0x5611d4495290 [label="k_1", shape=none];
        interface_3_out_0x5611d2d27a50 [label="H", shape=none];
        interface_3_out_0x5611d4495240 [label="C_in", shape=none];
        interface_3_out_0x5611d2d29910 [label="H", shape=none];
    }
    {
        rank = same;
        interface_3_out_0x5611d2dde4e0;
        interface_3_out_0x5611d4495290;
        interface_3_out_0x5611d2d27a50;
        interface_3_out_0x5611d4495240;
        interface_3_out_0x5611d2d29910;
    }
    // Input 0.
    subgraph cluster_subgraph_3_in_0 {
        label = "";
        interface_3_in_0x5611d2dde4e0 [label="N", shape=none];
        interface_3_in_0x5611d4495240 [label="C_in", shape=none];
        interface_3_in_0x5611d2d29910 [label="H", shape=none];
        interface_3_in_0x5611d33e1ce8 [label="H", shape=none];
    }
    {
        rank = same;
        interface_3_in_0x5611d2dde4e0;
        interface_3_in_0x5611d4495240;
        interface_3_in_0x5611d2d29910;
        interface_3_in_0x5611d33e1ce8;
    }
    // Op's.
    op_0x5611d33e1cc0 [label="Unfold"];
    // Dimension's.
    op_0x5611d33e1cc0 -> interface_3_out_0x5611d2d27a50 [label="H"];
    interface_3_in_0x5611d2d29910 -> interface_3_out_0x5611d2d29910 [label="H"];
    interface_3_in_0x5611d2dde4e0 -> interface_3_out_0x5611d2dde4e0 [label="N"];
    interface_3_in_0x5611d33e1ce8 -> op_0x5611d33e1cc0 [label="H"];
    interface_3_in_0x5611d4495240 -> interface_3_out_0x5611d4495240 [label="C_in"];
    op_0x5611d33e1cc0 -> interface_3_out_0x5611d4495290 [label="k_1"];
}

// Input tensor.
subgraph cluster_subgraph_4 {
    label = "Input 0";
    interface_4_out_0x5611d2dde4e0 [label="N", shape=none];
    interface_4_out_0x5611d4495240 [label="C_in", shape=none];
    interface_4_out_0x5611d2d29910 [label="H", shape=none];
    interface_4_out_0x5611d33e1ce8 [label="H", shape=none];
}

interface_4_out_0x5611d2dde4e0 -> interface_3_in_0x5611d2dde4e0;
interface_4_out_0x5611d4495240 -> interface_3_in_0x5611d4495240;
interface_4_out_0x5611d2d29910 -> interface_3_in_0x5611d2d29910;
interface_4_out_0x5611d33e1ce8 -> interface_3_in_0x5611d33e1ce8;

interface_3_out_0x5611d2dde4e0 -> interface_2_in_0x5611d2dde4e0;
interface_3_out_0x5611d4495290 -> interface_2_in_0x5611d4495290;
interface_3_out_0x5611d2d27a50 -> interface_2_in_0x5611d2d27a50;
interface_3_out_0x5611d4495240 -> interface_2_in_0x5611d4495240;
interface_3_out_0x5611d2d29910 -> interface_2_in_0x5611d2d29910;

// Input tensor.
subgraph cluster_subgraph_5 {
    label = "Input 1";
    interface_5_out_0x5611d44951b8 [label="C_out", shape=none];
    interface_5_out_0x5611d44952a8 [label="k_1", shape=none];
    interface_5_out_0x5611d44952f8 [label="s", shape=none];
    interface_5_out_0x5611d4495258 [label="C_in", shape=none];
}

interface_5_out_0x5611d44951b8 -> interface_2_in_0x5611d44951b8;
interface_5_out_0x5611d44952a8 -> interface_2_in_0x5611d44952a8;
interface_5_out_0x5611d44952f8 -> interface_2_in_0x5611d44952f8;
interface_5_out_0x5611d4495258 -> interface_2_in_0x5611d4495258;

interface_2_out_0x5611d2dde4e0 -> interface_1_in_0x5611d2dde4e0;
interface_2_out_0x5611d2dde508 -> interface_1_in_0x5611d2dde508;
interface_2_out_0x5611d2d27a50 -> interface_1_in_0x5611d2d27a50;
interface_2_out_0x5611d2d27a68 -> interface_1_in_0x5611d2d27a68;
interface_2_out_0x5611d2d29910 -> interface_1_in_0x5611d2d29910;

interface_1_out_0x5611d2dde4e0 -> interface_0_in_0x5611d2dde4e0;
interface_1_out_0x5611d2dde508 -> interface_0_in_0x5611d2dde508;
interface_1_out_0x5611d2dde530 -> interface_0_in_0x5611d2dde530;
interface_1_out_0x5611d2d29910 -> interface_0_in_0x5611d2d29910;

{
    rank = same;
    interface_4_out_0x5611d2dde4e0;
    interface_4_out_0x5611d4495240;
    interface_4_out_0x5611d2d29910;
    interface_4_out_0x5611d33e1ce8;
    interface_5_out_0x5611d44951b8;
    interface_5_out_0x5611d44952a8;
    interface_5_out_0x5611d44952f8;
    interface_5_out_0x5611d4495258;
}
subgraph cluster_subgraph_output {
    label = "Output";
    interface_6_in_0x5611d2dde4e0 [label="N", shape=none];
    interface_6_in_0x5611d2dde508 [label="C_out", shape=none];
    interface_6_in_0x5611d2dde530 [label="H", shape=none];
    interface_6_in_0x5611d2dde558 [label="H", shape=none];
}
interface_0_out_0x5611d2dde4e0 -> interface_6_in_0x5611d2dde4e0;
interface_0_out_0x5611d2dde508 -> interface_6_in_0x5611d2dde508;
interface_0_out_0x5611d2dde530 -> interface_6_in_0x5611d2dde530;
interface_0_out_0x5611d2dde558 -> interface_6_in_0x5611d2dde558;

}

"""
class kernel_generated_0(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([64, 3, 2, 64]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]

		# Perform contraction.
		t_2 = torch.einsum("jlik -> jkli", in_0)

		# [H]@Unfold9ee82d948cf711ad -> [H]@Merge5f50103ea583163b, [k_1]@Share26cfa48d169008e4
		t_2 = torch.reshape(t_2, (1024, 1, 56, 3584, ))
		t_2 = torch.nn.functional.unfold(t_2, (3, 1, ), padding=(1, 0, ))
		t_2 = torch.reshape(t_2, (1024, 3, 56, 64, 56, ))

		# Perform contraction.
		t_3 = torch.einsum("okmjn, iklj -> oimln", t_2, in_1)

		# No contraction needed.
		t_4 = t_3

		# [H]@Merge5f50103ea583163b, [s]@Merge5f50103ea5831638 -> [s*H]@Shift3c9c8e9d3c84cb9b
		t_4 = torch.reshape(t_4, (1024, 64, 112, 56, ))

		# [s*H]@Shift3c9c8e9d3c84cb9b -> [s*H]@Splitdb1af055f999951a
		t_4 = torch.roll(t_4, self.shift_direction, 2)

		# [s*H]@Splitdb1af055f999951a -> [H]@Iterator96123ba3184da39c, [s]@Reduced95c644a3c072d9a
		t_4 = torch.reshape(t_4, (1024, 64, 56, 2, 56, ))

		# [s]@Reduce
		t_4 = torch.sum(t_4, dim=(3, ))

		# No contraction needed.
		t_5 = t_4

		# [H]@Shift6b179c72f0c6dbad -> [H]@Iteratorb0a1def4ad5784ec
		t_5 = torch.roll(t_5, self.shift_direction, 3)

		# No need to crop the output tensor.
		y = t_5

		return y

class kernel_generated_1(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([128, 3, 2, 64]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]

		# Perform contraction.
		t_2 = torch.einsum("jlik -> jkli", in_0)

		# [H]@Unfold9ee82d948cf711ad -> [H]@Merge5f50103ea583163b, [k_1]@Share26cfa48d169008e4
		t_2 = torch.reshape(t_2, (1024, 1, 28, 1792, ))
		t_2 = torch.nn.functional.unfold(t_2, (3, 1, ), padding=(1, 0, ))
		t_2 = torch.reshape(t_2, (1024, 3, 28, 64, 28, ))

		# Perform contraction.
		t_3 = torch.einsum("okmjn, iklj -> oimln", t_2, in_1)

		# No contraction needed.
		t_4 = t_3

		# [H]@Merge5f50103ea583163b, [s]@Merge5f50103ea5831638 -> [s*H]@Shift3c9c8e9d3c84cb9b
		t_4 = torch.reshape(t_4, (1024, 128, 56, 28, ))

		# [s*H]@Shift3c9c8e9d3c84cb9b -> [s*H]@Splitdb1af055f999951a
		t_4 = torch.roll(t_4, self.shift_direction, 2)

		# [s*H]@Splitdb1af055f999951a -> [H]@Iterator96123ba3184da39c, [s]@Reduced95c644a3c072d9a
		t_4 = torch.reshape(t_4, (1024, 128, 28, 2, 28, ))

		# [s]@Reduce
		t_4 = torch.sum(t_4, dim=(3, ))

		# No contraction needed.
		t_5 = t_4

		# [H]@Shift6b179c72f0c6dbad -> [H]@Iteratorb0a1def4ad5784ec
		t_5 = torch.roll(t_5, self.shift_direction, 3)

		# No need to crop the output tensor.
		y = t_5

		return y

class kernel_generated_2(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([128, 3, 2, 128]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]

		# Perform contraction.
		t_2 = torch.einsum("jlik -> jkli", in_0)

		# [H]@Unfold9ee82d948cf711ad -> [H]@Merge5f50103ea583163b, [k_1]@Share26cfa48d169008e4
		t_2 = torch.reshape(t_2, (1024, 1, 28, 3584, ))
		t_2 = torch.nn.functional.unfold(t_2, (3, 1, ), padding=(1, 0, ))
		t_2 = torch.reshape(t_2, (1024, 3, 28, 128, 28, ))

		# Perform contraction.
		t_3 = torch.einsum("okmjn, iklj -> oimln", t_2, in_1)

		# No contraction needed.
		t_4 = t_3

		# [H]@Merge5f50103ea583163b, [s]@Merge5f50103ea5831638 -> [s*H]@Shift3c9c8e9d3c84cb9b
		t_4 = torch.reshape(t_4, (1024, 128, 56, 28, ))

		# [s*H]@Shift3c9c8e9d3c84cb9b -> [s*H]@Splitdb1af055f999951a
		t_4 = torch.roll(t_4, self.shift_direction, 2)

		# [s*H]@Splitdb1af055f999951a -> [H]@Iterator96123ba3184da39c, [s]@Reduced95c644a3c072d9a
		t_4 = torch.reshape(t_4, (1024, 128, 28, 2, 28, ))

		# [s]@Reduce
		t_4 = torch.sum(t_4, dim=(3, ))

		# No contraction needed.
		t_5 = t_4

		# [H]@Shift6b179c72f0c6dbad -> [H]@Iteratorb0a1def4ad5784ec
		t_5 = torch.roll(t_5, self.shift_direction, 3)

		# No need to crop the output tensor.
		y = t_5

		return y

class kernel_generated_3(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([256, 3, 2, 128]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]

		# Perform contraction.
		t_2 = torch.einsum("jlik -> jkli", in_0)

		# [H]@Unfold9ee82d948cf711ad -> [H]@Merge5f50103ea583163b, [k_1]@Share26cfa48d169008e4
		t_2 = torch.reshape(t_2, (1024, 1, 14, 1792, ))
		t_2 = torch.nn.functional.unfold(t_2, (3, 1, ), padding=(1, 0, ))
		t_2 = torch.reshape(t_2, (1024, 3, 14, 128, 14, ))

		# Perform contraction.
		t_3 = torch.einsum("okmjn, iklj -> oimln", t_2, in_1)

		# No contraction needed.
		t_4 = t_3

		# [H]@Merge5f50103ea583163b, [s]@Merge5f50103ea5831638 -> [s*H]@Shift3c9c8e9d3c84cb9b
		t_4 = torch.reshape(t_4, (1024, 256, 28, 14, ))

		# [s*H]@Shift3c9c8e9d3c84cb9b -> [s*H]@Splitdb1af055f999951a
		t_4 = torch.roll(t_4, self.shift_direction, 2)

		# [s*H]@Splitdb1af055f999951a -> [H]@Iterator96123ba3184da39c, [s]@Reduced95c644a3c072d9a
		t_4 = torch.reshape(t_4, (1024, 256, 14, 2, 14, ))

		# [s]@Reduce
		t_4 = torch.sum(t_4, dim=(3, ))

		# No contraction needed.
		t_5 = t_4

		# [H]@Shift6b179c72f0c6dbad -> [H]@Iteratorb0a1def4ad5784ec
		t_5 = torch.roll(t_5, self.shift_direction, 3)

		# No need to crop the output tensor.
		y = t_5

		return y

class kernel_generated_4(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([256, 3, 2, 256]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]

		# Perform contraction.
		t_2 = torch.einsum("jlik -> jkli", in_0)

		# [H]@Unfold9ee82d948cf711ad -> [H]@Merge5f50103ea583163b, [k_1]@Share26cfa48d169008e4
		t_2 = torch.reshape(t_2, (1024, 1, 14, 3584, ))
		t_2 = torch.nn.functional.unfold(t_2, (3, 1, ), padding=(1, 0, ))
		t_2 = torch.reshape(t_2, (1024, 3, 14, 256, 14, ))

		# Perform contraction.
		t_3 = torch.einsum("okmjn, iklj -> oimln", t_2, in_1)

		# No contraction needed.
		t_4 = t_3

		# [H]@Merge5f50103ea583163b, [s]@Merge5f50103ea5831638 -> [s*H]@Shift3c9c8e9d3c84cb9b
		t_4 = torch.reshape(t_4, (1024, 256, 28, 14, ))

		# [s*H]@Shift3c9c8e9d3c84cb9b -> [s*H]@Splitdb1af055f999951a
		t_4 = torch.roll(t_4, self.shift_direction, 2)

		# [s*H]@Splitdb1af055f999951a -> [H]@Iterator96123ba3184da39c, [s]@Reduced95c644a3c072d9a
		t_4 = torch.reshape(t_4, (1024, 256, 14, 2, 14, ))

		# [s]@Reduce
		t_4 = torch.sum(t_4, dim=(3, ))

		# No contraction needed.
		t_5 = t_4

		# [H]@Shift6b179c72f0c6dbad -> [H]@Iteratorb0a1def4ad5784ec
		t_5 = torch.roll(t_5, self.shift_direction, 3)

		# No need to crop the output tensor.
		y = t_5

		return y

class kernel_generated_5(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([512, 3, 2, 256]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]

		# Perform contraction.
		t_2 = torch.einsum("jlik -> jkli", in_0)

		# [H]@Unfold9ee82d948cf711ad -> [H]@Merge5f50103ea583163b, [k_1]@Share26cfa48d169008e4
		t_2 = torch.reshape(t_2, (1024, 1, 7, 1792, ))
		t_2 = torch.nn.functional.unfold(t_2, (3, 1, ), padding=(1, 0, ))
		t_2 = torch.reshape(t_2, (1024, 3, 7, 256, 7, ))

		# Perform contraction.
		t_3 = torch.einsum("okmjn, iklj -> oimln", t_2, in_1)

		# No contraction needed.
		t_4 = t_3

		# [H]@Merge5f50103ea583163b, [s]@Merge5f50103ea5831638 -> [s*H]@Shift3c9c8e9d3c84cb9b
		t_4 = torch.reshape(t_4, (1024, 512, 14, 7, ))

		# [s*H]@Shift3c9c8e9d3c84cb9b -> [s*H]@Splitdb1af055f999951a
		t_4 = torch.roll(t_4, self.shift_direction, 2)

		# [s*H]@Splitdb1af055f999951a -> [H]@Iterator96123ba3184da39c, [s]@Reduced95c644a3c072d9a
		t_4 = torch.reshape(t_4, (1024, 512, 7, 2, 7, ))

		# [s]@Reduce
		t_4 = torch.sum(t_4, dim=(3, ))

		# No contraction needed.
		t_5 = t_4

		# [H]@Shift6b179c72f0c6dbad -> [H]@Iteratorb0a1def4ad5784ec
		t_5 = torch.roll(t_5, self.shift_direction, 3)

		# No need to crop the output tensor.
		y = t_5

		return y

class kernel_generated_6(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([512, 3, 2, 512]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]

		# Perform contraction.
		t_2 = torch.einsum("jlik -> jkli", in_0)

		# [H]@Unfold9ee82d948cf711ad -> [H]@Merge5f50103ea583163b, [k_1]@Share26cfa48d169008e4
		t_2 = torch.reshape(t_2, (1024, 1, 7, 3584, ))
		t_2 = torch.nn.functional.unfold(t_2, (3, 1, ), padding=(1, 0, ))
		t_2 = torch.reshape(t_2, (1024, 3, 7, 512, 7, ))

		# Perform contraction.
		t_3 = torch.einsum("okmjn, iklj -> oimln", t_2, in_1)

		# No contraction needed.
		t_4 = t_3

		# [H]@Merge5f50103ea583163b, [s]@Merge5f50103ea5831638 -> [s*H]@Shift3c9c8e9d3c84cb9b
		t_4 = torch.reshape(t_4, (1024, 512, 14, 7, ))

		# [s*H]@Shift3c9c8e9d3c84cb9b -> [s*H]@Splitdb1af055f999951a
		t_4 = torch.roll(t_4, self.shift_direction, 2)

		# [s*H]@Splitdb1af055f999951a -> [H]@Iterator96123ba3184da39c, [s]@Reduced95c644a3c072d9a
		t_4 = torch.reshape(t_4, (1024, 512, 7, 2, 7, ))

		# [s]@Reduce
		t_4 = torch.sum(t_4, dim=(3, ))

		# No contraction needed.
		t_5 = t_4

		# [H]@Shift6b179c72f0c6dbad -> [H]@Iteratorb0a1def4ad5784ec
		t_5 = torch.roll(t_5, self.shift_direction, 3)

		# No need to crop the output tensor.
		y = t_5

		return y

