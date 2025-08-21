class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()

        def dfs(i, curr, currSum):
            if currSum == target:
                result.append(curr.copy())
                return

            for j in range(i, len(candidates)):
                if currSum + candidates[j] > target:
                    return

                curr.append(candidates[j])
                dfs(j, curr, currSum + candidates[j])
                curr.pop()

        dfs(0, [], 0)
        return result       
    