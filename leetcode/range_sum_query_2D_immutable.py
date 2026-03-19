# https://leetcode.com/problems/range-sum-query-2d-immutable/s


class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        self.mat = matrix
        self.p_sum = [[0] * (len(self.mat[0]) + 1) for i in range(len(self.mat) + 1)]
        for i in range(len(self.mat)):
            for j in range(len(self.mat[0])):
                self.p_sum[i + 1][j + 1] = (
                    self.mat[i][j]
                    + self.p_sum[i][j + 1]
                    + self.p_sum[i + 1][j]
                    - self.p_sum[i][j]
                )

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        return (
            self.p_sum[row2 + 1][col2 + 1]
            - self.p_sum[row1][col2 + 1]
            - self.p_sum[row2 + 1][col1]
            + self.p_sum[row1][col1]
        )


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
