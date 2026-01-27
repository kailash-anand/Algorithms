class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        from collections import deque

        voterQueue = deque(senate)
        Rcount, Dcount = 0, 0
        banDcount, banRcount = 0, 0

        for x in senate:
            if x == "D":
                Dcount += 1
            else:
                Rcount += 1

        while Rcount > 0 and Dcount > 0:
            if voterQueue[0] == "R":
                if banRcount > 0:
                    voterQueue.popleft()
                    banRcount -= 1
                    Rcount -= 1
                else:
                    banDcount += 1
                    voterQueue.append(voterQueue.popleft())
            else:
                if banDcount > 0:
                    voterQueue.popleft()
                    banDcount -= 1
                    Dcount -= 1
                else:
                    banRcount += 1
                    voterQueue.append(voterQueue.popleft())

        if voterQueue[0] == "R":
            return "Radiant"
        else:
            return "Dire"