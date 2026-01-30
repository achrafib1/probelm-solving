# https://leetcode.com/problems/check-if-all-the-integers-in-a-range-are-covered/


class Solution(object):
    def isCovered(self, ranges, left, right):
        """
        :type ranges: List[List[int]]
        :type left: int
        :type right: int
        :rtype: bool
        """
        ans = True
        for i in range(left, right + 1):
            current_ans = 0
            for j in range(len(ranges)):
                if i in range(ranges[j][0], ranges[j][1] + 1):
                    current_ans = 1
                    break
            if current_ans == 0:
                ans = False
                break
        return ans
