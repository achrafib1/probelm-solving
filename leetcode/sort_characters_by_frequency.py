# https://leetcode.com/problems/sort-characters-by-frequency/description/


class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        freq_dict = {}
        ans = ""

        for i in range(len(s)):
            freq_dict[s[i]] = freq_dict.get(s[i], 0) + 1

        sorted_s_list = sorted(
            freq_dict.items(), key=lambda item: item[1], reverse=True
        )

        for i in range(len(sorted_s_list)):
            for j in range(sorted_s_list[i][1]):
                ans += sorted_s_list[i][0]

        return ans
