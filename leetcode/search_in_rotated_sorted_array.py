# https://leetcode.com/problems/search-in-rotated-sorted-array/


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        left = 0
        right = len(nums) - 1
        ans = -1

        while left <= right:
            mid = int((left + right)) // 2

            if target == nums[mid]:
                ans = mid
                break

            elif target > nums[mid]:
                if target > nums[right]:
                    if nums[mid] > nums[left]:
                        left = mid + 1
                    else:
                        right = mid - 1
                else:
                    left = mid + 1
            else:
                if target < nums[left]:
                    if nums[right] < nums[mid]:
                        left = mid + 1
                    else:
                        right = mid - 1
                else:
                    right = mid - 1

        return ans
