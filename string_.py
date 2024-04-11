class Solution:
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
