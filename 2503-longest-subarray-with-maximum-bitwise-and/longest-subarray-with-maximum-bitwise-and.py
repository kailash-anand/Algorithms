class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        maxAND = max(nums)
        length, max_len = 0, 0

        for i in range(len(nums)):
            if nums[i] == maxAND:
                length += 1
            else:
                if length > max_len:
                    max_len = length
                length = 0

        if length > max_len:
            max_len = length

        return max_len