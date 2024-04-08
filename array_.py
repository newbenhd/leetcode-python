from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output = []
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            L, R = i + 1, len(nums) - 1
            while L < R:
                if nums[i] + nums[L] + nums[R] == 0:
                    output.append([nums[i], nums[L], nums[R]])
                    while L < R and nums[L] == nums[L + 1]:
                        L += 1
                    while L < R and nums[R] == nums[R - 1]:
                        R -= 1
                    L, R = L + 1, R - 1
                elif nums[i] + nums[L] + nums[R] > 0:
                    R -= 1
                else:
                    L += 1
        return output

    def binarySearch(self, partial: List[int], target: int) -> int:
        L, R = 0, len(partial) - 1
        while L < R:
            mid = L + ((R - L) // 2)
            if partial[mid] == target:
                return mid
            elif partial[mid] < target:
                L = mid
            else:
                R = mid
        return -1

    def search(self, nums: List[int], target: int) -> int:
        # [4,5,6,7,0,1,2], 0
        # [4,5,6] 7 [0,1,2]
        # [7,0,1,2]
        # [7,0] 1 [2]
        # [7,0,1]
        # [7] 0 [1]
        L, R = 0, len(nums) - 1

        while L <= R:
            mid = L + ((R - L) // 2)
            if nums[mid] == target:
                return mid
            if nums[L] <= nums[mid]:
                if nums[L] <= target < nums[mid]:
                    R = mid - 1
                else:
                    L = mid + 1
            else:
                if nums[mid] < target <= nums[R]:
                    L = mid + 1
                else:
                    R = mid - 1
        return -1

    def findMin(self, nums: List[int]) -> int:
        # when you divide the array into half, either one of the side
        # will have a[0] > a[-1]. Then you are sure that the side has
        # the lowest value. If none of the side has such pattern, then
        # you can return minimum of first elements of left and right side arrays.
        # continue do so until you find the minimum
        L, r = 0, len(nums) - 1
        while L < r:
            mid = L + ((r - L) // 2)
            if nums[mid] < nums[L]:
                r = mid
            elif nums[mid + 1] > nums[r]:
                L = mid + 1
            else:
                return min(nums[L], nums[mid + 1])
        return nums[L]

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
