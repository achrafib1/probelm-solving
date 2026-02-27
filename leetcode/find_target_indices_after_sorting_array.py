# https://leetcode.com/problems/find-target-indices-after-sorting-array/description/


class Solution(object):
    def targetIndices(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        ans = []
        sorted_nums = sorted(nums)
        for i in range(len(sorted_nums)):
            if sorted_nums[i] == target:
                ans.append(i)

        return ans
