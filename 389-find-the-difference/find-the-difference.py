class Solution:
    hashTable = {}

    def findTheDifference(self, s: str, t: str) -> str:
        self.initHashTable(s)

        for i in t:
            if i not in self.hashTable:
                self.clearHashTable()
                return i
            else:
                if(self.hashTable[i] == 0):
                    self.clearHashTable()
                    return i

                self.hashTable[i] -= 1

    def initHashTable(self, s: str):
        for i in s:
            if i in self.hashTable:
                self.hashTable[i] += 1
            else:
                self.hashTable[i] = 1

    def clearHashTable(self):
        self.hashTable.clear()

