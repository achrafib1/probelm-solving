# https://leetcode.com/problems/diagonal-traverse/description/


class Solution(object):
    def findDiagonalOrder(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        bucket_dict = {}
        pos_bucket_dict = {}
        ans = []
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if i == 0 or j == len(mat[0]) - 1:
                    pos_bucket_dict[(i, j)] = i + j
                    bucket_dict[i + j] = [mat[i][j]]
                else:
                    pos_bucket_dict[(i, j)] = pos_bucket_dict[(i - 1, j + 1)]
                    bucket_dict[pos_bucket_dict[(i, j)]].append(mat[i][j])

        for k, v in bucket_dict.items():
            if k % 2 == 0:
                v.reverse()
            ans += v

        return ans
