# https://leetcode.com/problems/count-number-of-nice-subarrays/description/


class Solution(object):
    def numberOfSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        ans = 0
        curr_sum = 0
        left = 0
        l_even_count = 0

        for right in range(len(nums)):
            if nums[right] % 2 != 0:
                curr_sum += 1
                l_even_count = 0

            while curr_sum > k:
                if nums[left] % 2 != 0:
                    curr_sum -= 1
                left += 1

            if curr_sum == k:
                while left < right and nums[left] % 2 == 0:
                    l_even_count += 1
                    left += 1
                ans += 1 + l_even_count

        return ans
