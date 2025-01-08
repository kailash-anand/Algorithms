class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        max = nums[0]
        for i in range(len(nums)):
            if count == 0:
                max = nums[i]
                count = 1
            elif max == nums[i]:
                count += 1
            else:
                count -= 1

        return max