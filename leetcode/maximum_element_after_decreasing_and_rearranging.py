# https://leetcode.com/problems/maximum-element-after-decreasing-and-rearranging/description/


class Solution(object):
    def maximumElementAfterDecrementingAndRearranging(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        ans = 0
        arr.sort()
        arr[0] = 1
        for i in range(len(arr) - 1):
            if abs(arr[i + 1] - arr[i]) > 1:
                arr[i + 1] = arr[i] + 1

        ans = arr[len(arr) - 1]

        return ans
