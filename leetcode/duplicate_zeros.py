# https://leetcode.com/problems/duplicate-zeros/


class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        left = 0
        right = len(arr) - 1
        count_0 = 0
        while left <= right - count_0:
            if arr[left] == 0:
                if left == right - count_0:
                    arr[right] = 0
                    right -= 1
                    break
                count_0 += 1
            left += 1

        i = left - 1
        while i >= 0:
            if arr[i] == 0:
                arr[right] = 0
                right -= 1
                arr[right] = 0
            else:
                arr[right] = arr[i]

            i -= 1
            right -= 1

        return 0
