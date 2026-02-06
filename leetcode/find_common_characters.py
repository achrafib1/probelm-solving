# https://leetcode.com/problems/find-common-characters/description/


class Solution(object):
    def commonChars(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        ans = []
        characters = {}
        for i in range(len(words[0])):
            characters[words[0][i]] = characters.get(words[0][i], 0) + 1

        for i in range(1, len(words)):
            curr_characters = {}
            new_characters = {}
            for j in range(len(words[0])):
                curr_characters[words[i][j]] = curr_characters.get(words[i][j], 0) + 1

            for k, v in curr_characters.items():
                if characters.get(k, "") != "":
                    new_characters[k] = min(characters[k], curr_characters[k])

            characters = new_characters

        for k, v in characters.items():
            for i in range(v):
                ans.append(k)

        return ans
