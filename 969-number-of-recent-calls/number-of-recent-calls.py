class RecentCounter:
    from collections import deque

    def __init__(self):
        self.requestQueue = deque()
        self.requestHistoryTime = 3000

    def ping(self, t: int) -> int:
        self.requestQueue.append(t)

        if t > self.requestHistoryTime:
            startTime = t - self.requestHistoryTime

            while self.requestQueue[0] < startTime:
                self.requestQueue.popleft()

        return len(self.requestQueue)

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)