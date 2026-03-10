# https://leetcode.com/problems/move-zeroes/description/


class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        holder = 0

        while holder < len(nums) and nums[holder] != 0:
            holder += 1

        seeker = holder + 1

        while holder < len(nums) and seeker < len(nums):
            if nums[holder] == 0 and nums[seeker] != 0:
                nums[holder], nums[seeker] = nums[seeker], nums[holder]
                holder += 1
                seeker += 1
            else:
                if nums[holder] != 0:
                    holder += 1
                if nums[seeker] == 0:
                    seeker += 1

        return nums
