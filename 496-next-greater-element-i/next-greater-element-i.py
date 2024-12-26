class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        hashtable = {}

        for i in range(len(nums2)):
            hashtable[nums2[i]] = i

        for i in range(len(nums1)):
            j = hashtable[nums1[i]]
            ans.append(-1)

            for j in range(j, len(nums2)):
                if nums2[j] > nums1[i]:
                    ans.pop(len(ans) - 1)
                    ans.append(nums2[j])
                    break

        return ans
                
