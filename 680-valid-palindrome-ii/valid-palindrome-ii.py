class Solution:
    def validPalindrome(self, s: str) -> bool:
        length = len(s)
        start = 0
        end = length - 1

        if length == 1:
            return True

        while start < end:
            if(s[start] != s[end]):
                if self.isPalindrome(s[0:start] + s[start + 1:length]):
                    return True
                if self.isPalindrome(s[0:end] + s[end + 1:length]):
                    return True
                return False

            start += 1
            end -= 1

        return True
        
    def isPalindrome(self, s: str) -> bool:
        if s[::-1] == s:
            return True
        
        return False