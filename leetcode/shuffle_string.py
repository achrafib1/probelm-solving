# https://leetcode.com/problems/shuffle-string/description/


class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        s_indices_list = sorted(
            [(s[i], indices[i]) for i in range(len(s))], key=lambda x: x[1]
        )
        ans = "".join([s_indices_list[i][0] for i in range(len(s))])
        return ans
