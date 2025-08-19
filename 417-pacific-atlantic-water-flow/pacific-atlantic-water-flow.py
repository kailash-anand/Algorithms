class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        canFlowPacific = [[False for _ in row] for row in heights]
        canFlowAtlantic = [[False for _ in row] for row in heights]
        seen = set()

        def dfs(startIndex):
            i, j = startIndex
            seen.add((i, j))

            if canFlowPacific[i][j] and canFlowAtlantic[i][j]:
                return

            # Top
            if (i - 1) >= 0:
                if heights[i - 1][j] <= heights[i][j]:
                    if not canFlowPacific[i - 1][j] and not canFlowAtlantic[i - 1][j] and not ((i - 1), j) in seen:
                        dfs(((i - 1), j))

                    if canFlowPacific[i - 1][j]:
                        canFlowPacific[i][j] = True

                    if canFlowAtlantic[i - 1][j]:
                        canFlowAtlantic[i][j] = True
            else:
                canFlowPacific[i][j] = True

            if canFlowPacific[i][j] and canFlowAtlantic[i][j]:
                return

            # Left
            if (j - 1) >= 0:
                if heights[i][j - 1] <= heights[i][j]:
                    if not canFlowPacific[i][j - 1] and not canFlowAtlantic[i][j - 1] and not (i, (j - 1)) in seen:
                        dfs((i, (j - 1)))

                    if canFlowPacific[i][j - 1]:
                        canFlowPacific[i][j] = True

                    if canFlowAtlantic[i][j - 1]:
                        canFlowAtlantic[i][j] = True
            else:
                canFlowPacific[i][j] = True

            if canFlowPacific[i][j] and canFlowAtlantic[i][j]:
                return

            # Bottom
            if (i + 1) <= (len(heights) - 1):
                if heights[i + 1][j] <= heights[i][j]:
                    if not canFlowPacific[i + 1][j] and not canFlowAtlantic[i + 1][j] and not ((i + 1), j) in seen:
                        dfs(((i + 1), j))

                    if canFlowPacific[i + 1][j]:
                        canFlowPacific[i][j] = True

                    if canFlowAtlantic[i + 1][j]:
                        canFlowAtlantic[i][j] = True
            else:
                canFlowAtlantic[i][j] = True

            if canFlowPacific[i][j] and canFlowAtlantic[i][j]:
                return

            # Right
            if (j + 1) <= (len(heights[0]) - 1):
                if heights[i][j + 1] <= heights[i][j]:
                    if not canFlowPacific[i][j + 1] and not canFlowAtlantic[i][j + 1] and not (i, (j + 1)) in seen:
                        dfs((i, (j + 1)))

                    if canFlowPacific[i][j + 1]:
                        canFlowPacific[i][j] = True

                    if canFlowAtlantic[i][j + 1]:
                        canFlowAtlantic[i][j] = True
            else:
                canFlowAtlantic[i][j] = True

        for i in range(len(heights)):
            for j in range(len(heights[0])):
                seen.clear()
                dfs((i, j))

        canFlow = []

        for i in range(len(heights)):
            for j in range(len(heights[0])):
                if canFlowPacific[i][j] and canFlowAtlantic[i][j]:
                    canFlow.append([i, j])

        return canFlow