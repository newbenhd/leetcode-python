from typing import List, Dict
from collections import Counter


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        book: Dict[str, List[str]] = {}
        for s in strs:
            cs = [0] * 26
            for k, v in Counter(s).items():
                cs[ord(k) - ord("a")] = v
            key = ",".join(map(lambda x: str(x), cs))
            if key not in book:
                book[key] = []
            book[key].append(s)

        return list(book.values())

    def isAnagram2(self, s: str, t: str) -> bool:
        def index(x: str):
            return ord(x) - ord("a")

        if len(s) != len(t):
            return False
        v = [0] * 26
        for i in range(len(s)):
            v[index(s[i])] += 1
            v[index(t[i])] -= 1
        return not any(v)

    def isAnagram(self, s: str, t: str) -> bool:
        # check two strings have same length
        # map s to dictionary of key equal to character and value to occurance and track the count of unique characters
        # iterate t over index and decrement the s dictionary's value on the key equal to the character of current index
        # if it ever goes to zero decrement the count of unique character by 1. If it's less than zero, increment the count by 1
        # at the end of iteration, check if the count of unique character is equal to zero.
        s_count = Counter(s)
        unique = len(s_count)
        for c in t:
            if c not in s_count:
                return False
            s_count[c] -= 1
            if s_count[c] == 0:
                unique -= 1
            if s_count[c] < 0:
                return False
        return unique == 0

    def minWindow(self, s: str, t: str) -> str:
        # ("aaaaaaaaaaaabbbbbcdd", "abcdd", "abbbbbcdd"),
        # "abbbb"
        # a: 0
        # b: -1
        # c: 1
        # L: 4
        # count: 0
        # lowest: a
        t_table = Counter(t)
        count = len(t_table)
        found = False
        lowest = s
        L = 0
        for i in range(len(s)):
            if s[i] in t_table:
                t_table[s[i]] -= 1
                if t_table[s[i]] == 0:
                    count -= 1
            while count == 0:
                found = True
                if i - L + 1 < len(lowest):
                    lowest = s[L : i + 1]
                if s[L] in t_table:
                    t_table[s[L]] += 1
                    if t_table[s[L]] > 0:
                        count += 1
                L += 1
        return lowest if found else ""

    def characterReplacement(self, s: str, k: int) -> int:
        # sum(minor_character_count) < k.
        # major = A
        # {
        #   A: 4,
        #   B: 2,
        #   C: 3,
        # }
        # L: 0
        # The overall plan is that when we count the substring
        # we have to keep the sum of minor characters, meaning
        # any characters which is not major, and constantly update
        # the current major character. if the sum of minor character
        # is greater than k, then we increment the left pointer until
        # the sum is less than K (also, update the major character).
        # During iteration, keep track of the maximum substring length.
        # At the end of iteration, we return the maximum substring length.
        L = 0
        dominant = 0
        highest = 0
        cache = [0] * 26
        index = lambda x: ord(x) - ord("A")
        for i in range(len(s)):
            cache[index(s[i])] += 1
            dominant = max(dominant, cache[index(s[i])])
            if i - L + 1 > k + dominant:
                cache[index(s[L])] -= 1
                L += 1
            highest = max(highest, i - L + 1)
        return highest

    def lengthOfLongestSubstring(self, s: str) -> int:
        # keep track of substring without repeating characters using two pointers: left and right
        # iterate through the input string and check if the current substring contains duplicate
        # if it contains the duplicate, then update the left pointer to next left pointer
        # how to find the duplicate: cache the unique characters as key and its current index as value
        cache = {}
        longest = 0
        left = -1
        for i in range(len(s)):
            if s[i] in cache and left < cache[s[i]]:
                left = cache[s[i]]
            longest = max(longest, i - left)
            cache[s[i]] = i
        return longest
