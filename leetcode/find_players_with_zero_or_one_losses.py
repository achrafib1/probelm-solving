# https://leetcode.com/problems/find-players-with-zero-or-one-losses


class Solution(object):
    def findWinners(self, matches):
        """
        :type matches: List[List[int]]
        :rtype: List[List[int]]
        """
        winners_list = []
        winners_with_one_l_list = []
        def_count_dict = {}
        ans = []
        for i in range(len(matches)):
            winners_list.append(matches[i][0])
            def_count_dict[matches[i][1]] = def_count_dict.get(matches[i][1], 0) + 1
        ans.append(sorted(list(set(winners_list) - set(def_count_dict.keys()))))
        for k, v in def_count_dict.items():
            if v == 1:
                winners_with_one_l_list.append(k)
        ans.append(sorted(winners_with_one_l_list))

        return ans
