# https://leetcode.com/problems/koko-eating-bananas/description/


class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """

        def check_k(k, piles, h):

            n_h = 0
            for i in range(len(piles)):
                if piles[i] > k:
                    if piles[i] % k > 0:
                        n_h += 1
                    n_h += piles[i] // k
                else:
                    n_h += 1

                if n_h > h:
                    return False

            return True

        left = 1
        right = max(piles)
        ans = right

        while left <= right:
            mid = int((left + right)) // 2

            if check_k(mid, piles, h):
                ans = min(ans, mid)
                right = mid - 1
            else:
                left = mid + 1

        return ans
