class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        leftPrefix = [nums[0]]
        rightPrefix = [nums[len(nums) - 1]]
        result = []

        for i in range(1, len(nums)):
            leftPrefix.append(leftPrefix[i - 1] * nums[i])
            rightPrefix.append(rightPrefix[i - 1] * nums[len(nums) - i - 1])

        for i in range(len(nums)):
            rightIndex = len(nums) - i - 2
            leftIndex = i - 1
            product = 1

            if leftIndex >= 0:
                product *= leftPrefix[leftIndex]

            if rightIndex >= 0:
                product *= rightPrefix[rightIndex]

            result.append(product)

        return result