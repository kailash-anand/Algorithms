class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        if a == b:
            return -1

        aLen = len(a)
        bLen = len(b)

        if aLen > bLen:
            return aLen
        else:
            return bLen

        