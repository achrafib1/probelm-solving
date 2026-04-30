# https://leetcode.com/problems/find-the-winner-of-the-circular-game/


class Solution(object):
    def findTheWinner(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """

        if n == 1:
            return 1

        return (((self.findTheWinner(n - 1, k)) - 1 + k) % n) + 1
