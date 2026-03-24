# https://leetcode.com/problems/find-the-longest-semi-repetitive-substring/description/


class Solution(object):
    def longestSemiRepetitiveSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        left = 0
        right = 0
        rep_index = -1
        rep_count = 1
        ans = 1

        for right in range(1, len(s)):
            if s[right] == s[right - 1]:
                if rep_count == 1:
                    rep_index = right
                rep_count -= 1

            if rep_count < 0:
                left = rep_index
                rep_count = 0
                rep_index = right

            ans = max(ans, right - left + 1)

        return ans
