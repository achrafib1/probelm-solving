# https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        j = 1
        if len(nums) > 1:
            while i < len(nums) and j < len(nums):

                while j < len(nums) and nums[i] == nums[j]:
                    j += 1

                if i + 1 < len(nums) and j < len(nums):
                    nums[i + 1] = nums[j]

                i += 1
        else:
            i = 1

        return i
