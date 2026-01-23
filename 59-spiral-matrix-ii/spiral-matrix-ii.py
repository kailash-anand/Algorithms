class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0] * n for _ in range(n)]
        value = 1
        
        left, right = 0, n - 1
        top, down = 0, n - 1

        while left <= right and top <= down:
            for i in range(left, right + 1):
                matrix[top][i] = value
                value += 1
            top += 1

            for i in range(top, down + 1):
                matrix[i][right] = value
                value += 1
            right -= 1

            for i in range(right, left - 1, -1):
                matrix[down][i] = value
                value += 1
            down -= 1

            for i in range(down, top - 1, -1):
                matrix[i][left] = value
                value += 1
            left += 1

        return matrix