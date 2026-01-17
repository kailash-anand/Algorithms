class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        from collections import defaultdict

        color_to_balls = defaultdict(set)
        ball_to_color = defaultdict(int)
        result = []

        for ball, color in queries:
            if ball in ball_to_color: 
                prev_color = ball_to_color[ball]
                color_to_balls[prev_color].remove(ball)

                if not color_to_balls[prev_color]:
                    del color_to_balls[prev_color]

            ball_to_color[ball] = color
            color_to_balls[color].add(ball)

            result.append(len(color_to_balls.keys()))

        return result