# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        left = 0
        right = 0

        freq_dict = {}
        ans = 0
        while right < len(s):

            if freq_dict.get(s[right], 0) == 0:
                freq_dict[s[right]] = 1
                right += 1
                ans = max(ans, right - left)
            else:
                while s[left] != s[right]:
                    freq_dict[s[left]] = 0
                    left += 1

                left += 1
                right += 1

        return ans
