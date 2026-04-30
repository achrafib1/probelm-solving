# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/


class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        left = 0
        right = len(nums) - 1
        ans = [-1, -1]

        def searchbound(isfirst):
            left = 0
            right = len(nums) - 1
            curr_ans = -1
            while left <= right:
                mid = int((left + right)) // 2

                if target == nums[mid]:
                    curr_ans = mid
                    if isfirst:
                        right = mid - 1
                    else:
                        left = mid + 1

                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1

            return curr_ans

        ans[0] = searchbound(isfirst=True)
        ans[1] = searchbound(isfirst=False)

        return ans
