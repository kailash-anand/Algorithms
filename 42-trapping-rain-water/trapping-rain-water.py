class Solution:
    def trap(self, height: List[int]) -> int:
        leftMaxes = [0] * len(height)
        rightMaxes = [0] * len(height)

        runningMax = 0
        for i in range(0, len(height)):
            leftMaxes[i] = runningMax
            if height[i] > runningMax:
                runningMax = height[i]

        runningMax = 0
        for i in range(len(height) - 1, -1, -1):
            rightMaxes[i] = runningMax
            if height[i] > runningMax:
                runningMax = height[i]

        totalWaterTrapped = 0
        for i in range(len(height)):
            water = min(leftMaxes[i], rightMaxes[i]) - height[i]
            if water > 0:
                totalWaterTrapped += water

        return totalWaterTrapped