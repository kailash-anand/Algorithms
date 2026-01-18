class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        rows, cols = len(mat), len(mat[0])

        if (rows * cols) != (r * c):
            return mat

        new_mat = [[0] * c for _ in range(r)]

        row, col = 0, 0
        for i in range(r):
            for j in range(c):
                new_mat[i][j] = mat[row][col]

                if (col + 1) < cols:
                    col += 1
                else:
                    row += 1
                    col = 0

        return new_mat
