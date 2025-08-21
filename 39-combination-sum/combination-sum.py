class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def dfs(i, curr, currSum):
            if currSum == target:
                result.append(curr.copy())
                return

            if i >= len(candidates) or currSum > target:
                return

            curr.append(candidates[i])
            dfs(i, curr, currSum + candidates[i])
            curr.pop()
            dfs(i + 1, curr, currSum)

        dfs(0, [], 0)
        return result       
    