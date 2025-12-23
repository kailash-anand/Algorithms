class Solution:
    def countBits(self, n: int) -> List[int]:
        if n == 0:
            return [0]

        answer = []
        answer.append(0)
        answer.append(1)

        for i in range(2, n + 1):
            if (i % 2) == 0:
                answer.append(answer[i // 2])
            else:
                answer.append(answer[i // 2] + 1)

        return answer