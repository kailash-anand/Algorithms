class Solution:
    def countPermutations(self, complexity: List[int]) -> int:
        if complexity[0] != min(complexity) or complexity.count(complexity[0]) > 1:
            return 0

        MOD = 10**9 + 7
        n = len(complexity)
        combinations = 1

        for i in range(1, n):
            combinations = (combinations * i) % MOD

        return combinations 