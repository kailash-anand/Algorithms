class Solution:
    def doesAliceWin(self, s: str) -> bool:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        
        if any(ch in vowels for ch in s):
            return True

        return False
        