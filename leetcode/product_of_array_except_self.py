# https://leetcode.com/problems/product-of-array-except-self/


class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        p_mult = [1] * (len(nums) + 1)
        s_mult = [1] * (len(nums) + 1)

        for i in range(len(nums)):
            p_mult[i + 1] = p_mult[i] * nums[i]

        for i in range(len(nums)):
            s_mult[i + 1] = s_mult[i] * nums[len(nums) - 1 - i]

        for i in range(1, len(p_mult)):
            ans.append(s_mult[len(nums) - i] * p_mult[i - 1])

        return ans
