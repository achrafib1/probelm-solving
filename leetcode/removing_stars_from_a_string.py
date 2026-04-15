# https://leetcode.com/problems/removing-stars-from-a-string/description/


class Solution(object):
    def removeStars(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        ans = ""
        for i in range(len(s)):
            if s[i] != "*":
                stack.append(s[i])
            else:
                if len(stack) != 0:
                    stack.pop()

        ans = "".join(stack)

        return ans
