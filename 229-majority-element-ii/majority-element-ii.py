import math

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        target = math.floor(len(nums)/3)
        table = Counter(nums)
        result = list()

        for x in table:
            if table[x] > target:
                result.append(x)

        return result
