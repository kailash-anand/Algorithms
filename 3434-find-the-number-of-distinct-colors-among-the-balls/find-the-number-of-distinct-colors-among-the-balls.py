class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        color_counts = {}
        ball_to_color = {}
        result = []

        for ball, color in queries:
            if ball in ball_to_color: 
                prev_color = ball_to_color[ball]
                color_counts[prev_color] -= 1

                if color_counts[prev_color] == 0:
                    del color_counts[prev_color]

            ball_to_color[ball] = color
            color_counts[color] = color_counts.get(color, 0) + 1

            result.append(len(color_counts))

        return result