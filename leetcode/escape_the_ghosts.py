# https://leetcode.com/problems/escape-the-ghosts/


class Solution(object):
    def escapeGhosts(self, ghosts, target):
        """
        :type ghosts: List[List[int]]
        :type target: List[int]
        :rtype: bool
        """
        ghosts_target_distances_list = [
            abs(target[0] - ghosts[i][0]) + abs(target[1] - ghosts[i][1])
            for i in range(len(ghosts))
        ]
        target_distance = abs(target[0] - 0) + abs(target[1] - 0)
        ans = True
        for i in range(len(ghosts_target_distances_list)):
            if target_distance >= ghosts_target_distances_list[i]:
                ans = False
                break

        return ans
