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
        interface_0_out_0x5581660a87e0 [label="N", shape=none];
        interface_0_out_0x5581660a8808 [label="C_out", shape=none];
        interface_0_out_0x5581660a8830 [label="H", shape=none];
        interface_0_out_0x5581660a8858 [label="H", shape=none];
    }
    {
        rank = same;
        interface_0_out_0x5581660a87e0;
        interface_0_out_0x5581660a8808;
        interface_0_out_0x5581660a8830;
        interface_0_out_0x5581660a8858;
    }
    // Input 0.
    subgraph cluster_subgraph_0_in_0 {
        label = "";
        interface_0_in_0x5581660a87e0 [label="N", shape=none];
        interface_0_in_0x5581660a8808 [label="C_out", shape=none];
        interface_0_in_0x7fcf880062b0 [label="s^-1*H", shape=none];
        interface_0_in_0x7fcf880062c8 [label="s", shape=none];
        interface_0_in_0x7fcf7c003e90 [label="H", shape=none];
    }
    {
        rank = same;
        interface_0_in_0x5581660a87e0;
        interface_0_in_0x5581660a8808;
        interface_0_in_0x7fcf880062b0;
        interface_0_in_0x7fcf880062c8;
        interface_0_in_0x7fcf7c003e90;
    }
    // Op's.
    op_0x7fcf7c003e70 [label="Shift"];
    op_0x7fcf88006270 [label="Merge"];
    // Dimension's.
    interface_0_in_0x5581660a87e0 -> interface_0_out_0x5581660a87e0 [label="N"];
    interface_0_in_0x5581660a8808 -> interface_0_out_0x5581660a8808 [label="C_out"];
    op_0x7fcf88006270 -> interface_0_out_0x5581660a8830 [label="H"];
    op_0x7fcf7c003e70 -> interface_0_out_0x5581660a8858 [label="H"];
    interface_0_in_0x7fcf7c003e90 -> op_0x7fcf7c003e70 [label="H"];
    interface_0_in_0x7fcf880062b0 -> op_0x7fcf88006270 [label="s^-1*H"];
    interface_0_in_0x7fcf880062c8 -> op_0x7fcf88006270 [label="s"];
}

// Stage tensor.
subgraph cluster_subgraph_1 {
    label = "Subgraph 1";
    // Reductions.
    reduce_0x7fc7f0005e70 [label="Sum", shape=box];
    reduce_0x7fc7f0001998 [label="Sum", shape=box];
    // Output.
    subgraph cluster_subgraph_1_out {
        label = "";
        interface_1_out_0x5581660a87e0 [label="N", shape=none];
        interface_1_out_0x5581660a8808 [label="C_out", shape=none];
        interface_1_out_0x7fcf880062b0 [label="s^-1*H", shape=none];
        interface_1_out_0x7fcf880062c8 [label="s", shape=none];
        interface_1_out_0x7fcf7c003e90 [label="H", shape=none];
    }
    {
        rank = same;
        reduce_0x7fc7f0005e70;
        reduce_0x7fc7f0001998;
        interface_1_out_0x5581660a87e0;
        interface_1_out_0x5581660a8808;
        interface_1_out_0x7fcf880062b0;
        interface_1_out_0x7fcf880062c8;
        interface_1_out_0x7fcf7c003e90;
    }
    // Input 0.
    subgraph cluster_subgraph_1_in_0 {
        label = "";
        interface_1_in_0x5581660a87e0 [label="N", shape=none];
        interface_1_in_0x7fcf840040b0 [label="C_in", shape=none];
        interface_1_in_0x7fcf84004330 [label="k_1", shape=none];
        interface_1_in_0x7fcf880062b0 [label="s^-1*H", shape=none];
        interface_1_in_0x7fcf880062c8 [label="s", shape=none];
        interface_1_in_0x7fcf7c003e90 [label="H", shape=none];
    }
    // Input 1.
    subgraph cluster_subgraph_1_in_1 {
        label = "";
        interface_1_in_0x7fcf84003f38 [label="C_out", shape=none];
        interface_1_in_0x7fcf840040c8 [label="C_in", shape=none];
        interface_1_in_0x7fcf84004348 [label="k_1", shape=none];
    }
    {
        rank = same;
        interface_1_in_0x5581660a87e0;
        interface_1_in_0x7fcf840040b0;
        interface_1_in_0x7fcf84004330;
        interface_1_in_0x7fcf880062b0;
        interface_1_in_0x7fcf880062c8;
        interface_1_in_0x7fcf7c003e90;
        interface_1_in_0x7fcf84003f38;
        interface_1_in_0x7fcf840040c8;
        interface_1_in_0x7fcf84004348;
    }
    // Op's.
    op_0x7fcf84003f00 [label="Share"];
    op_0x7fcf84004090 [label="Share"];
    op_0x7fcf84004310 [label="Share"];
    op_0x7fcf84004638 [label="Expand"];
    // Dimension's.
    interface_1_in_0x5581660a87e0 -> interface_1_out_0x5581660a87e0 [label="N"];
    op_0x7fcf84003f00 -> interface_1_out_0x5581660a8808 [label="C_out"];
    op_0x7fcf84004310 -> reduce_0x7fc7f0001998 [label="k_1"];
    op_0x7fcf84004090 -> reduce_0x7fc7f0005e70 [label="C_in"];
    interface_1_in_0x7fcf7c003e90 -> interface_1_out_0x7fcf7c003e90 [label="H"];
    op_0x7fcf84004638 -> op_0x7fcf84003f00 [label="C_out"];
    interface_1_in_0x7fcf84003f38 -> op_0x7fcf84003f00 [label="C_out"];
    interface_1_in_0x7fcf840040b0 -> op_0x7fcf84004090 [label="C_in"];
    interface_1_in_0x7fcf840040c8 -> op_0x7fcf84004090 [label="C_in"];
    interface_1_in_0x7fcf84004330 -> op_0x7fcf84004310 [label="k_1"];
    interface_1_in_0x7fcf84004348 -> op_0x7fcf84004310 [label="k_1"];
    interface_1_in_0x7fcf880062b0 -> interface_1_out_0x7fcf880062b0 [label="s^-1*H"];
    interface_1_in_0x7fcf880062c8 -> interface_1_out_0x7fcf880062c8 [label="s"];
}

// Stage tensor.
subgraph cluster_subgraph_2 {
    label = "Subgraph 2";
    // Reductions.
    // Output.
    subgraph cluster_subgraph_2_out {
        label = "";
        interface_2_out_0x5581660a87e0 [label="N", shape=none];
        interface_2_out_0x7fcf840040b0 [label="C_in", shape=none];
        interface_2_out_0x7fcf84004330 [label="k_1", shape=none];
        interface_2_out_0x7fcf880062b0 [label="s^-1*H", shape=none];
        interface_2_out_0x7fcf880062c8 [label="s", shape=none];
        interface_2_out_0x7fcf7c003e90 [label="H", shape=none];
    }
    {
        rank = same;
        interface_2_out_0x5581660a87e0;
        interface_2_out_0x7fcf840040b0;
        interface_2_out_0x7fcf84004330;
        interface_2_out_0x7fcf880062b0;
        interface_2_out_0x7fcf880062c8;
        interface_2_out_0x7fcf7c003e90;
    }
    // Input 0.
    subgraph cluster_subgraph_2_in_0 {
        label = "";
        interface_2_in_0x5581660a87e0 [label="N", shape=none];
        interface_2_in_0x7fcf840040b0 [label="C_in", shape=none];
        interface_2_in_0x7fcb94099440 [label="H", shape=none];
        interface_2_in_0x7fcf7c003e90 [label="H", shape=none];
    }
    {
        rank = same;
        interface_2_in_0x5581660a87e0;
        interface_2_in_0x7fcf840040b0;
        interface_2_in_0x7fcb94099440;
        interface_2_in_0x7fcf7c003e90;
    }
    // Op's.
    op_0x7fcb94099400 [label="Split"];
    op_0x7fcc34032a80 [label="Unfold"];
    op_0x7fce780304d0 [label="Shift"];
    // Dimension's.
    interface_2_in_0x5581660a87e0 -> interface_2_out_0x5581660a87e0 [label="N"];
    interface_2_in_0x7fcb94099440 -> op_0x7fcb94099400 [label="H"];
    op_0x7fce780304d0 -> op_0x7fcc34032a80 [label="s^-1*H"];
    op_0x7fcb94099400 -> op_0x7fce780304d0 [label="s^-1*H"];
    interface_2_in_0x7fcf7c003e90 -> interface_2_out_0x7fcf7c003e90 [label="H"];
    interface_2_in_0x7fcf840040b0 -> interface_2_out_0x7fcf840040b0 [label="C_in"];
    op_0x7fcc34032a80 -> interface_2_out_0x7fcf84004330 [label="k_1"];
    op_0x7fcc34032a80 -> interface_2_out_0x7fcf880062b0 [label="s^-1*H"];
    op_0x7fcb94099400 -> interface_2_out_0x7fcf880062c8 [label="s"];
}

// Input tensor.
subgraph cluster_subgraph_3 {
    label = "Input 0";
    interface_3_out_0x5581660a87e0 [label="N", shape=none];
    interface_3_out_0x7fcf840040b0 [label="C_in", shape=none];
    interface_3_out_0x7fcb94099440 [label="H", shape=none];
    interface_3_out_0x7fcf7c003e90 [label="H", shape=none];
}

interface_3_out_0x5581660a87e0 -> interface_2_in_0x5581660a87e0;
interface_3_out_0x7fcf840040b0 -> interface_2_in_0x7fcf840040b0;
interface_3_out_0x7fcb94099440 -> interface_2_in_0x7fcb94099440;
interface_3_out_0x7fcf7c003e90 -> interface_2_in_0x7fcf7c003e90;

interface_2_out_0x5581660a87e0 -> interface_1_in_0x5581660a87e0;
interface_2_out_0x7fcf840040b0 -> interface_1_in_0x7fcf840040b0;
interface_2_out_0x7fcf84004330 -> interface_1_in_0x7fcf84004330;
interface_2_out_0x7fcf880062b0 -> interface_1_in_0x7fcf880062b0;
interface_2_out_0x7fcf880062c8 -> interface_1_in_0x7fcf880062c8;
interface_2_out_0x7fcf7c003e90 -> interface_1_in_0x7fcf7c003e90;

// Input tensor.
subgraph cluster_subgraph_4 {
    label = "Input 1";
    interface_4_out_0x7fcf84003f38 [label="C_out", shape=none];
    interface_4_out_0x7fcf840040c8 [label="C_in", shape=none];
    interface_4_out_0x7fcf84004348 [label="k_1", shape=none];
}

interface_4_out_0x7fcf84003f38 -> interface_1_in_0x7fcf84003f38;
interface_4_out_0x7fcf840040c8 -> interface_1_in_0x7fcf840040c8;
interface_4_out_0x7fcf84004348 -> interface_1_in_0x7fcf84004348;

interface_1_out_0x5581660a87e0 -> interface_0_in_0x5581660a87e0;
interface_1_out_0x5581660a8808 -> interface_0_in_0x5581660a8808;
interface_1_out_0x7fcf880062b0 -> interface_0_in_0x7fcf880062b0;
interface_1_out_0x7fcf880062c8 -> interface_0_in_0x7fcf880062c8;
interface_1_out_0x7fcf7c003e90 -> interface_0_in_0x7fcf7c003e90;

{
    rank = same;
    interface_3_out_0x5581660a87e0;
    interface_3_out_0x7fcf840040b0;
    interface_3_out_0x7fcb94099440;
    interface_3_out_0x7fcf7c003e90;
    interface_4_out_0x7fcf84003f38;
    interface_4_out_0x7fcf840040c8;
    interface_4_out_0x7fcf84004348;
}
subgraph cluster_subgraph_output {
    label = "Output";
    interface_5_in_0x5581660a87e0 [label="N", shape=none];
    interface_5_in_0x5581660a8808 [label="C_out", shape=none];
    interface_5_in_0x5581660a8830 [label="H", shape=none];
    interface_5_in_0x5581660a8858 [label="H", shape=none];
}
interface_0_out_0x5581660a87e0 -> interface_5_in_0x5581660a87e0;
interface_0_out_0x5581660a8808 -> interface_5_in_0x5581660a8808;
interface_0_out_0x5581660a8830 -> interface_5_in_0x5581660a8830;
interface_0_out_0x5581660a8858 -> interface_5_in_0x5581660a8858;

}

"""
class kernel_generated_0(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([24, 24, 3]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]

		# No contraction needed.
		t_2 = in_0

		# [H]@Split14839c94d488f758 -> [s^-1*H]@Shiftcdaaca31e176569f, [s]@Merge3e25d6fc76d0e079
		t_2 = torch.reshape(t_2, (128, 24, 56, 2, 112, ))

		# [s^-1*H]@Shiftcdaaca31e176569f -> [s^-1*H]@Unfold0a04b4b1bf080a1e
		t_2 = torch.roll(t_2, self.shift_direction, 2)

		# [s^-1*H]@Unfold0a04b4b1bf080a1e -> [s^-1*H]@Merge3e25d6fc76d0e07a, [k_1]@Share26cfa48d169008e4
		t_2 = torch.reshape(t_2, (128, 24, 56, 224, ))
		t_2 = torch.nn.functional.unfold(t_2, (3, 1, ), padding=(1, 0, ))
		t_2 = torch.reshape(t_2, (128, 24, 3, 56, 2, 112, ))

		# Perform contraction.
		t_3 = torch.einsum("ljknom, ijk -> linom", t_2, in_1)

		# No contraction needed.
		t_4 = t_3

		# [s^-1*H]@Merge3e25d6fc76d0e07a, [s]@Merge3e25d6fc76d0e079 -> [H]@Iterator96123ba3184da39c
		t_4 = torch.reshape(t_4, (128, 24, 112, 112, ))

		# [H]@Shift6b179c72f0c6dbad -> [H]@Iteratorb0a1def4ad5784ec
		t_4 = torch.roll(t_4, self.shift_direction, 3)

		# No need to crop the output tensor.
		y = t_4

		return y

class kernel_generated_1(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([96, 24, 3]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]

		# No contraction needed.
		t_2 = in_0

		# [H]@Split14839c94d488f758 -> [s^-1*H]@Shiftcdaaca31e176569f, [s]@Merge3e25d6fc76d0e079
		t_2 = torch.reshape(t_2, (128, 24, 28, 2, 56, ))

		# [s^-1*H]@Shiftcdaaca31e176569f -> [s^-1*H]@Unfold0a04b4b1bf080a1e
		t_2 = torch.roll(t_2, self.shift_direction, 2)

		# [s^-1*H]@Unfold0a04b4b1bf080a1e -> [s^-1*H]@Merge3e25d6fc76d0e07a, [k_1]@Share26cfa48d169008e4
		t_2 = torch.reshape(t_2, (128, 24, 28, 112, ))
		t_2 = torch.nn.functional.unfold(t_2, (3, 1, ), padding=(1, 0, ))
		t_2 = torch.reshape(t_2, (128, 24, 3, 28, 2, 56, ))

		# Perform contraction.
		t_3 = torch.einsum("ljknom, ijk -> linom", t_2, in_1)

		# No contraction needed.
		t_4 = t_3

		# [s^-1*H]@Merge3e25d6fc76d0e07a, [s]@Merge3e25d6fc76d0e079 -> [H]@Iterator96123ba3184da39c
		t_4 = torch.reshape(t_4, (128, 96, 56, 56, ))

		# [H]@Shift6b179c72f0c6dbad -> [H]@Iteratorb0a1def4ad5784ec
		t_4 = torch.roll(t_4, self.shift_direction, 3)

		# No need to crop the output tensor.
		y = t_4

		return y

class kernel_generated_2(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([192, 48, 3]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]

		# No contraction needed.
		t_2 = in_0

		# [H]@Split14839c94d488f758 -> [s^-1*H]@Shiftcdaaca31e176569f, [s]@Merge3e25d6fc76d0e079
		t_2 = torch.reshape(t_2, (128, 48, 28, 2, 56, ))

		# [s^-1*H]@Shiftcdaaca31e176569f -> [s^-1*H]@Unfold0a04b4b1bf080a1e
		t_2 = torch.roll(t_2, self.shift_direction, 2)

		# [s^-1*H]@Unfold0a04b4b1bf080a1e -> [s^-1*H]@Merge3e25d6fc76d0e07a, [k_1]@Share26cfa48d169008e4
		t_2 = torch.reshape(t_2, (128, 48, 28, 112, ))
		t_2 = torch.nn.functional.unfold(t_2, (3, 1, ), padding=(1, 0, ))
		t_2 = torch.reshape(t_2, (128, 48, 3, 28, 2, 56, ))

		# Perform contraction.
		t_3 = torch.einsum("ljknom, ijk -> linom", t_2, in_1)

		# No contraction needed.
		t_4 = t_3

		# [s^-1*H]@Merge3e25d6fc76d0e07a, [s]@Merge3e25d6fc76d0e079 -> [H]@Iterator96123ba3184da39c
		t_4 = torch.reshape(t_4, (128, 192, 56, 56, ))

		# [H]@Shift6b179c72f0c6dbad -> [H]@Iteratorb0a1def4ad5784ec
		t_4 = torch.roll(t_4, self.shift_direction, 3)

		# No need to crop the output tensor.
		y = t_4

		return y

class kernel_generated_3(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([192, 48, 3]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]

		# No contraction needed.
		t_2 = in_0

		# [H]@Split14839c94d488f758 -> [s^-1*H]@Shiftcdaaca31e176569f, [s]@Merge3e25d6fc76d0e079
		t_2 = torch.reshape(t_2, (128, 48, 14, 2, 28, ))

		# [s^-1*H]@Shiftcdaaca31e176569f -> [s^-1*H]@Unfold0a04b4b1bf080a1e
		t_2 = torch.roll(t_2, self.shift_direction, 2)

		# [s^-1*H]@Unfold0a04b4b1bf080a1e -> [s^-1*H]@Merge3e25d6fc76d0e07a, [k_1]@Share26cfa48d169008e4
		t_2 = torch.reshape(t_2, (128, 48, 14, 56, ))
		t_2 = torch.nn.functional.unfold(t_2, (3, 1, ), padding=(1, 0, ))
		t_2 = torch.reshape(t_2, (128, 48, 3, 14, 2, 28, ))

		# Perform contraction.
		t_3 = torch.einsum("ljknom, ijk -> linom", t_2, in_1)

		# No contraction needed.
		t_4 = t_3

		# [s^-1*H]@Merge3e25d6fc76d0e07a, [s]@Merge3e25d6fc76d0e079 -> [H]@Iterator96123ba3184da39c
		t_4 = torch.reshape(t_4, (128, 192, 28, 28, ))

		# [H]@Shift6b179c72f0c6dbad -> [H]@Iteratorb0a1def4ad5784ec
		t_4 = torch.roll(t_4, self.shift_direction, 3)

		# No need to crop the output tensor.
		y = t_4

		return y

class kernel_generated_4(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([256, 64, 3]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]

		# No contraction needed.
		t_2 = in_0

		# [H]@Split14839c94d488f758 -> [s^-1*H]@Shiftcdaaca31e176569f, [s]@Merge3e25d6fc76d0e079
		t_2 = torch.reshape(t_2, (128, 64, 14, 2, 28, ))

		# [s^-1*H]@Shiftcdaaca31e176569f -> [s^-1*H]@Unfold0a04b4b1bf080a1e
		t_2 = torch.roll(t_2, self.shift_direction, 2)

		# [s^-1*H]@Unfold0a04b4b1bf080a1e -> [s^-1*H]@Merge3e25d6fc76d0e07a, [k_1]@Share26cfa48d169008e4
		t_2 = torch.reshape(t_2, (128, 64, 14, 56, ))
		t_2 = torch.nn.functional.unfold(t_2, (3, 1, ), padding=(1, 0, ))
		t_2 = torch.reshape(t_2, (128, 64, 3, 14, 2, 28, ))

		# Perform contraction.
		t_3 = torch.einsum("ljknom, ijk -> linom", t_2, in_1)

		# No contraction needed.
		t_4 = t_3

		# [s^-1*H]@Merge3e25d6fc76d0e07a, [s]@Merge3e25d6fc76d0e079 -> [H]@Iterator96123ba3184da39c
		t_4 = torch.reshape(t_4, (128, 256, 28, 28, ))

		# [H]@Shift6b179c72f0c6dbad -> [H]@Iteratorb0a1def4ad5784ec
		t_4 = torch.roll(t_4, self.shift_direction, 3)

		# No need to crop the output tensor.
		y = t_4

		return y

