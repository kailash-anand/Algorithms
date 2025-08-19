class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rowLen, colLen = len(heights), len(heights[0])
        pacific, atlantic = set(), set()

        def dfs(row, col, visitSet, prevHeight):
            if (row < 0 or col < 0 or row == rowLen or col == colLen
                or (row, col) in visitSet or heights[row][col] < prevHeight):
                return

            visitSet.add((row, col))
            dfs(row - 1, col, visitSet, heights[row][col])
            dfs(row + 1, col, visitSet, heights[row][col])
            dfs(row, col - 1, visitSet, heights[row][col])
            dfs(row, col + 1, visitSet, heights[row][col])

        for col in range(colLen):
            dfs(0, col, pacific, heights[0][col])
            dfs(rowLen - 1, col, atlantic, heights[rowLen - 1][col])

        for row in range(rowLen):
            dfs(row, 0, pacific, heights[row][0])
            dfs(row, colLen - 1, atlantic, heights[row][colLen - 1])

        return list(pacific.intersection(atlantic))