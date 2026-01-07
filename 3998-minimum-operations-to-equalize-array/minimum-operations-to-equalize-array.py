class Solution:
    def minOperations(self, nums: List[int]) -> int:
        if len(set(nums)) != 1:
            return 1

        return 0
