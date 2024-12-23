class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        letterDatabase = {}

        self.initLetterDatabase(magazine, letterDatabase)

        for x in ransomNote:
            if x in letterDatabase:
                letterDatabase[x] -= 1

                if(letterDatabase[x] < 0):
                    return False
            else:
                return False
        
        return True

    def initLetterDatabase(self, magazine: str, letterDatabase: dict):
        for x in magazine:
            if x in letterDatabase:
                letterDatabase[x] += 1
            else:
                letterDatabase[x] = 1