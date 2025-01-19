class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rowLength = len(matrix)
        colLength = len(matrix[0])
        rows = [0] * rowLength
        cols = [0] * colLength

        for i in range(rowLength):
            for j in range(colLength):
                if matrix[i][j] == 0:
                    rows[i] = 1
                    cols[j] = 1

        for i in range(rowLength):
            for j in range(colLength):
                if rows[i] == 1 or cols[j] == 1:
                    matrix[i][j] = 0