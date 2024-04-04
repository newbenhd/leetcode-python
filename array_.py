from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # keep highest and lowest product subarray.
        # iterate through the array nums and
        # set highest or lowest to current element if
        # product of current element to highest or lowest is
        # either lower or greater than current element respectively,
        # and vice versa.
        # return the maximum of the possible product subarray.
        # a-b-c-d-e
        # a: a
        # b: b, ba
        # c: c, cb, cba
        # d: d, dc, dcb, dcba
        # e: e, ed, edc, edcb, edcba
        high = low = highest = nums[0]
        for n in nums[1:]:
            high, low = max(high * n, low * n, n), min(high * n, low * n, n)
            if high > highest:
                highest = high
        return highest

    def maxSubArray(self, nums: List[int]) -> int:
        # element in the subarray has to be adjacent to one another. Therefore,
        # if we iterate through the array nums, let's keep track of the max number,
        # and set/reset cutting point to current index when current element is greater
        # than the sum of subarray.
        high, sub = nums[0], nums[0]
        for i in range(1, len(nums)):
            sub = max(nums[i], sub + nums[i])
            if sub > high:
                high = sub
        return high

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
