# https://leetcode.com/problems/reduction-operations-to-make-the-array-elements-equal/description/


class Solution(object):
    def reductionOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        freq_dict = {}
        ans = 0
        cum_sum = 0
        for i in range(len(nums)):
            freq_dict[nums[i]] = freq_dict.get(nums[i], 0) + 1

        sorted_unique_nums = sorted(set(nums), reverse=True)

        for i in range(len(sorted_unique_nums) - 1):
            ans += freq_dict[sorted_unique_nums[i]] + cum_sum
            cum_sum += freq_dict[sorted_unique_nums[i]]

        return ans
