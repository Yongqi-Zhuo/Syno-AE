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
        interface_0_out_0x56459a9d6050 [label="N", shape=none];
        interface_0_out_0x56459a9d6078 [label="C_out", shape=none];
        interface_0_out_0x56459a9d60a0 [label="H", shape=none];
        interface_0_out_0x56459a9d60c8 [label="H", shape=none];
    }
    {
        rank = same;
        interface_0_out_0x56459a9d6050;
        interface_0_out_0x56459a9d6078;
        interface_0_out_0x56459a9d60a0;
        interface_0_out_0x56459a9d60c8;
    }
    // Input 0.
    subgraph cluster_subgraph_0_in_0 {
        label = "";
        interface_0_in_0x56459a9d6050 [label="N", shape=none];
        interface_0_in_0x56459c25a880 [label="s", shape=none];
        interface_0_in_0x56459c25a898 [label="s^-1*C_out", shape=none];
        interface_0_in_0x56459c259020 [label="H", shape=none];
        interface_0_in_0x56459a9d60c8 [label="H", shape=none];
    }
    {
        rank = same;
        interface_0_in_0x56459a9d6050;
        interface_0_in_0x56459c25a880;
        interface_0_in_0x56459c25a898;
        interface_0_in_0x56459c259020;
        interface_0_in_0x56459a9d60c8;
    }
    // Op's.
    op_0x56459c259000 [label="Shift"];
    op_0x56459c25a840 [label="Merge"];
    // Dimension's.
    interface_0_in_0x56459a9d6050 -> interface_0_out_0x56459a9d6050 [label="N"];
    op_0x56459c25a840 -> interface_0_out_0x56459a9d6078 [label="C_out"];
    op_0x56459c259000 -> interface_0_out_0x56459a9d60a0 [label="H"];
    interface_0_in_0x56459a9d60c8 -> interface_0_out_0x56459a9d60c8 [label="H"];
    interface_0_in_0x56459c259020 -> op_0x56459c259000 [label="H"];
    interface_0_in_0x56459c25a880 -> op_0x56459c25a840 [label="s"];
    interface_0_in_0x56459c25a898 -> op_0x56459c25a840 [label="s^-1*C_out"];
}

// Stage tensor.
subgraph cluster_subgraph_1 {
    label = "Subgraph 1";
    // Reductions.
    reduce_0x7fdbac005768 [label="Sum", shape=box];
    reduce_0x7fdbac001ee8 [label="Sum", shape=box];
    // Output.
    subgraph cluster_subgraph_1_out {
        label = "";
        interface_1_out_0x56459a9d6050 [label="N", shape=none];
        interface_1_out_0x56459c25a880 [label="s", shape=none];
        interface_1_out_0x56459c25a898 [label="s^-1*C_out", shape=none];
        interface_1_out_0x56459c259020 [label="H", shape=none];
        interface_1_out_0x56459a9d60c8 [label="H", shape=none];
    }
    {
        rank = same;
        reduce_0x7fdbac005768;
        reduce_0x7fdbac001ee8;
        interface_1_out_0x56459a9d6050;
        interface_1_out_0x56459c25a880;
        interface_1_out_0x56459c25a898;
        interface_1_out_0x56459c259020;
        interface_1_out_0x56459a9d60c8;
    }
    // Input 0.
    subgraph cluster_subgraph_1_in_0 {
        label = "";
        interface_1_in_0x56459a9d6050 [label="N", shape=none];
        interface_1_in_0x56459c25a880 [label="s", shape=none];
        interface_1_in_0x56459c2582f0 [label="s^-1*C_in", shape=none];
        interface_1_in_0x56459c259020 [label="H", shape=none];
        interface_1_in_0x56459c258340 [label="k_2", shape=none];
        interface_1_in_0x56459a9d60c8 [label="H", shape=none];
    }
    // Input 1.
    subgraph cluster_subgraph_1_in_1 {
        label = "";
        interface_1_in_0x56459c258308 [label="s^-1*C_in", shape=none];
        interface_1_in_0x56459c2583f8 [label="s^-1*C_out", shape=none];
        interface_1_in_0x56459c258358 [label="k_2", shape=none];
    }
    {
        rank = same;
        interface_1_in_0x56459a9d6050;
        interface_1_in_0x56459c25a880;
        interface_1_in_0x56459c2582f0;
        interface_1_in_0x56459c259020;
        interface_1_in_0x56459c258340;
        interface_1_in_0x56459a9d60c8;
        interface_1_in_0x56459c258308;
        interface_1_in_0x56459c2583f8;
        interface_1_in_0x56459c258358;
    }
    // Op's.
    op_0x56459c2582d0 [label="Share"];
    op_0x56459c258320 [label="Share"];
    op_0x56459c2583c0 [label="Share"];
    op_0x56459c258798 [label="Expand"];
    // Dimension's.
    interface_1_in_0x56459a9d6050 -> interface_1_out_0x56459a9d6050 [label="N"];
    interface_1_in_0x56459a9d60c8 -> interface_1_out_0x56459a9d60c8 [label="H"];
    interface_1_in_0x56459c2582f0 -> op_0x56459c2582d0 [label="s^-1*C_in"];
    interface_1_in_0x56459c258308 -> op_0x56459c2582d0 [label="s^-1*C_in"];
    interface_1_in_0x56459c258340 -> op_0x56459c258320 [label="k_2"];
    interface_1_in_0x56459c258358 -> op_0x56459c258320 [label="k_2"];
    op_0x56459c258798 -> op_0x56459c2583c0 [label="s^-1*C_out"];
    interface_1_in_0x56459c2583f8 -> op_0x56459c2583c0 [label="s^-1*C_out"];
    interface_1_in_0x56459c259020 -> interface_1_out_0x56459c259020 [label="H"];
    interface_1_in_0x56459c25a880 -> interface_1_out_0x56459c25a880 [label="s"];
    op_0x56459c2583c0 -> interface_1_out_0x56459c25a898 [label="s^-1*C_out"];
    op_0x56459c258320 -> reduce_0x7fdbac001ee8 [label="k_2"];
    op_0x56459c2582d0 -> reduce_0x7fdbac005768 [label="s^-1*C_in"];
}

// Stage tensor.
subgraph cluster_subgraph_2 {
    label = "Subgraph 2";
    // Reductions.
    // Output.
    subgraph cluster_subgraph_2_out {
        label = "";
        interface_2_out_0x56459a9d6050 [label="N", shape=none];
        interface_2_out_0x56459c25a880 [label="s", shape=none];
        interface_2_out_0x56459c2582f0 [label="s^-1*C_in", shape=none];
        interface_2_out_0x56459c259020 [label="H", shape=none];
        interface_2_out_0x56459c258340 [label="k_2", shape=none];
        interface_2_out_0x56459a9d60c8 [label="H", shape=none];
    }
    {
        rank = same;
        interface_2_out_0x56459a9d6050;
        interface_2_out_0x56459c25a880;
        interface_2_out_0x56459c2582f0;
        interface_2_out_0x56459c259020;
        interface_2_out_0x56459c258340;
        interface_2_out_0x56459a9d60c8;
    }
    // Input 0.
    subgraph cluster_subgraph_2_in_0 {
        label = "";
        interface_2_in_0x56459a9d6050 [label="N", shape=none];
        interface_2_in_0x56459c266040 [label="C_in", shape=none];
        interface_2_in_0x56459c259020 [label="H", shape=none];
        interface_2_in_0x56459c25c768 [label="H", shape=none];
    }
    {
        rank = same;
        interface_2_in_0x56459a9d6050;
        interface_2_in_0x56459c266040;
        interface_2_in_0x56459c259020;
        interface_2_in_0x56459c25c768;
    }
    // Op's.
    op_0x56459c25c740 [label="Unfold"];
    op_0x56459c266000 [label="Split"];
    // Dimension's.
    interface_2_in_0x56459a9d6050 -> interface_2_out_0x56459a9d6050 [label="N"];
    op_0x56459c25c740 -> interface_2_out_0x56459a9d60c8 [label="H"];
    op_0x56459c266000 -> interface_2_out_0x56459c2582f0 [label="s^-1*C_in"];
    op_0x56459c25c740 -> interface_2_out_0x56459c258340 [label="k_2"];
    interface_2_in_0x56459c259020 -> interface_2_out_0x56459c259020 [label="H"];
    op_0x56459c266000 -> interface_2_out_0x56459c25a880 [label="s"];
    interface_2_in_0x56459c25c768 -> op_0x56459c25c740 [label="H"];
    interface_2_in_0x56459c266040 -> op_0x56459c266000 [label="C_in"];
}

// Input tensor.
subgraph cluster_subgraph_3 {
    label = "Input 0";
    interface_3_out_0x56459a9d6050 [label="N", shape=none];
    interface_3_out_0x56459c266040 [label="C_in", shape=none];
    interface_3_out_0x56459c259020 [label="H", shape=none];
    interface_3_out_0x56459c25c768 [label="H", shape=none];
}

interface_3_out_0x56459a9d6050 -> interface_2_in_0x56459a9d6050;
interface_3_out_0x56459c266040 -> interface_2_in_0x56459c266040;
interface_3_out_0x56459c259020 -> interface_2_in_0x56459c259020;
interface_3_out_0x56459c25c768 -> interface_2_in_0x56459c25c768;

interface_2_out_0x56459a9d6050 -> interface_1_in_0x56459a9d6050;
interface_2_out_0x56459c25a880 -> interface_1_in_0x56459c25a880;
interface_2_out_0x56459c2582f0 -> interface_1_in_0x56459c2582f0;
interface_2_out_0x56459c259020 -> interface_1_in_0x56459c259020;
interface_2_out_0x56459c258340 -> interface_1_in_0x56459c258340;
interface_2_out_0x56459a9d60c8 -> interface_1_in_0x56459a9d60c8;

// Input tensor.
subgraph cluster_subgraph_4 {
    label = "Input 1";
    interface_4_out_0x56459c258308 [label="s^-1*C_in", shape=none];
    interface_4_out_0x56459c2583f8 [label="s^-1*C_out", shape=none];
    interface_4_out_0x56459c258358 [label="k_2", shape=none];
}

interface_4_out_0x56459c258308 -> interface_1_in_0x56459c258308;
interface_4_out_0x56459c2583f8 -> interface_1_in_0x56459c2583f8;
interface_4_out_0x56459c258358 -> interface_1_in_0x56459c258358;

interface_1_out_0x56459a9d6050 -> interface_0_in_0x56459a9d6050;
interface_1_out_0x56459c25a880 -> interface_0_in_0x56459c25a880;
interface_1_out_0x56459c25a898 -> interface_0_in_0x56459c25a898;
interface_1_out_0x56459c259020 -> interface_0_in_0x56459c259020;
interface_1_out_0x56459a9d60c8 -> interface_0_in_0x56459a9d60c8;

{
    rank = same;
    interface_3_out_0x56459a9d6050;
    interface_3_out_0x56459c266040;
    interface_3_out_0x56459c259020;
    interface_3_out_0x56459c25c768;
    interface_4_out_0x56459c258308;
    interface_4_out_0x56459c2583f8;
    interface_4_out_0x56459c258358;
}
subgraph cluster_subgraph_output {
    label = "Output";
    interface_5_in_0x56459a9d6050 [label="N", shape=none];
    interface_5_in_0x56459a9d6078 [label="C_out", shape=none];
    interface_5_in_0x56459a9d60a0 [label="H", shape=none];
    interface_5_in_0x56459a9d60c8 [label="H", shape=none];
}
interface_0_out_0x56459a9d6050 -> interface_5_in_0x56459a9d6050;
interface_0_out_0x56459a9d6078 -> interface_5_in_0x56459a9d6078;
interface_0_out_0x56459a9d60a0 -> interface_5_in_0x56459a9d60a0;
interface_0_out_0x56459a9d60c8 -> interface_5_in_0x56459a9d60c8;

}

"""
class kernel_generated_0(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([12, 12, 7]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]

		# No contraction needed.
		t_2 = in_0

		# [C_in]@Split69dd43e05c8c5ddb -> [s]@Merge03a73148aa81036c, [s^-1*C_in]@Share8de6f167adbbf8aa
		t_2 = torch.reshape(t_2, (1, 2, 12, 112, 112, ))

		# [H]@Unfold411df364a19ddc8b -> [H]@Iteratorb0a1def4ad5784ec, [k_2]@Sharec0d065a85569cbbe
		t_2 = torch.reshape(t_2, (1, 2688, 112, 1, ))
		t_2 = torch.nn.functional.unfold(t_2, (7, 1, ), padding=(3, 0, ))
		t_2 = torch.reshape(t_2, (1, 2, 12, 112, 7, 112, ))

		# Perform contraction.
		t_3 = torch.einsum("loinjm, ikj -> loknm", t_2, in_1)

		# No contraction needed.
		t_4 = t_3

		# [s]@Merge03a73148aa81036c, [s^-1*C_out]@Merge03a73148aa81036f -> [C_out]@Iteratorc7f8eb87a5a0a9e0
		t_4 = torch.reshape(t_4, (1, 24, 112, 112, ))

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
			torch.randn([12, 48, 7]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]

		# No contraction needed.
		t_2 = in_0

		# [C_in]@Split69dd43e05c8c5ddb -> [s]@Merge03a73148aa81036c, [s^-1*C_in]@Share8de6f167adbbf8aa
		t_2 = torch.reshape(t_2, (1, 2, 12, 56, 56, ))

		# [H]@Unfold411df364a19ddc8b -> [H]@Iteratorb0a1def4ad5784ec, [k_2]@Sharec0d065a85569cbbe
		t_2 = torch.reshape(t_2, (1, 1344, 56, 1, ))
		t_2 = torch.nn.functional.unfold(t_2, (7, 1, ), padding=(3, 0, ))
		t_2 = torch.reshape(t_2, (1, 2, 12, 56, 7, 56, ))

		# Perform contraction.
		t_3 = torch.einsum("loinjm, ikj -> loknm", t_2, in_1)

		# No contraction needed.
		t_4 = t_3

		# [s]@Merge03a73148aa81036c, [s^-1*C_out]@Merge03a73148aa81036f -> [C_out]@Iteratorc7f8eb87a5a0a9e0
		t_4 = torch.reshape(t_4, (1, 96, 56, 56, ))

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
			torch.randn([24, 96, 7]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]

		# No contraction needed.
		t_2 = in_0

		# [C_in]@Split69dd43e05c8c5ddb -> [s]@Merge03a73148aa81036c, [s^-1*C_in]@Share8de6f167adbbf8aa
		t_2 = torch.reshape(t_2, (1, 2, 24, 56, 56, ))

		# [H]@Unfold411df364a19ddc8b -> [H]@Iteratorb0a1def4ad5784ec, [k_2]@Sharec0d065a85569cbbe
		t_2 = torch.reshape(t_2, (1, 2688, 56, 1, ))
		t_2 = torch.nn.functional.unfold(t_2, (7, 1, ), padding=(3, 0, ))
		t_2 = torch.reshape(t_2, (1, 2, 24, 56, 7, 56, ))

		# Perform contraction.
		t_3 = torch.einsum("loinjm, ikj -> loknm", t_2, in_1)

		# No contraction needed.
		t_4 = t_3

		# [s]@Merge03a73148aa81036c, [s^-1*C_out]@Merge03a73148aa81036f -> [C_out]@Iteratorc7f8eb87a5a0a9e0
		t_4 = torch.reshape(t_4, (1, 192, 56, 56, ))

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
			torch.randn([24, 96, 7]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]

		# No contraction needed.
		t_2 = in_0

		# [C_in]@Split69dd43e05c8c5ddb -> [s]@Merge03a73148aa81036c, [s^-1*C_in]@Share8de6f167adbbf8aa
		t_2 = torch.reshape(t_2, (1, 2, 24, 28, 28, ))

		# [H]@Unfold411df364a19ddc8b -> [H]@Iteratorb0a1def4ad5784ec, [k_2]@Sharec0d065a85569cbbe
		t_2 = torch.reshape(t_2, (1, 1344, 28, 1, ))
		t_2 = torch.nn.functional.unfold(t_2, (7, 1, ), padding=(3, 0, ))
		t_2 = torch.reshape(t_2, (1, 2, 24, 28, 7, 28, ))

		# Perform contraction.
		t_3 = torch.einsum("loinjm, ikj -> loknm", t_2, in_1)

		# No contraction needed.
		t_4 = t_3

		# [s]@Merge03a73148aa81036c, [s^-1*C_out]@Merge03a73148aa81036f -> [C_out]@Iteratorc7f8eb87a5a0a9e0
		t_4 = torch.reshape(t_4, (1, 192, 28, 28, ))

		# [H]@Shift41a433c05e30b91d -> [H]@Iterator96123ba3184da39c
		t_4 = torch.roll(t_4, self.shift_direction, 2)

		# No need to crop the output tensor.
		y = t_4

		return y

class kernel_generated_4(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([32, 128, 7]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]

		# No contraction needed.
		t_2 = in_0

		# [C_in]@Split69dd43e05c8c5ddb -> [s]@Merge03a73148aa81036c, [s^-1*C_in]@Share8de6f167adbbf8aa
		t_2 = torch.reshape(t_2, (1, 2, 32, 28, 28, ))

		# [H]@Unfold411df364a19ddc8b -> [H]@Iteratorb0a1def4ad5784ec, [k_2]@Sharec0d065a85569cbbe
		t_2 = torch.reshape(t_2, (1, 1792, 28, 1, ))
		t_2 = torch.nn.functional.unfold(t_2, (7, 1, ), padding=(3, 0, ))
		t_2 = torch.reshape(t_2, (1, 2, 32, 28, 7, 28, ))

		# Perform contraction.
		t_3 = torch.einsum("loinjm, ikj -> loknm", t_2, in_1)

		# No contraction needed.
		t_4 = t_3

		# [s]@Merge03a73148aa81036c, [s^-1*C_out]@Merge03a73148aa81036f -> [C_out]@Iteratorc7f8eb87a5a0a9e0
		t_4 = torch.reshape(t_4, (1, 256, 28, 28, ))

		# [H]@Shift41a433c05e30b91d -> [H]@Iterator96123ba3184da39c
		t_4 = torch.roll(t_4, self.shift_direction, 2)

		# No need to crop the output tensor.
		y = t_4

		return y

