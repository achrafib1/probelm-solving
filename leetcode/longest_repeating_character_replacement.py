# https://leetcode.com/problems/longest-repeating-character-replacement/description/


class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        left = 0
        right = 0
        ans = 0
        freq_dict = {}
        max_freq_c = ("", 0)

        for right in range(len(s)):
            freq_dict[s[right]] = freq_dict.get(s[right], 0) + 1
            if freq_dict[s[right]] > max_freq_c[1]:
                max_freq_c = (s[right], freq_dict[s[right]])

            while (right - left + 1) - max_freq_c[1] > k:
                freq_dict[s[left]] -= 1
                left += 1

            ans = max(ans, right - left + 1)

        return ans
