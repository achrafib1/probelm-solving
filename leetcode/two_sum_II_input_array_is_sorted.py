# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/


class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        left = 0
        right = len(numbers) - 1
        ans = []
        while left < right:
            if numbers[left] + numbers[right] == target:
                ans = [left + 1, right + 1]
                break
            elif numbers[left] + numbers[right] > target:
                right -= 1
            else:
                left += 1

        return ans
