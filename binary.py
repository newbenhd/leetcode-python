from typing import List


class Solution:
    def hammingWeight(self, n: int) -> int:
        b = f"{n:b}"
        count = 0
        for c in b:
            if c == "1":
                count += 1
        return count

    def countBits(self, n: int) -> List[int]:
        # 0 - 0000
        # 1 - 0001
        # 2 - 0010
        # 3 - 0011
        # 4 - 0100
        # 5 - 0101
        # 6 - 0110
        # 7 - 0111
        # 8 - 1000
        dp = [0] * (n + 1)
        offset = 1
        for i in range(1, n + 1):
            if offset * 2 == i:
                offset = i
            dp[i] = 1 + dp[i - offset]
        return dp

    def getSum(self, a: int, b: int) -> int:
        while b != 0:
            temp = (a & b) << 1
            a = a ^ b
            b = temp
        return a
