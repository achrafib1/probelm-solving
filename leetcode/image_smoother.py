# https://leetcode.com/problems/image-smoother/description/


class Solution(object):
    def imageSmoother(self, img):
        """
        :type img: List[List[int]]
        :rtype: List[List[int]]
        """
        img_with_padding = [
            [0 for i in range(len(img[0]) + 2)] for j in range(len(img) + 2)
        ]
        ans = [[0 for i in range(len(img[0]))] for j in range(len(img))]
        for i in range(len(img)):
            for j in range(len(img[0])):
                img_with_padding[i + 1][j + 1] = img[i][j]

        for i in range(len(img)):
            for j in range(len(img[0])):
                cells = [row[j : j + 3] for row in img_with_padding[i : i + 3]]

                total = sum(sum(row) for row in cells)

                num_pixels = 0
                for ri in range(i - 1, i + 2):
                    for rj in range(j - 1, j + 2):
                        if 0 <= ri < len(img) and 0 <= rj < len(img[0]):
                            num_pixels += 1

                ans[i][j] = total // num_pixels

        return ans
