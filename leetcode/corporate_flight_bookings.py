# https://leetcode.com/problems/corporate-flight-bookings/description/


class Solution(object):
    def corpFlightBookings(self, bookings, n):
        """
        :type bookings: List[List[int]]
        :type n: int
        :rtype: List[int]
        """
        prefix_sum = [0] * (n + 1)
        flights_arr = [0] * (n + 1)
        ans = []
        for first, last, seats in bookings:
            flights_arr[first - 1] += seats
            flights_arr[last] -= seats

        curr_sum = 0
        for i in range(len(flights_arr)):
            curr_sum += flights_arr[i]
            prefix_sum[i] = curr_sum

        for i in range(n):
            ans.append(prefix_sum[i])

        return ans
