# https://leetcode.com/problems/running-sum-of-1d-array/description/s


class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        curr_sum = 0
        ans = []
        for i in range(len(nums)):
            curr_sum += nums[i]
            ans.append(curr_sum)

        return ans
