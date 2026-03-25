# https://leetcode.com/problems/fruit-into-baskets/description/


class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        curr_sum = 0
        freq_dict = {}
        left = 0
        right = 0
        ans = 0

        for right in range(len(fruits)):
            curr_sum += 1
            freq_dict[fruits[right]] = freq_dict.get(fruits[right], 0) + 1

            while len(freq_dict) > 2:
                curr_sum -= 1
                freq_dict[fruits[left]] -= 1

                if freq_dict[fruits[left]] == 0:
                    del freq_dict[fruits[left]]

                left += 1

            ans = max(ans, curr_sum)

        return ans
