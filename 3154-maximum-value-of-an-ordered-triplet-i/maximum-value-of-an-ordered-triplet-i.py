class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        max = 0

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    curr = (nums[i] - nums[j]) * nums[k]
                    if curr > max:
                        max = curr

        return max