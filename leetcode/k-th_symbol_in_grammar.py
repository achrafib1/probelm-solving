# https://leetcode.com/problems/k-th-symbol-in-grammar/description/


class Solution(object):
    def kthGrammar(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        ans = 0
        if n == 0:
            return 0

        if k % 2 != 0:
            ans = self.kthGrammar(n - 1, int((k + 1)) // 2)
        else:
            ans = 1 - self.kthGrammar(n - 1, int(k) // 2)

        return ans
