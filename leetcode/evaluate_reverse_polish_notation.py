# https://leetcode.com/problems/evaluate-reverse-polish-notation/


class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        ans = 0

        for i in range(len(tokens)):
            if tokens[i] == "+":
                opr1 = stack.pop()
                opr2 = stack.pop()
                stack.append(int(opr1) + int(opr2))

            elif tokens[i] == "-":
                opr1 = stack.pop()
                opr2 = stack.pop()
                stack.append(int(opr2) - int(opr1))

            elif tokens[i] == "*":
                opr1 = stack.pop()
                opr2 = stack.pop()
                stack.append(int(opr1) * int(opr2))

            elif tokens[i] == "/":
                opr1 = stack.pop()
                opr2 = stack.pop()
                stack.append(int(float(opr2) / int(opr1)))

            else:
                stack.append(tokens[i])

        ans = int(stack.pop())

        return ans
