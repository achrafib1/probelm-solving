# https://leetcode.com/problems/find-all-duplicates-in-an-array/


class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sorted_nums = sorted(nums)
        ans = []
        for i in range(len(nums) - 1):
            if sorted_nums[i] == sorted_nums[i + 1]:
                ans.append(sorted_nums[i])

        return ans
