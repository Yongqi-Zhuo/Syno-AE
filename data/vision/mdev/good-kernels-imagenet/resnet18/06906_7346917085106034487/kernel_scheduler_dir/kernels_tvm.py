import tvm
from tvm import relax, te
from tvm.relax import BlockBuilder
from typing import List
import numpy as np

def weights(C_in: int = -1, C_out: int = -1, H: int = -1, N: int = -1, g: int = 32, k_1: int = 3, k_2: int = 7, s: int = 2, ) -> List[relax.Constant]:
	in_1: relax.Constant = relax.const(np.random.normal(size=(C_in, k_1, s, C_out,)).astype("float32"))
	return [in_1]

def build(bb: BlockBuilder, in_0: relax.Expr, in_1: relax.Expr, C_in: int = -1, C_out: int = -1, H: int = -1, N: int = -1, g: int = 32, k_1: int = 3, k_2: int = 7, s: int = 2, ) -> relax.Var:
	assert C_in > 0 and C_out > 0 and H > 0 and N > 0 and g > 0 and k_1 > 0 and k_2 > 0 and s > 0
	def build_subgraph_3(in_0: te.Tensor, in_1: te.Tensor) -> te.Tensor:
		ri_0 = te.reduce_axis((0, C_in), "ri_0")
		ri_1 = te.reduce_axis((0, s), "ri_1")
		ri_2 = te.reduce_axis((0, k_1), "ri_2")
		return te.compute(
			(N, H, H, C_out,),
			lambda i_0, i_1, i_2, i_3:
				te.sum(
					te.if_then_else(
						te.all(te.floormod(i_2 * s + ri_1 + 1, H * s) // s + ri_2 - k_1 // 2 >= 0, te.floormod(i_2 * s + ri_1 + 1, H * s) // s + ri_2 - k_1 // 2 < k_1),
						in_0[i_0, ri_0, i_1, te.floormod(i_2 * s + ri_1 + 1, H * s) // s + ri_2 - k_1 // 2] * in_1[ri_0, ri_2, te.floormod(i_2 * s + ri_1 + 1, H * s) % s, i_3],
						0.0,
					),
					axis=[ri_0, ri_1, ri_2],
				),
			name="subgraph_3",
		)
	def build_subgraph_2(in_0: te.Tensor) -> te.Tensor:
		return te.compute(
			(N, C_out, H, H,),
			lambda i_0, i_1, i_2, i_3:
				in_0[i_0, te.floormod(i_3 + 1, H), i_2, i_1],
			name="subgraph_2",
		)
	subgraph_3 = bb.emit_te(build_subgraph_3, in_0, in_1)
	subgraph_2 = bb.emit_te(build_subgraph_2, subgraph_3)
	return subgraph_2
