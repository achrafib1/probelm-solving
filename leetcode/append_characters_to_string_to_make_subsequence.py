# https://leetcode.com/problems/append-characters-to-string-to-make-subsequence/


class Solution(object):
    def appendCharacters(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        ans = 0
        i = 0
        j = 0
        while i < len(t):
            while j < len(s):
                if i < len(t) and t[i] == s[j]:
                    i += 1
                j += 1

            break

        ans = len(t) - i

        return ans
