# https://leetcode.com/problems/find-right-interval/description/


class Solution(object):
    def findRightInterval(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[int]
        """

        starts = []

        for i in range(len(intervals)):
            starts.append((intervals[i][0], i))

        starts.sort()

        ans = []

        for i in range(len(intervals)):
            left = 0
            right = len(starts) - 1

            curr_ans = -1

            while left <= right:
                mid = int((left + right)) // 2

                if starts[mid][0] >= intervals[i][1]:
                    curr_ans = starts[mid][1]
                    right = mid - 1
                else:
                    left = mid + 1

            ans.append(curr_ans)

        return ans
