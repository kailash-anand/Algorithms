class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        from collections import defaultdict
        counts = defaultdict(int)

        for x in arr:
            counts[x] += 1

        if len(set(counts.values())) != len(counts.values()):
            return False
        else:
            return True