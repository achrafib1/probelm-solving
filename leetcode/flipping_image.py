# https://leetcode.com/problems/flipping-an-image/description/


class Solution(object):
    def flipAndInvertImage(self, image):
        """
        :type image: List[List[int]]
        :rtype: List[List[int]]
        """
        flipped_image = [list(reversed(row)) for row in image]
        ans = [
            [1 if row[i] == 0 else 0 for i in range(len(row))] for row in flipped_image
        ]
        return ans
