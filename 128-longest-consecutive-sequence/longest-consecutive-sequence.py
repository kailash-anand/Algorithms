class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        setNums = set(nums)

        count = 0
        res = 0

        for num in setNums:
            if (num - 1) not in setNums:
                count = 1
                value = num + 1

                while value in setNums:
                    count += 1
                    value += 1

                res = max(res, count)
            
        return res