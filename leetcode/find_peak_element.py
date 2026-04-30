# https://leetcode.com/problems/find-peak-element/


class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        ans = -1

        while left <= right:
            mid = int((left + right)) // 2

            if mid + 1 < len(nums) and nums[mid] < nums[mid + 1]:
                left = mid + 1
            else:
                ans = mid
                right = mid - 1

        return ans
