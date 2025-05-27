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
        interface_0_in_0x55b7501bb040 [label="s", shape=none];
        interface_0_in_0x55b7501bb058 [label="s^-1*C_out", shape=none];
        interface_0_in_0x55b7501b6ea0 [label="H", shape=none];
        interface_0_in_0x55b7386312f8 [label="H", shape=none];
    }
    {
        rank = same;
        interface_0_in_0x55b738631280;
        interface_0_in_0x55b7501bb040;
        interface_0_in_0x55b7501bb058;
        interface_0_in_0x55b7501b6ea0;
        interface_0_in_0x55b7386312f8;
    }
    // Op's.
    op_0x55b7501b6e80 [label="Shift"];
    op_0x55b7501bb000 [label="Merge"];
    // Dimension's.
    interface_0_in_0x55b738631280 -> interface_0_out_0x55b738631280 [label="N"];
    op_0x55b7501bb000 -> interface_0_out_0x55b7386312a8 [label="C_out"];
    op_0x55b7501b6e80 -> interface_0_out_0x55b7386312d0 [label="H"];
    interface_0_in_0x55b7386312f8 -> interface_0_out_0x55b7386312f8 [label="H"];
    interface_0_in_0x55b7501b6ea0 -> op_0x55b7501b6e80 [label="H"];
    interface_0_in_0x55b7501bb040 -> op_0x55b7501bb000 [label="s"];
    interface_0_in_0x55b7501bb058 -> op_0x55b7501bb000 [label="s^-1*C_out"];
}

// Stage tensor.
subgraph cluster_subgraph_1 {
    label = "Subgraph 1";
    // Reductions.
    reduce_0x7f6f600077d8 [label="Sum", shape=box];
    reduce_0x7f6f60003a98 [label="Sum", shape=box];
    // Output.
    subgraph cluster_subgraph_1_out {
        label = "";
        interface_1_out_0x55b738631280 [label="N", shape=none];
        interface_1_out_0x55b7501bb040 [label="s", shape=none];
        interface_1_out_0x55b7501bb058 [label="s^-1*C_out", shape=none];
        interface_1_out_0x55b7501b6ea0 [label="H", shape=none];
        interface_1_out_0x55b7386312f8 [label="H", shape=none];
    }
    {
        rank = same;
        reduce_0x7f6f600077d8;
        reduce_0x7f6f60003a98;
        interface_1_out_0x55b738631280;
        interface_1_out_0x55b7501bb040;
        interface_1_out_0x55b7501bb058;
        interface_1_out_0x55b7501b6ea0;
        interface_1_out_0x55b7386312f8;
    }
    // Input 0.
    subgraph cluster_subgraph_1_in_0 {
        label = "";
        interface_1_in_0x55b738631280 [label="N", shape=none];
        interface_1_in_0x55b7501bb040 [label="s", shape=none];
        interface_1_in_0x55b7501f5ba0 [label="s^-1*C_in", shape=none];
        interface_1_in_0x55b7501b6ea0 [label="H", shape=none];
        interface_1_in_0x55b7501b6290 [label="k_1", shape=none];
        interface_1_in_0x55b7386312f8 [label="H", shape=none];
    }
    // Input 1.
    subgraph cluster_subgraph_1_in_1 {
        label = "";
        interface_1_in_0x55b7501f5bb8 [label="s^-1*C_in", shape=none];
        interface_1_in_0x55b7501f5c08 [label="s^-1*C_out", shape=none];
        interface_1_in_0x55b7501b62a8 [label="k_1", shape=none];
    }
    {
        rank = same;
        interface_1_in_0x55b738631280;
        interface_1_in_0x55b7501bb040;
        interface_1_in_0x55b7501f5ba0;
        interface_1_in_0x55b7501b6ea0;
        interface_1_in_0x55b7501b6290;
        interface_1_in_0x55b7386312f8;
        interface_1_in_0x55b7501f5bb8;
        interface_1_in_0x55b7501f5c08;
        interface_1_in_0x55b7501b62a8;
    }
    // Op's.
    op_0x55b7501b6270 [label="Share"];
    op_0x55b7501b66f8 [label="Expand"];
    op_0x55b7501f5b80 [label="Share"];
    op_0x55b7501f5bd0 [label="Share"];
    // Dimension's.
    interface_1_in_0x55b738631280 -> interface_1_out_0x55b738631280 [label="N"];
    interface_1_in_0x55b7386312f8 -> interface_1_out_0x55b7386312f8 [label="H"];
    interface_1_in_0x55b7501b6290 -> op_0x55b7501b6270 [label="k_1"];
    interface_1_in_0x55b7501b62a8 -> op_0x55b7501b6270 [label="k_1"];
    interface_1_in_0x55b7501b6ea0 -> interface_1_out_0x55b7501b6ea0 [label="H"];
    interface_1_in_0x55b7501bb040 -> interface_1_out_0x55b7501bb040 [label="s"];
    op_0x55b7501f5bd0 -> interface_1_out_0x55b7501bb058 [label="s^-1*C_out"];
    interface_1_in_0x55b7501f5ba0 -> op_0x55b7501f5b80 [label="s^-1*C_in"];
    interface_1_in_0x55b7501f5bb8 -> op_0x55b7501f5b80 [label="s^-1*C_in"];
    op_0x55b7501b66f8 -> op_0x55b7501f5bd0 [label="s^-1*C_out"];
    interface_1_in_0x55b7501f5c08 -> op_0x55b7501f5bd0 [label="s^-1*C_out"];
    op_0x55b7501b6270 -> reduce_0x7f6f60003a98 [label="k_1"];
    op_0x55b7501f5b80 -> reduce_0x7f6f600077d8 [label="s^-1*C_in"];
}

// Stage tensor.
subgraph cluster_subgraph_2 {
    label = "Subgraph 2";
    // Reductions.
    // Output.
    subgraph cluster_subgraph_2_out {
        label = "";
        interface_2_out_0x55b738631280 [label="N", shape=none];
        interface_2_out_0x55b7501bb040 [label="s", shape=none];
        interface_2_out_0x55b7501f5ba0 [label="s^-1*C_in", shape=none];
        interface_2_out_0x55b7501b6ea0 [label="H", shape=none];
        interface_2_out_0x55b7501b6290 [label="k_1", shape=none];
        interface_2_out_0x55b7386312f8 [label="H", shape=none];
    }
    {
        rank = same;
        interface_2_out_0x55b738631280;
        interface_2_out_0x55b7501bb040;
        interface_2_out_0x55b7501f5ba0;
        interface_2_out_0x55b7501b6ea0;
        interface_2_out_0x55b7501b6290;
        interface_2_out_0x55b7386312f8;
    }
    // Input 0.
    subgraph cluster_subgraph_2_in_0 {
        label = "";
        interface_2_in_0x55b738631280 [label="N", shape=none];
        interface_2_in_0x55b7501f4790 [label="C_in", shape=none];
        interface_2_in_0x55b7501b6ea0 [label="H", shape=none];
        interface_2_in_0x55b7501b6f60 [label="H", shape=none];
    }
    {
        rank = same;
        interface_2_in_0x55b738631280;
        interface_2_in_0x55b7501f4790;
        interface_2_in_0x55b7501b6ea0;
        interface_2_in_0x55b7501b6f60;
    }
    // Op's.
    op_0x55b7501b6f40 [label="Shift"];
    op_0x55b7501d45c0 [label="Unfold"];
    op_0x55b7501f4750 [label="Split"];
    // Dimension's.
    interface_2_in_0x55b738631280 -> interface_2_out_0x55b738631280 [label="N"];
    op_0x55b7501d45c0 -> interface_2_out_0x55b7386312f8 [label="H"];
    op_0x55b7501d45c0 -> interface_2_out_0x55b7501b6290 [label="k_1"];
    interface_2_in_0x55b7501b6ea0 -> interface_2_out_0x55b7501b6ea0 [label="H"];
    interface_2_in_0x55b7501b6f60 -> op_0x55b7501b6f40 [label="H"];
    op_0x55b7501f4750 -> interface_2_out_0x55b7501bb040 [label="s"];
    op_0x55b7501b6f40 -> op_0x55b7501d45c0 [label="H"];
    interface_2_in_0x55b7501f4790 -> op_0x55b7501f4750 [label="C_in"];
    op_0x55b7501f4750 -> interface_2_out_0x55b7501f5ba0 [label="s^-1*C_in"];
}

// Input tensor.
subgraph cluster_subgraph_3 {
    label = "Input 0";
    interface_3_out_0x55b738631280 [label="N", shape=none];
    interface_3_out_0x55b7501f4790 [label="C_in", shape=none];
    interface_3_out_0x55b7501b6ea0 [label="H", shape=none];
    interface_3_out_0x55b7501b6f60 [label="H", shape=none];
}

interface_3_out_0x55b738631280 -> interface_2_in_0x55b738631280;
interface_3_out_0x55b7501f4790 -> interface_2_in_0x55b7501f4790;
interface_3_out_0x55b7501b6ea0 -> interface_2_in_0x55b7501b6ea0;
interface_3_out_0x55b7501b6f60 -> interface_2_in_0x55b7501b6f60;

interface_2_out_0x55b738631280 -> interface_1_in_0x55b738631280;
interface_2_out_0x55b7501bb040 -> interface_1_in_0x55b7501bb040;
interface_2_out_0x55b7501f5ba0 -> interface_1_in_0x55b7501f5ba0;
interface_2_out_0x55b7501b6ea0 -> interface_1_in_0x55b7501b6ea0;
interface_2_out_0x55b7501b6290 -> interface_1_in_0x55b7501b6290;
interface_2_out_0x55b7386312f8 -> interface_1_in_0x55b7386312f8;

// Input tensor.
subgraph cluster_subgraph_4 {
    label = "Input 1";
    interface_4_out_0x55b7501f5bb8 [label="s^-1*C_in", shape=none];
    interface_4_out_0x55b7501f5c08 [label="s^-1*C_out", shape=none];
    interface_4_out_0x55b7501b62a8 [label="k_1", shape=none];
}

interface_4_out_0x55b7501f5bb8 -> interface_1_in_0x55b7501f5bb8;
interface_4_out_0x55b7501f5c08 -> interface_1_in_0x55b7501f5c08;
interface_4_out_0x55b7501b62a8 -> interface_1_in_0x55b7501b62a8;

interface_1_out_0x55b738631280 -> interface_0_in_0x55b738631280;
interface_1_out_0x55b7501bb040 -> interface_0_in_0x55b7501bb040;
interface_1_out_0x55b7501bb058 -> interface_0_in_0x55b7501bb058;
interface_1_out_0x55b7501b6ea0 -> interface_0_in_0x55b7501b6ea0;
interface_1_out_0x55b7386312f8 -> interface_0_in_0x55b7386312f8;

{
    rank = same;
    interface_3_out_0x55b738631280;
    interface_3_out_0x55b7501f4790;
    interface_3_out_0x55b7501b6ea0;
    interface_3_out_0x55b7501b6f60;
    interface_4_out_0x55b7501f5bb8;
    interface_4_out_0x55b7501f5c08;
    interface_4_out_0x55b7501b62a8;
}
subgraph cluster_subgraph_output {
    label = "Output";
    interface_5_in_0x55b738631280 [label="N", shape=none];
    interface_5_in_0x55b7386312a8 [label="C_out", shape=none];
    interface_5_in_0x55b7386312d0 [label="H", shape=none];
    interface_5_in_0x55b7386312f8 [label="H", shape=none];
}
interface_0_out_0x55b738631280 -> interface_5_in_0x55b738631280;
interface_0_out_0x55b7386312a8 -> interface_5_in_0x55b7386312a8;
interface_0_out_0x55b7386312d0 -> interface_5_in_0x55b7386312d0;
interface_0_out_0x55b7386312f8 -> interface_5_in_0x55b7386312f8;

}

"""
class kernel_generated_0(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([64, 64, 3]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]

		# No contraction needed.
		t_2 = in_0

		# [C_in]@Split69dd43e05c8c5ddb -> [s]@Merge03a73148aa81036c, [s^-1*C_in]@Share8de6f167adbbf8aa
		t_2 = torch.reshape(t_2, (1, 2, 64, 56, 56, ))

		# [H]@Shiftdbd5b2e652804221 -> [H]@Unfold0063bc810b9e1e60
		t_2 = torch.roll(t_2, self.shift_direction, 4)

		# [H]@Unfold0063bc810b9e1e60 -> [H]@Iteratorb0a1def4ad5784ec, [k_1]@Share26cfa48d169008e4
		t_2 = torch.reshape(t_2, (1, 7168, 56, 1, ))
		t_2 = torch.nn.functional.unfold(t_2, (3, 1, ), padding=(1, 0, ))
		t_2 = torch.reshape(t_2, (1, 2, 64, 56, 3, 56, ))

		# Perform contraction.
		t_3 = torch.einsum("lojnim, jki -> loknm", t_2, in_1)

		# No contraction needed.
		t_4 = t_3

		# [s]@Merge03a73148aa81036c, [s^-1*C_out]@Merge03a73148aa81036f -> [C_out]@Iteratorc7f8eb87a5a0a9e0
		t_4 = torch.reshape(t_4, (1, 128, 56, 56, ))

		# [H]@Shift41a433c05e30b91d -> [H]@Iterator96123ba3184da39c
		t_4 = torch.roll(t_4, self.shift_direction, 2)

		# No need to crop the output tensor.
		y = t_4

		return y

class kernel_generated_1(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([128, 128, 3]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]

		# No contraction needed.
		t_2 = in_0

		# [C_in]@Split69dd43e05c8c5ddb -> [s]@Merge03a73148aa81036c, [s^-1*C_in]@Share8de6f167adbbf8aa
		t_2 = torch.reshape(t_2, (1, 2, 128, 28, 28, ))

		# [H]@Shiftdbd5b2e652804221 -> [H]@Unfold0063bc810b9e1e60
		t_2 = torch.roll(t_2, self.shift_direction, 4)

		# [H]@Unfold0063bc810b9e1e60 -> [H]@Iteratorb0a1def4ad5784ec, [k_1]@Share26cfa48d169008e4
		t_2 = torch.reshape(t_2, (1, 7168, 28, 1, ))
		t_2 = torch.nn.functional.unfold(t_2, (3, 1, ), padding=(1, 0, ))
		t_2 = torch.reshape(t_2, (1, 2, 128, 28, 3, 28, ))

		# Perform contraction.
		t_3 = torch.einsum("lojnim, jki -> loknm", t_2, in_1)

		# No contraction needed.
		t_4 = t_3

		# [s]@Merge03a73148aa81036c, [s^-1*C_out]@Merge03a73148aa81036f -> [C_out]@Iteratorc7f8eb87a5a0a9e0
		t_4 = torch.reshape(t_4, (1, 256, 28, 28, ))

		# [H]@Shift41a433c05e30b91d -> [H]@Iterator96123ba3184da39c
		t_4 = torch.roll(t_4, self.shift_direction, 2)

		# No need to crop the output tensor.
		y = t_4

		return y

class kernel_generated_2(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([256, 256, 3]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]

		# No contraction needed.
		t_2 = in_0

		# [C_in]@Split69dd43e05c8c5ddb -> [s]@Merge03a73148aa81036c, [s^-1*C_in]@Share8de6f167adbbf8aa
		t_2 = torch.reshape(t_2, (1, 2, 256, 14, 14, ))

		# [H]@Shiftdbd5b2e652804221 -> [H]@Unfold0063bc810b9e1e60
		t_2 = torch.roll(t_2, self.shift_direction, 4)

		# [H]@Unfold0063bc810b9e1e60 -> [H]@Iteratorb0a1def4ad5784ec, [k_1]@Share26cfa48d169008e4
		t_2 = torch.reshape(t_2, (1, 7168, 14, 1, ))
		t_2 = torch.nn.functional.unfold(t_2, (3, 1, ), padding=(1, 0, ))
		t_2 = torch.reshape(t_2, (1, 2, 256, 14, 3, 14, ))

		# Perform contraction.
		t_3 = torch.einsum("lojnim, jki -> loknm", t_2, in_1)

		# No contraction needed.
		t_4 = t_3

		# [s]@Merge03a73148aa81036c, [s^-1*C_out]@Merge03a73148aa81036f -> [C_out]@Iteratorc7f8eb87a5a0a9e0
		t_4 = torch.reshape(t_4, (1, 512, 14, 14, ))

		# [H]@Shift41a433c05e30b91d -> [H]@Iterator96123ba3184da39c
		t_4 = torch.roll(t_4, self.shift_direction, 2)

		# No need to crop the output tensor.
		y = t_4

		return y

class kernel_generated_3(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([512, 512, 3]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]

		# No contraction needed.
		t_2 = in_0

		# [C_in]@Split69dd43e05c8c5ddb -> [s]@Merge03a73148aa81036c, [s^-1*C_in]@Share8de6f167adbbf8aa
		t_2 = torch.reshape(t_2, (1, 2, 512, 7, 7, ))

		# [H]@Shiftdbd5b2e652804221 -> [H]@Unfold0063bc810b9e1e60
		t_2 = torch.roll(t_2, self.shift_direction, 4)

		# [H]@Unfold0063bc810b9e1e60 -> [H]@Iteratorb0a1def4ad5784ec, [k_1]@Share26cfa48d169008e4
		t_2 = torch.reshape(t_2, (1, 7168, 7, 1, ))
		t_2 = torch.nn.functional.unfold(t_2, (3, 1, ), padding=(1, 0, ))
		t_2 = torch.reshape(t_2, (1, 2, 512, 7, 3, 7, ))

		# Perform contraction.
		t_3 = torch.einsum("lojnim, jki -> loknm", t_2, in_1)

		# No contraction needed.
		t_4 = t_3

		# [s]@Merge03a73148aa81036c, [s^-1*C_out]@Merge03a73148aa81036f -> [C_out]@Iteratorc7f8eb87a5a0a9e0
		t_4 = torch.reshape(t_4, (1, 1024, 7, 7, ))

		# [H]@Shift41a433c05e30b91d -> [H]@Iterator96123ba3184da39c
		t_4 = torch.roll(t_4, self.shift_direction, 2)

		# No need to crop the output tensor.
		y = t_4

		return y

