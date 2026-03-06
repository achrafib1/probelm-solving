# https://leetcode.com/problems/smallest-value-of-the-rearranged-number/description/


class Solution(object):
    def smallestNumber(self, num):
        """
        :type num: int
        :rtype: int
        """

        ans = 0
        rearranged_num = []
        count_0 = 0
        first_num_id = 0
        if num > 0:
            sorted_num = sorted(list(str(num)))
            for i in range(len(sorted_num)):
                if sorted_num[i] == "0":
                    count_0 += 1
                else:
                    if first_num_id == 0:
                        rearranged_num.append(sorted_num[i])
                        rearranged_num = rearranged_num + ["0"] * count_0
                        first_num_id = 1
                    else:
                        rearranged_num.append(sorted_num[i])
            rearranged_num = int("".join(rearranged_num))
        elif num == 0:
            rearranged_num = 0
        else:
            sorted_num = sorted(list(str(-num)), reverse=True)
            rearranged_num = -int("".join(sorted_num))

        ans = rearranged_num

        return ans
