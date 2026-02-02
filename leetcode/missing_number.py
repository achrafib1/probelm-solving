# https://leetcode.com/problems/missing-number


class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        complete_nums_set = set([i for i in range(len(nums) + 1)])
        return list(complete_nums_set - set(nums))[0]


# 6min
