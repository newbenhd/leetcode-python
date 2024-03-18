from typing import List


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [1] + [0] * target
        for r in range(1, target + 1):
            for n in nums:
                if r - n >= 0:
                    dp[r] += dp[r - n]
        return dp[-1]

    def combinationSum4Recursion(self, nums: List[int], target: int) -> int:
        dp = [[1 for _ in range(len(nums))]] + [
            [0 for _ in range(len(nums))] for _ in range(target)
        ]
        for r in range(1, target + 1):
            for c in range(len(nums)):
                p = r - nums[c]
                if p >= 0:
                    dp[r][c] += dp[p][c]

        return sum(dp[target])

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * len(s) + [True]
        for i in range(len(s) - 1, -1, -1):
            for word in wordDict:
                if (len(word) + i) <= len(s) and s[i : i + len(word)] == word:
                    dp[i] = dp[i + len(word)]
                if dp[i]:
                    break
        return dp[0]

    def wordBreakRecursion(self, s: str, wordDict: List[str]) -> bool:
        dp = {key: True for key in wordDict}

        current = ""

        def dfs(sub: str) -> bool:
            nonlocal current
            if len(sub) == 0:
                return True
            output = False
            for word in wordDict:
                if sub[: len(word)] in dp:
                    current += sub[: len(word)]
                    if len(current) > len(word):
                        dp[current] = True
                    if sub[len(word) :] in dp:
                        return True
                    output = output or dfs(sub[len(word) :])
            return output

        return dfs(s)

    def longestCommonSubsequenceRecursion(self, text1: str, text2: str) -> int:
        dp = [[-1] * len(text2) for _ in range(len(text1))]

        def dfs(r: int, c: int) -> int:
            if r >= len(text1) or c >= len(text2):
                return 0
            if dp[r][c] != -1:
                return dp[r][c]
            count = 0
            if text1[r] == text2[c]:
                count = 1 + dfs(r + 1, c + 1)
            left = dfs(r + 1, c)
            right = dfs(r, c + 1)
            dp[r][c] = max(left, right, count)
            return dp[r][c]

        return dfs(0, 0)

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]
        for r in range(len(text1) - 1, -1, -1):
            for c in range(len(text2) - 1, -1, -1):
                count = 0
                if text1[r] == text2[c]:
                    count = 1 + dp[r + 1][c + 1]
                count = max(count, dp[r + 1][c], dp[r][c + 1])
                dp[r][c] = count

        return dp[0][0]

    def climbStairs(self, n: int) -> int:
        if n < 2:
            return 1
        step_minus_two, step_minus_one = 1, 1
        for _ in range(2, n + 1):
            step_minus_two, step_minus_one = (
                step_minus_one,
                step_minus_two + step_minus_one,
            )
        return step_minus_one

    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] + [amount + 1] * amount
        # bottom to up computation.
        for coin in coins:
            for n in range(coin, amount + 1):
                dp[n] = min(dp[n], dp[n - coin] + 1)
        return -1 if dp[amount] == amount + 1 else dp[amount]

    def lengthOfLIS(self, nums: List[int]) -> int:
        def bst(sub: List[int], n) -> int:
            L, R = 0, len(sub) - 1
            while L <= R:
                mid = L + (R - L) // 2
                if sub[mid] < n:
                    L = mid + 1
                elif sub[mid] > n:
                    R = mid - 1
                else:
                    return mid

            return L

        output = []
        for n in nums:
            if len(output) == 0 or output[-1] < n:
                output.append(n)
            else:
                i = bst(output, n)
                if output[i] > n:
                    output[i] = n
        return len(output)
