# https://leetcode.com/problems/longest-turbulent-subarray/


class Solution(object):
    def maxTurbulenceSize(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        left = 0
        right = 0
        curr_dir = 0
        prev_dir = 0
        ans = 1

        for right in range(1, len(arr)):
            if arr[right] > arr[right - 1]:
                curr_dir = 1
            elif arr[right] < arr[right - 1]:
                curr_dir = -1
            else:
                curr_dir = 0

            if curr_dir == 0:
                left = right

            else:
                if curr_dir == prev_dir:
                    left = right - 1

            ans = max(ans, right - left + 1)
            prev_dir = curr_dir

        return ans
