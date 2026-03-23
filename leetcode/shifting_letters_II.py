# https://leetcode.com/problems/shifting-letters-ii/description/


class Solution(object):
    def shiftingLetters(self, s, shifts):
        """
        :type s: str
        :type shifts: List[List[int]]
        :rtype: str
        """
        prefix_sum = [0] * (len(s) + 1)
        shifts_arr = [0] * (len(s) + 1)
        ans = []
        for left, right, direction in shifts:
            shifts_arr[left] += 1 if direction == 1 else -1
            shifts_arr[right + 1] -= 1 if direction == 1 else -1

        curr_sum = 0
        for i in range(len(shifts_arr)):
            curr_sum += shifts_arr[i]
            prefix_sum[i] = curr_sum

        for i in range(len(s)):
            ans.append(chr((((ord(s[i]) - ord("a")) + prefix_sum[i]) % 26) + ord("a")))

        ans = "".join(ans)
        return ans
