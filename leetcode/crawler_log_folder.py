# https://leetcode.com/problems/crawler-log-folder/description/


class Solution(object):
    def minOperations(self, logs):
        """
        :type logs: List[str]
        :rtype: int
        """
        stack = []
        ans = 0
        for i in range(len(logs)):
            if logs[i] == "../":
                if len(stack):
                    stack.pop()
            else:
                if logs[i] != "./":
                    stack.append(logs[i])

        ans = len(stack)

        return ans
