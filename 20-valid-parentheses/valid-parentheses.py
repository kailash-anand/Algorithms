class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        PARENTHESIS_MAP = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for char in s:
            if char not in PARENTHESIS_MAP:
                stack.append(char)
            else:
                if not bool(stack):
                    return False
                elif PARENTHESIS_MAP[char] != stack[-1]:
                    return False
                else:
                    stack.pop()

        if bool(stack):
            return False
        
        return True

            

            