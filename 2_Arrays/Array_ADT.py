"""
1-D array is a collection of contiguous elements
in which individual elements are identified by a unique integer subscripts starting 0
SIZE CANNOT BE CHANGED AFTER CREATION

Array(size)
length()
getitem(index), setitem(index, value)
clearing(value) -- Clears the array by setting every element to value
iterator()
"""

import ctypes

class Array:
    def __init__(self, size):
        assert size > 0, "Array size must be >0"
        self._size = size
        PyArrayType = ctypes.py_object * size
        self._elements = PyArrayType()
        self.clear(None)

    def __len__(self):
        return self._size

    def __getitem__(self, index):
        assert index >= 0 and index < len(self), "Array subscript out of range"
        return self._elements[index]

    def __setitem__(self, index, value):
        assert index >= 0 and index < len(self), "Array subscript out of range"
        self._elements[index] = value

    def clear(self, value):
        for i in range(len(self)):
            self._elements[i] = value

    def __iter__(self):
        return _ArrayIterator(self._elements)

class _ArrayIterator:
    def __init__(self, arr):
        self._array_ref = arr
        self._curr_idx = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._curr_idx < len(self._array_ref):
            entry = self._array_ref[self._curr_idx]
            self._curr_idx += 1
            return entry
        else:
            raise StopIteration