# https://leetcode.com/problems/find-smallest-letter-greater-than-target/description/


class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """

        left = 0
        right = len(letters) - 1
        ans = letters[0]

        while left <= right:
            mid = int((left + right)) // 2

            if target >= letters[mid]:
                left = mid + 1
            else:
                ans = letters[mid]
                right = mid - 1

        return ans
