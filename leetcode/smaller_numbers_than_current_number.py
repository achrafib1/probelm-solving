# https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/description/


class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        sorted_nums = sorted(nums)
        count_dict = {}
        count = 0
        duplicates_count = 0
        for i in range(len(sorted_nums) - 1):
            if sorted_nums[i] != sorted_nums[i + 1]:
                count_dict[sorted_nums[i]] = count
                count += duplicates_count + 1
                duplicates_count = 0
            else:
                duplicates_count += 1

        count_dict[sorted_nums[len(sorted_nums) - 1]] = count

        for i in range(len(nums)):
            ans.append(count_dict[nums[i]])

        return ans


#22min