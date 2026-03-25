# https://leetcode.com/problems/sum-of-square-numbers/description/


class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        ans = False
        left = 0
        right = int(c**0.5)
        while left <= right:
            if left**2 + right**2 == c:
                ans = True
                break
            elif left**2 + right**2 > c:
                right -= 1
            else:
                left += 1

        return ans
