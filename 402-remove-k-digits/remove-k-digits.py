class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []

        for ch in num:
            while stack and int(ch) < int(stack[-1]) and k > 0:
                stack.pop()
                k -= 1

            stack.append(ch)

        while k > 0:
            stack.pop()
            k -= 1

        res = ''.join(stack).lstrip('0')
        return '0' if res == '' else res