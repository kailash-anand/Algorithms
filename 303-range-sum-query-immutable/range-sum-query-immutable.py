class NumArray(object):
    numsMain = []

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.numsMain = nums
        

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        sum = 0
        for val in range(left, right + 1):
            sum += self.numsMain[val]

        return sum
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)