# https://leetcode.com/problems/transpose-matrix/


class Solution(object):
    def transpose(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        transpose_matrix = [
            [0 for i in range(len(matrix))] for j in range(len(matrix[0]))
        ]
        for i in range(len(matrix[0])):
            for j in range(len(matrix)):
                transpose_matrix[i][j] = matrix[j][i]

        return transpose_matrix


#10min