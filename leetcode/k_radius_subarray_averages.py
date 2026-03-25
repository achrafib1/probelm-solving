# https://leetcode.com/problems/k-radius-subarray-averages/description/


class Solution(object):
    def getAverages(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        curr_sum = sum(nums[:k])
        ans = [-1] * len(nums)
        if 2 * k + 1 <= len(nums):
            for i in range(k, k + k + 1):
                curr_sum += nums[i]

            ans[k] = curr_sum // (2 * k + 1)

            for i in range(k + 1, len(nums) - k):
                curr_sum += nums[i + k]
                curr_sum -= nums[i - k - 1]

                ans[i] = curr_sum // (2 * k + 1)

        return ans
