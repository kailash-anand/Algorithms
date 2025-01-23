class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result = list()
        intervals.sort()
        currentStart = intervals[0][0]
        currentEnd = intervals[0][1]

        for x in intervals:
            if result == []:
                result.append(x)
            else:
                if x[0] <= currentEnd:
                    newStart = 0
                    newEnd = 0

                    if x[0] < currentStart:
                        newStart = x[0]
                    else:
                        newStart = currentStart

                    if x[1] > currentEnd:
                        newEnd = x[1]
                    else:
                        newEnd = currentEnd

                    result.pop(len(result) - 1)
                    result.append([newStart, newEnd])
                    currentStart = newStart
                    currentEnd = newEnd
                else:
                    result.append(x)
                    currentStart = x[0]
                    currentEnd = x[1]

        return result