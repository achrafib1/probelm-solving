class Solution(object):
    def intervalIntersection(self, firstList, secondList):
        """
        :type firstList: List[List[int]]
        :type secondList: List[List[int]]
        :rtype: List[List[int]]
        """
        i = 0
        j = 0
        ans = []
        while i < len(firstList) and j < len(secondList):

            if max(firstList[i][0], secondList[j][0]) <= min(
                firstList[i][1], secondList[j][1]
            ):
                ans.append(
                    [
                        max(firstList[i][0], secondList[j][0]),
                        min(firstList[i][1], secondList[j][1]),
                    ]
                )

            if firstList[i][1] > secondList[j][1]:
                j += 1
            else:
                i += 1

        return ans
