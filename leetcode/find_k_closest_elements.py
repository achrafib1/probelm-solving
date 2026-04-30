# https://leetcode.com/problems/find-k-closest-elements/description/


class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """

        target_idx = -1
        left = 0
        right = len(arr) - 1
        ans = []

        while left <= right:
            mid = int((left + right)) // 2
            target_idx = mid
            if x == arr[mid]:
                break
            elif x > arr[mid]:
                left = mid + 1
            else:
                right = mid - 1

        if x > arr[target_idx]:
            left = target_idx
            right = target_idx + 1
        else:
            left = target_idx - 1
            right = target_idx

        while right - left - 1 < k:
            if left < 0:
                right += 1
            elif right >= len(arr):
                left -= 1

            else:
                if abs(arr[left] - x) <= abs(arr[right] - x):
                    left -= 1
                else:
                    right += 1

        ans = arr[left + 1 : right]

        return ans
