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
