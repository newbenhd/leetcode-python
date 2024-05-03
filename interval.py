from typing import List


class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        output = []
        for i in range(len(intervals)):
            if intervals[i][1] < newInterval[0]:
                output.append(intervals[i])
            elif intervals[i][0] > newInterval[1]:
                output.append(newInterval)
                return output + intervals[i:]
            else:
                newInterval = [
                    min(intervals[i][0], newInterval[0]),
                    max(intervals[i][1], newInterval[1]),
                ]
        output.append(newInterval)
        return output
