class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        disappeared = []

        for i in range(len(nums)):
            while (nums[i] != (i + 1)) and (nums[i] != (nums[nums[i] - 1])):
                temp = nums[nums[i] - 1]
                nums[nums[i] - 1] = nums[i]
                nums[i] = temp   

        for i in range(len(nums)):
            if nums[i] != (i + 1):
                disappeared.append(i + 1)

        return disappeared

        

            