# https://leetcode.com/problems/subarray-product-less-than-k/


class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        curr_p = 1
        ans = 0

        left = 0
        right = 0

        for right in range(len(nums)):
            curr_p *= nums[right]

            while curr_p >= k and left <= right:
                curr_p //= nums[left]
                left += 1

            ans += right - left + 1

        return ans
