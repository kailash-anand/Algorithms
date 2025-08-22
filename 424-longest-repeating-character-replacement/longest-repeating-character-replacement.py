class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freqTable = dict()
        left, right = 0, 0
        maxF = 0
        res = 0

        for right in range(len(s)):
            freqTable[s[right]] = 1 + freqTable.get(s[right], 0)
            maxF = max(maxF, freqTable[s[right]])

            while (right - left + 1) - maxF > k:
                freqTable[s[left]] -= 1
                left += 1

            res = max(res, right - left + 1)

        return res       