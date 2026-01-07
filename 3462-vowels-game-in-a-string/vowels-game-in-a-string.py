class Solution:
    def doesAliceWin(self, s: str) -> bool:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        count = 0

        for ch in s:    
            if ch in vowels:
                count += 1

        if count == 0:
            return False

        return True
        