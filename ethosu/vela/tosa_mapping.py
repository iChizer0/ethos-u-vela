# SPDX-FileCopyrightText: Copyright 2021-2024 Arm Limited and/or its affiliates <open-source-office@arm.com>
#
# SPDX-License-Identifier: Apache-2.0
#
# Licensed under the Apache License, Version 2.0 (the License); you may
# not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an AS IS BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Description:
# TOSA mapping functions used by reader.
# Contains a mapping from the various TOSA enums and options structs, generated by the FlatBuffer code
# generator, to Vela's internal format.
import numpy as np

from .data_type import DataType
from .operation import Op
from .operation import TensorIndices
from .tosa import ArithmeticRightShiftAttribute  # noqa: F401
from .tosa import AxisAttribute  # noqa: F401
from .tosa import ClampAttribute  # noqa: F401
from .tosa import CondIfAttribute  # noqa: F401
from .tosa import ConvAttribute  # noqa: F401
from .tosa import FullyConnectedAttribute  # noqa: F401
from .tosa import MulAttribute  # noqa: F401
from .tosa import PoolAttribute  # noqa: F401
from .tosa import RescaleAttribute  # noqa: F401
from .tosa import ReshapeAttribute  # noqa: F401
from .tosa import ResizeAttribute  # noqa: F401
from .tosa import SliceAttribute  # noqa: F401
from .tosa import TileAttribute  # noqa: F401
from .tosa import TransposeAttribute  # noqa: F401
from .tosa import TransposeConvAttribute  # noqa: F401
from .tosa import WhileLoopAttribute  # noqa: F401
from .tosa.DType import DType
from .tosa.Op import Op as TosaOp


datatype_map = {
    DType.BOOL: DataType.bool,
    DType.UINT8: DataType.uint8,
    DType.INT4: DataType.int4,
    DType.INT8: DataType.int8,
    DType.INT16: DataType.int16,
    DType.INT32: DataType.int32,
    DType.INT48: DataType.int48,
    DType.FP32: DataType.float32,
}

datatype_map_numpy = {
    DType.BOOL: bool,
    DType.UINT8: np.uint8,
    DType.INT8: np.int8,
    DType.INT16: np.int16,
    DType.INT32: np.int32,
    DType.FP32: np.float32,
}


# TODO duplicate of tflite_mapping
def underscore_to_camel_case(s):
    return "".join(x.title() for x in s.split("_"))


# TODO duplicate of tflite_mapping
def identity(x):
    return x


class AttrSerializer:
    def __init__(self, name, members=None):
        self.name = name
        self.module = globals()[self.name]
        self.cls = getattr(self.module, self.name)
        self.members = []
        if members is not None:
            for mem in members:
                deserialize = identity
                is_vector = False
                if isinstance(mem, tuple):
                    if len(mem) == 2:
                        mem, is_vector = mem
                        deserialize = tuple
                    else:
                        assert 0
                underscore_mem = mem
                camelcase_mem = underscore_to_camel_case(mem)
                self.members.append((underscore_mem, camelcase_mem, deserialize, is_vector))

    def deserialize(self, op_data):
        attr_type = op_data.AttributeType()
        attr = op_data.Attribute()
        attrs = {}
        if attr_type:
            tosa_attrs = self.cls()
            tosa_attrs.Init(attr.Bytes, attr.Pos)
            for underscore_mem, camelcase_mem, deserialize, is_vector in self.members:
                fun = camelcase_mem
                if is_vector:
                    fun += "AsNumpy"

                attr = getattr(tosa_attrs, fun)()
                try:
                    attrs[underscore_mem] = deserialize(attr)
                except TypeError:
                    print("Warning: {0} could not read attribute '{1}'.".format(self.name, underscore_mem))

        return attrs


is_vec = True
pool_attrs = AttrSerializer(
    "PoolAttribute",
    (
        ("pad", is_vec),
        ("kernel", is_vec),
        ("stride", is_vec),
        ("input_zp"),
        ("output_zp"),
    ),
)
conv_attrs = AttrSerializer(
    "ConvAttribute",
    (
        ("pad", is_vec),
        ("stride", is_vec),
        ("dilation", is_vec),
        ("input_zp"),
        ("weight_zp"),
    ),
)
fc_attrs = AttrSerializer("FullyConnectedAttribute", (("input_zp"), ("weight_zp")))
transpose_conv_attrs = AttrSerializer(
    "TransposeConvAttribute",
    (
        ("outpad", is_vec),
        ("stride", is_vec),
        ("dilation", is_vec),
        ("out_shape", is_vec),
    ),
)
transpose_attrs = AttrSerializer("TransposeAttribute", (("perms", is_vec),))
axis_attrs = AttrSerializer("AxisAttribute", ("axis",))
reshape_attrs = AttrSerializer("ReshapeAttribute", (("new_shape", is_vec),))
slice_attrs = AttrSerializer("SliceAttribute", (("start", is_vec), ("size", is_vec)))
tile_attrs = AttrSerializer("TileAttribute", (("multiplies", is_vec),))
resize_attrs = AttrSerializer(
    "ResizeAttribute",
    (("output_size", is_vec), ("stride", is_vec), ("offset", is_vec), ("shift")),
)
clamp_attrs = AttrSerializer("ClampAttribute", (("min_int"), ("max_int")))
rescale_attrs = AttrSerializer(
    "RescaleAttribute",
    (
        "input_zp",
        "output_zp",
        ("multiplier", is_vec),
        ("shift", is_vec),
        "scale32",
        "double_round",
        "per_channel",
    ),
)
mul_attrs = AttrSerializer("MulAttribute", ("shift",))
ars_attrs = AttrSerializer("ArithmeticRightShiftAttribute", ("round",))
condif_attrs = AttrSerializer("CondIfAttribute", (("then_branch"), ("else_branch")))  # TODO these are references
while_attrs = AttrSerializer("WhileLoopAttribute", (("cond_branch"), ("body_branch")))  # TODO these are references

unsupported_tosa_operators = {
    TosaOp.UNKNOWN,
    TosaOp.ARGMAX,
    TosaOp.CONV3D,
    TosaOp.MATMUL,
    TosaOp.TRANSPOSE_CONV2D,
    TosaOp.SIGMOID,
    TosaOp.TANH,
    TosaOp.BITWISE_AND,
    TosaOp.BITWISE_OR,
    TosaOp.BITWISE_XOR,
    TosaOp.INTDIV,
    TosaOp.LOGICAL_AND,
    TosaOp.LOGICAL_LEFT_SHIFT,
    TosaOp.LOGICAL_RIGHT_SHIFT,
    TosaOp.LOGICAL_OR,
    TosaOp.LOGICAL_XOR,
    TosaOp.MAXIMUM,
    TosaOp.MINIMUM,
    TosaOp.POW,
    TosaOp.ABS,
    TosaOp.BITWISE_NOT,
    TosaOp.CEIL,
    TosaOp.CLZ,
    TosaOp.EXP,
    TosaOp.FLOOR,
    TosaOp.LOG,
    TosaOp.LOGICAL_NOT,
    TosaOp.NEGATE,
    TosaOp.RECIPROCAL,
    TosaOp.RSQRT,
    TosaOp.SELECT,
    TosaOp.EQUAL,
    TosaOp.GREATER,
    TosaOp.GREATER_EQUAL,
    TosaOp.REDUCE_ANY,
    TosaOp.REDUCE_ALL,
    TosaOp.REDUCE_MAX,
    TosaOp.REDUCE_MIN,
    TosaOp.REDUCE_PRODUCT,
    TosaOp.REDUCE_SUM,
    TosaOp.REVERSE,
    TosaOp.TILE,
    TosaOp.GATHER,
    TosaOp.SCATTER,
    TosaOp.RESIZE,
    TosaOp.CAST,
    TosaOp.CUSTOM,
    TosaOp.COND_IF,
    TosaOp.WHILE_LOOP,
}


TOSA_NO_INDICES = TensorIndices([], [], [])
TOSA_IFM_INDICES = TensorIndices([0], [], [])
# TOSA_IFM_WEIGHTS_INDICES = TensorIndices([0], [1], [])
TOSA_IFM_WEIGHTS_BIAS_INDICES = TensorIndices([0], [1], [2])
TOSA_IFM_IFM2_INDICES = TensorIndices([0, 1], [], [])
# TOSA_CONV2D_BACKPROP_INDICES = TensorIndices([2], [1], [3])
# TOSA_TRANSPOSE_CONV_INDICES = TensorIndices([0], [1], [3])
TOSA_CONCAT_INDICES = TensorIndices([1, 2], [], [])
# TOSA_SPLIT_IFM_INDICES = TensorIndices([1], [], [])
# TOSA_BLOCK_LSTM_INDICES = TensorIndices([3], [4], [])


tosa_operator_map = {
    # TosaOp.UNKNOWN: (),
    # TODO TosaOp.ARGMAX: (Op.ArgMax, axis_attrs, None),
    TosaOp.AVG_POOL2D: (Op.AvgPool, pool_attrs, None, TOSA_IFM_INDICES),
    TosaOp.CONV2D: (Op.Conv2DBias, conv_attrs, None, TOSA_IFM_WEIGHTS_BIAS_INDICES),
    # TODO TosaOp.CONV3D:
    TosaOp.DEPTHWISE_CONV2D: (
        Op.DepthwiseConv2DBias,
        conv_attrs,
        None,
        TOSA_IFM_WEIGHTS_BIAS_INDICES,
    ),
    TosaOp.FULLY_CONNECTED: (
        Op.FullyConnected,
        fc_attrs,
        None,
        TOSA_IFM_WEIGHTS_BIAS_INDICES,
    ),
    # TODO TosaOp.MATMUL:
    TosaOp.MAX_POOL2D: (Op.MaxPool, pool_attrs, None, TOSA_IFM_INDICES),
    # TODO TosaOp.TRANSPOSE_CONV2D: (Op.Conv2DBackpropInput, transpose_conv_attrs, None)
    TosaOp.CLAMP: (Op.Clamp, clamp_attrs, None, TOSA_IFM_INDICES),
    # TODO: BUG: No longer a relu - presumably a clamp - TosaOp.RELUN: (Op.ReluN, relun_attrs, None, TOSA_IFM_INDICES),
    # TODO TosaOp.SIGMOID
    # TODO TosaOp.TANH
    TosaOp.ADD: (Op.Add, None, None, TOSA_IFM_IFM2_INDICES),
    TosaOp.ARITHMETIC_RIGHT_SHIFT: (Op.SHR, ars_attrs, None, TOSA_IFM_IFM2_INDICES),
    # TODO TosaOp.BITWISE_AND
    # TODO TosaOp.BITWISE_OR
    # TODO TosaOp.BITWISE_XOR
    # TODO TosaOp.INTDIV
    # TODO TosaOp.LOGICAL_AND
    # TODO TosaOp.LOGICAL_LEFT_SHIFT
    # TODO TosaOp.LOGICAL_RIGHT_SHIFT
    # TODO TosaOp.LOGICAL_OR
    # TODO TosaOp.LOGICAL_XOR
    # TODO TosaOp.MAXIMUM
    # TODO TosaOp.MINIMUM
    TosaOp.MUL: (Op.Mul, mul_attrs, None, TOSA_IFM_IFM2_INDICES),
    # TODO TosaOp.POW
    TosaOp.SUB: (Op.Sub, None, None, TOSA_IFM_IFM2_INDICES),
    # TODO is table content in input[1] always constant?
    TosaOp.TABLE: (Op.Table, None, None, TOSA_IFM_INDICES),
    # TODO TosaOp.ABS
    # TODO TosaOp.BITWISE_NOT
    # TODO TosaOp.CEIL
    # TODO TosaOp.CLZ
    # TODO TosaOp.EXP
    # TODO TosaOp.FLOOR
    # TODO TosaOp.LOG
    # TODO TosaOp.LOGICAL_NOT
    # TODO TosaOp.NEGATE
    # TODO TosaOp.RECIPROCAL
    # TODO TosaOp.RSQRT
    # TODO TosaOp.SELECT
    # TODO TosaOp.EQUAL
    # TODO TosaOp.GREATER
    # TODO TosaOp.GREATER_EQUAL
    # TODO TosaOp.REDUCE_ANY
    # TODO TosaOp.REDUCE_ALL
    # TODO TosaOp.REDUCE_MAX
    # TODO TosaOp.REDUCE_MIN
    # TODO TosaOp.REDUCE_PRODUCT
    # TODO TosaOp.REDUCE_SUM
    TosaOp.CONCAT: (Op.Concat, axis_attrs, None, TOSA_CONCAT_INDICES),
    # TODO Is the padding intended to be dynamic input, TOSA spec state it as attribute
    # Handled as for TFLite for now
    TosaOp.PAD: (Op.Pad, None, None, TOSA_IFM_INDICES),
    TosaOp.RESHAPE: (Op.Reshape, reshape_attrs, None, TOSA_IFM_INDICES),
    # TODO TosaOp.REVERSE
    TosaOp.SLICE: (Op.SplitSliceRead, slice_attrs, None, TOSA_IFM_INDICES),
    # TODO TosaOp.TILE
    TosaOp.TRANSPOSE: (
        Op.Transpose,
        transpose_attrs,
        None,
        # TODO: why is this IFM2 indices but then overridden to TOSA_IFM_INDICES in _reader?
        # TOSA_IFM_IFM2_INDICES,
        TOSA_IFM_IFM2_INDICES,
    ),  # TODO Is the perms intended to be dynamic input, TOSA spec state it as attribute
    # TODO TosaOp.GATHER
    # TODO TosaOp.SCATTER
    # TODO TosaOp.RESIZE
    # TODO TosaOp.CAST
    TosaOp.RESCALE: (Op.Rescale, rescale_attrs, None, TOSA_IFM_INDICES),
    TosaOp.CONST: (Op.Const, None, None, TOSA_NO_INDICES),
    TosaOp.IDENTITY: (Op.Identity, None, None, TOSA_IFM_INDICES),
    # TODO TosaOp.CUSTOM
    # TODO TosaOp.COND_IF
    # TODO TosaOp.WHILE_LOOP
}

tosa_operator_inv_map = {v[0]: (k, v[1]) for k, v in tosa_operator_map.items()}

tosa_operator_name_map = {v: k for k, v in vars(TosaOp).items()}


# TODO will return UNKNOWN for the once that have not yet been defined in tosa_operator_map
def optype_to_tosa_op_type(op_type: Op):
    if op_type in tosa_operator_inv_map:
        return tosa_operator_name_map[tosa_operator_inv_map[op_type][0]]
    else:
        return TosaOp.UNKNOWN
