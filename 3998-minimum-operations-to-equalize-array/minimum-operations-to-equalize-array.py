class Solution:
    def minOperations(self, nums: List[int]) -> int:
        all_equal = True

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                all_equal = False

        if all_equal:
            return 0
        else:
            return 1
