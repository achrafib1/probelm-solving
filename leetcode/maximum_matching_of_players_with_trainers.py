# https://leetcode.com/problems/maximum-matching-of-players-with-trainers/description/


class Solution(object):
    def matchPlayersAndTrainers(self, players, trainers):
        """
        :type players: List[int]
        :type trainers: List[int]
        :rtype: int
        """
        ans = 0
        j = 0
        players.sort()
        trainers.sort()
        for i in range(len(players)):

            while j < len(trainers) and players[i] > trainers[j]:
                j += 1

            if j < len(trainers):
                ans += 1
                j += 1
            else:
                break

        return ans
