# https://leetcode.com/problems/maximum-erasure-value/


class Solution(object):
    def maximumUniqueSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = 0
        unique_elments = {}
        ans = 0

        for right in range(len(nums)):
            unique_elments[nums[right]] = unique_elments.get(nums[right], 0) + 1

            while unique_elments[nums[right]] > 1:
                unique_elments[nums[left]] -= 1
                left += 1

            ans = max(ans, sum(nums[left : right + 1]))

        return ans
