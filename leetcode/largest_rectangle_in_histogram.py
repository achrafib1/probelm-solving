# https://leetcode.com/problems/largest-rectangle-in-histogram/description/


class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """

        stack = []
        w = 1
        ans = 0
        heights.append(0)
        for i in range(len(heights)):

            while stack and heights[stack[-1]] > heights[i]:

                h = stack.pop()
                h = heights[h]
                if len(stack) > 0:
                    w = i - stack[-1] - 1
                else:
                    w = i

                area = w * h
                ans = max(ans, area)

            stack.append(i)

        return ans
