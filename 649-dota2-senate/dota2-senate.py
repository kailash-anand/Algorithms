class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        from collections import deque

        voterQueue = deque(senate)
        banDcount, banRcount = 0, 0

        while len(set(voterQueue)) > 1:
            if voterQueue[0] == "R":
                if banRcount > 0:
                    voterQueue.popleft()
                    banRcount -= 1
                else:
                    banDcount += 1
                    voterQueue.append(voterQueue.popleft())
            else:
                if banDcount > 0:
                    voterQueue.popleft()
                    banDcount -= 1
                else:
                    banRcount += 1
                    voterQueue.append(voterQueue.popleft())

        if voterQueue[0] == "R":
            return "Radiant"
        else:
            return "Dire"