# https://leetcode.com/problems/minimum-recolors-to-get-k-consecutive-black-blocks/


class Solution(object):
    def minimumRecolors(self, blocks, k):
        """
        :type blocks: str
        :type k: int
        :rtype: int
        """

        freq_dict = {}
        curr_ans = 0
        ans = 0
        for i in range(k):
            freq_dict[blocks[i]] = freq_dict.get(blocks[i], 0) + 1

        curr_ans = k - freq_dict.get("B", 0)
        ans = curr_ans

        for i in range(k, len(blocks)):
            freq_dict[blocks[i]] = freq_dict.get(blocks[i], 0) + 1
            freq_dict[blocks[i - k]] -= 1

            curr_ans = k - freq_dict.get("B", 0)
            ans = min(ans, curr_ans)

        return ans
