from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        new_end = intervals[0][1]
        removal = 0
        for start, end in intervals[1:]:
            if start >= new_end:
                new_end = end
            else:
                removal += 1
                new_end = min(new_end, end)
        return removal
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        output = []
        start, end = intervals[0]
        for interval in intervals[1:]:
            if interval[0] > end:
                output.append([start, end])
                start, end = interval
            start, end = min(interval[0], start), max(interval[1], end)
        output.append([start, end])
        return output

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
