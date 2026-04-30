# https://leetcode.com/problems/simplify-path/description/


class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack = []
        path_list = path.split("/")

        for i in range(len(path_list)):
            if path_list[i] == "..":
                if stack:
                    stack.pop()
            else:
                if path_list[i] != "." and path_list[i] != "":
                    stack.append(path_list[i])

        ans = "/" + "/".join(stack)

        return ans
