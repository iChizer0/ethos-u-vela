# automatically generated by the FlatBuffers compiler, do not modify

# namespace: tosa

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class TosaRegion(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = TosaRegion()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsTosaRegion(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    @classmethod
    def TosaRegionBufferHasIdentifier(cls, buf, offset, size_prefixed=False):
        return flatbuffers.util.BufferHasIdentifier(buf, offset, b"\x54\x4F\x53\x41", size_prefixed=size_prefixed)

    # TosaRegion
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # TosaRegion
    def Name(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # TosaRegion
    def Blocks(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            x = self._tab.Indirect(x)
            from .TosaBasicBlock import TosaBasicBlock
            obj = TosaBasicBlock()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # TosaRegion
    def BlocksLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # TosaRegion
    def BlocksIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        return o == 0

def TosaRegionStart(builder):
    builder.StartObject(2)

def Start(builder):
    TosaRegionStart(builder)

def TosaRegionAddName(builder, name):
    builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(name), 0)

def AddName(builder, name):
    TosaRegionAddName(builder, name)

def TosaRegionAddBlocks(builder, blocks):
    builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(blocks), 0)

def AddBlocks(builder, blocks):
    TosaRegionAddBlocks(builder, blocks)

def TosaRegionStartBlocksVector(builder, numElems):
    return builder.StartVector(4, numElems, 4)

def StartBlocksVector(builder, numElems: int) -> int:
    return TosaRegionStartBlocksVector(builder, numElems)

def TosaRegionEnd(builder):
    return builder.EndObject()

def End(builder):
    return TosaRegionEnd(builder)
