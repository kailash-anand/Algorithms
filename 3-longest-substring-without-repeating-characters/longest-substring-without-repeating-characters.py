class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()

        left = 0
        right = 0
        count = 0

        while right < len(s):
            if s[right] not in charSet:
                charSet.add(s[right])
                right += 1

                count = max(count, (right - left))
            else:
                while left < len(s) and s[left] != s[right]:
                    charSet.remove(s[left])
                    left += 1
                left += 1
                
                charSet.remove(s[right])

        return count