class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        histogram = {}
        size = len(nums)
        count = 0
        
        self.initHistogram(histogram, nums)
        if(self.isDistinct(histogram)):
            return 0

        while(1):
            if size > 2:
                val1 = nums.pop(0)
                val2 = nums.pop(0)
                val3 = nums.pop(0)

                histogram[val1] -= 1
                histogram[val2] -= 1
                histogram[val3] -= 1

                if(histogram[val1] <= 1 and histogram[val2] <= 1 and histogram[val3] <= 1):
                    if(self.isDistinct(histogram)):
                        return count + 1

                size -= 3
                count += 1
            else:
                if size <= 0:
                    return count
                return count + 1
            
    def initHistogram(self, histogram: dict, nums: List[int]):
        for x in nums:
            if x in histogram:
                histogram[x] += 1
            else:
                histogram[x] = 1

    def isDistinct(self, histogram: dict) -> bool:
        for x in histogram:
            if histogram[x] > 1:
                return False

        return True