# https://leetcode.com/problems/unique-morse-code-words/description/


class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        characters_list = [
            "a",
            "b",
            "c",
            "d",
            "e",
            "f",
            "g",
            "h",
            "i",
            "j",
            "k",
            "l",
            "m",
            "n",
            "o",
            "p",
            "q",
            "r",
            "s",
            "t",
            "u",
            "v",
            "w",
            "x",
            "y",
            "z",
        ]
        code_list = [
            ".-",
            "-...",
            "-.-.",
            "-..",
            ".",
            "..-.",
            "--.",
            "....",
            "..",
            ".---",
            "-.-",
            ".-..",
            "--",
            "-.",
            "---",
            ".--.",
            "--.-",
            ".-.",
            "...",
            "-",
            "..-",
            "...-",
            ".--",
            "-..-",
            "-.--",
            "--..",
        ]
        characters_code_dict = dict(zip(characters_list, code_list))
        transformation_set = set()
        for i in range(len(words)):
            current_word_transformation = ""
            for j in range(len(words[i])):
                current_word_transformation += characters_code_dict[words[i][j]]
            transformation_set.add(current_word_transformation)

        return len(transformation_set)
