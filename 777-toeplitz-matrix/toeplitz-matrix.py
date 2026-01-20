class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        row = 0
        for col in range(len(matrix[0])):
            row = 0
            diagonal_val = matrix[row][col]

            while row < len(matrix) and col < len(matrix[0]):
                if matrix[row][col] != diagonal_val:
                    return False

                row += 1
                col += 1
            
        col = 0
        for row in range(1, len(matrix)):
            col = 0
            diagonal_val = matrix[row][col]
            
            while row < len(matrix) and col < len(matrix[0]):
                if matrix[row][col] != diagonal_val:
                    return False

                row += 1
                col += 1

        return True