# https://leetcode.com/problems/maximum-average-subarray-i/description/


class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        ans = -10000000000000000000000

        curr_sum = 0

        for i in range(k):
            curr_sum += nums[i]

        ans = max(ans, float(curr_sum) / k)

        for i in range(k, len(nums)):
            curr_sum += nums[i]
            curr_sum -= nums[i - k]

            ans = max(ans, float(curr_sum) / k)

        return ans
