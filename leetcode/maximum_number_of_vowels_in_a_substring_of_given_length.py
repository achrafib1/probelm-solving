# https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/


class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """

        vowels_set = {"a", "e", "i", "o", "u"}
        curr_max = 0
        ans = 0

        for i in range(k):
            if s[i] in vowels_set:
                curr_max += 1

        ans = curr_max

        for i in range(k, len(s)):

            if s[i] in vowels_set:
                curr_max += 1

            if s[i - k] in vowels_set:
                curr_max -= 1

            ans = max(ans, curr_max)

        return ans
