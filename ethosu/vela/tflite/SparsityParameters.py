# automatically generated by the FlatBuffers compiler, do not modify

# namespace: tflite

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class SparsityParameters(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = SparsityParameters()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsSparsityParameters(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    @classmethod
    def SparsityParametersBufferHasIdentifier(cls, buf, offset, size_prefixed=False):
        return flatbuffers.util.BufferHasIdentifier(buf, offset, b"\x54\x46\x4C\x33", size_prefixed=size_prefixed)

    # SparsityParameters
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # SparsityParameters
    def TraversalOrder(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int32Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return 0

    # SparsityParameters
    def TraversalOrderAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int32Flags, o)
        return 0

    # SparsityParameters
    def TraversalOrderLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # SparsityParameters
    def TraversalOrderIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        return o == 0

    # SparsityParameters
    def BlockMap(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int32Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return 0

    # SparsityParameters
    def BlockMapAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int32Flags, o)
        return 0

    # SparsityParameters
    def BlockMapLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # SparsityParameters
    def BlockMapIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        return o == 0

    # SparsityParameters
    def DimMetadata(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            x = self._tab.Indirect(x)
            from .DimensionMetadata import DimensionMetadata
            obj = DimensionMetadata()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # SparsityParameters
    def DimMetadataLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # SparsityParameters
    def DimMetadataIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        return o == 0

def SparsityParametersStart(builder): builder.StartObject(3)
def Start(builder):
    return SparsityParametersStart(builder)
def SparsityParametersAddTraversalOrder(builder, traversalOrder): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(traversalOrder), 0)
def AddTraversalOrder(builder, traversalOrder):
    return SparsityParametersAddTraversalOrder(builder, traversalOrder)
def SparsityParametersStartTraversalOrderVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def StartTraversalOrderVector(builder, numElems):
    return SparsityParametersStartTraversalOrderVector(builder, numElems)
def SparsityParametersAddBlockMap(builder, blockMap): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(blockMap), 0)
def AddBlockMap(builder, blockMap):
    return SparsityParametersAddBlockMap(builder, blockMap)
def SparsityParametersStartBlockMapVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def StartBlockMapVector(builder, numElems):
    return SparsityParametersStartBlockMapVector(builder, numElems)
def SparsityParametersAddDimMetadata(builder, dimMetadata): builder.PrependUOffsetTRelativeSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(dimMetadata), 0)
def AddDimMetadata(builder, dimMetadata):
    return SparsityParametersAddDimMetadata(builder, dimMetadata)
def SparsityParametersStartDimMetadataVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def StartDimMetadataVector(builder, numElems):
    return SparsityParametersStartDimMetadataVector(builder, numElems)
def SparsityParametersEnd(builder): return builder.EndObject()
def End(builder):
    return SparsityParametersEnd(builder)