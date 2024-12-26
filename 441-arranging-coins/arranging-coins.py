class Solution:
    def arrangeCoins(self, n: int) -> int:
        if n == 1:
            return 1

        current = 1

        while n > 0:
            if n < current:
                return current - 1

            n -= current
            current += 1

        return current - 1