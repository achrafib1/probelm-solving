# https://leetcode.com/problems/minimum-index-sum-of-two-lists/


class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        list1_pos_dict = {}
        list2_pos_dict = {}
        ans = []
        min_sum_dict = {}
        min_sum = 100000000000000000000000000000000000000
        for i in range(len(list1)):
            if list1_pos_dict.get(list1[i], 0) == 0:
                list1_pos_dict[list1[i]] = i + 1

        for i in range(len(list2)):
            if list2_pos_dict.get(list2[i], 0) == 0:
                list2_pos_dict[list2[i]] = i + 1

        for k, v in list1_pos_dict.items():
            if list2_pos_dict.get(k, 0) != 0:
                if list2_pos_dict.get(k, 0) + v <= min_sum:
                    min_sum = list2_pos_dict.get(k, 0) + v
                    min_sum_dict[k] = min_sum

        for k, v in min_sum_dict.items():
            if v == min_sum:
                ans.append(k)

        return ans
