# https://leetcode.com/problems/different-ways-to-add-parentheses/description/


class Solution(object):
    def diffWaysToCompute(self, expression):
        """
        :type expression: str
        :rtype: List[int]
        """

        ans = []

        if expression.isdigit():
            return [int(expression)]

        for i in range(len(expression)):
            if expression[i].isdigit() == False:

                left_side = self.diffWaysToCompute(expression[:i])
                right_side = self.diffWaysToCompute(expression[i + 1 :])

                for left in range(len(left_side)):
                    for right in range(len(right_side)):
                        if expression[i] == "+":
                            ans.append(left_side[left] + right_side[right])
                        elif expression[i] == "-":
                            ans.append(left_side[left] - right_side[right])
                        else:
                            ans.append(left_side[left] * right_side[right])

        return ans
