class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        result = 0
        n, m = len(nums1), len(nums2)

        if m % 2 != 0:
            for x in nums1:
                result ^= x

        if n % 2 != 0:
            for y in nums2:
                result ^= y

        return result