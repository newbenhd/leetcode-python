from typing import List
import random


class RandomizedSet:
    def __init__(self):
        self.position = []
        self.index = {}
        # same propability of randomly pick element
        # O(1) for every function

    def search(self, val: int) -> bool:
        return val in self.index

    def insert(self, val: int) -> bool:
        if self.search(val):
            return False
        self.position.append(val)
        self.index[val] = len(self.position) - 1
        return True

    def remove(self, val: int) -> bool:
        if not self.search(val):
            return False
        idx = self.index[val]
        self.position[idx] = self.position[-1]
        self.index[self.position[-1]] = idx
        self.position.pop()
        del self.index[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.position)


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
