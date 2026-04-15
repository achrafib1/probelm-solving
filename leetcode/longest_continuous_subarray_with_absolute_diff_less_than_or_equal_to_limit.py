# https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/description/


from collections import deque


class Solution(object):
    def longestSubarray(self, nums, limit):
        """
        :type nums: List[int]
        :type limit: int
        :rtype: int
        """
        left = 0
        right = 0
        max_queue = deque()
        min_queue = deque()
        ans = 0

        for right in range(len(nums)):

            while max_queue and max_queue[-1] < nums[right]:
                max_queue.pop()

            max_queue.append(nums[right])

            while min_queue and min_queue[-1] > nums[right]:
                min_queue.pop()

            min_queue.append(nums[right])

            while max_queue[0] - min_queue[0] > limit:
                if max_queue[0] == nums[left]:
                    max_queue.popleft()

                if min_queue[0] == nums[left]:
                    min_queue.popleft()

                left += 1

            ans = max(ans, right - left + 1)

        return ans
