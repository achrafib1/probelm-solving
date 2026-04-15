# https://leetcode.com/problems/pascals-triangle/description/


class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        ans = []

        ans = self.Ptriangle(numRows, 1, ans)

        return ans

    def Ptriangle(self, numRows, numRow, ans):

        if numRow == 1:
            ans.append([1])

        if numRows == numRow:
            return ans

        curr_ans = [1]
        for i in range(len(ans[-1]) - 1):
            curr_ans.append(ans[-1][i] + ans[-1][i + 1])

        curr_ans.append(1)

        ans.append(curr_ans)

        ans = self.Ptriangle(numRows, numRow + 1, ans)

        return ans
