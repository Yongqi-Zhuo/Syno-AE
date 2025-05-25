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
        interface_0_out_0x5635f60844a0 [label="N", shape=none];
        interface_0_out_0x5635f60844c8 [label="seq_len", shape=none];
        interface_0_out_0x5635f60844f0 [label="t*H_in", shape=none];
    }
    {
        rank = same;
        interface_0_out_0x5635f60844a0;
        interface_0_out_0x5635f60844c8;
        interface_0_out_0x5635f60844f0;
    }
    // Input 0.
    subgraph cluster_subgraph_0_in_0 {
        label = "";
        interface_0_in_0x5635f60844a0 [label="N", shape=none];
        interface_0_in_0x5635f60844c8 [label="seq_len", shape=none];
        interface_0_in_0x5635fe5d5fa0 [label="k_1^3*t^2", shape=none];
        interface_0_in_0x7fef5c00ebf0 [label="k_1", shape=none];
        interface_0_in_0x7fef5c00ec08 [label="k_1^-4*t^-1*H_in", shape=none];
    }
    {
        rank = same;
        interface_0_in_0x5635f60844a0;
        interface_0_in_0x5635f60844c8;
        interface_0_in_0x5635fe5d5fa0;
        interface_0_in_0x7fef5c00ebf0;
        interface_0_in_0x7fef5c00ec08;
    }
    // Op's.
    op_0x5635fe5d5f60 [label="Merge"];
    op_0x7fef5c00ebb0 [label="Merge"];
    // Dimension's.
    interface_0_in_0x5635f60844a0 -> interface_0_out_0x5635f60844a0 [label="N"];
    interface_0_in_0x5635f60844c8 -> interface_0_out_0x5635f60844c8 [label="seq_len"];
    op_0x5635fe5d5f60 -> interface_0_out_0x5635f60844f0 [label="t*H_in"];
    interface_0_in_0x5635fe5d5fa0 -> op_0x5635fe5d5f60 [label="k_1^3*t^2"];
    op_0x7fef5c00ebb0 -> op_0x5635fe5d5f60 [label="k_1^-3*t^-1*H_in"];
    interface_0_in_0x7fef5c00ebf0 -> op_0x7fef5c00ebb0 [label="k_1"];
    interface_0_in_0x7fef5c00ec08 -> op_0x7fef5c00ebb0 [label="k_1^-4*t^-1*H_in"];
}

// Stage tensor.
subgraph cluster_subgraph_1 {
    label = "Subgraph 1";
    // Reductions.
    reduce_0x7feecc006d90 [label="Sum", shape=box];
    // Output.
    subgraph cluster_subgraph_1_out {
        label = "";
        interface_1_out_0x5635f60844a0 [label="N", shape=none];
        interface_1_out_0x5635f60844c8 [label="seq_len", shape=none];
        interface_1_out_0x5635fe5d5fa0 [label="k_1^3*t^2", shape=none];
        interface_1_out_0x7fef5c00ebf0 [label="k_1", shape=none];
        interface_1_out_0x7fef5c00ec08 [label="k_1^-4*t^-1*H_in", shape=none];
    }
    {
        rank = same;
        reduce_0x7feecc006d90;
        interface_1_out_0x5635f60844a0;
        interface_1_out_0x5635f60844c8;
        interface_1_out_0x5635fe5d5fa0;
        interface_1_out_0x7fef5c00ebf0;
        interface_1_out_0x7fef5c00ec08;
    }
    // Input 0.
    subgraph cluster_subgraph_1_in_0 {
        label = "";
        interface_1_in_0x5635f60844a0 [label="N", shape=none];
        interface_1_in_0x5635f60844c8 [label="seq_len", shape=none];
        interface_1_in_0x7fef5c00ebf0 [label="k_1", shape=none];
        interface_1_in_0x7fef38003ad0 [label="k_1^-1*H_in", shape=none];
    }
    // Input 1.
    subgraph cluster_subgraph_1_in_1 {
        label = "";
        interface_1_in_0x7fef6000f858 [label="k_1^3*t^2", shape=none];
        interface_1_in_0x7fef38003ae8 [label="k_1^-1*H_in", shape=none];
        interface_1_in_0x7ff0000b31d8 [label="k_1^-4*t^-1*H_in", shape=none];
    }
    {
        rank = same;
        interface_1_in_0x5635f60844a0;
        interface_1_in_0x5635f60844c8;
        interface_1_in_0x7fef5c00ebf0;
        interface_1_in_0x7fef38003ad0;
        interface_1_in_0x7fef6000f858;
        interface_1_in_0x7fef38003ae8;
        interface_1_in_0x7ff0000b31d8;
    }
    // Op's.
    op_0x7fef0c1133f8 [label="Expand"];
    op_0x7fef38003ab0 [label="Share"];
    op_0x7fef6000f820 [label="Share"];
    op_0x7fefa0016858 [label="Expand"];
    op_0x7ff0000b31a0 [label="Share"];
    // Dimension's.
    interface_1_in_0x5635f60844a0 -> interface_1_out_0x5635f60844a0 [label="N"];
    interface_1_in_0x5635f60844c8 -> interface_1_out_0x5635f60844c8 [label="seq_len"];
    op_0x7fef6000f820 -> interface_1_out_0x5635fe5d5fa0 [label="k_1^3*t^2"];
    op_0x7fef38003ab0 -> reduce_0x7feecc006d90 [label="k_1^-1*H_in"];
    interface_1_in_0x7fef38003ad0 -> op_0x7fef38003ab0 [label="k_1^-1*H_in"];
    interface_1_in_0x7fef38003ae8 -> op_0x7fef38003ab0 [label="k_1^-1*H_in"];
    interface_1_in_0x7fef5c00ebf0 -> interface_1_out_0x7fef5c00ebf0 [label="k_1"];
    op_0x7ff0000b31a0 -> interface_1_out_0x7fef5c00ec08 [label="k_1^-4*t^-1*H_in"];
    op_0x7fefa0016858 -> op_0x7fef6000f820 [label="k_1^3*t^2"];
    interface_1_in_0x7fef6000f858 -> op_0x7fef6000f820 [label="k_1^3*t^2"];
    op_0x7fef0c1133f8 -> op_0x7ff0000b31a0 [label="k_1^-4*t^-1*H_in"];
    interface_1_in_0x7ff0000b31d8 -> op_0x7ff0000b31a0 [label="k_1^-4*t^-1*H_in"];
}

// Stage tensor.
subgraph cluster_subgraph_2 {
    label = "Subgraph 2";
    // Reductions.
    // Output.
    subgraph cluster_subgraph_2_out {
        label = "";
        interface_2_out_0x5635f60844a0 [label="N", shape=none];
        interface_2_out_0x5635f60844c8 [label="seq_len", shape=none];
        interface_2_out_0x7fef5c00ebf0 [label="k_1", shape=none];
        interface_2_out_0x7fef38003ad0 [label="k_1^-1*H_in", shape=none];
    }
    {
        rank = same;
        interface_2_out_0x5635f60844a0;
        interface_2_out_0x5635f60844c8;
        interface_2_out_0x7fef5c00ebf0;
        interface_2_out_0x7fef38003ad0;
    }
    // Input 0.
    subgraph cluster_subgraph_2_in_0 {
        label = "";
        interface_2_in_0x5635f60844a0 [label="N", shape=none];
        interface_2_in_0x5635f60844c8 [label="seq_len", shape=none];
        interface_2_in_0x7fef2ae37740 [label="H_in", shape=none];
    }
    {
        rank = same;
        interface_2_in_0x5635f60844a0;
        interface_2_in_0x5635f60844c8;
        interface_2_in_0x7fef2ae37740;
    }
    // Op's.
    op_0x7fef2ae37700 [label="Split"];
    // Dimension's.
    interface_2_in_0x5635f60844a0 -> interface_2_out_0x5635f60844a0 [label="N"];
    interface_2_in_0x5635f60844c8 -> interface_2_out_0x5635f60844c8 [label="seq_len"];
    interface_2_in_0x7fef2ae37740 -> op_0x7fef2ae37700 [label="H_in"];
    op_0x7fef2ae37700 -> interface_2_out_0x7fef38003ad0 [label="k_1^-1*H_in"];
    op_0x7fef2ae37700 -> interface_2_out_0x7fef5c00ebf0 [label="k_1"];
}

// Input tensor.
subgraph cluster_subgraph_3 {
    label = "Input 0";
    interface_3_out_0x5635f60844a0 [label="N", shape=none];
    interface_3_out_0x5635f60844c8 [label="seq_len", shape=none];
    interface_3_out_0x7fef2ae37740 [label="H_in", shape=none];
}

interface_3_out_0x5635f60844a0 -> interface_2_in_0x5635f60844a0;
interface_3_out_0x5635f60844c8 -> interface_2_in_0x5635f60844c8;
interface_3_out_0x7fef2ae37740 -> interface_2_in_0x7fef2ae37740;

interface_2_out_0x5635f60844a0 -> interface_1_in_0x5635f60844a0;
interface_2_out_0x5635f60844c8 -> interface_1_in_0x5635f60844c8;
interface_2_out_0x7fef5c00ebf0 -> interface_1_in_0x7fef5c00ebf0;
interface_2_out_0x7fef38003ad0 -> interface_1_in_0x7fef38003ad0;

// Input tensor.
subgraph cluster_subgraph_4 {
    label = "Input 1";
    interface_4_out_0x7fef6000f858 [label="k_1^3*t^2", shape=none];
    interface_4_out_0x7fef38003ae8 [label="k_1^-1*H_in", shape=none];
    interface_4_out_0x7ff0000b31d8 [label="k_1^-4*t^-1*H_in", shape=none];
}

interface_4_out_0x7fef6000f858 -> interface_1_in_0x7fef6000f858;
interface_4_out_0x7fef38003ae8 -> interface_1_in_0x7fef38003ae8;
interface_4_out_0x7ff0000b31d8 -> interface_1_in_0x7ff0000b31d8;

interface_1_out_0x5635f60844a0 -> interface_0_in_0x5635f60844a0;
interface_1_out_0x5635f60844c8 -> interface_0_in_0x5635f60844c8;
interface_1_out_0x5635fe5d5fa0 -> interface_0_in_0x5635fe5d5fa0;
interface_1_out_0x7fef5c00ebf0 -> interface_0_in_0x7fef5c00ebf0;
interface_1_out_0x7fef5c00ec08 -> interface_0_in_0x7fef5c00ec08;

{
    rank = same;
    interface_3_out_0x5635f60844a0;
    interface_3_out_0x5635f60844c8;
    interface_3_out_0x7fef2ae37740;
    interface_4_out_0x7fef6000f858;
    interface_4_out_0x7fef38003ae8;
    interface_4_out_0x7ff0000b31d8;
}
subgraph cluster_subgraph_output {
    label = "Output";
    interface_5_in_0x5635f60844a0 [label="N", shape=none];
    interface_5_in_0x5635f60844c8 [label="seq_len", shape=none];
    interface_5_in_0x5635f60844f0 [label="t*H_in", shape=none];
}
interface_0_out_0x5635f60844a0 -> interface_5_in_0x5635f60844a0;
interface_0_out_0x5635f60844c8 -> interface_5_in_0x5635f60844c8;
interface_0_out_0x5635f60844f0 -> interface_5_in_0x5635f60844f0;

}

"""
class kernel_generated_0(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([72, 384, 16]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]

		# No contraction needed.
		t_2 = in_0

		# [H_in]@Split1ffc0546f6a4490e -> [k_1]@Merge6ca7ac0e28ad3e95, [k_1^-1*H_in]@Share7b3b31bf2538a937
		t_2 = torch.reshape(t_2, (1, 2048, 2, 384, ))

		# Perform contraction.
		t_3 = torch.einsum("lmni, jik -> lmjnk", t_2, in_1)

		# No contraction needed.
		t_4 = t_3

		# [k_1]@Merge6ca7ac0e28ad3e95, [k_1^-4*t^-1*H_in]@Merge6ca7ac0e28ad3e96 -> [k_1^-3*t^-1*H_in]@Mergea351ee6ccc42a26b
		t_4 = torch.reshape(t_4, (1, 2048, 72, 32, ))

		# [k_1^3*t^2]@Mergea351ee6ccc42a268, [k_1^-3*t^-1*H_in]@Mergea351ee6ccc42a26b -> [t*H_in]@Iterator96123ba3184da39c
		t_4 = torch.reshape(t_4, (1, 2048, 2304, ))

		# No need to crop the output tensor.
		y = t_4

		return y

