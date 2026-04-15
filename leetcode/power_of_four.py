# https://leetcode.com/problems/power-of-four/description/


class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 1:
            return True
        if n < 1:
            return False

        return self.isPowerOfFour(float(n) / 4)
