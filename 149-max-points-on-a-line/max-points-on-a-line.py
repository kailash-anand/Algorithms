import math
from typing import List
from collections import defaultdict

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        n = len(points)
        maxCount = 1  

        for i in range(n):
            basePoint = points[i]
            vectorTable = defaultdict(int)
            duplicates = 0

            for j in range(n):
                if i == j:
                    continue
                targetPoint = points[j]

                dx, dy = self.vector(basePoint, targetPoint)

                if dx == 0 and dy == 0:
                    duplicates += 1
                    continue

                direction = self.normalizeVector((dx, dy))
                vectorTable[direction] += 1

            currentMax = max(vectorTable.values(), default=0)
            maxCount = max(maxCount, currentMax + duplicates + 1)  

        return maxCount

    def vector(self, basePoint: List[int], targetPoint: List[int]) -> (int, int):
        return (targetPoint[0] - basePoint[0], targetPoint[1] - basePoint[1])

    def normalizeVector(self, point: (int, int)) -> (int, int):
        dx, dy = point
        g = math.gcd(dx, dy)
        dx //= g
        dy //= g

        if dx < 0:
            dx, dy = -dx, -dy
        elif dx == 0 and dy < 0:
            dy = -dy

        return (dx, dy)
