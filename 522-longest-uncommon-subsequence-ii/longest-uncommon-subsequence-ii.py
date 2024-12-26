class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        strs.sort(reverse=True, key=self.sort)
        
        rejected = []
        selected = []

        for i in range(len(strs)):
            if i == 0:
                selected.append(strs[i])
            elif self.validate(selected, rejected, strs[i]):
                if selected != [] and len(strs[i]) > len(selected[0]):
                    rejected.extend(selected)
                    selected.clear()
                    selected.append(strs[i])
                else:
                    selected.append(strs[i])
            else:
                for x in selected:
                    if x == strs[i]:
                        selected.remove(strs[i])
                        break
                rejected.append(strs[i])

        if selected == []:
            return -1
        else:
            return len(selected[0])
            
    def sort(self, e):
        return len(e)


    def validate(self, selected: str, rejected: List[str], s: str) -> bool:
        for x in selected:
            if self.isSubsequence(x, s):
                return False

        for x in rejected:
            if self.isSubsequence(x, s):
                return False

        return True

    def isSubsequence(self, a: str, b: str) -> bool:
        if a == b:
            return True

        aLen = len(a)
        bLen = len(b)

        if bLen > aLen:
            return False

        aCount = 0
        bCount = 0

        while(aCount < aLen and bCount < bLen):
            if a[aCount] == b[bCount]:
                bCount += 1

            aCount += 1

        if bCount == bLen:
            return True
        else:
            return False
