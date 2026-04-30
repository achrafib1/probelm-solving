# https://leetcode.com/problems/clear-digits/description/


class Solution(object):
    def clearDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        ans = ""
        stack = []

        for i in range(len(s)):

            if stack and s[i].isdigit() == True:
                stack.pop()

            if s[i].isdigit() == False:
                stack.append(s[i])

        ans = "".join(stack)

        return ans
