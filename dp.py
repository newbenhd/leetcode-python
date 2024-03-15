from typing import List


class Solution:
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
