# https://leetcode.com/problems/relative-sort-array/description/


class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        ans = []
        unique_elments_list = []
        freq_dict = {}
        for i in range(len(arr1)):
            freq_dict[arr1[i]] = freq_dict.get(arr1[i], 0) + 1

        for i in range(len(arr2)):
            for j in range(freq_dict[arr2[i]]):
                ans.append(arr2[i])

        for element in set(arr1) - set(arr2):
            for i in range(freq_dict[element]):
                unique_elments_list.append(element)

        ans = ans + sorted(unique_elments_list)

        return ans
