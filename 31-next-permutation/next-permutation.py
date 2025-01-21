class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        minimum = 0
        pivot = 0

        for i in reversed(range(1, length)):
            if nums[i - 1] < nums[i]:
                pivot = i - 1
                break

        minimum = pivot + 1

        for i in reversed(range(1, length)):
            if nums[i - 1] < nums[i]:
                self.swap(i-1, minimum, nums)
                self.sortSelective(nums[i:length], nums)
                return
            else:
                if nums[i] < nums[minimum] and nums[i] > nums[pivot]:
                    minimum = i

        nums.sort()

    def swap(self, num1, num2, list):
        temp = list[num1]
        list[num1] = list[num2]
        list[num2] = temp

    def sortSelective(self, toSort, toAdd):
        toSort.sort()

        start = len(toAdd) - len(toSort)
        end = len(toAdd)
        
        toAdd[start:end] = toSort