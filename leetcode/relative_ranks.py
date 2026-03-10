# https://leetcode.com/problems/relative-ranks/


class Solution(object):
    def findRelativeRanks(self, score):
        """
        :type score: List[int]
        :rtype: List[str]
        """
        ans = ["" for i in range(len(score))]
        score_idx_dict = {}
        for i in range(len(score)):
            score_idx_dict[score[i]] = i

        score.sort()
        for i in range(len(score)):
            if i == len(score) - 1:
                ans[score_idx_dict[score[i]]] = "Gold Medal"
            if i == len(score) - 2:
                ans[score_idx_dict[score[i]]] = "Silver Medal"
            if i == len(score) - 3:
                ans[score_idx_dict[score[i]]] = "Bronze Medal"
            if i < len(score) - 3:
                ans[score_idx_dict[score[i]]] = str(len(score) - i)

        return ans
