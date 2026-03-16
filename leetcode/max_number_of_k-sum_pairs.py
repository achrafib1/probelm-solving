# https://leetcode.com/problems/max-number-of-k-sum-pairs/description


class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        sorted_nums = sorted(nums)
        left = 0
        right = len(nums) - 1
        ans = 0
        while left < right:
            if sorted_nums[left] + sorted_nums[right] == k:
                ans += 1
                right -= 1
                left += 1
            elif sorted_nums[left] + sorted_nums[right] > k:
                right -= 1
            else:
                left += 1

        return ans
