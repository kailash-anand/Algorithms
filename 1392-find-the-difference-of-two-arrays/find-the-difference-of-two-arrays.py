class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        answer = []
        nums1_set = set(nums1)
        nums2_set = set(nums2)

        answer.append(list(nums1_set - nums2_set))
        answer.append(list(nums2_set - nums1_set))

        return answer