"""
2-D array consists of a collection of elements organized into rows and columns
Elements are referenced as (r, c), indexes starting at 0

Array2D(rows, columns)
num_rows(), num_cols()
clear(value) -- Clears the array by setting each element to value
get_item(r,c), set_item(r, c, value)
"""

from Array_ADT import Array


class Array2D:
    def __init__(self, rows, columns):
        self._rows = Array(rows)

        for i in range(rows):
            self._rows[i] = Array(columns)

    def num_rows(self):
        return len(self._rows)

    def num_cols(self):
        return len(self._rows[0])

    def clear(self, value):
        for row in range(self.num_rows()):
            self._rows[row].clear(value)

    def __getitem__(self, tuple_idx):
        assert len(tuple_idx) == 2, "Invalid number of array subscripts"
        row = tuple_idx[0]
        col = tuple_idx[1]
        assert 0 <= row < self.num_rows() \
               and 0 <= col < self.num_cols(), \
            "Array subscript out of range"
        req_row = self._rows[row]
        return req_row[col]

    def __setitem__(self, tuple_idx, value):
        assert len(tuple_idx) == 2, "Invalid number of array subscripts"
        row = tuple_idx[0]
        col = tuple_idx[1]
        assert 0 <= row < self.num_rows() \
               and 0 <= col < self.num_cols(), \
            "Array subscript out of range"
        req_row = self._rows[row]
        req_row[col] = value
