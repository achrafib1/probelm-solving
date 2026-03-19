# https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/


class Solution(object):
    def maxScore(self, cardPoints, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """
        curr_sum = 0
        min_sum = 0
        ans = 0
        curr_sum = sum(cardPoints[: len(cardPoints) - k])

        min_sum = curr_sum

        for i in range(len(cardPoints) - k, len(cardPoints)):
            curr_sum += cardPoints[i]
            curr_sum -= cardPoints[i - len(cardPoints) + k]

            min_sum = min(min_sum, curr_sum)

        ans = sum(cardPoints) - min_sum

        return ans
