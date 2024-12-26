class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maximum = 0
        count = 0

        for x in nums:
            if x == 0:
                if count > maximum:
                    maximum = count
                count = 0
            else:
                count += 1

        if count > maximum:
            maximum = count

        return maximum