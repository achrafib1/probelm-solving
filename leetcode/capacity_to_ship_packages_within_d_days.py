# https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/


class Solution(object):
    def shipWithinDays(self, weights, days):
        """
        :type weights: List[int]
        :type days: int
        :rtype: int
        """

        def checkcapacity(n, weights, days):
            curr_sum = 0
            i = 0
            n_days = 0
            while i < len(weights):
                curr_sum = 0
                while i < len(weights) and curr_sum + weights[i] <= n:
                    curr_sum += weights[i]
                    i += 1
                n_days += 1

                if n_days > days:
                    return False
                    break

            return True

        total_sum = sum(weights)
        left = max(weights)
        right = total_sum
        ans = total_sum

        while left <= right:
            mid = int((left + right)) // 2

            if checkcapacity(mid, weights, days):
                ans = min(ans, mid)
                right = mid - 1
            else:
                left = mid + 1

        return ans
