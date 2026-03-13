# https://leetcode.com/problems/divide-players-into-teams-of-equal-skill/description/


class Solution(object):
    def dividePlayers(self, skill):
        """
        :type skill: List[int]
        :rtype: int
        """
        target_skill = 0
        right = len(skill) - 1
        left = 0
        ans = 0
        sorted_skill = sorted(skill)
        target_skill = sorted_skill[0] + sorted_skill[len(skill) - 1]
        while left < right:
            if sorted_skill[left] + sorted_skill[right] != target_skill:
                ans = -1
                break
            ans += sorted_skill[left] * sorted_skill[right]
            left += 1
            right -= 1

        return ans
