# https://leetcode.com/problems/minimum-number-of-moves-to-seat-everyone/description/s


class Solution(object):
    def minMovesToSeat(self, seats, students):
        """
        :type seats: List[int]
        :type students: List[int]
        :rtype: int
        """
        ans = 0
        sorted_seats = sorted(seats)
        sorted_students = sorted(students)
        for i in range(len(seats)):
            ans += abs(sorted_seats[i] - sorted_students[i])

        return ans
