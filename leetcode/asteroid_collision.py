# https://leetcode.com/problems/asteroid-collision/description/


class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        stack = []
        curr_ast = 0
        ans = []

        for i in range(len(asteroids)):

            curr_ast = 0
            while stack and asteroids[i] < 0:
                if stack[-1] > 0:
                    if abs(asteroids[i]) > abs(stack[-1]):
                        stack.pop()
                    else:
                        if abs(asteroids[i]) == abs(stack[-1]):
                            stack.pop()
                        curr_ast = 1
                        break
                else:
                    break

            if curr_ast != 1:
                stack.append(asteroids[i])

        ans = stack

        return ans
