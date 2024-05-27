# automatically generated by the FlatBuffers compiler, do not modify

# namespace: tosa

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class TosaBasicBlock(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = TosaBasicBlock()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsTosaBasicBlock(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    @classmethod
    def TosaBasicBlockBufferHasIdentifier(cls, buf, offset, size_prefixed=False):
        return flatbuffers.util.BufferHasIdentifier(buf, offset, b"\x54\x4F\x53\x41", size_prefixed=size_prefixed)

    # TosaBasicBlock
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # TosaBasicBlock
    def Name(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # TosaBasicBlock
    def Operators(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            x = self._tab.Indirect(x)
            from .TosaOperator import TosaOperator
            obj = TosaOperator()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # TosaBasicBlock
    def OperatorsLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # TosaBasicBlock
    def OperatorsIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        return o == 0

    # TosaBasicBlock
    def Tensors(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            x = self._tab.Indirect(x)
            from .TosaTensor import TosaTensor
            obj = TosaTensor()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # TosaBasicBlock
    def TensorsLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # TosaBasicBlock
    def TensorsIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        return o == 0

    # TosaBasicBlock
    def Inputs(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.String(a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return ""

    # TosaBasicBlock
    def InputsLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # TosaBasicBlock
    def InputsIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        return o == 0

    # TosaBasicBlock
    def Outputs(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.String(a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return ""

    # TosaBasicBlock
    def OutputsLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # TosaBasicBlock
    def OutputsIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        return o == 0

def TosaBasicBlockStart(builder):
    builder.StartObject(5)

def Start(builder):
    TosaBasicBlockStart(builder)

def TosaBasicBlockAddName(builder, name):
    builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(name), 0)

def AddName(builder, name):
    TosaBasicBlockAddName(builder, name)

def TosaBasicBlockAddOperators(builder, operators):
    builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(operators), 0)

def AddOperators(builder, operators):
    TosaBasicBlockAddOperators(builder, operators)

def TosaBasicBlockStartOperatorsVector(builder, numElems):
    return builder.StartVector(4, numElems, 4)

def StartOperatorsVector(builder, numElems: int) -> int:
    return TosaBasicBlockStartOperatorsVector(builder, numElems)

def TosaBasicBlockAddTensors(builder, tensors):
    builder.PrependUOffsetTRelativeSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(tensors), 0)

def AddTensors(builder, tensors):
    TosaBasicBlockAddTensors(builder, tensors)

def TosaBasicBlockStartTensorsVector(builder, numElems):
    return builder.StartVector(4, numElems, 4)

def StartTensorsVector(builder, numElems: int) -> int:
    return TosaBasicBlockStartTensorsVector(builder, numElems)

def TosaBasicBlockAddInputs(builder, inputs):
    builder.PrependUOffsetTRelativeSlot(3, flatbuffers.number_types.UOffsetTFlags.py_type(inputs), 0)

def AddInputs(builder, inputs):
    TosaBasicBlockAddInputs(builder, inputs)

def TosaBasicBlockStartInputsVector(builder, numElems):
    return builder.StartVector(4, numElems, 4)

def StartInputsVector(builder, numElems: int) -> int:
    return TosaBasicBlockStartInputsVector(builder, numElems)

def TosaBasicBlockAddOutputs(builder, outputs):
    builder.PrependUOffsetTRelativeSlot(4, flatbuffers.number_types.UOffsetTFlags.py_type(outputs), 0)

def AddOutputs(builder, outputs):
    TosaBasicBlockAddOutputs(builder, outputs)

def TosaBasicBlockStartOutputsVector(builder, numElems):
    return builder.StartVector(4, numElems, 4)

def StartOutputsVector(builder, numElems: int) -> int:
    return TosaBasicBlockStartOutputsVector(builder, numElems)

def TosaBasicBlockEnd(builder):
    return builder.EndObject()

def End(builder):
    return TosaBasicBlockEnd(builder)
