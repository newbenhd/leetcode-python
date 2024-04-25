from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        freq = [0] * (len(citations) + 1)
        for x in citations:
            if x >= len(citations):
                freq[len(citations)] += 1
            else:
                freq[x] += 1
        total = 0
        for i in range(len(freq) - 1, -1, -1):
            total += freq[i]
            if total >= i:
                return i

    def hIndexSort(self, citations: List[int]) -> int:
        citations.sort()
        for i in range(len(citations)):
            if citations[i] >= len(citations) - i:
                return len(citations) - i
        return 0
