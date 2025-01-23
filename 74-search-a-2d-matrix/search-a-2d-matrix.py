import math

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        totalLength = m * n

        left = 0
        right = totalLength - 1

        while left < right:
            mid = int((left + right)/2)
            midIndex = self.getIndex(mid, m, n)

            if matrix[midIndex[0]][midIndex[1]] == target:
                return True

            if target > matrix[midIndex[0]][midIndex[1]]:
                left = mid + 1
            else:
                right = mid
            
        midIndex = self.getIndex(int((left + right)/2), m, n)
        if matrix[midIndex[0]][midIndex[1]] == target:
                return True

        return False

    def getIndex(self, target: int, rows: int, columns: int) -> list:
        if target >= (rows * columns):
            return None

        row = int(math.floor(target/columns))
        col = target - (row * columns)

        return [row, col]



