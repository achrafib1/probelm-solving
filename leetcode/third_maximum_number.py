# https://leetcode.com/problems/third-maximum-number/description/


class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        sorted_dis_nums = sorted(list(set(nums)))

        return (
            sorted_dis_nums[len(sorted_dis_nums) - 3]
            if len(sorted_dis_nums) - 3 >= 0
            else sorted_dis_nums[len(sorted_dis_nums) - 1]
        )
