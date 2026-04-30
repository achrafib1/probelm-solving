# https://leetcode.com/problems/arranging-coins/description/


class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 0
        right = n
        ans = -1

        while left <= right:
            mid = int((left + right)) // 2

            if (mid * (mid + 1)) // 2 == n:
                ans = mid
                break
            elif (mid * (mid + 1)) // 2 < n:
                ans = mid
                left = mid + 1
            else:
                right = mid - 1

        return ans
