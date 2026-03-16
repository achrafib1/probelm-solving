# https://leetcode.com/problems/count-vowel-substrings-of-a-string/description/


class Solution(object):
    def countVowelSubstrings(self, word):
        """
        :type word: str
        :rtype: int
        """
        left = 0
        in_left = 0
        freq_dict = {}
        v_set = {"a", "e", "i", "o", "u"}
        ans = 0

        for right in range(len(word)):
            if word[right] not in v_set:
                freq_dict = {}
                in_left = right + 1
                left = right + 1
            else:
                freq_dict[word[right]] = freq_dict.get(word[right], 0) + 1

                while len(freq_dict) == 5:
                    freq_dict[word[in_left]] -= 1
                    if freq_dict[word[in_left]] == 0:
                        freq_dict[word[in_left]] = 1
                        break
                    in_left += 1

                if len(freq_dict) == 5:
                    ans += in_left - left + 1

        return ans
