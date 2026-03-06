# https://leetcode.com/problems/widest-vertical-area-between-two-points-containing-no-points/description/


class Solution(object):
    def maxWidthOfVerticalArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        ans = 0
        points.sort()
        for i in range(len(points) - 1):
            ans = max(ans, abs(points[i][0] - points[i + 1][0]))

        return ans
