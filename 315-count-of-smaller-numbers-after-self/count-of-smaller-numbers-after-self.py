class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        pair_nums = [(v, i) for i, v in enumerate(nums)]
        counts = [0] * len(nums)

        def merge(nums, left, mid, right):
            n1 = mid - left + 1
            n2 = right - mid

            L = [0] * n1
            R = [0] * n2

            for i in range(n1):
                L[i] = nums[left + i]
            for i in range(n2):
                R[i] = nums[mid + 1 + i]

            i = 0
            j = 0
            k = left

            while i < n1 and j < n2:
                if L[i][0] <= R[j][0]:
                    nums[k] = L[i]
                    counts[L[i][1]] += j
                    i += 1
                else:
                    nums[k] = R[j]
                    j += 1
                k += 1

            while i < n1:
                nums[k] = L[i]
                counts[L[i][1]] += j
                i += 1
                k += 1

            while j < n2:
                nums[k] = R[j]
                j += 1
                k += 1

        def merge_sort(nums, left, right):
            if left < right:
                mid = (left + right) // 2

                merge_sort(nums, left, mid)
                merge_sort(nums, mid + 1, right)
                merge(nums, left, mid, right)

        merge_sort(pair_nums, 0, len(nums) - 1)
        return counts