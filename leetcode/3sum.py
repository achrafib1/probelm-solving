# https://leetcode.com/problems/3sum/description/


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        left = 0
        right = len(nums) - 1
        mid_index = left + 1
        ans = []
        nums.sort()

        for i in range(len(nums) - 2):
            if i == 0 or nums[i] != nums[i - 1]:
                left = i + 1
                right = len(nums) - 1
                while left < right:
                    if nums[i] + nums[left] + nums[right] == 0:
                        ans.append([nums[i], nums[left], nums[right]])

                        while left < right and nums[left] == nums[left + 1]:
                            left += 1

                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1

                        left += 1
                        right -= 1

                    elif nums[i] + nums[left] + nums[right] > 0:
                        right -= 1

                    else:
                        left += 1

        return ans
