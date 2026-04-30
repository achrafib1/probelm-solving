# https://leetcode.com/problems/search-a-2d-matrix/


class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        left = 0
        right = len(matrix) * len(matrix[0]) - 1
        ans = False
        while left <= right:
            mid = int((left + right)) // 2

            i = int(mid) // len(matrix[0])
            j = mid % len(matrix[0])

            if target == matrix[i][j]:
                ans = True
                break
            elif target > matrix[i][j]:
                left = mid + 1
            else:
                right = mid - 1

        return ans
