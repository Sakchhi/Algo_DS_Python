"""
2D array of numerical values
scale_by(scalar),
transpose()
add(another_matrix), subtract(another_matrix), multiply(another_matrix)
"""

from Array2d_ADT import Array2D

class Matrix:
    def __init__(self, row, col):
        self._matrix = Array2D(row, col)
        self._matrix.clear(0)

    def num_rows(self):
        return self._matrix.num_rows()

    def num_cols(self):
        return self._matrix.num_cols()

    def __getitem__(self, tuple_idx):
        return self._matrix[tuple_idx[0], tuple_idx[1]]

    def __setitem__(self, tuple_idx, value):
        self._matrix[tuple_idx[0], tuple_idx[1]] = value

    def scale_by(self, value):
        for r in range(self._matrix.num_rows):
            for c in range(self._matrix.num_cols):
                self._matrix[r, c] = self._matrix[r, c] * value

    def __add__(self, other):
        assert other.num_rows() == self._matrix.num_rows() and \
            other.num_cols() == self._matrix.num_cols(), \
        "Matrices should be of same size for addition"
        result_mat = Matrix(self._matrix.num_rows(), self._matrix.num_cols())
        for r in range(self._matrix.num_rows()):
            for c in range(self._matrix.num_cols()):
                result_mat[r, c] = self._matrix[r,c] + other[r,c]
        return result_mat

    def __sub__(self, other):
        assert other.num_rows() == self._matrix.num_rows() and \
            other.num_cols() == self._matrix.num_cols(), \
        "Matrices should be of same size for subtraction"
        result_mat = Matrix(self._matrix.num_rows(), self._matrix.num_cols())
        for r in range(self._matrix.num_rows()):
            for c in range(self._matrix.num_cols()):
                result_mat[r, c] = self._matrix[r,c] - other[r,c]
        return result_mat

    def transpose(self):
        result_mat = Matrix(self._matrix.num_cols(), self._matrix.num_rows())
        for r in range(self._matrix.num_cols()):
            for c in range(self._matrix.num_rows()):
                result_mat[r, c] = self._matrix[c,r]
        return result_mat

    def __mul__(self, other):
        assert other.num_rows() == self._matrix.num_cols(), \
        "Matrices not of compatible size for mutliplication"
        result_mat = Matrix(self._matrix.num_rows(), other.num_cols())

        for i in range(result_mat.num_rows()):
            for j in range(result_mat.num_cols()):
                prod = 0
                for k in range(self._matrix.num_cols()):
                    prod += self._matrix[i,k]*other[k,j]
                result_mat[i,j] = prod
        return result_mat

