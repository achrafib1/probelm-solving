# https://leetcode.com/problems/find-pivot-index/description/


class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = -1
        total_sum = sum(nums)
        left_sum = 0

        for i in range(len(nums)):

            right_sum = total_sum - left_sum - nums[i]

            if left_sum == right_sum:
                ans = i
                break

            left_sum += nums[i]

        return ans
