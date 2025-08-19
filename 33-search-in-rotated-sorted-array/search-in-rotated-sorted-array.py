class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2 

            if target == nums[mid]:
                return mid

            if nums[left] < nums[right]:
                if target > nums[mid]:
                    left = mid + 1
                else:
                    right = mid - 1  
            elif nums[mid] >= nums[left] and target >= nums[left]:
                if target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            elif nums[mid] >= nums[left] and target < nums[left]:
                left = mid + 1
            elif nums[mid] < nums[left] and target >= nums[left]:
                right = mid - 1
            elif nums[mid] < nums[left] and target < nums[left]:
                if target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                break

        return -1