# https://leetcode.com/problems/binary-search/description/


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        left = 0
        right = len(nums) - 1
        ans = -1

        while left <= right:
            mid = int((left + right)) // 2

            if target == nums[mid]:
                ans = mid
                break
            elif target > nums[mid]:
                left = mid + 1
            else:
                right = mid - 1

        return ans
