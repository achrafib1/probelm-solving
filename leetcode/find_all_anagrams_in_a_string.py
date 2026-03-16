# https://leetcode.com/problems/find-all-anagrams-in-a-string/description/


class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        p_dict = {}
        w_dict = {}
        ans = []

        if len(p) <= len(s):
            for c in p:
                p_dict[c] = p_dict.get(c, 0) + 1

            for i in range(len(p)):
                w_dict[s[i]] = w_dict.get(s[i], 0) + 1

            if p_dict == w_dict:
                ans.append(0)

            for i in range(len(p), len(s)):
                w_dict[s[i]] = w_dict.get(s[i], 0) + 1
                w_dict[s[i - len(p)]] -= 1
                if w_dict[s[i - len(p)]] == 0:
                    del w_dict[s[i - len(p)]]

                if p_dict == w_dict:
                    ans.append(i - len(p) + 1)

        return ans
