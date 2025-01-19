class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1,1]]

        triangle = list()
        temp = list()

        triangle.append([1])
        triangle.append([1,1])

        for i in range(2, numRows):
            temp.append(1)
            for j in range(len(triangle[i - 1]) - 1):
                temp.append(triangle[i - 1][j] + triangle[i - 1][j + 1])
            temp.append(1)
            triangle.append(temp.copy())
            temp.clear()

        return triangle