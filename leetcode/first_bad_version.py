# https://leetcode.com/problems/first-bad-version/description/


# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):


class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 1
        right = n
        ans = -1

        while left <= right:
            mid = int((left + right)) // 2

            if isBadVersion(mid):  # type: ignore
                ans = mid
                right = mid - 1
            else:
                left = mid + 1

        return ans
