class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n == 0:
            return

        temp = nums1[0:m]

        index1 = 0
        index2 = 0

        while index1 < m and index2 < n:
            if temp[index1] < nums2[index2]:
                nums1[index1 + index2] = temp[index1]
                index1 += 1
            else:
                nums1[index1 + index2] = nums2[index2]
                index2 += 1

        if index2 == n:
            for i in range(index1, m):
                nums1[index1 + index2] = temp[i]
                index1 += 1
        else:
            for i in range(index2, n):
                nums1[index1 + index2] = nums2[i]
                index2 += 1
            
