# https://leetcode.com/problems/next-greater-element-ii/description/


class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        stack = []
        nums = nums + nums
        ans = [-1] * len(nums)
        for i in range(len(nums)):

            while stack and nums[i] > nums[stack[-1]]:
                ans[stack[-1]] = nums[i]
                stack.pop()

            stack.append(i)

        ans = ans[: int(len(nums) // 2)]

        return ans
