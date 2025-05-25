import torch
import random
"""
digraph kernel_preview {
newrank = true;

// Stage tensor.
subgraph cluster_subgraph_0 {
    label = "Subgraph 0";
    // Reductions.
    reduce_0x7effd8001a98 [label="Sum", shape=box];
    reduce_0x7effd8002ce8 [label="Sum", shape=box];
    reduce_0x7effd8005640 [label="Sum", shape=box];
    // Output.
    subgraph cluster_subgraph_0_out {
        label = "";
        interface_0_out_0x55a308c0a8f0 [label="N", shape=none];
        interface_0_out_0x55a308c0a918 [label="C_out", shape=none];
        interface_0_out_0x55a308c0a940 [label="H", shape=none];
        interface_0_out_0x55a308c0a968 [label="H", shape=none];
    }
    {
        rank = same;
        reduce_0x7effd8001a98;
        reduce_0x7effd8002ce8;
        reduce_0x7effd8005640;
        interface_0_out_0x55a308c0a8f0;
        interface_0_out_0x55a308c0a918;
        interface_0_out_0x55a308c0a940;
        interface_0_out_0x55a308c0a968;
    }
    // Input 0.
    subgraph cluster_subgraph_0_in_0 {
        label = "";
        interface_0_in_0x55a308c0a8f0 [label="N", shape=none];
        interface_0_in_0x55a3093ce490 [label="s^-1*C_in", shape=none];
        interface_0_in_0x55a308c0a940 [label="H", shape=none];
        interface_0_in_0x55a3093b8ae0 [label="s", shape=none];
        interface_0_in_0x55a308c0a968 [label="H", shape=none];
        interface_0_in_0x55a3093b8810 [label="k_1", shape=none];
    }
    // Input 1.
    subgraph cluster_subgraph_0_in_1 {
        label = "";
        interface_0_in_0x55a3093b8af8 [label="s", shape=none];
        interface_0_in_0x55a3093ce4a8 [label="s^-1*C_in", shape=none];
        interface_0_in_0x55a3093b8828 [label="k_1", shape=none];
        interface_0_in_0x55a3093b8738 [label="C_out", shape=none];
    }
    {
        rank = same;
        interface_0_in_0x55a308c0a8f0;
        interface_0_in_0x55a3093ce490;
        interface_0_in_0x55a308c0a940;
        interface_0_in_0x55a3093b8ae0;
        interface_0_in_0x55a308c0a968;
        interface_0_in_0x55a3093b8810;
        interface_0_in_0x55a3093b8af8;
        interface_0_in_0x55a3093ce4a8;
        interface_0_in_0x55a3093b8828;
        interface_0_in_0x55a3093b8738;
    }
    // Op's.
    op_0x55a3093b8700 [label="Share"];
    op_0x55a3093b87f0 [label="Share"];
    op_0x55a3093b8ac0 [label="Share"];
    op_0x55a3093b8c98 [label="Expand"];
    op_0x55a3093ce470 [label="Share"];
    // Dimension's.
    interface_0_in_0x55a308c0a8f0 -> interface_0_out_0x55a308c0a8f0 [label="N"];
    op_0x55a3093b8700 -> interface_0_out_0x55a308c0a918 [label="C_out"];
    interface_0_in_0x55a308c0a940 -> interface_0_out_0x55a308c0a940 [label="H"];
    interface_0_in_0x55a308c0a968 -> interface_0_out_0x55a308c0a968 [label="H"];
    op_0x55a3093b8c98 -> op_0x55a3093b8700 [label="C_out"];
    interface_0_in_0x55a3093b8738 -> op_0x55a3093b8700 [label="C_out"];
    interface_0_in_0x55a3093b8810 -> op_0x55a3093b87f0 [label="k_1"];
    interface_0_in_0x55a3093b8828 -> op_0x55a3093b87f0 [label="k_1"];
    interface_0_in_0x55a3093b8ae0 -> op_0x55a3093b8ac0 [label="s"];
    interface_0_in_0x55a3093b8af8 -> op_0x55a3093b8ac0 [label="s"];
    interface_0_in_0x55a3093ce490 -> op_0x55a3093ce470 [label="s^-1*C_in"];
    interface_0_in_0x55a3093ce4a8 -> op_0x55a3093ce470 [label="s^-1*C_in"];
    op_0x55a3093b87f0 -> reduce_0x7effd8001a98 [label="k_1"];
    op_0x55a3093b8ac0 -> reduce_0x7effd8002ce8 [label="s"];
    op_0x55a3093ce470 -> reduce_0x7effd8005640 [label="s^-1*C_in"];
}

// Stage tensor.
subgraph cluster_subgraph_1 {
    label = "Subgraph 1";
    // Reductions.
    // Output.
    subgraph cluster_subgraph_1_out {
        label = "";
        interface_1_out_0x55a308c0a8f0 [label="N", shape=none];
        interface_1_out_0x55a3093ce490 [label="s^-1*C_in", shape=none];
        interface_1_out_0x55a308c0a940 [label="H", shape=none];
        interface_1_out_0x55a3093b8ae0 [label="s", shape=none];
        interface_1_out_0x55a308c0a968 [label="H", shape=none];
        interface_1_out_0x55a3093b8810 [label="k_1", shape=none];
    }
    {
        rank = same;
        interface_1_out_0x55a308c0a8f0;
        interface_1_out_0x55a3093ce490;
        interface_1_out_0x55a308c0a940;
        interface_1_out_0x55a3093b8ae0;
        interface_1_out_0x55a308c0a968;
        interface_1_out_0x55a3093b8810;
    }
    // Input 0.
    subgraph cluster_subgraph_1_in_0 {
        label = "";
        interface_1_in_0x55a308c0a8f0 [label="N", shape=none];
        interface_1_in_0x55a3093d3910 [label="C_in", shape=none];
        interface_1_in_0x55a3093bb690 [label="H", shape=none];
        interface_1_in_0x55a3093b96e0 [label="H", shape=none];
    }
    {
        rank = same;
        interface_1_in_0x55a308c0a8f0;
        interface_1_in_0x55a3093d3910;
        interface_1_in_0x55a3093bb690;
        interface_1_in_0x55a3093b96e0;
    }
    // Op's.
    op_0x55a3093b9690 [label="Shift"];
    op_0x55a3093b96c0 [label="Shift"];
    op_0x55a3093bb650 [label="Merge"];
    op_0x55a3093bb900 [label="Unfold"];
    op_0x55a3093d32e0 [label="Split"];
    op_0x55a3093d38d0 [label="Split"];
    // Dimension's.
    interface_1_in_0x55a308c0a8f0 -> interface_1_out_0x55a308c0a8f0 [label="N"];
    op_0x55a3093d32e0 -> interface_1_out_0x55a308c0a940 [label="H"];
    op_0x55a3093bb900 -> interface_1_out_0x55a308c0a968 [label="H"];
    op_0x55a3093bb900 -> interface_1_out_0x55a3093b8810 [label="k_1"];
    op_0x55a3093d32e0 -> interface_1_out_0x55a3093b8ae0 [label="s"];
    op_0x55a3093bb650 -> op_0x55a3093b9690 [label="s*H"];
    interface_1_in_0x55a3093b96e0 -> op_0x55a3093b96c0 [label="H"];
    interface_1_in_0x55a3093bb690 -> op_0x55a3093bb650 [label="H"];
    op_0x55a3093d38d0 -> op_0x55a3093bb650 [label="s"];
    op_0x55a3093b96c0 -> op_0x55a3093bb900 [label="H"];
    op_0x55a3093d38d0 -> interface_1_out_0x55a3093ce490 [label="s^-1*C_in"];
    op_0x55a3093b9690 -> op_0x55a3093d32e0 [label="s*H"];
    interface_1_in_0x55a3093d3910 -> op_0x55a3093d38d0 [label="C_in"];
}

// Input tensor.
subgraph cluster_subgraph_2 {
    label = "Input 0";
    interface_2_out_0x55a308c0a8f0 [label="N", shape=none];
    interface_2_out_0x55a3093d3910 [label="C_in", shape=none];
    interface_2_out_0x55a3093bb690 [label="H", shape=none];
    interface_2_out_0x55a3093b96e0 [label="H", shape=none];
}

interface_2_out_0x55a308c0a8f0 -> interface_1_in_0x55a308c0a8f0;
interface_2_out_0x55a3093d3910 -> interface_1_in_0x55a3093d3910;
interface_2_out_0x55a3093bb690 -> interface_1_in_0x55a3093bb690;
interface_2_out_0x55a3093b96e0 -> interface_1_in_0x55a3093b96e0;

interface_1_out_0x55a308c0a8f0 -> interface_0_in_0x55a308c0a8f0;
interface_1_out_0x55a3093ce490 -> interface_0_in_0x55a3093ce490;
interface_1_out_0x55a308c0a940 -> interface_0_in_0x55a308c0a940;
interface_1_out_0x55a3093b8ae0 -> interface_0_in_0x55a3093b8ae0;
interface_1_out_0x55a308c0a968 -> interface_0_in_0x55a308c0a968;
interface_1_out_0x55a3093b8810 -> interface_0_in_0x55a3093b8810;

// Input tensor.
subgraph cluster_subgraph_3 {
    label = "Input 1";
    interface_3_out_0x55a3093b8af8 [label="s", shape=none];
    interface_3_out_0x55a3093ce4a8 [label="s^-1*C_in", shape=none];
    interface_3_out_0x55a3093b8828 [label="k_1", shape=none];
    interface_3_out_0x55a3093b8738 [label="C_out", shape=none];
}

interface_3_out_0x55a3093b8af8 -> interface_0_in_0x55a3093b8af8;
interface_3_out_0x55a3093ce4a8 -> interface_0_in_0x55a3093ce4a8;
interface_3_out_0x55a3093b8828 -> interface_0_in_0x55a3093b8828;
interface_3_out_0x55a3093b8738 -> interface_0_in_0x55a3093b8738;

{
    rank = same;
    interface_2_out_0x55a308c0a8f0;
    interface_2_out_0x55a3093d3910;
    interface_2_out_0x55a3093bb690;
    interface_2_out_0x55a3093b96e0;
    interface_3_out_0x55a3093b8af8;
    interface_3_out_0x55a3093ce4a8;
    interface_3_out_0x55a3093b8828;
    interface_3_out_0x55a3093b8738;
}
subgraph cluster_subgraph_output {
    label = "Output";
    interface_4_in_0x55a308c0a8f0 [label="N", shape=none];
    interface_4_in_0x55a308c0a918 [label="C_out", shape=none];
    interface_4_in_0x55a308c0a940 [label="H", shape=none];
    interface_4_in_0x55a308c0a968 [label="H", shape=none];
}
interface_0_out_0x55a308c0a8f0 -> interface_4_in_0x55a308c0a8f0;
interface_0_out_0x55a308c0a918 -> interface_4_in_0x55a308c0a918;
interface_0_out_0x55a308c0a940 -> interface_4_in_0x55a308c0a940;
interface_0_out_0x55a308c0a968 -> interface_4_in_0x55a308c0a968;

}

"""
class kernel_generated_0(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([2, 32, 3, 64]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]

		# No contraction needed.
		t_2 = in_0

		# [C_in]@Spliteef7ce0b7703d88a -> [s]@Merge6f1a0d6b662fae85, [s^-1*C_in]@Share8de6f167adbbf8aa
		t_2 = torch.reshape(t_2, (1024, 2, 32, 56, 56, ))

		# [H]@Merge6f1a0d6b662fae84, [s]@Merge6f1a0d6b662fae85 -> [s*H]@Shift594e1a6314829db7
		t_2 = torch.permute(t_2, (0, 2, 3, 1, 4, ))
		t_2 = torch.reshape(t_2, (1024, 32, 112, 56, ))

		# [s*H]@Shift594e1a6314829db7 -> [s*H]@Split7ee86503d19bbef6
		t_2 = torch.roll(t_2, self.shift_direction, 2)

		# [s*H]@Split7ee86503d19bbef6 -> [H]@Iterator96123ba3184da39c, [s]@Shareb15a7faee0f8b868
		t_2 = torch.reshape(t_2, (1024, 32, 56, 2, 56, ))

		# [H]@Shiftdbd5b2e652804221 -> [H]@Unfold0063bc810b9e1e60
		t_2 = torch.roll(t_2, self.shift_direction, 4)

		# [H]@Unfold0063bc810b9e1e60 -> [H]@Iteratorb0a1def4ad5784ec, [k_1]@Share26cfa48d169008e4
		t_2 = torch.reshape(t_2, (1024, 3584, 56, 1, ))
		t_2 = torch.nn.functional.unfold(t_2, (3, 1, ), padding=(1, 0, ))
		t_2 = torch.reshape(t_2, (1024, 32, 56, 2, 3, 56, ))

		# Permute to match the output of this subgraph.
		t_2 = torch.permute(t_2, (0, 1, 2, 3, 5, 4, ))

		# Perform contraction.
		t_3 = torch.einsum("mlnkoj, klji -> mnoi", t_2, in_1)

		# Permute to match the output of this subgraph.
		t_3 = torch.permute(t_3, (0, 3, 1, 2, ))

		# No need to crop the output tensor.
		y = t_3

		return y

class kernel_generated_1(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([2, 32, 3, 128]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]

		# No contraction needed.
		t_2 = in_0

		# [C_in]@Spliteef7ce0b7703d88a -> [s]@Merge6f1a0d6b662fae85, [s^-1*C_in]@Share8de6f167adbbf8aa
		t_2 = torch.reshape(t_2, (1024, 2, 32, 28, 28, ))

		# [H]@Merge6f1a0d6b662fae84, [s]@Merge6f1a0d6b662fae85 -> [s*H]@Shift594e1a6314829db7
		t_2 = torch.permute(t_2, (0, 2, 3, 1, 4, ))
		t_2 = torch.reshape(t_2, (1024, 32, 56, 28, ))

		# [s*H]@Shift594e1a6314829db7 -> [s*H]@Split7ee86503d19bbef6
		t_2 = torch.roll(t_2, self.shift_direction, 2)

		# [s*H]@Split7ee86503d19bbef6 -> [H]@Iterator96123ba3184da39c, [s]@Shareb15a7faee0f8b868
		t_2 = torch.reshape(t_2, (1024, 32, 28, 2, 28, ))

		# [H]@Shiftdbd5b2e652804221 -> [H]@Unfold0063bc810b9e1e60
		t_2 = torch.roll(t_2, self.shift_direction, 4)

		# [H]@Unfold0063bc810b9e1e60 -> [H]@Iteratorb0a1def4ad5784ec, [k_1]@Share26cfa48d169008e4
		t_2 = torch.reshape(t_2, (1024, 1792, 28, 1, ))
		t_2 = torch.nn.functional.unfold(t_2, (3, 1, ), padding=(1, 0, ))
		t_2 = torch.reshape(t_2, (1024, 32, 28, 2, 3, 28, ))

		# Permute to match the output of this subgraph.
		t_2 = torch.permute(t_2, (0, 1, 2, 3, 5, 4, ))

		# Perform contraction.
		t_3 = torch.einsum("mlnkoj, klji -> mnoi", t_2, in_1)

		# Permute to match the output of this subgraph.
		t_3 = torch.permute(t_3, (0, 3, 1, 2, ))

		# No need to crop the output tensor.
		y = t_3

		return y

class kernel_generated_2(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([2, 64, 3, 128]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]

		# No contraction needed.
		t_2 = in_0

		# [C_in]@Spliteef7ce0b7703d88a -> [s]@Merge6f1a0d6b662fae85, [s^-1*C_in]@Share8de6f167adbbf8aa
		t_2 = torch.reshape(t_2, (1024, 2, 64, 28, 28, ))

		# [H]@Merge6f1a0d6b662fae84, [s]@Merge6f1a0d6b662fae85 -> [s*H]@Shift594e1a6314829db7
		t_2 = torch.permute(t_2, (0, 2, 3, 1, 4, ))
		t_2 = torch.reshape(t_2, (1024, 64, 56, 28, ))

		# [s*H]@Shift594e1a6314829db7 -> [s*H]@Split7ee86503d19bbef6
		t_2 = torch.roll(t_2, self.shift_direction, 2)

		# [s*H]@Split7ee86503d19bbef6 -> [H]@Iterator96123ba3184da39c, [s]@Shareb15a7faee0f8b868
		t_2 = torch.reshape(t_2, (1024, 64, 28, 2, 28, ))

		# [H]@Shiftdbd5b2e652804221 -> [H]@Unfold0063bc810b9e1e60
		t_2 = torch.roll(t_2, self.shift_direction, 4)

		# [H]@Unfold0063bc810b9e1e60 -> [H]@Iteratorb0a1def4ad5784ec, [k_1]@Share26cfa48d169008e4
		t_2 = torch.reshape(t_2, (1024, 3584, 28, 1, ))
		t_2 = torch.nn.functional.unfold(t_2, (3, 1, ), padding=(1, 0, ))
		t_2 = torch.reshape(t_2, (1024, 64, 28, 2, 3, 28, ))

		# Permute to match the output of this subgraph.
		t_2 = torch.permute(t_2, (0, 1, 2, 3, 5, 4, ))

		# Perform contraction.
		t_3 = torch.einsum("mlnkoj, klji -> mnoi", t_2, in_1)

		# Permute to match the output of this subgraph.
		t_3 = torch.permute(t_3, (0, 3, 1, 2, ))

		# No need to crop the output tensor.
		y = t_3

		return y

class kernel_generated_3(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([2, 64, 3, 256]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]

		# No contraction needed.
		t_2 = in_0

		# [C_in]@Spliteef7ce0b7703d88a -> [s]@Merge6f1a0d6b662fae85, [s^-1*C_in]@Share8de6f167adbbf8aa
		t_2 = torch.reshape(t_2, (1024, 2, 64, 14, 14, ))

		# [H]@Merge6f1a0d6b662fae84, [s]@Merge6f1a0d6b662fae85 -> [s*H]@Shift594e1a6314829db7
		t_2 = torch.permute(t_2, (0, 2, 3, 1, 4, ))
		t_2 = torch.reshape(t_2, (1024, 64, 28, 14, ))

		# [s*H]@Shift594e1a6314829db7 -> [s*H]@Split7ee86503d19bbef6
		t_2 = torch.roll(t_2, self.shift_direction, 2)

		# [s*H]@Split7ee86503d19bbef6 -> [H]@Iterator96123ba3184da39c, [s]@Shareb15a7faee0f8b868
		t_2 = torch.reshape(t_2, (1024, 64, 14, 2, 14, ))

		# [H]@Shiftdbd5b2e652804221 -> [H]@Unfold0063bc810b9e1e60
		t_2 = torch.roll(t_2, self.shift_direction, 4)

		# [H]@Unfold0063bc810b9e1e60 -> [H]@Iteratorb0a1def4ad5784ec, [k_1]@Share26cfa48d169008e4
		t_2 = torch.reshape(t_2, (1024, 1792, 14, 1, ))
		t_2 = torch.nn.functional.unfold(t_2, (3, 1, ), padding=(1, 0, ))
		t_2 = torch.reshape(t_2, (1024, 64, 14, 2, 3, 14, ))

		# Permute to match the output of this subgraph.
		t_2 = torch.permute(t_2, (0, 1, 2, 3, 5, 4, ))

		# Perform contraction.
		t_3 = torch.einsum("mlnkoj, klji -> mnoi", t_2, in_1)

		# Permute to match the output of this subgraph.
		t_3 = torch.permute(t_3, (0, 3, 1, 2, ))

		# No need to crop the output tensor.
		y = t_3

		return y

class kernel_generated_4(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([2, 128, 3, 256]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]

		# No contraction needed.
		t_2 = in_0

		# [C_in]@Spliteef7ce0b7703d88a -> [s]@Merge6f1a0d6b662fae85, [s^-1*C_in]@Share8de6f167adbbf8aa
		t_2 = torch.reshape(t_2, (1024, 2, 128, 14, 14, ))

		# [H]@Merge6f1a0d6b662fae84, [s]@Merge6f1a0d6b662fae85 -> [s*H]@Shift594e1a6314829db7
		t_2 = torch.permute(t_2, (0, 2, 3, 1, 4, ))
		t_2 = torch.reshape(t_2, (1024, 128, 28, 14, ))

		# [s*H]@Shift594e1a6314829db7 -> [s*H]@Split7ee86503d19bbef6
		t_2 = torch.roll(t_2, self.shift_direction, 2)

		# [s*H]@Split7ee86503d19bbef6 -> [H]@Iterator96123ba3184da39c, [s]@Shareb15a7faee0f8b868
		t_2 = torch.reshape(t_2, (1024, 128, 14, 2, 14, ))

		# [H]@Shiftdbd5b2e652804221 -> [H]@Unfold0063bc810b9e1e60
		t_2 = torch.roll(t_2, self.shift_direction, 4)

		# [H]@Unfold0063bc810b9e1e60 -> [H]@Iteratorb0a1def4ad5784ec, [k_1]@Share26cfa48d169008e4
		t_2 = torch.reshape(t_2, (1024, 3584, 14, 1, ))
		t_2 = torch.nn.functional.unfold(t_2, (3, 1, ), padding=(1, 0, ))
		t_2 = torch.reshape(t_2, (1024, 128, 14, 2, 3, 14, ))

		# Permute to match the output of this subgraph.
		t_2 = torch.permute(t_2, (0, 1, 2, 3, 5, 4, ))

		# Perform contraction.
		t_3 = torch.einsum("mlnkoj, klji -> mnoi", t_2, in_1)

		# Permute to match the output of this subgraph.
		t_3 = torch.permute(t_3, (0, 3, 1, 2, ))

		# No need to crop the output tensor.
		y = t_3

		return y

class kernel_generated_5(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([2, 128, 3, 512]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]

		# No contraction needed.
		t_2 = in_0

		# [C_in]@Spliteef7ce0b7703d88a -> [s]@Merge6f1a0d6b662fae85, [s^-1*C_in]@Share8de6f167adbbf8aa
		t_2 = torch.reshape(t_2, (1024, 2, 128, 7, 7, ))

		# [H]@Merge6f1a0d6b662fae84, [s]@Merge6f1a0d6b662fae85 -> [s*H]@Shift594e1a6314829db7
		t_2 = torch.permute(t_2, (0, 2, 3, 1, 4, ))
		t_2 = torch.reshape(t_2, (1024, 128, 14, 7, ))

		# [s*H]@Shift594e1a6314829db7 -> [s*H]@Split7ee86503d19bbef6
		t_2 = torch.roll(t_2, self.shift_direction, 2)

		# [s*H]@Split7ee86503d19bbef6 -> [H]@Iterator96123ba3184da39c, [s]@Shareb15a7faee0f8b868
		t_2 = torch.reshape(t_2, (1024, 128, 7, 2, 7, ))

		# [H]@Shiftdbd5b2e652804221 -> [H]@Unfold0063bc810b9e1e60
		t_2 = torch.roll(t_2, self.shift_direction, 4)

		# [H]@Unfold0063bc810b9e1e60 -> [H]@Iteratorb0a1def4ad5784ec, [k_1]@Share26cfa48d169008e4
		t_2 = torch.reshape(t_2, (1024, 1792, 7, 1, ))
		t_2 = torch.nn.functional.unfold(t_2, (3, 1, ), padding=(1, 0, ))
		t_2 = torch.reshape(t_2, (1024, 128, 7, 2, 3, 7, ))

		# Permute to match the output of this subgraph.
		t_2 = torch.permute(t_2, (0, 1, 2, 3, 5, 4, ))

		# Perform contraction.
		t_3 = torch.einsum("mlnkoj, klji -> mnoi", t_2, in_1)

		# Permute to match the output of this subgraph.
		t_3 = torch.permute(t_3, (0, 3, 1, 2, ))

		# No need to crop the output tensor.
		y = t_3

		return y

class kernel_generated_6(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([2, 256, 3, 512]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]

		# No contraction needed.
		t_2 = in_0

		# [C_in]@Spliteef7ce0b7703d88a -> [s]@Merge6f1a0d6b662fae85, [s^-1*C_in]@Share8de6f167adbbf8aa
		t_2 = torch.reshape(t_2, (1024, 2, 256, 7, 7, ))

		# [H]@Merge6f1a0d6b662fae84, [s]@Merge6f1a0d6b662fae85 -> [s*H]@Shift594e1a6314829db7
		t_2 = torch.permute(t_2, (0, 2, 3, 1, 4, ))
		t_2 = torch.reshape(t_2, (1024, 256, 14, 7, ))

		# [s*H]@Shift594e1a6314829db7 -> [s*H]@Split7ee86503d19bbef6
		t_2 = torch.roll(t_2, self.shift_direction, 2)

		# [s*H]@Split7ee86503d19bbef6 -> [H]@Iterator96123ba3184da39c, [s]@Shareb15a7faee0f8b868
		t_2 = torch.reshape(t_2, (1024, 256, 7, 2, 7, ))

		# [H]@Shiftdbd5b2e652804221 -> [H]@Unfold0063bc810b9e1e60
		t_2 = torch.roll(t_2, self.shift_direction, 4)

		# [H]@Unfold0063bc810b9e1e60 -> [H]@Iteratorb0a1def4ad5784ec, [k_1]@Share26cfa48d169008e4
		t_2 = torch.reshape(t_2, (1024, 3584, 7, 1, ))
		t_2 = torch.nn.functional.unfold(t_2, (3, 1, ), padding=(1, 0, ))
		t_2 = torch.reshape(t_2, (1024, 256, 7, 2, 3, 7, ))

		# Permute to match the output of this subgraph.
		t_2 = torch.permute(t_2, (0, 1, 2, 3, 5, 4, ))

		# Perform contraction.
		t_3 = torch.einsum("mlnkoj, klji -> mnoi", t_2, in_1)

		# Permute to match the output of this subgraph.
		t_3 = torch.permute(t_3, (0, 3, 1, 2, ))

		# No need to crop the output tensor.
		y = t_3

		return y

