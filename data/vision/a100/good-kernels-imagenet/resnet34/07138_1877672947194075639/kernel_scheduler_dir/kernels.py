import torch
import random
"""
digraph kernel_preview {
newrank = true;

// Stage tensor.
subgraph cluster_subgraph_0 {
    label = "Subgraph 0";
    // Reductions.
    reduce_0x7fa474001ab0 [label="Sum", shape=box];
    reduce_0x7fa474005640 [label="Sum", shape=box];
    reduce_0x7fa474001a98 [label="Sum", shape=box];
    // Output.
    subgraph cluster_subgraph_0_out {
        label = "";
        interface_0_out_0x5601d07b95b0 [label="N", shape=none];
        interface_0_out_0x5601d07b95d8 [label="C_out", shape=none];
        interface_0_out_0x5601d07b9600 [label="H", shape=none];
        interface_0_out_0x5601d07b9628 [label="H", shape=none];
    }
    {
        rank = same;
        reduce_0x7fa474001ab0;
        reduce_0x7fa474005640;
        reduce_0x7fa474001a98;
        interface_0_out_0x5601d07b95b0;
        interface_0_out_0x5601d07b95d8;
        interface_0_out_0x5601d07b9600;
        interface_0_out_0x5601d07b9628;
    }
    // Input 0.
    subgraph cluster_subgraph_0_in_0 {
        label = "";
        interface_0_in_0x5601d07b95b0 [label="N", shape=none];
        interface_0_in_0x5601d05c01e0 [label="k_1", shape=none];
        interface_0_in_0x5601d07b9600 [label="H", shape=none];
        interface_0_in_0x5601d05c00f0 [label="s^-1*C_in", shape=none];
        interface_0_in_0x5601d05c0190 [label="k_1", shape=none];
        interface_0_in_0x5601d07b9628 [label="H", shape=none];
    }
    // Input 1.
    subgraph cluster_subgraph_0_in_1 {
        label = "";
        interface_0_in_0x5601d05c00b8 [label="C_out", shape=none];
        interface_0_in_0x5601d05c01f8 [label="k_1", shape=none];
        interface_0_in_0x5601d05c0108 [label="s^-1*C_in", shape=none];
        interface_0_in_0x5601d05c01a8 [label="k_1", shape=none];
    }
    {
        rank = same;
        interface_0_in_0x5601d07b95b0;
        interface_0_in_0x5601d05c01e0;
        interface_0_in_0x5601d07b9600;
        interface_0_in_0x5601d05c00f0;
        interface_0_in_0x5601d05c0190;
        interface_0_in_0x5601d07b9628;
        interface_0_in_0x5601d05c00b8;
        interface_0_in_0x5601d05c01f8;
        interface_0_in_0x5601d05c0108;
        interface_0_in_0x5601d05c01a8;
    }
    // Op's.
    op_0x5601d05c0080 [label="Share"];
    op_0x5601d05c00d0 [label="Share"];
    op_0x5601d05c0170 [label="Share"];
    op_0x5601d05c01c0 [label="Share"];
    op_0x5601d05f8b78 [label="Expand"];
    // Dimension's.
    op_0x5601d05f8b78 -> op_0x5601d05c0080 [label="C_out"];
    interface_0_in_0x5601d05c00b8 -> op_0x5601d05c0080 [label="C_out"];
    interface_0_in_0x5601d05c00f0 -> op_0x5601d05c00d0 [label="s^-1*C_in"];
    interface_0_in_0x5601d05c0108 -> op_0x5601d05c00d0 [label="s^-1*C_in"];
    interface_0_in_0x5601d05c0190 -> op_0x5601d05c0170 [label="k_1"];
    interface_0_in_0x5601d05c01a8 -> op_0x5601d05c0170 [label="k_1"];
    interface_0_in_0x5601d05c01e0 -> op_0x5601d05c01c0 [label="k_1"];
    interface_0_in_0x5601d05c01f8 -> op_0x5601d05c01c0 [label="k_1"];
    interface_0_in_0x5601d07b95b0 -> interface_0_out_0x5601d07b95b0 [label="N"];
    op_0x5601d05c0080 -> interface_0_out_0x5601d07b95d8 [label="C_out"];
    interface_0_in_0x5601d07b9600 -> interface_0_out_0x5601d07b9600 [label="H"];
    interface_0_in_0x5601d07b9628 -> interface_0_out_0x5601d07b9628 [label="H"];
    op_0x5601d05c0170 -> reduce_0x7fa474001a98 [label="k_1"];
    op_0x5601d05c01c0 -> reduce_0x7fa474001ab0 [label="k_1"];
    op_0x5601d05c00d0 -> reduce_0x7fa474005640 [label="s^-1*C_in"];
}

// Stage tensor.
subgraph cluster_subgraph_1 {
    label = "Subgraph 1";
    // Reductions.
    // Output.
    subgraph cluster_subgraph_1_out {
        label = "";
        interface_1_out_0x5601d07b95b0 [label="N", shape=none];
        interface_1_out_0x5601d05c01e0 [label="k_1", shape=none];
        interface_1_out_0x5601d07b9600 [label="H", shape=none];
        interface_1_out_0x5601d05c00f0 [label="s^-1*C_in", shape=none];
        interface_1_out_0x5601d05c0190 [label="k_1", shape=none];
        interface_1_out_0x5601d07b9628 [label="H", shape=none];
    }
    {
        rank = same;
        interface_1_out_0x5601d07b95b0;
        interface_1_out_0x5601d05c01e0;
        interface_1_out_0x5601d07b9600;
        interface_1_out_0x5601d05c00f0;
        interface_1_out_0x5601d05c0190;
        interface_1_out_0x5601d07b9628;
    }
    // Input 0.
    subgraph cluster_subgraph_1_in_0 {
        label = "";
        interface_1_in_0x5601d07b95b0 [label="N", shape=none];
        interface_1_in_0x5601d05c01e0 [label="k_1", shape=none];
        interface_1_in_0x5601d07b9600 [label="H", shape=none];
        interface_1_in_0x5601d05c00f0 [label="s^-1*C_in", shape=none];
        interface_1_in_0x5601d0706768 [label="H", shape=none];
    }
    {
        rank = same;
        interface_1_in_0x5601d07b95b0;
        interface_1_in_0x5601d05c01e0;
        interface_1_in_0x5601d07b9600;
        interface_1_in_0x5601d05c00f0;
        interface_1_in_0x5601d0706768;
    }
    // Op's.
    op_0x5601d0706740 [label="Unfold"];
    // Dimension's.
    interface_1_in_0x5601d05c00f0 -> interface_1_out_0x5601d05c00f0 [label="s^-1*C_in"];
    op_0x5601d0706740 -> interface_1_out_0x5601d05c0190 [label="k_1"];
    interface_1_in_0x5601d05c01e0 -> interface_1_out_0x5601d05c01e0 [label="k_1"];
    interface_1_in_0x5601d0706768 -> op_0x5601d0706740 [label="H"];
    interface_1_in_0x5601d07b95b0 -> interface_1_out_0x5601d07b95b0 [label="N"];
    interface_1_in_0x5601d07b9600 -> interface_1_out_0x5601d07b9600 [label="H"];
    op_0x5601d0706740 -> interface_1_out_0x5601d07b9628 [label="H"];
}

// Stage tensor.
subgraph cluster_subgraph_2 {
    label = "Subgraph 2";
    // Reductions.
    reduce_0x7fa474002ce8 [label="Sum", shape=box];
    // Output.
    subgraph cluster_subgraph_2_out {
        label = "";
        interface_2_out_0x5601d07b95b0 [label="N", shape=none];
        interface_2_out_0x5601d05c01e0 [label="k_1", shape=none];
        interface_2_out_0x5601d07b9600 [label="H", shape=none];
        interface_2_out_0x5601d05c00f0 [label="s^-1*C_in", shape=none];
        interface_2_out_0x5601d0706768 [label="H", shape=none];
    }
    {
        rank = same;
        reduce_0x7fa474002ce8;
        interface_2_out_0x5601d07b95b0;
        interface_2_out_0x5601d05c01e0;
        interface_2_out_0x5601d07b9600;
        interface_2_out_0x5601d05c00f0;
        interface_2_out_0x5601d0706768;
    }
    // Input 0.
    subgraph cluster_subgraph_2_in_0 {
        label = "";
        interface_2_in_0x5601d07b95b0 [label="N", shape=none];
        interface_2_in_0x5601d0707e50 [label="C_in", shape=none];
        interface_2_in_0x5601d07066a8 [label="H", shape=none];
        interface_2_in_0x5601d0706768 [label="H", shape=none];
    }
    {
        rank = same;
        interface_2_in_0x5601d07b95b0;
        interface_2_in_0x5601d0707e50;
        interface_2_in_0x5601d07066a8;
        interface_2_in_0x5601d0706768;
    }
    // Op's.
    op_0x5601d00d82a0 [label="Shift"];
    op_0x5601d00d8a20 [label="Split"];
    op_0x5601d0706680 [label="Unfold"];
    op_0x5601d0707e10 [label="Split"];
    op_0x5601d0731c30 [label="Merge"];
    // Dimension's.
    op_0x5601d0731c30 -> op_0x5601d00d82a0 [label="s*H"];
    op_0x5601d00d82a0 -> op_0x5601d00d8a20 [label="s*H"];
    op_0x5601d0707e10 -> interface_2_out_0x5601d05c00f0 [label="s^-1*C_in"];
    op_0x5601d0706680 -> interface_2_out_0x5601d05c01e0 [label="k_1"];
    interface_2_in_0x5601d07066a8 -> op_0x5601d0706680 [label="H"];
    interface_2_in_0x5601d0706768 -> interface_2_out_0x5601d0706768 [label="H"];
    interface_2_in_0x5601d0707e50 -> op_0x5601d0707e10 [label="C_in"];
    op_0x5601d0706680 -> op_0x5601d0731c30 [label="H"];
    op_0x5601d0707e10 -> op_0x5601d0731c30 [label="s"];
    interface_2_in_0x5601d07b95b0 -> interface_2_out_0x5601d07b95b0 [label="N"];
    op_0x5601d00d8a20 -> interface_2_out_0x5601d07b9600 [label="H"];
    op_0x5601d00d8a20 -> reduce_0x7fa474002ce8 [label="s"];
}

// Input tensor.
subgraph cluster_subgraph_3 {
    label = "Input 0";
    interface_3_out_0x5601d07b95b0 [label="N", shape=none];
    interface_3_out_0x5601d0707e50 [label="C_in", shape=none];
    interface_3_out_0x5601d07066a8 [label="H", shape=none];
    interface_3_out_0x5601d0706768 [label="H", shape=none];
}

interface_3_out_0x5601d07b95b0 -> interface_2_in_0x5601d07b95b0;
interface_3_out_0x5601d0707e50 -> interface_2_in_0x5601d0707e50;
interface_3_out_0x5601d07066a8 -> interface_2_in_0x5601d07066a8;
interface_3_out_0x5601d0706768 -> interface_2_in_0x5601d0706768;

interface_2_out_0x5601d07b95b0 -> interface_1_in_0x5601d07b95b0;
interface_2_out_0x5601d05c01e0 -> interface_1_in_0x5601d05c01e0;
interface_2_out_0x5601d07b9600 -> interface_1_in_0x5601d07b9600;
interface_2_out_0x5601d05c00f0 -> interface_1_in_0x5601d05c00f0;
interface_2_out_0x5601d0706768 -> interface_1_in_0x5601d0706768;

interface_1_out_0x5601d07b95b0 -> interface_0_in_0x5601d07b95b0;
interface_1_out_0x5601d05c01e0 -> interface_0_in_0x5601d05c01e0;
interface_1_out_0x5601d07b9600 -> interface_0_in_0x5601d07b9600;
interface_1_out_0x5601d05c00f0 -> interface_0_in_0x5601d05c00f0;
interface_1_out_0x5601d05c0190 -> interface_0_in_0x5601d05c0190;
interface_1_out_0x5601d07b9628 -> interface_0_in_0x5601d07b9628;

// Input tensor.
subgraph cluster_subgraph_4 {
    label = "Input 1";
    interface_4_out_0x5601d05c00b8 [label="C_out", shape=none];
    interface_4_out_0x5601d05c01f8 [label="k_1", shape=none];
    interface_4_out_0x5601d05c0108 [label="s^-1*C_in", shape=none];
    interface_4_out_0x5601d05c01a8 [label="k_1", shape=none];
}

interface_4_out_0x5601d05c00b8 -> interface_0_in_0x5601d05c00b8;
interface_4_out_0x5601d05c01f8 -> interface_0_in_0x5601d05c01f8;
interface_4_out_0x5601d05c0108 -> interface_0_in_0x5601d05c0108;
interface_4_out_0x5601d05c01a8 -> interface_0_in_0x5601d05c01a8;

{
    rank = same;
    interface_3_out_0x5601d07b95b0;
    interface_3_out_0x5601d0707e50;
    interface_3_out_0x5601d07066a8;
    interface_3_out_0x5601d0706768;
    interface_4_out_0x5601d05c00b8;
    interface_4_out_0x5601d05c01f8;
    interface_4_out_0x5601d05c0108;
    interface_4_out_0x5601d05c01a8;
}
subgraph cluster_subgraph_output {
    label = "Output";
    interface_5_in_0x5601d07b95b0 [label="N", shape=none];
    interface_5_in_0x5601d07b95d8 [label="C_out", shape=none];
    interface_5_in_0x5601d07b9600 [label="H", shape=none];
    interface_5_in_0x5601d07b9628 [label="H", shape=none];
}
interface_0_out_0x5601d07b95b0 -> interface_5_in_0x5601d07b95b0;
interface_0_out_0x5601d07b95d8 -> interface_5_in_0x5601d07b95d8;
interface_0_out_0x5601d07b9600 -> interface_5_in_0x5601d07b9600;
interface_0_out_0x5601d07b9628 -> interface_5_in_0x5601d07b9628;

}

"""
class kernel_generated_0(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([64, 3, 32, 3]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]

		# Perform contraction.
		t_2 = torch.einsum("lkij -> likj", in_0)

		# [H]@Unfold5462ce2dd0c9bf76 -> [H]@Merge5f50103ea583163b, [k_1]@Share02da0a485106ab3d
		t_2 = torch.reshape(t_2, (1024, 1, 56, 3584, ))
		t_2 = torch.nn.functional.unfold(t_2, (3, 1, ), padding=(1, 0, ))
		t_2 = torch.reshape(t_2, (1024, 3, 56, 64, 56, ))

		# [C_in]@Splitf4535f3a98ce8ba2 -> [s]@Merge5f50103ea5831638, [s^-1*C_in]@Share8de6f167adbbf8aa
		t_2 = torch.reshape(t_2, (1024, 3, 56, 2, 32, 56, ))

		# [H]@Merge5f50103ea583163b, [s]@Merge5f50103ea5831638 -> [s*H]@Shift3c9c8e9d3c84cb9b
		t_2 = torch.reshape(t_2, (1024, 3, 112, 32, 56, ))

		# [s*H]@Shift3c9c8e9d3c84cb9b -> [s*H]@Splitdb1af055f999951a
		t_2 = torch.roll(t_2, self.shift_direction, 2)

		# [s*H]@Splitdb1af055f999951a -> [H]@Iterator96123ba3184da39c, [s]@Reduced95c644a3c072d9a
		t_2 = torch.reshape(t_2, (1024, 3, 56, 2, 32, 56, ))

		# [s]@Reduce
		t_2 = torch.sum(t_2, dim=(3, ))

		# No contraction needed.
		t_3 = t_2

		# [H]@Unfold0063bc810b9e1e60 -> [H]@Iteratorb0a1def4ad5784ec, [k_1]@Share26cfa48d169008e4
		t_3 = torch.reshape(t_3, (1024, 5376, 56, 1, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (1024, 3, 56, 32, 3, 56, ))

		# Perform contraction.
		t_4 = torch.einsum("mlnjko, iljk -> mino", t_3, in_1)

		# No need to crop the output tensor.
		y = t_4

		return y

class kernel_generated_1(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([128, 3, 32, 3]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]

		# Perform contraction.
		t_2 = torch.einsum("lkij -> likj", in_0)

		# [H]@Unfold5462ce2dd0c9bf76 -> [H]@Merge5f50103ea583163b, [k_1]@Share02da0a485106ab3d
		t_2 = torch.reshape(t_2, (1024, 1, 28, 1792, ))
		t_2 = torch.nn.functional.unfold(t_2, (3, 1, ), padding=(1, 0, ))
		t_2 = torch.reshape(t_2, (1024, 3, 28, 64, 28, ))

		# [C_in]@Splitf4535f3a98ce8ba2 -> [s]@Merge5f50103ea5831638, [s^-1*C_in]@Share8de6f167adbbf8aa
		t_2 = torch.reshape(t_2, (1024, 3, 28, 2, 32, 28, ))

		# [H]@Merge5f50103ea583163b, [s]@Merge5f50103ea5831638 -> [s*H]@Shift3c9c8e9d3c84cb9b
		t_2 = torch.reshape(t_2, (1024, 3, 56, 32, 28, ))

		# [s*H]@Shift3c9c8e9d3c84cb9b -> [s*H]@Splitdb1af055f999951a
		t_2 = torch.roll(t_2, self.shift_direction, 2)

		# [s*H]@Splitdb1af055f999951a -> [H]@Iterator96123ba3184da39c, [s]@Reduced95c644a3c072d9a
		t_2 = torch.reshape(t_2, (1024, 3, 28, 2, 32, 28, ))

		# [s]@Reduce
		t_2 = torch.sum(t_2, dim=(3, ))

		# No contraction needed.
		t_3 = t_2

		# [H]@Unfold0063bc810b9e1e60 -> [H]@Iteratorb0a1def4ad5784ec, [k_1]@Share26cfa48d169008e4
		t_3 = torch.reshape(t_3, (1024, 2688, 28, 1, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (1024, 3, 28, 32, 3, 28, ))

		# Perform contraction.
		t_4 = torch.einsum("mlnjko, iljk -> mino", t_3, in_1)

		# No need to crop the output tensor.
		y = t_4

		return y

class kernel_generated_2(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([128, 3, 64, 3]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]

		# Perform contraction.
		t_2 = torch.einsum("lkij -> likj", in_0)

		# [H]@Unfold5462ce2dd0c9bf76 -> [H]@Merge5f50103ea583163b, [k_1]@Share02da0a485106ab3d
		t_2 = torch.reshape(t_2, (1024, 1, 28, 3584, ))
		t_2 = torch.nn.functional.unfold(t_2, (3, 1, ), padding=(1, 0, ))
		t_2 = torch.reshape(t_2, (1024, 3, 28, 128, 28, ))

		# [C_in]@Splitf4535f3a98ce8ba2 -> [s]@Merge5f50103ea5831638, [s^-1*C_in]@Share8de6f167adbbf8aa
		t_2 = torch.reshape(t_2, (1024, 3, 28, 2, 64, 28, ))

		# [H]@Merge5f50103ea583163b, [s]@Merge5f50103ea5831638 -> [s*H]@Shift3c9c8e9d3c84cb9b
		t_2 = torch.reshape(t_2, (1024, 3, 56, 64, 28, ))

		# [s*H]@Shift3c9c8e9d3c84cb9b -> [s*H]@Splitdb1af055f999951a
		t_2 = torch.roll(t_2, self.shift_direction, 2)

		# [s*H]@Splitdb1af055f999951a -> [H]@Iterator96123ba3184da39c, [s]@Reduced95c644a3c072d9a
		t_2 = torch.reshape(t_2, (1024, 3, 28, 2, 64, 28, ))

		# [s]@Reduce
		t_2 = torch.sum(t_2, dim=(3, ))

		# No contraction needed.
		t_3 = t_2

		# [H]@Unfold0063bc810b9e1e60 -> [H]@Iteratorb0a1def4ad5784ec, [k_1]@Share26cfa48d169008e4
		t_3 = torch.reshape(t_3, (1024, 5376, 28, 1, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (1024, 3, 28, 64, 3, 28, ))

		# Perform contraction.
		t_4 = torch.einsum("mlnjko, iljk -> mino", t_3, in_1)

		# No need to crop the output tensor.
		y = t_4

		return y

class kernel_generated_3(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([256, 3, 64, 3]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]

		# Perform contraction.
		t_2 = torch.einsum("lkij -> likj", in_0)

		# [H]@Unfold5462ce2dd0c9bf76 -> [H]@Merge5f50103ea583163b, [k_1]@Share02da0a485106ab3d
		t_2 = torch.reshape(t_2, (1024, 1, 14, 1792, ))
		t_2 = torch.nn.functional.unfold(t_2, (3, 1, ), padding=(1, 0, ))
		t_2 = torch.reshape(t_2, (1024, 3, 14, 128, 14, ))

		# [C_in]@Splitf4535f3a98ce8ba2 -> [s]@Merge5f50103ea5831638, [s^-1*C_in]@Share8de6f167adbbf8aa
		t_2 = torch.reshape(t_2, (1024, 3, 14, 2, 64, 14, ))

		# [H]@Merge5f50103ea583163b, [s]@Merge5f50103ea5831638 -> [s*H]@Shift3c9c8e9d3c84cb9b
		t_2 = torch.reshape(t_2, (1024, 3, 28, 64, 14, ))

		# [s*H]@Shift3c9c8e9d3c84cb9b -> [s*H]@Splitdb1af055f999951a
		t_2 = torch.roll(t_2, self.shift_direction, 2)

		# [s*H]@Splitdb1af055f999951a -> [H]@Iterator96123ba3184da39c, [s]@Reduced95c644a3c072d9a
		t_2 = torch.reshape(t_2, (1024, 3, 14, 2, 64, 14, ))

		# [s]@Reduce
		t_2 = torch.sum(t_2, dim=(3, ))

		# No contraction needed.
		t_3 = t_2

		# [H]@Unfold0063bc810b9e1e60 -> [H]@Iteratorb0a1def4ad5784ec, [k_1]@Share26cfa48d169008e4
		t_3 = torch.reshape(t_3, (1024, 2688, 14, 1, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (1024, 3, 14, 64, 3, 14, ))

		# Perform contraction.
		t_4 = torch.einsum("mlnjko, iljk -> mino", t_3, in_1)

		# No need to crop the output tensor.
		y = t_4

		return y

class kernel_generated_4(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([256, 3, 128, 3]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]

		# Perform contraction.
		t_2 = torch.einsum("lkij -> likj", in_0)

		# [H]@Unfold5462ce2dd0c9bf76 -> [H]@Merge5f50103ea583163b, [k_1]@Share02da0a485106ab3d
		t_2 = torch.reshape(t_2, (1024, 1, 14, 3584, ))
		t_2 = torch.nn.functional.unfold(t_2, (3, 1, ), padding=(1, 0, ))
		t_2 = torch.reshape(t_2, (1024, 3, 14, 256, 14, ))

		# [C_in]@Splitf4535f3a98ce8ba2 -> [s]@Merge5f50103ea5831638, [s^-1*C_in]@Share8de6f167adbbf8aa
		t_2 = torch.reshape(t_2, (1024, 3, 14, 2, 128, 14, ))

		# [H]@Merge5f50103ea583163b, [s]@Merge5f50103ea5831638 -> [s*H]@Shift3c9c8e9d3c84cb9b
		t_2 = torch.reshape(t_2, (1024, 3, 28, 128, 14, ))

		# [s*H]@Shift3c9c8e9d3c84cb9b -> [s*H]@Splitdb1af055f999951a
		t_2 = torch.roll(t_2, self.shift_direction, 2)

		# [s*H]@Splitdb1af055f999951a -> [H]@Iterator96123ba3184da39c, [s]@Reduced95c644a3c072d9a
		t_2 = torch.reshape(t_2, (1024, 3, 14, 2, 128, 14, ))

		# [s]@Reduce
		t_2 = torch.sum(t_2, dim=(3, ))

		# No contraction needed.
		t_3 = t_2

		# [H]@Unfold0063bc810b9e1e60 -> [H]@Iteratorb0a1def4ad5784ec, [k_1]@Share26cfa48d169008e4
		t_3 = torch.reshape(t_3, (1024, 5376, 14, 1, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (1024, 3, 14, 128, 3, 14, ))

		# Perform contraction.
		t_4 = torch.einsum("mlnjko, iljk -> mino", t_3, in_1)

		# No need to crop the output tensor.
		y = t_4

		return y

class kernel_generated_5(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([512, 3, 128, 3]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]

		# Perform contraction.
		t_2 = torch.einsum("lkij -> likj", in_0)

		# [H]@Unfold5462ce2dd0c9bf76 -> [H]@Merge5f50103ea583163b, [k_1]@Share02da0a485106ab3d
		t_2 = torch.reshape(t_2, (1024, 1, 7, 1792, ))
		t_2 = torch.nn.functional.unfold(t_2, (3, 1, ), padding=(1, 0, ))
		t_2 = torch.reshape(t_2, (1024, 3, 7, 256, 7, ))

		# [C_in]@Splitf4535f3a98ce8ba2 -> [s]@Merge5f50103ea5831638, [s^-1*C_in]@Share8de6f167adbbf8aa
		t_2 = torch.reshape(t_2, (1024, 3, 7, 2, 128, 7, ))

		# [H]@Merge5f50103ea583163b, [s]@Merge5f50103ea5831638 -> [s*H]@Shift3c9c8e9d3c84cb9b
		t_2 = torch.reshape(t_2, (1024, 3, 14, 128, 7, ))

		# [s*H]@Shift3c9c8e9d3c84cb9b -> [s*H]@Splitdb1af055f999951a
		t_2 = torch.roll(t_2, self.shift_direction, 2)

		# [s*H]@Splitdb1af055f999951a -> [H]@Iterator96123ba3184da39c, [s]@Reduced95c644a3c072d9a
		t_2 = torch.reshape(t_2, (1024, 3, 7, 2, 128, 7, ))

		# [s]@Reduce
		t_2 = torch.sum(t_2, dim=(3, ))

		# No contraction needed.
		t_3 = t_2

		# [H]@Unfold0063bc810b9e1e60 -> [H]@Iteratorb0a1def4ad5784ec, [k_1]@Share26cfa48d169008e4
		t_3 = torch.reshape(t_3, (1024, 2688, 7, 1, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (1024, 3, 7, 128, 3, 7, ))

		# Perform contraction.
		t_4 = torch.einsum("mlnjko, iljk -> mino", t_3, in_1)

		# No need to crop the output tensor.
		y = t_4

		return y

class kernel_generated_6(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([512, 3, 256, 3]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]

		# Perform contraction.
		t_2 = torch.einsum("lkij -> likj", in_0)

		# [H]@Unfold5462ce2dd0c9bf76 -> [H]@Merge5f50103ea583163b, [k_1]@Share02da0a485106ab3d
		t_2 = torch.reshape(t_2, (1024, 1, 7, 3584, ))
		t_2 = torch.nn.functional.unfold(t_2, (3, 1, ), padding=(1, 0, ))
		t_2 = torch.reshape(t_2, (1024, 3, 7, 512, 7, ))

		# [C_in]@Splitf4535f3a98ce8ba2 -> [s]@Merge5f50103ea5831638, [s^-1*C_in]@Share8de6f167adbbf8aa
		t_2 = torch.reshape(t_2, (1024, 3, 7, 2, 256, 7, ))

		# [H]@Merge5f50103ea583163b, [s]@Merge5f50103ea5831638 -> [s*H]@Shift3c9c8e9d3c84cb9b
		t_2 = torch.reshape(t_2, (1024, 3, 14, 256, 7, ))

		# [s*H]@Shift3c9c8e9d3c84cb9b -> [s*H]@Splitdb1af055f999951a
		t_2 = torch.roll(t_2, self.shift_direction, 2)

		# [s*H]@Splitdb1af055f999951a -> [H]@Iterator96123ba3184da39c, [s]@Reduced95c644a3c072d9a
		t_2 = torch.reshape(t_2, (1024, 3, 7, 2, 256, 7, ))

		# [s]@Reduce
		t_2 = torch.sum(t_2, dim=(3, ))

		# No contraction needed.
		t_3 = t_2

		# [H]@Unfold0063bc810b9e1e60 -> [H]@Iteratorb0a1def4ad5784ec, [k_1]@Share26cfa48d169008e4
		t_3 = torch.reshape(t_3, (1024, 5376, 7, 1, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (1024, 3, 7, 256, 3, 7, ))

		# Perform contraction.
		t_4 = torch.einsum("mlnjko, iljk -> mino", t_3, in_1)

		# No need to crop the output tensor.
		y = t_4

		return y

