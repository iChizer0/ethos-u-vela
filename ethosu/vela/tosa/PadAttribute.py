# automatically generated by the FlatBuffers compiler, do not modify

# namespace: tosa

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class PadAttribute(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = PadAttribute()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsPadAttribute(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    @classmethod
    def PadAttributeBufferHasIdentifier(cls, buf, offset, size_prefixed=False):
        return flatbuffers.util.BufferHasIdentifier(buf, offset, b"\x54\x4F\x53\x41", size_prefixed=size_prefixed)

    # PadAttribute
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # PadAttribute
    def Padding(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int32Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return 0

    # PadAttribute
    def PaddingAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int32Flags, o)
        return 0

    # PadAttribute
    def PaddingLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # PadAttribute
    def PaddingIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        return o == 0

    # PadAttribute
    def PadConstInt(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # PadAttribute
    def PadConstFp(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Uint8Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 1))
        return 0

    # PadAttribute
    def PadConstFpAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Uint8Flags, o)
        return 0

    # PadAttribute
    def PadConstFpLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # PadAttribute
    def PadConstFpIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        return o == 0

def PadAttributeStart(builder):
    builder.StartObject(3)

def Start(builder):
    PadAttributeStart(builder)

def PadAttributeAddPadding(builder, padding):
    builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(padding), 0)

def AddPadding(builder, padding):
    PadAttributeAddPadding(builder, padding)

def PadAttributeStartPaddingVector(builder, numElems):
    return builder.StartVector(4, numElems, 4)

def StartPaddingVector(builder, numElems: int) -> int:
    return PadAttributeStartPaddingVector(builder, numElems)

def PadAttributeAddPadConstInt(builder, padConstInt):
    builder.PrependInt32Slot(1, padConstInt, 0)

def AddPadConstInt(builder, padConstInt):
    PadAttributeAddPadConstInt(builder, padConstInt)

def PadAttributeAddPadConstFp(builder, padConstFp):
    builder.PrependUOffsetTRelativeSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(padConstFp), 0)

def AddPadConstFp(builder, padConstFp):
    PadAttributeAddPadConstFp(builder, padConstFp)

def PadAttributeStartPadConstFpVector(builder, numElems):
    return builder.StartVector(1, numElems, 1)

def StartPadConstFpVector(builder, numElems: int) -> int:
    return PadAttributeStartPadConstFpVector(builder, numElems)

def PadAttributeEnd(builder):
    return builder.EndObject()

def End(builder):
    return PadAttributeEnd(builder)
