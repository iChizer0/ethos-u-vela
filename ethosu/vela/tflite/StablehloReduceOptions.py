# automatically generated by the FlatBuffers compiler, do not modify

# namespace: tflite

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class StablehloReduceOptions(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = StablehloReduceOptions()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsStablehloReduceOptions(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    @classmethod
    def StablehloReduceOptionsBufferHasIdentifier(cls, buf, offset, size_prefixed=False):
        return flatbuffers.util.BufferHasIdentifier(buf, offset, b"\x54\x46\x4C\x33", size_prefixed=size_prefixed)

    # StablehloReduceOptions
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # StablehloReduceOptions
    def Dimensions(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int64Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 8))
        return 0

    # StablehloReduceOptions
    def DimensionsAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int64Flags, o)
        return 0

    # StablehloReduceOptions
    def DimensionsLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # StablehloReduceOptions
    def DimensionsIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        return o == 0

    # StablehloReduceOptions
    def BodySubgraphIndex(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

def StablehloReduceOptionsStart(builder): builder.StartObject(2)
def Start(builder):
    return StablehloReduceOptionsStart(builder)
def StablehloReduceOptionsAddDimensions(builder, dimensions): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(dimensions), 0)
def AddDimensions(builder, dimensions):
    return StablehloReduceOptionsAddDimensions(builder, dimensions)
def StablehloReduceOptionsStartDimensionsVector(builder, numElems): return builder.StartVector(8, numElems, 8)
def StartDimensionsVector(builder, numElems):
    return StablehloReduceOptionsStartDimensionsVector(builder, numElems)
def StablehloReduceOptionsAddBodySubgraphIndex(builder, bodySubgraphIndex): builder.PrependInt32Slot(1, bodySubgraphIndex, 0)
def AddBodySubgraphIndex(builder, bodySubgraphIndex):
    return StablehloReduceOptionsAddBodySubgraphIndex(builder, bodySubgraphIndex)
def StablehloReduceOptionsEnd(builder): return builder.EndObject()
def End(builder):
    return StablehloReduceOptionsEnd(builder)