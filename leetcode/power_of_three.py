# https://leetcode.com/problems/power-of-three/description/


class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 1:
            return True
        if n < 1:
            return False

        return self.isPowerOfThree(float(n) / 3)
