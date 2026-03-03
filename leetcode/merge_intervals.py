# https://leetcode.com/problems/merge-intervals/


class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        res = []

        intervals.sort()
        curr_pair = intervals[0]

        for pair in intervals:

            if curr_pair[1] >= pair[0]:
                curr_pair[1] = max(curr_pair[1], pair[1])
            else:
                res.append(curr_pair)
                curr_pair = pair

        res.append(curr_pair)

        return res
