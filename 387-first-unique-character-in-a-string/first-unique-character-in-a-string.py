class Solution:
    def firstUniqChar(self, s: str) -> int:
        hashTable = {}

        self.initHashTable(s, hashTable)

        for x in s:
            if hashTable[x] == True:
                return s.find(x)

        return -1

    def initHashTable(self, s: str, table: dict):
        for x in s:
            if x in table:
                table[x] = False
            else:
                table[x] = True