class NumArray:
    prefixSum = []

    def __init__(self, nums: List[int]):
        self.prefixSum.clear()
        self.prefixSum.append(nums[0])

        for i in range(1, len(nums)):
            self.prefixSum.append(nums[i] + self.prefixSum[i - 1])

    def sumRange(self, left: int, right: int) -> int:
        if((left - 1) >= 0):
            return self.prefixSum[right] - self.prefixSum[left - 1]

        return self.prefixSum[right]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)