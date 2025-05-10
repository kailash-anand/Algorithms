class Solution:
    def averageValue(self, nums: List[int]) -> int:
        sum = 0
        count = 0

        for x in nums:
            if (x % 2) == 0 and (x % 3) == 0:
                sum += x
                count += 1

        return 0 if count == 0 else int(sum/count)
