# https://leetcode.com/problems/first-unique-character-in-a-string/


class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        element_indices_dict = {}
        ans = -1
        for i in range(len(s)):
            element_indices_dict[s[i]] = i

        for i in range(len(s)):
            if element_indices_dict[s[i]] != -1:
                if element_indices_dict[s[i]] == i:
                    ans = i
                    break
                else:
                    element_indices_dict[s[i]] = -1

        return ans
