# https://leetcode.com/problems/sum-in-a-matrix/description/


class Solution(object):
    def matrixSum(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: int
        """
        max_dict = {}
        ans = 0
        for i in range(len(nums)):
            row = list(reversed(sorted(nums[i])))
            for j in range(len(row)):
                max_dict[j] = max(max_dict.get(j, 0), row[j])

        for k, v in max_dict.items():
            ans += v

        return ans
