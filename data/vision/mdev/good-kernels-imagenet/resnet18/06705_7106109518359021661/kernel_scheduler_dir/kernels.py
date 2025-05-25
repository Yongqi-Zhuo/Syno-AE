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
    reduce_0x7effd8001ab0 [label="Sum", shape=box];
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
        reduce_0x7effd8001ab0;
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
        interface_0_in_0x55a3093b8810 [label="k_1", shape=none];
        interface_0_in_0x55a308c0a968 [label="H", shape=none];
        interface_0_in_0x55a3093b88b0 [label="k_1", shape=none];
    }
    // Input 1.
    subgraph cluster_subgraph_0_in_1 {
        label = "";
        interface_0_in_0x55a3093ce4a8 [label="s^-1*C_in", shape=none];
        interface_0_in_0x55a3093b8828 [label="k_1", shape=none];
        interface_0_in_0x55a3093b88c8 [label="k_1", shape=none];
        interface_0_in_0x55a3093b8738 [label="C_out", shape=none];
    }
    {
        rank = same;
        interface_0_in_0x55a308c0a8f0;
        interface_0_in_0x55a3093ce490;
        interface_0_in_0x55a308c0a940;
        interface_0_in_0x55a3093b8810;
        interface_0_in_0x55a308c0a968;
        interface_0_in_0x55a3093b88b0;
        interface_0_in_0x55a3093ce4a8;
        interface_0_in_0x55a3093b8828;
        interface_0_in_0x55a3093b88c8;
        interface_0_in_0x55a3093b8738;
    }
    // Op's.
    op_0x55a3093b8700 [label="Share"];
    op_0x55a3093b87f0 [label="Share"];
    op_0x55a3093b8890 [label="Share"];
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
    interface_0_in_0x55a3093b88b0 -> op_0x55a3093b8890 [label="k_1"];
    interface_0_in_0x55a3093b88c8 -> op_0x55a3093b8890 [label="k_1"];
    interface_0_in_0x55a3093ce490 -> op_0x55a3093ce470 [label="s^-1*C_in"];
    interface_0_in_0x55a3093ce4a8 -> op_0x55a3093ce470 [label="s^-1*C_in"];
    op_0x55a3093b87f0 -> reduce_0x7effd8001a98 [label="k_1"];
    op_0x55a3093b8890 -> reduce_0x7effd8001ab0 [label="k_1"];
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
        interface_1_out_0x55a3093b8810 [label="k_1", shape=none];
        interface_1_out_0x55a308c0a968 [label="H", shape=none];
        interface_1_out_0x55a3093b88b0 [label="k_1", shape=none];
    }
    {
        rank = same;
        interface_1_out_0x55a308c0a8f0;
        interface_1_out_0x55a3093ce490;
        interface_1_out_0x55a308c0a940;
        interface_1_out_0x55a3093b8810;
        interface_1_out_0x55a308c0a968;
        interface_1_out_0x55a3093b88b0;
    }
    // Input 0.
    subgraph cluster_subgraph_1_in_0 {
        label = "";
        interface_1_in_0x55a308c0a8f0 [label="N", shape=none];
        interface_1_in_0x55a3093ce490 [label="s^-1*C_in", shape=none];
        interface_1_in_0x55a3093bb8e8 [label="H", shape=none];
        interface_1_in_0x55a308c0a968 [label="H", shape=none];
        interface_1_in_0x55a3093b88b0 [label="k_1", shape=none];
    }
    {
        rank = same;
        interface_1_in_0x55a308c0a8f0;
        interface_1_in_0x55a3093ce490;
        interface_1_in_0x55a3093bb8e8;
        interface_1_in_0x55a308c0a968;
        interface_1_in_0x55a3093b88b0;
    }
    // Op's.
    op_0x55a3093bb8c0 [label="Unfold"];
    // Dimension's.
    interface_1_in_0x55a308c0a8f0 -> interface_1_out_0x55a308c0a8f0 [label="N"];
    op_0x55a3093bb8c0 -> interface_1_out_0x55a308c0a940 [label="H"];
    interface_1_in_0x55a308c0a968 -> interface_1_out_0x55a308c0a968 [label="H"];
    op_0x55a3093bb8c0 -> interface_1_out_0x55a3093b8810 [label="k_1"];
    interface_1_in_0x55a3093b88b0 -> interface_1_out_0x55a3093b88b0 [label="k_1"];
    interface_1_in_0x55a3093bb8e8 -> op_0x55a3093bb8c0 [label="H"];
    interface_1_in_0x55a3093ce490 -> interface_1_out_0x55a3093ce490 [label="s^-1*C_in"];
}

// Stage tensor.
subgraph cluster_subgraph_2 {
    label = "Subgraph 2";
    // Reductions.
    reduce_0x7effd8002ce8 [label="Sum", shape=box];
    // Output.
    subgraph cluster_subgraph_2_out {
        label = "";
        interface_2_out_0x55a308c0a8f0 [label="N", shape=none];
        interface_2_out_0x55a3093ce490 [label="s^-1*C_in", shape=none];
        interface_2_out_0x55a3093bb8e8 [label="H", shape=none];
        interface_2_out_0x55a308c0a968 [label="H", shape=none];
        interface_2_out_0x55a3093b88b0 [label="k_1", shape=none];
    }
    {
        rank = same;
        reduce_0x7effd8002ce8;
        interface_2_out_0x55a308c0a8f0;
        interface_2_out_0x55a3093ce490;
        interface_2_out_0x55a3093bb8e8;
        interface_2_out_0x55a308c0a968;
        interface_2_out_0x55a3093b88b0;
    }
    // Input 0.
    subgraph cluster_subgraph_2_in_0 {
        label = "";
        interface_2_in_0x55a308c0a8f0 [label="N", shape=none];
        interface_2_in_0x55a308d94f00 [label="C_in", shape=none];
        interface_2_in_0x55a3093bb8e8 [label="H", shape=none];
        interface_2_in_0x55a3093b97a0 [label="H", shape=none];
    }
    {
        rank = same;
        interface_2_in_0x55a308c0a8f0;
        interface_2_in_0x55a308d94f00;
        interface_2_in_0x55a3093bb8e8;
        interface_2_in_0x55a3093b97a0;
    }
    // Op's.
    op_0x55a308d94ec0 [label="Split"];
    op_0x55a3093b96f0 [label="Shift"];
    op_0x55a3093b9780 [label="Shift"];
    op_0x55a3093bb6c0 [label="Merge"];
    op_0x55a3093bba00 [label="Unfold"];
    op_0x55a3093bde00 [label="Split"];
    // Dimension's.
    interface_2_in_0x55a308c0a8f0 -> interface_2_out_0x55a308c0a8f0 [label="N"];
    op_0x55a3093bde00 -> interface_2_out_0x55a308c0a968 [label="H"];
    interface_2_in_0x55a308d94f00 -> op_0x55a308d94ec0 [label="C_in"];
    op_0x55a3093bba00 -> interface_2_out_0x55a3093b88b0 [label="k_1"];
    op_0x55a3093bb6c0 -> op_0x55a3093b96f0 [label="s*H"];
    interface_2_in_0x55a3093b97a0 -> op_0x55a3093b9780 [label="H"];
    op_0x55a3093bba00 -> op_0x55a3093bb6c0 [label="H"];
    op_0x55a308d94ec0 -> op_0x55a3093bb6c0 [label="s"];
    interface_2_in_0x55a3093bb8e8 -> interface_2_out_0x55a3093bb8e8 [label="H"];
    op_0x55a3093b9780 -> op_0x55a3093bba00 [label="H"];
    op_0x55a3093b96f0 -> op_0x55a3093bde00 [label="s*H"];
    op_0x55a308d94ec0 -> interface_2_out_0x55a3093ce490 [label="s^-1*C_in"];
    op_0x55a3093bde00 -> reduce_0x7effd8002ce8 [label="s"];
}

// Input tensor.
subgraph cluster_subgraph_3 {
    label = "Input 0";
    interface_3_out_0x55a308c0a8f0 [label="N", shape=none];
    interface_3_out_0x55a308d94f00 [label="C_in", shape=none];
    interface_3_out_0x55a3093bb8e8 [label="H", shape=none];
    interface_3_out_0x55a3093b97a0 [label="H", shape=none];
}

interface_3_out_0x55a308c0a8f0 -> interface_2_in_0x55a308c0a8f0;
interface_3_out_0x55a308d94f00 -> interface_2_in_0x55a308d94f00;
interface_3_out_0x55a3093bb8e8 -> interface_2_in_0x55a3093bb8e8;
interface_3_out_0x55a3093b97a0 -> interface_2_in_0x55a3093b97a0;

interface_2_out_0x55a308c0a8f0 -> interface_1_in_0x55a308c0a8f0;
interface_2_out_0x55a3093ce490 -> interface_1_in_0x55a3093ce490;
interface_2_out_0x55a3093bb8e8 -> interface_1_in_0x55a3093bb8e8;
interface_2_out_0x55a308c0a968 -> interface_1_in_0x55a308c0a968;
interface_2_out_0x55a3093b88b0 -> interface_1_in_0x55a3093b88b0;

interface_1_out_0x55a308c0a8f0 -> interface_0_in_0x55a308c0a8f0;
interface_1_out_0x55a3093ce490 -> interface_0_in_0x55a3093ce490;
interface_1_out_0x55a308c0a940 -> interface_0_in_0x55a308c0a940;
interface_1_out_0x55a3093b8810 -> interface_0_in_0x55a3093b8810;
interface_1_out_0x55a308c0a968 -> interface_0_in_0x55a308c0a968;
interface_1_out_0x55a3093b88b0 -> interface_0_in_0x55a3093b88b0;

// Input tensor.
subgraph cluster_subgraph_4 {
    label = "Input 1";
    interface_4_out_0x55a3093ce4a8 [label="s^-1*C_in", shape=none];
    interface_4_out_0x55a3093b8828 [label="k_1", shape=none];
    interface_4_out_0x55a3093b88c8 [label="k_1", shape=none];
    interface_4_out_0x55a3093b8738 [label="C_out", shape=none];
}

interface_4_out_0x55a3093ce4a8 -> interface_0_in_0x55a3093ce4a8;
interface_4_out_0x55a3093b8828 -> interface_0_in_0x55a3093b8828;
interface_4_out_0x55a3093b88c8 -> interface_0_in_0x55a3093b88c8;
interface_4_out_0x55a3093b8738 -> interface_0_in_0x55a3093b8738;

{
    rank = same;
    interface_3_out_0x55a308c0a8f0;
    interface_3_out_0x55a308d94f00;
    interface_3_out_0x55a3093bb8e8;
    interface_3_out_0x55a3093b97a0;
    interface_4_out_0x55a3093ce4a8;
    interface_4_out_0x55a3093b8828;
    interface_4_out_0x55a3093b88c8;
    interface_4_out_0x55a3093b8738;
}
subgraph cluster_subgraph_output {
    label = "Output";
    interface_5_in_0x55a308c0a8f0 [label="N", shape=none];
    interface_5_in_0x55a308c0a918 [label="C_out", shape=none];
    interface_5_in_0x55a308c0a940 [label="H", shape=none];
    interface_5_in_0x55a308c0a968 [label="H", shape=none];
}
interface_0_out_0x55a308c0a8f0 -> interface_5_in_0x55a308c0a8f0;
interface_0_out_0x55a308c0a918 -> interface_5_in_0x55a308c0a918;
interface_0_out_0x55a308c0a940 -> interface_5_in_0x55a308c0a940;
interface_0_out_0x55a308c0a968 -> interface_5_in_0x55a308c0a968;

}

"""
class kernel_generated_0(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([32, 3, 3, 64]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]

		# No contraction needed.
		t_2 = in_0

		# [H]@Shift2906cc2f461505d0 -> [H]@Unfoldeeb0aec8202b574f
		t_2 = torch.roll(t_2, self.shift_direction, 3)

		# [H]@Unfoldeeb0aec8202b574f -> [H]@Merge0bce4580e08cd69c, [k_1]@Share02da0a485106ab3d
		t_2 = torch.reshape(t_2, (1024, 3584, 56, 1, ))
		t_2 = torch.nn.functional.unfold(t_2, (3, 1, ), padding=(1, 0, ))
		t_2 = torch.reshape(t_2, (1024, 64, 56, 3, 56, ))

		# [C_in]@Split3524ae88ad3a30bc -> [s]@Merge0bce4580e08cd69d, [s^-1*C_in]@Share8de6f167adbbf8aa
		t_2 = torch.reshape(t_2, (1024, 2, 32, 56, 3, 56, ))

		# [H]@Merge0bce4580e08cd69c, [s]@Merge0bce4580e08cd69d -> [s*H]@Shift8a9f243357a7f717
		t_2 = torch.permute(t_2, (0, 2, 3, 4, 5, 1, ))
		t_2 = torch.reshape(t_2, (1024, 32, 56, 3, 112, ))

		# [s*H]@Shift8a9f243357a7f717 -> [s*H]@Split511946b410b86996
		t_2 = torch.roll(t_2, self.shift_direction, 4)

		# [s*H]@Split511946b410b86996 -> [H]@Iteratorb0a1def4ad5784ec, [s]@Reduced95c644a3c072d9a
		t_2 = torch.reshape(t_2, (1024, 32, 56, 3, 56, 2, ))

		# [s]@Reduce
		t_2 = torch.sum(t_2, dim=(5, ))

		# Permute to match the output of this subgraph.
		t_2 = torch.permute(t_2, (0, 1, 2, 4, 3, ))

		# No contraction needed.
		t_3 = t_2

		# [H]@Unfold4d77c1e3da5bca44 -> [H]@Iterator96123ba3184da39c, [k_1]@Share26cfa48d169008e4
		t_3 = torch.reshape(t_3, (1024, 32, 56, 168, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (1024, 32, 3, 56, 56, 3, ))

		# Permute to match the output of this subgraph.
		t_3 = torch.permute(t_3, (0, 1, 3, 2, 4, 5, ))

		# Perform contraction.
		t_4 = torch.einsum("mlnjok, ljki -> mnoi", t_3, in_1)

		# Permute to match the output of this subgraph.
		t_4 = torch.permute(t_4, (0, 3, 1, 2, ))

		# No need to crop the output tensor.
		y = t_4

		return y

class kernel_generated_1(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([32, 3, 3, 128]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]

		# No contraction needed.
		t_2 = in_0

		# [H]@Shift2906cc2f461505d0 -> [H]@Unfoldeeb0aec8202b574f
		t_2 = torch.roll(t_2, self.shift_direction, 3)

		# [H]@Unfoldeeb0aec8202b574f -> [H]@Merge0bce4580e08cd69c, [k_1]@Share02da0a485106ab3d
		t_2 = torch.reshape(t_2, (1024, 1792, 28, 1, ))
		t_2 = torch.nn.functional.unfold(t_2, (3, 1, ), padding=(1, 0, ))
		t_2 = torch.reshape(t_2, (1024, 64, 28, 3, 28, ))

		# [C_in]@Split3524ae88ad3a30bc -> [s]@Merge0bce4580e08cd69d, [s^-1*C_in]@Share8de6f167adbbf8aa
		t_2 = torch.reshape(t_2, (1024, 2, 32, 28, 3, 28, ))

		# [H]@Merge0bce4580e08cd69c, [s]@Merge0bce4580e08cd69d -> [s*H]@Shift8a9f243357a7f717
		t_2 = torch.permute(t_2, (0, 2, 3, 4, 5, 1, ))
		t_2 = torch.reshape(t_2, (1024, 32, 28, 3, 56, ))

		# [s*H]@Shift8a9f243357a7f717 -> [s*H]@Split511946b410b86996
		t_2 = torch.roll(t_2, self.shift_direction, 4)

		# [s*H]@Split511946b410b86996 -> [H]@Iteratorb0a1def4ad5784ec, [s]@Reduced95c644a3c072d9a
		t_2 = torch.reshape(t_2, (1024, 32, 28, 3, 28, 2, ))

		# [s]@Reduce
		t_2 = torch.sum(t_2, dim=(5, ))

		# Permute to match the output of this subgraph.
		t_2 = torch.permute(t_2, (0, 1, 2, 4, 3, ))

		# No contraction needed.
		t_3 = t_2

		# [H]@Unfold4d77c1e3da5bca44 -> [H]@Iterator96123ba3184da39c, [k_1]@Share26cfa48d169008e4
		t_3 = torch.reshape(t_3, (1024, 32, 28, 84, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (1024, 32, 3, 28, 28, 3, ))

		# Permute to match the output of this subgraph.
		t_3 = torch.permute(t_3, (0, 1, 3, 2, 4, 5, ))

		# Perform contraction.
		t_4 = torch.einsum("mlnjok, ljki -> mnoi", t_3, in_1)

		# Permute to match the output of this subgraph.
		t_4 = torch.permute(t_4, (0, 3, 1, 2, ))

		# No need to crop the output tensor.
		y = t_4

		return y

class kernel_generated_2(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([64, 3, 3, 128]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]

		# No contraction needed.
		t_2 = in_0

		# [H]@Shift2906cc2f461505d0 -> [H]@Unfoldeeb0aec8202b574f
		t_2 = torch.roll(t_2, self.shift_direction, 3)

		# [H]@Unfoldeeb0aec8202b574f -> [H]@Merge0bce4580e08cd69c, [k_1]@Share02da0a485106ab3d
		t_2 = torch.reshape(t_2, (1024, 3584, 28, 1, ))
		t_2 = torch.nn.functional.unfold(t_2, (3, 1, ), padding=(1, 0, ))
		t_2 = torch.reshape(t_2, (1024, 128, 28, 3, 28, ))

		# [C_in]@Split3524ae88ad3a30bc -> [s]@Merge0bce4580e08cd69d, [s^-1*C_in]@Share8de6f167adbbf8aa
		t_2 = torch.reshape(t_2, (1024, 2, 64, 28, 3, 28, ))

		# [H]@Merge0bce4580e08cd69c, [s]@Merge0bce4580e08cd69d -> [s*H]@Shift8a9f243357a7f717
		t_2 = torch.permute(t_2, (0, 2, 3, 4, 5, 1, ))
		t_2 = torch.reshape(t_2, (1024, 64, 28, 3, 56, ))

		# [s*H]@Shift8a9f243357a7f717 -> [s*H]@Split511946b410b86996
		t_2 = torch.roll(t_2, self.shift_direction, 4)

		# [s*H]@Split511946b410b86996 -> [H]@Iteratorb0a1def4ad5784ec, [s]@Reduced95c644a3c072d9a
		t_2 = torch.reshape(t_2, (1024, 64, 28, 3, 28, 2, ))

		# [s]@Reduce
		t_2 = torch.sum(t_2, dim=(5, ))

		# Permute to match the output of this subgraph.
		t_2 = torch.permute(t_2, (0, 1, 2, 4, 3, ))

		# No contraction needed.
		t_3 = t_2

		# [H]@Unfold4d77c1e3da5bca44 -> [H]@Iterator96123ba3184da39c, [k_1]@Share26cfa48d169008e4
		t_3 = torch.reshape(t_3, (1024, 64, 28, 84, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (1024, 64, 3, 28, 28, 3, ))

		# Permute to match the output of this subgraph.
		t_3 = torch.permute(t_3, (0, 1, 3, 2, 4, 5, ))

		# Perform contraction.
		t_4 = torch.einsum("mlnjok, ljki -> mnoi", t_3, in_1)

		# Permute to match the output of this subgraph.
		t_4 = torch.permute(t_4, (0, 3, 1, 2, ))

		# No need to crop the output tensor.
		y = t_4

		return y

class kernel_generated_3(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([64, 3, 3, 256]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]

		# No contraction needed.
		t_2 = in_0

		# [H]@Shift2906cc2f461505d0 -> [H]@Unfoldeeb0aec8202b574f
		t_2 = torch.roll(t_2, self.shift_direction, 3)

		# [H]@Unfoldeeb0aec8202b574f -> [H]@Merge0bce4580e08cd69c, [k_1]@Share02da0a485106ab3d
		t_2 = torch.reshape(t_2, (1024, 1792, 14, 1, ))
		t_2 = torch.nn.functional.unfold(t_2, (3, 1, ), padding=(1, 0, ))
		t_2 = torch.reshape(t_2, (1024, 128, 14, 3, 14, ))

		# [C_in]@Split3524ae88ad3a30bc -> [s]@Merge0bce4580e08cd69d, [s^-1*C_in]@Share8de6f167adbbf8aa
		t_2 = torch.reshape(t_2, (1024, 2, 64, 14, 3, 14, ))

		# [H]@Merge0bce4580e08cd69c, [s]@Merge0bce4580e08cd69d -> [s*H]@Shift8a9f243357a7f717
		t_2 = torch.permute(t_2, (0, 2, 3, 4, 5, 1, ))
		t_2 = torch.reshape(t_2, (1024, 64, 14, 3, 28, ))

		# [s*H]@Shift8a9f243357a7f717 -> [s*H]@Split511946b410b86996
		t_2 = torch.roll(t_2, self.shift_direction, 4)

		# [s*H]@Split511946b410b86996 -> [H]@Iteratorb0a1def4ad5784ec, [s]@Reduced95c644a3c072d9a
		t_2 = torch.reshape(t_2, (1024, 64, 14, 3, 14, 2, ))

		# [s]@Reduce
		t_2 = torch.sum(t_2, dim=(5, ))

		# Permute to match the output of this subgraph.
		t_2 = torch.permute(t_2, (0, 1, 2, 4, 3, ))

		# No contraction needed.
		t_3 = t_2

		# [H]@Unfold4d77c1e3da5bca44 -> [H]@Iterator96123ba3184da39c, [k_1]@Share26cfa48d169008e4
		t_3 = torch.reshape(t_3, (1024, 64, 14, 42, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (1024, 64, 3, 14, 14, 3, ))

		# Permute to match the output of this subgraph.
		t_3 = torch.permute(t_3, (0, 1, 3, 2, 4, 5, ))

		# Perform contraction.
		t_4 = torch.einsum("mlnjok, ljki -> mnoi", t_3, in_1)

		# Permute to match the output of this subgraph.
		t_4 = torch.permute(t_4, (0, 3, 1, 2, ))

		# No need to crop the output tensor.
		y = t_4

		return y

class kernel_generated_4(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([128, 3, 3, 256]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]

		# No contraction needed.
		t_2 = in_0

		# [H]@Shift2906cc2f461505d0 -> [H]@Unfoldeeb0aec8202b574f
		t_2 = torch.roll(t_2, self.shift_direction, 3)

		# [H]@Unfoldeeb0aec8202b574f -> [H]@Merge0bce4580e08cd69c, [k_1]@Share02da0a485106ab3d
		t_2 = torch.reshape(t_2, (1024, 3584, 14, 1, ))
		t_2 = torch.nn.functional.unfold(t_2, (3, 1, ), padding=(1, 0, ))
		t_2 = torch.reshape(t_2, (1024, 256, 14, 3, 14, ))

		# [C_in]@Split3524ae88ad3a30bc -> [s]@Merge0bce4580e08cd69d, [s^-1*C_in]@Share8de6f167adbbf8aa
		t_2 = torch.reshape(t_2, (1024, 2, 128, 14, 3, 14, ))

		# [H]@Merge0bce4580e08cd69c, [s]@Merge0bce4580e08cd69d -> [s*H]@Shift8a9f243357a7f717
		t_2 = torch.permute(t_2, (0, 2, 3, 4, 5, 1, ))
		t_2 = torch.reshape(t_2, (1024, 128, 14, 3, 28, ))

		# [s*H]@Shift8a9f243357a7f717 -> [s*H]@Split511946b410b86996
		t_2 = torch.roll(t_2, self.shift_direction, 4)

		# [s*H]@Split511946b410b86996 -> [H]@Iteratorb0a1def4ad5784ec, [s]@Reduced95c644a3c072d9a
		t_2 = torch.reshape(t_2, (1024, 128, 14, 3, 14, 2, ))

		# [s]@Reduce
		t_2 = torch.sum(t_2, dim=(5, ))

		# Permute to match the output of this subgraph.
		t_2 = torch.permute(t_2, (0, 1, 2, 4, 3, ))

		# No contraction needed.
		t_3 = t_2

		# [H]@Unfold4d77c1e3da5bca44 -> [H]@Iterator96123ba3184da39c, [k_1]@Share26cfa48d169008e4
		t_3 = torch.reshape(t_3, (1024, 128, 14, 42, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (1024, 128, 3, 14, 14, 3, ))

		# Permute to match the output of this subgraph.
		t_3 = torch.permute(t_3, (0, 1, 3, 2, 4, 5, ))

		# Perform contraction.
		t_4 = torch.einsum("mlnjok, ljki -> mnoi", t_3, in_1)

		# Permute to match the output of this subgraph.
		t_4 = torch.permute(t_4, (0, 3, 1, 2, ))

		# No need to crop the output tensor.
		y = t_4

		return y

class kernel_generated_5(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([128, 3, 3, 512]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]

		# No contraction needed.
		t_2 = in_0

		# [H]@Shift2906cc2f461505d0 -> [H]@Unfoldeeb0aec8202b574f
		t_2 = torch.roll(t_2, self.shift_direction, 3)

		# [H]@Unfoldeeb0aec8202b574f -> [H]@Merge0bce4580e08cd69c, [k_1]@Share02da0a485106ab3d
		t_2 = torch.reshape(t_2, (1024, 1792, 7, 1, ))
		t_2 = torch.nn.functional.unfold(t_2, (3, 1, ), padding=(1, 0, ))
		t_2 = torch.reshape(t_2, (1024, 256, 7, 3, 7, ))

		# [C_in]@Split3524ae88ad3a30bc -> [s]@Merge0bce4580e08cd69d, [s^-1*C_in]@Share8de6f167adbbf8aa
		t_2 = torch.reshape(t_2, (1024, 2, 128, 7, 3, 7, ))

		# [H]@Merge0bce4580e08cd69c, [s]@Merge0bce4580e08cd69d -> [s*H]@Shift8a9f243357a7f717
		t_2 = torch.permute(t_2, (0, 2, 3, 4, 5, 1, ))
		t_2 = torch.reshape(t_2, (1024, 128, 7, 3, 14, ))

		# [s*H]@Shift8a9f243357a7f717 -> [s*H]@Split511946b410b86996
		t_2 = torch.roll(t_2, self.shift_direction, 4)

		# [s*H]@Split511946b410b86996 -> [H]@Iteratorb0a1def4ad5784ec, [s]@Reduced95c644a3c072d9a
		t_2 = torch.reshape(t_2, (1024, 128, 7, 3, 7, 2, ))

		# [s]@Reduce
		t_2 = torch.sum(t_2, dim=(5, ))

		# Permute to match the output of this subgraph.
		t_2 = torch.permute(t_2, (0, 1, 2, 4, 3, ))

		# No contraction needed.
		t_3 = t_2

		# [H]@Unfold4d77c1e3da5bca44 -> [H]@Iterator96123ba3184da39c, [k_1]@Share26cfa48d169008e4
		t_3 = torch.reshape(t_3, (1024, 128, 7, 21, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (1024, 128, 3, 7, 7, 3, ))

		# Permute to match the output of this subgraph.
		t_3 = torch.permute(t_3, (0, 1, 3, 2, 4, 5, ))

		# Perform contraction.
		t_4 = torch.einsum("mlnjok, ljki -> mnoi", t_3, in_1)

		# Permute to match the output of this subgraph.
		t_4 = torch.permute(t_4, (0, 3, 1, 2, ))

		# No need to crop the output tensor.
		y = t_4

		return y

class kernel_generated_6(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([256, 3, 3, 512]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]

		# No contraction needed.
		t_2 = in_0

		# [H]@Shift2906cc2f461505d0 -> [H]@Unfoldeeb0aec8202b574f
		t_2 = torch.roll(t_2, self.shift_direction, 3)

		# [H]@Unfoldeeb0aec8202b574f -> [H]@Merge0bce4580e08cd69c, [k_1]@Share02da0a485106ab3d
		t_2 = torch.reshape(t_2, (1024, 3584, 7, 1, ))
		t_2 = torch.nn.functional.unfold(t_2, (3, 1, ), padding=(1, 0, ))
		t_2 = torch.reshape(t_2, (1024, 512, 7, 3, 7, ))

		# [C_in]@Split3524ae88ad3a30bc -> [s]@Merge0bce4580e08cd69d, [s^-1*C_in]@Share8de6f167adbbf8aa
		t_2 = torch.reshape(t_2, (1024, 2, 256, 7, 3, 7, ))

		# [H]@Merge0bce4580e08cd69c, [s]@Merge0bce4580e08cd69d -> [s*H]@Shift8a9f243357a7f717
		t_2 = torch.permute(t_2, (0, 2, 3, 4, 5, 1, ))
		t_2 = torch.reshape(t_2, (1024, 256, 7, 3, 14, ))

		# [s*H]@Shift8a9f243357a7f717 -> [s*H]@Split511946b410b86996
		t_2 = torch.roll(t_2, self.shift_direction, 4)

		# [s*H]@Split511946b410b86996 -> [H]@Iteratorb0a1def4ad5784ec, [s]@Reduced95c644a3c072d9a
		t_2 = torch.reshape(t_2, (1024, 256, 7, 3, 7, 2, ))

		# [s]@Reduce
		t_2 = torch.sum(t_2, dim=(5, ))

		# Permute to match the output of this subgraph.
		t_2 = torch.permute(t_2, (0, 1, 2, 4, 3, ))

		# No contraction needed.
		t_3 = t_2

		# [H]@Unfold4d77c1e3da5bca44 -> [H]@Iterator96123ba3184da39c, [k_1]@Share26cfa48d169008e4
		t_3 = torch.reshape(t_3, (1024, 256, 7, 21, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (1024, 256, 3, 7, 7, 3, ))

		# Permute to match the output of this subgraph.
		t_3 = torch.permute(t_3, (0, 1, 3, 2, 4, 5, ))

		# Perform contraction.
		t_4 = torch.einsum("mlnjok, ljki -> mnoi", t_3, in_1)

		# Permute to match the output of this subgraph.
		t_4 = torch.permute(t_4, (0, 3, 1, 2, ))

		# No need to crop the output tensor.
		y = t_4

		return y

