# https://leetcode.com/problems/keyboard-row/description/


class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        row1 = set("qwertyuiop")
        row2 = set("asdfghjkl")
        row3 = set("zxcvbnm")
        ans = []
        for i in range(len(words)):
            curr_word_set = set(words[i].lower())
            if curr_word_set <= row1 or curr_word_set <= row2 or curr_word_set <= row3:
                ans.append(words[i])

        return ans
