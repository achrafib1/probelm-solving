# https://leetcode.com/problems/check-if-one-string-swap-can-make-strings-equal/


class Solution(object):
    def areAlmostEqual(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        strings_diff_count = 0
        first_c = ""
        second_c = ""
        ans = True
        if len(s1) == len(s2):
            for i in range(len(s1)):
                if s1[i] != s2[i]:
                    if strings_diff_count == 0:
                        first_c = s1[i]
                        second_c = s2[i]
                    else:
                        if first_c != s2[i] or second_c != s1[i]:
                            ans = False
                            break
                    strings_diff_count += 1
        else:
            ans = False

        if strings_diff_count > 2 or strings_diff_count == 1:
            ans = False

        return ans
