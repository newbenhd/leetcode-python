from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)
        prefix = nums[0]
        for i in range(1, len(nums)):
            output[i] *= prefix
            prefix = prefix * nums[i]
        postfix = nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            output[i] *= postfix
            postfix = postfix * nums[i]
        return output

    def containsDuplicate(self, nums: List[int]) -> bool:
        hash = set()
        for n in nums:
            if n in hash:
                return True
            hash.add(n)
        return False

    def maxProfit(self, prices: List[int]) -> int:
        low, high = prices[0], 0
        for n in prices[1:]:
            if low > n:
                low = n
            elif n - low > high:
                high = n - low
        return high

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        cache = {}
        for i in range(len(nums)):
            compl = target - nums[i]
            if compl in cache:
                return [cache[compl], i]
            cache[nums[i]] = i
        return []
