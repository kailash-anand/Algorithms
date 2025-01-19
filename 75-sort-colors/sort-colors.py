class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeroCount = 0
        oneCount = 0

        for x in nums:
            if x == 0:
                zeroCount += 1
            elif x == 1:
                oneCount += 1

        for i in range(len(nums)):
            if zeroCount > 0:
                nums[i] = 0
                zeroCount -= 1
            elif oneCount > 0:
                nums[i] = 1
                oneCount -= 1
            else:
                nums[i] = 2
            