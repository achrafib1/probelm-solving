# https://leetcode.com/problems/string-compression/description/


class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """

        ans = []
        comp_s = ""
        freq_dict = {}
        curr_count = 1
        for i in range(len(chars) - 1):
            if chars[i] == chars[i + 1]:
                curr_count += 1
            else:
                comp_s += chars[i] + str(curr_count) if curr_count > 1 else chars[i]
                curr_count = 1

        comp_s += (
            chars[len(chars) - 1] + str(curr_count)
            if curr_count > 1
            else chars[len(chars) - 1]
        )

        for i in range(len(comp_s)):
            chars[i] = list(comp_s)[i]

        return len(chars[: len(comp_s)])
