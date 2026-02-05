# https://leetcode.com/problems/majority-element/


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        freq_dict = {}
        for i in range(len(nums)):
            freq_dict[nums[i]] = freq_dict.get(nums[i], 0) + 1

        sorted_nums_by_freq = sorted(freq_dict.items(), key=lambda item: item[1])

        return sorted_nums_by_freq[len(sorted_nums_by_freq) - 1][0]
