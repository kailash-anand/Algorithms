class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum = 0
        max = -10**100 

        for x in nums:
            sum += x

            if sum > max:
                max = sum

            if sum < 0:
                sum = 0
            
        return max