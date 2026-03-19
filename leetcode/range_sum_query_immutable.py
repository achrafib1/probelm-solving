# https://leetcode.com/problems/range-sum-query-immutable/


class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        for i in range(1, len(self.nums)):
            self.nums[i] += self.nums[i - 1]

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        ans = 0
        if left == 0:
            ans = self.nums[right]
        else:
            ans = self.nums[right] - self.nums[left - 1]

        return ans


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
