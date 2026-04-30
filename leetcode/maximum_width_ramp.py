# https://leetcode.com/problems/maximum-width-ramp/description/


class Solution(object):
    def maxWidthRamp(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        stack = []
        ans = 0

        for i in range(len(nums)):
            if len(stack) == 0 or nums[i] < nums[stack[-1]]:
                stack.append(i)

        for i in range(len(nums) - 1, -1, -1):
            while stack and nums[i] >= nums[stack[-1]]:
                ans = max(ans, i - stack[-1])

                stack.pop()

        return ans
