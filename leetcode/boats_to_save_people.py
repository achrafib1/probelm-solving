# https://leetcode.com/problems/boats-to-save-people/description/


class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        sorted_people = sorted(people)
        left = 0
        right = len(people) - 1
        ans = 0
        while left <= right:
            if sorted_people[left] + sorted_people[right] <= limit:
                left += 1

            right -= 1
            ans += 1

        return ans
