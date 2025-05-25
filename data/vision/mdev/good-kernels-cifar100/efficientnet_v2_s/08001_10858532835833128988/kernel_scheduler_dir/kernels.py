import torch
import random
"""
digraph kernel_preview {
newrank = true;

// Stage tensor.
subgraph cluster_subgraph_0 {
    label = "Subgraph 0";
    // Reductions.
    reduce_0x7fc7f0001bc0 [label="Sum", shape=box];
    reduce_0x7fc7f00035d0 [label="Sum", shape=box];
    // Output.
    subgraph cluster_subgraph_0_out {
        label = "";
        interface_0_out_0x5581660a87e0 [label="N", shape=none];
        interface_0_out_0x5581660a8808 [label="C_out", shape=none];
        interface_0_out_0x5581660a8830 [label="H", shape=none];
        interface_0_out_0x5581660a8858 [label="H", shape=none];
    }
    {
        rank = same;
        reduce_0x7fc7f0001bc0;
        reduce_0x7fc7f00035d0;
        interface_0_out_0x5581660a87e0;
        interface_0_out_0x5581660a8808;
        interface_0_out_0x5581660a8830;
        interface_0_out_0x5581660a8858;
    }
    // Input 0.
    subgraph cluster_subgraph_0_in_0 {
        label = "";
        interface_0_in_0x5581660a87e0 [label="N", shape=none];
        interface_0_in_0x5581660a8830 [label="H", shape=none];
        interface_0_in_0x7fcf58004dc0 [label="k_1^2", shape=none];
        interface_0_in_0x5581660a8858 [label="H", shape=none];
        interface_0_in_0x7fcf58004c80 [label="k_2*s", shape=none];
    }
    // Input 1.
    subgraph cluster_subgraph_0_in_1 {
        label = "";
        interface_0_in_0x7fcf84003f38 [label="C_out", shape=none];
        interface_0_in_0x7fcf58004dd8 [label="k_1^2", shape=none];
        interface_0_in_0x7fcf58004c98 [label="k_2*s", shape=none];
    }
    {
        rank = same;
        interface_0_in_0x5581660a87e0;
        interface_0_in_0x5581660a8830;
        interface_0_in_0x7fcf58004dc0;
        interface_0_in_0x5581660a8858;
        interface_0_in_0x7fcf58004c80;
        interface_0_in_0x7fcf84003f38;
        interface_0_in_0x7fcf58004dd8;
        interface_0_in_0x7fcf58004c98;
    }
    // Op's.
    op_0x7fcf58004c60 [label="Share"];
    op_0x7fcf58004da0 [label="Share"];
    op_0x7fcf84003f00 [label="Share"];
    op_0x7fcf84004638 [label="Expand"];
    // Dimension's.
    interface_0_in_0x5581660a87e0 -> interface_0_out_0x5581660a87e0 [label="N"];
    op_0x7fcf84003f00 -> interface_0_out_0x5581660a8808 [label="C_out"];
    interface_0_in_0x5581660a8830 -> interface_0_out_0x5581660a8830 [label="H"];
    interface_0_in_0x5581660a8858 -> interface_0_out_0x5581660a8858 [label="H"];
    op_0x7fcf58004da0 -> reduce_0x7fc7f0001bc0 [label="k_1^2"];
    op_0x7fcf58004c60 -> reduce_0x7fc7f00035d0 [label="k_2*s"];
    interface_0_in_0x7fcf58004c80 -> op_0x7fcf58004c60 [label="k_2*s"];
    interface_0_in_0x7fcf58004c98 -> op_0x7fcf58004c60 [label="k_2*s"];
    interface_0_in_0x7fcf58004dc0 -> op_0x7fcf58004da0 [label="k_1^2"];
    interface_0_in_0x7fcf58004dd8 -> op_0x7fcf58004da0 [label="k_1^2"];
    op_0x7fcf84004638 -> op_0x7fcf84003f00 [label="C_out"];
    interface_0_in_0x7fcf84003f38 -> op_0x7fcf84003f00 [label="C_out"];
}

// Stage tensor.
subgraph cluster_subgraph_1 {
    label = "Subgraph 1";
    // Reductions.
    reduce_0x7fc7f0002f58 [label="Sum", shape=box];
    // Output.
    subgraph cluster_subgraph_1_out {
        label = "";
        interface_1_out_0x5581660a87e0 [label="N", shape=none];
        interface_1_out_0x5581660a8830 [label="H", shape=none];
        interface_1_out_0x7fcf58004dc0 [label="k_1^2", shape=none];
        interface_1_out_0x5581660a8858 [label="H", shape=none];
        interface_1_out_0x7fcf58004c80 [label="k_2*s", shape=none];
    }
    {
        rank = same;
        reduce_0x7fc7f0002f58;
        interface_1_out_0x5581660a87e0;
        interface_1_out_0x5581660a8830;
        interface_1_out_0x7fcf58004dc0;
        interface_1_out_0x5581660a8858;
        interface_1_out_0x7fcf58004c80;
    }
    // Input 0.
    subgraph cluster_subgraph_1_in_0 {
        label = "";
        interface_1_in_0x5581660a87e0 [label="N", shape=none];
        interface_1_in_0x5581660a8830 [label="H", shape=none];
        interface_1_in_0x7fcef031bb68 [label="H", shape=none];
        interface_1_in_0x7fcbb4027668 [label="s", shape=none];
        interface_1_in_0x7fcf58004c80 [label="k_2*s", shape=none];
    }
    {
        rank = same;
        interface_1_in_0x5581660a87e0;
        interface_1_in_0x5581660a8830;
        interface_1_in_0x7fcef031bb68;
        interface_1_in_0x7fcbb4027668;
        interface_1_in_0x7fcf58004c80;
    }
    // Op's.
    op_0x7fcbb4027610 [label="Merge"];
    op_0x7fccd4008390 [label="Split"];
    op_0x7fcef031bb40 [label="Unfold"];
    op_0x7fcef400a680 [label="Shift"];
    // Dimension's.
    interface_1_in_0x5581660a87e0 -> interface_1_out_0x5581660a87e0 [label="N"];
    interface_1_in_0x5581660a8830 -> interface_1_out_0x5581660a8830 [label="H"];
    op_0x7fccd4008390 -> interface_1_out_0x5581660a8858 [label="H"];
    op_0x7fccd4008390 -> reduce_0x7fc7f0002f58 [label="s"];
    op_0x7fcef031bb40 -> op_0x7fcbb4027610 [label="H"];
    interface_1_in_0x7fcbb4027668 -> op_0x7fcbb4027610 [label="s"];
    op_0x7fcef400a680 -> op_0x7fccd4008390 [label="s*H"];
    interface_1_in_0x7fcef031bb68 -> op_0x7fcef031bb40 [label="H"];
    op_0x7fcbb4027610 -> op_0x7fcef400a680 [label="s*H"];
    interface_1_in_0x7fcf58004c80 -> interface_1_out_0x7fcf58004c80 [label="k_2*s"];
    op_0x7fcef031bb40 -> interface_1_out_0x7fcf58004dc0 [label="k_1^2"];
}

// Stage tensor.
subgraph cluster_subgraph_2 {
    label = "Subgraph 2";
    // Reductions.
    reduce_0x7fc7f0005e70 [label="Sum", shape=box];
    // Output.
    subgraph cluster_subgraph_2_out {
        label = "";
        interface_2_out_0x5581660a87e0 [label="N", shape=none];
        interface_2_out_0x5581660a8830 [label="H", shape=none];
        interface_2_out_0x7fcef031bb68 [label="H", shape=none];
        interface_2_out_0x7fcbb4027668 [label="s", shape=none];
        interface_2_out_0x7fcf58004c80 [label="k_2*s", shape=none];
    }
    {
        rank = same;
        reduce_0x7fc7f0005e70;
        interface_2_out_0x5581660a87e0;
        interface_2_out_0x5581660a8830;
        interface_2_out_0x7fcef031bb68;
        interface_2_out_0x7fcbb4027668;
        interface_2_out_0x7fcf58004c80;
    }
    // Input 0.
    subgraph cluster_subgraph_2_in_0 {
        label = "";
        interface_2_in_0x5581660a87e0 [label="N", shape=none];
        interface_2_in_0x7fc950008e30 [label="C_in", shape=none];
        interface_2_in_0x5581660a8830 [label="H", shape=none];
        interface_2_in_0x7fcef031bb68 [label="H", shape=none];
    }
    // Input 1.
    subgraph cluster_subgraph_2_in_1 {
        label = "";
        interface_2_in_0x7fc950008e48 [label="C_in", shape=none];
        interface_2_in_0x7fcf100212b8 [label="s", shape=none];
        interface_2_in_0x7fc950008588 [label="k_2*s", shape=none];
    }
    {
        rank = same;
        interface_2_in_0x5581660a87e0;
        interface_2_in_0x7fc950008e30;
        interface_2_in_0x5581660a8830;
        interface_2_in_0x7fcef031bb68;
        interface_2_in_0x7fc950008e48;
        interface_2_in_0x7fcf100212b8;
        interface_2_in_0x7fc950008588;
    }
    // Op's.
    op_0x7fc950008550 [label="Share"];
    op_0x7fc950008e10 [label="Share"];
    op_0x7fce2c019d98 [label="Expand"];
    op_0x7fcf10021280 [label="Share"];
    op_0x7fcf840048b8 [label="Expand"];
    // Dimension's.
    interface_2_in_0x5581660a87e0 -> interface_2_out_0x5581660a87e0 [label="N"];
    interface_2_in_0x5581660a8830 -> interface_2_out_0x5581660a8830 [label="H"];
    op_0x7fc950008e10 -> reduce_0x7fc7f0005e70 [label="C_in"];
    op_0x7fcf840048b8 -> op_0x7fc950008550 [label="k_2*s"];
    interface_2_in_0x7fc950008588 -> op_0x7fc950008550 [label="k_2*s"];
    interface_2_in_0x7fc950008e30 -> op_0x7fc950008e10 [label="C_in"];
    interface_2_in_0x7fc950008e48 -> op_0x7fc950008e10 [label="C_in"];
    op_0x7fcf10021280 -> interface_2_out_0x7fcbb4027668 [label="s"];
    interface_2_in_0x7fcef031bb68 -> interface_2_out_0x7fcef031bb68 [label="H"];
    op_0x7fce2c019d98 -> op_0x7fcf10021280 [label="s"];
    interface_2_in_0x7fcf100212b8 -> op_0x7fcf10021280 [label="s"];
    op_0x7fc950008550 -> interface_2_out_0x7fcf58004c80 [label="k_2*s"];
}

// Input tensor.
subgraph cluster_subgraph_3 {
    label = "Input 0";
    interface_3_out_0x5581660a87e0 [label="N", shape=none];
    interface_3_out_0x7fc950008e30 [label="C_in", shape=none];
    interface_3_out_0x5581660a8830 [label="H", shape=none];
    interface_3_out_0x7fcef031bb68 [label="H", shape=none];
}

interface_3_out_0x5581660a87e0 -> interface_2_in_0x5581660a87e0;
interface_3_out_0x7fc950008e30 -> interface_2_in_0x7fc950008e30;
interface_3_out_0x5581660a8830 -> interface_2_in_0x5581660a8830;
interface_3_out_0x7fcef031bb68 -> interface_2_in_0x7fcef031bb68;

// Input tensor.
subgraph cluster_subgraph_4 {
    label = "Input 2";
    interface_4_out_0x7fc950008e48 [label="C_in", shape=none];
    interface_4_out_0x7fcf100212b8 [label="s", shape=none];
    interface_4_out_0x7fc950008588 [label="k_2*s", shape=none];
}

interface_4_out_0x7fc950008e48 -> interface_2_in_0x7fc950008e48;
interface_4_out_0x7fcf100212b8 -> interface_2_in_0x7fcf100212b8;
interface_4_out_0x7fc950008588 -> interface_2_in_0x7fc950008588;

interface_2_out_0x5581660a87e0 -> interface_1_in_0x5581660a87e0;
interface_2_out_0x5581660a8830 -> interface_1_in_0x5581660a8830;
interface_2_out_0x7fcef031bb68 -> interface_1_in_0x7fcef031bb68;
interface_2_out_0x7fcbb4027668 -> interface_1_in_0x7fcbb4027668;
interface_2_out_0x7fcf58004c80 -> interface_1_in_0x7fcf58004c80;

interface_1_out_0x5581660a87e0 -> interface_0_in_0x5581660a87e0;
interface_1_out_0x5581660a8830 -> interface_0_in_0x5581660a8830;
interface_1_out_0x7fcf58004dc0 -> interface_0_in_0x7fcf58004dc0;
interface_1_out_0x5581660a8858 -> interface_0_in_0x5581660a8858;
interface_1_out_0x7fcf58004c80 -> interface_0_in_0x7fcf58004c80;

// Input tensor.
subgraph cluster_subgraph_5 {
    label = "Input 1";
    interface_5_out_0x7fcf84003f38 [label="C_out", shape=none];
    interface_5_out_0x7fcf58004dd8 [label="k_1^2", shape=none];
    interface_5_out_0x7fcf58004c98 [label="k_2*s", shape=none];
}

interface_5_out_0x7fcf84003f38 -> interface_0_in_0x7fcf84003f38;
interface_5_out_0x7fcf58004dd8 -> interface_0_in_0x7fcf58004dd8;
interface_5_out_0x7fcf58004c98 -> interface_0_in_0x7fcf58004c98;

{
    rank = same;
    interface_3_out_0x5581660a87e0;
    interface_3_out_0x7fc950008e30;
    interface_3_out_0x5581660a8830;
    interface_3_out_0x7fcef031bb68;
    interface_5_out_0x7fcf84003f38;
    interface_5_out_0x7fcf58004dd8;
    interface_5_out_0x7fcf58004c98;
    interface_4_out_0x7fc950008e48;
    interface_4_out_0x7fcf100212b8;
    interface_4_out_0x7fc950008588;
}
subgraph cluster_subgraph_output {
    label = "Output";
    interface_6_in_0x5581660a87e0 [label="N", shape=none];
    interface_6_in_0x5581660a8808 [label="C_out", shape=none];
    interface_6_in_0x5581660a8830 [label="H", shape=none];
    interface_6_in_0x5581660a8858 [label="H", shape=none];
}
interface_0_out_0x5581660a87e0 -> interface_6_in_0x5581660a87e0;
interface_0_out_0x5581660a8808 -> interface_6_in_0x5581660a8808;
interface_0_out_0x5581660a8830 -> interface_6_in_0x5581660a8830;
interface_0_out_0x5581660a8858 -> interface_6_in_0x5581660a8858;

}

"""
class kernel_generated_0(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([24, 9, 14]),
			torch.randn([24, 2, 14]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]
		in_2 = self.weights[1]

		# Perform contraction.
		t_3 = torch.einsum("ljmn, jki -> lmnki", in_0, in_2)

		# No contraction needed.
		t_4 = t_3

		# [H]@Unfoldcb2b4caf443f161e -> [H]@Merge0bce4580e08cd69c, [k_1^2]@Share26ce4977369008e4
		t_4 = torch.reshape(t_4, (128, 112, 112, 28, ))
		t_4 = torch.nn.functional.unfold(t_4, (9, 1, ), padding=(4, 0, ))
		t_4 = torch.reshape(t_4, (128, 112, 9, 112, 2, 14, ))

		# [H]@Merge0bce4580e08cd69c, [s]@Merge0bce4580e08cd69d -> [s*H]@Shift8a9f243357a7f717
		t_4 = torch.reshape(t_4, (128, 112, 9, 224, 14, ))

		# [s*H]@Shift8a9f243357a7f717 -> [s*H]@Split511946b410b86996
		t_4 = torch.roll(t_4, self.shift_direction, 3)

		# [s*H]@Split511946b410b86996 -> [H]@Iteratorb0a1def4ad5784ec, [s]@Reduced95c644a3c072d9a
		t_4 = torch.reshape(t_4, (128, 112, 9, 112, 2, 14, ))

		# [s]@Reduce
		t_4 = torch.sum(t_4, dim=(4, ))

		# Perform contraction.
		t_5 = torch.einsum("lmjni, kji -> lkmn", t_4, in_1)

		# No need to crop the output tensor.
		y = t_5

		return y

class kernel_generated_1(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([96, 9, 14]),
			torch.randn([24, 2, 14]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]
		in_2 = self.weights[1]

		# Perform contraction.
		t_3 = torch.einsum("ljmn, jki -> lmnki", in_0, in_2)

		# No contraction needed.
		t_4 = t_3

		# [H]@Unfoldcb2b4caf443f161e -> [H]@Merge0bce4580e08cd69c, [k_1^2]@Share26ce4977369008e4
		t_4 = torch.reshape(t_4, (128, 56, 56, 28, ))
		t_4 = torch.nn.functional.unfold(t_4, (9, 1, ), padding=(4, 0, ))
		t_4 = torch.reshape(t_4, (128, 56, 9, 56, 2, 14, ))

		# [H]@Merge0bce4580e08cd69c, [s]@Merge0bce4580e08cd69d -> [s*H]@Shift8a9f243357a7f717
		t_4 = torch.reshape(t_4, (128, 56, 9, 112, 14, ))

		# [s*H]@Shift8a9f243357a7f717 -> [s*H]@Split511946b410b86996
		t_4 = torch.roll(t_4, self.shift_direction, 3)

		# [s*H]@Split511946b410b86996 -> [H]@Iteratorb0a1def4ad5784ec, [s]@Reduced95c644a3c072d9a
		t_4 = torch.reshape(t_4, (128, 56, 9, 56, 2, 14, ))

		# [s]@Reduce
		t_4 = torch.sum(t_4, dim=(4, ))

		# Perform contraction.
		t_5 = torch.einsum("lmjni, kji -> lkmn", t_4, in_1)

		# No need to crop the output tensor.
		y = t_5

		return y

class kernel_generated_2(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([192, 9, 14]),
			torch.randn([48, 2, 14]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]
		in_2 = self.weights[1]

		# Perform contraction.
		t_3 = torch.einsum("ljmn, jki -> lmnki", in_0, in_2)

		# No contraction needed.
		t_4 = t_3

		# [H]@Unfoldcb2b4caf443f161e -> [H]@Merge0bce4580e08cd69c, [k_1^2]@Share26ce4977369008e4
		t_4 = torch.reshape(t_4, (128, 56, 56, 28, ))
		t_4 = torch.nn.functional.unfold(t_4, (9, 1, ), padding=(4, 0, ))
		t_4 = torch.reshape(t_4, (128, 56, 9, 56, 2, 14, ))

		# [H]@Merge0bce4580e08cd69c, [s]@Merge0bce4580e08cd69d -> [s*H]@Shift8a9f243357a7f717
		t_4 = torch.reshape(t_4, (128, 56, 9, 112, 14, ))

		# [s*H]@Shift8a9f243357a7f717 -> [s*H]@Split511946b410b86996
		t_4 = torch.roll(t_4, self.shift_direction, 3)

		# [s*H]@Split511946b410b86996 -> [H]@Iteratorb0a1def4ad5784ec, [s]@Reduced95c644a3c072d9a
		t_4 = torch.reshape(t_4, (128, 56, 9, 56, 2, 14, ))

		# [s]@Reduce
		t_4 = torch.sum(t_4, dim=(4, ))

		# Perform contraction.
		t_5 = torch.einsum("lmjni, kji -> lkmn", t_4, in_1)

		# No need to crop the output tensor.
		y = t_5

		return y

class kernel_generated_3(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([192, 9, 14]),
			torch.randn([48, 2, 14]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]
		in_2 = self.weights[1]

		# Perform contraction.
		t_3 = torch.einsum("ljmn, jki -> lmnki", in_0, in_2)

		# No contraction needed.
		t_4 = t_3

		# [H]@Unfoldcb2b4caf443f161e -> [H]@Merge0bce4580e08cd69c, [k_1^2]@Share26ce4977369008e4
		t_4 = torch.reshape(t_4, (128, 28, 28, 28, ))
		t_4 = torch.nn.functional.unfold(t_4, (9, 1, ), padding=(4, 0, ))
		t_4 = torch.reshape(t_4, (128, 28, 9, 28, 2, 14, ))

		# [H]@Merge0bce4580e08cd69c, [s]@Merge0bce4580e08cd69d -> [s*H]@Shift8a9f243357a7f717
		t_4 = torch.reshape(t_4, (128, 28, 9, 56, 14, ))

		# [s*H]@Shift8a9f243357a7f717 -> [s*H]@Split511946b410b86996
		t_4 = torch.roll(t_4, self.shift_direction, 3)

		# [s*H]@Split511946b410b86996 -> [H]@Iteratorb0a1def4ad5784ec, [s]@Reduced95c644a3c072d9a
		t_4 = torch.reshape(t_4, (128, 28, 9, 28, 2, 14, ))

		# [s]@Reduce
		t_4 = torch.sum(t_4, dim=(4, ))

		# Perform contraction.
		t_5 = torch.einsum("lmjni, kji -> lkmn", t_4, in_1)

		# No need to crop the output tensor.
		y = t_5

		return y

class kernel_generated_4(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([256, 9, 14]),
			torch.randn([64, 2, 14]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]
		in_2 = self.weights[1]

		# Perform contraction.
		t_3 = torch.einsum("ljmn, jki -> lmnki", in_0, in_2)

		# No contraction needed.
		t_4 = t_3

		# [H]@Unfoldcb2b4caf443f161e -> [H]@Merge0bce4580e08cd69c, [k_1^2]@Share26ce4977369008e4
		t_4 = torch.reshape(t_4, (128, 28, 28, 28, ))
		t_4 = torch.nn.functional.unfold(t_4, (9, 1, ), padding=(4, 0, ))
		t_4 = torch.reshape(t_4, (128, 28, 9, 28, 2, 14, ))

		# [H]@Merge0bce4580e08cd69c, [s]@Merge0bce4580e08cd69d -> [s*H]@Shift8a9f243357a7f717
		t_4 = torch.reshape(t_4, (128, 28, 9, 56, 14, ))

		# [s*H]@Shift8a9f243357a7f717 -> [s*H]@Split511946b410b86996
		t_4 = torch.roll(t_4, self.shift_direction, 3)

		# [s*H]@Split511946b410b86996 -> [H]@Iteratorb0a1def4ad5784ec, [s]@Reduced95c644a3c072d9a
		t_4 = torch.reshape(t_4, (128, 28, 9, 28, 2, 14, ))

		# [s]@Reduce
		t_4 = torch.sum(t_4, dim=(4, ))

		# Perform contraction.
		t_5 = torch.einsum("lmjni, kji -> lkmn", t_4, in_1)

		# No need to crop the output tensor.
		y = t_5

		return y

