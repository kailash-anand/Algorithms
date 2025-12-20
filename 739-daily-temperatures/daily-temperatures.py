class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        answer = [0] * n
        stack = [0]

        for i in range(1, n):
            while bool(stack) and temperatures[i] > temperatures[stack[-1]]:
                answer[stack.pop()] = i - stack[-1]

            stack.append(i)

        return answer