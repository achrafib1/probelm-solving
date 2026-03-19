# https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k/description/


class Solution(object):
    def maximumSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        curr_sum = 0
        freq_dict = {}
        left = 0
        right = 0
        ans = 0

        for right in range(len(nums)):
            curr_sum += nums[right]
            freq_dict[nums[right]] = freq_dict.get(nums[right], 0) + 1

            if right - left + 1 > k:
                curr_sum -= nums[left]
                freq_dict[nums[left]] -= 1

                if freq_dict[nums[left]] == 0:
                    del freq_dict[nums[left]]

                left += 1

            if right - left + 1 == k:
                if len(freq_dict) == k:
                    ans = max(ans, curr_sum)

        return ans
