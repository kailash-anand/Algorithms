class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rowLength = len(matrix)
        colLength = len(matrix[0])

        extra = 1

        for i in range(rowLength):
            for j in range(colLength):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    if j == 0:
                        extra = 0
                    else:
                        matrix[0][j] = 0

        for i in range(1, rowLength):
            for j in range(1, colLength):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if matrix[0][0] == 0:
            for i in range(colLength):
                matrix[0][i] = 0

        if extra == 0:
            for i in range(rowLength):
                matrix[i][0] = 0