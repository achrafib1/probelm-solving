# https://leetcode.com/problems/count-good-numbers/description/


class Solution(object):
    def countGoodNumbers(self, n):
        """
        :type n: int
        :rtype: int
        """
        # return (pow(4,(int(n)//2),(10**9 + 7))*pow(5,(int(n+1)//2),(10**9 + 7)))%(10**9 + 7)

        return (
            self.powerofn(4, (int(n) // 2), (10**9 + 7))
            * self.powerofn(5, (int(n + 1) // 2), (10**9 + 7))
        ) % (10**9 + 7)

    def powerofn(self, n, p, mod):

        if p < 0:
            n = 1 / n
            p = -p

        if p == 0:
            return 1

        half = self.powerofn(n, p // 2, mod)
        if p % 2 == 0:
            return (half * half) % mod
        else:
            return (n * half * half) % mod
