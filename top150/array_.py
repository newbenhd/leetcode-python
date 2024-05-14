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
    def romanToInt(self, s: str) -> int:
        output = 0
        map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        last = 'I'
        for i in range(len(s)):
            if i + 1 < len(s) and map[s[i]] < map[s[i + 1]]:
                output -= map[s[i]]
            else:
                output += map[s[i]]
        return output

    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        total, output = 0, 0
        for i in range(len(gas)):
            total += (gas[i] - cost[i])
            if total < 0:
                total = 0
                output = i + 1
        return output


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
