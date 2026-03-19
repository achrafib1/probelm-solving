# https://leetcode.com/problems/permutation-in-string/


class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        ans = False
        freq_dict_s1 = {}
        freq_dict_s2 = {}

        if len(s1) <= len(s2):
            for i in range(len(s1)):
                freq_dict_s1[s1[i]] = freq_dict_s1.get(s1[i], 0) + 1

            for i in range(len(s1)):
                freq_dict_s2[s2[i]] = freq_dict_s2.get(s2[i], 0) + 1

            if freq_dict_s1 == freq_dict_s2:
                ans = True
            else:

                for i in range(len(s1), len(s2)):
                    freq_dict_s2[s2[i]] = freq_dict_s2.get(s2[i], 0) + 1

                    if freq_dict_s2.get(s2[i - len(s1)], 0) == 1:
                        del freq_dict_s2[s2[i - len(s1)]]
                    else:
                        freq_dict_s2[s2[i - len(s1)]] -= 1

                    if freq_dict_s1 == freq_dict_s2:
                        ans = True
                        break

        return ans
