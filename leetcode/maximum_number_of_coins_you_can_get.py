# https://leetcode.com/problems/maximum-number-of-coins-you-can-get/description/


class Solution(object):
    def maxCoins(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """

        sorted_piles = sorted(piles)
        number_of_turns = len(piles) // 3
        ans = 0
        print(sorted_piles)
        i = number_of_turns
        while i < len(sorted_piles):
            ans += sorted_piles[i]
            i += 2

        return ans
