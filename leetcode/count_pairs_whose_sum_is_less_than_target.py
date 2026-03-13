# https://leetcode.com/problems/count-pairs-whose-sum-is-less-than-target/


class Solution(object):
    def countPairs(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        ans = 0
        left = 0
        right = len(nums) - 1
        nums.sort()
        while left < right:
            if nums[left] + nums[right] < target:
                ans += right - left
                left += 1
            else:
                right -= 1

        return ans

        # for i in range(len(nums)):
        #     for j in range(len(nums)):
        #         if(i!=j and i<j and nums[i]+nums[j]<target):
        #             ans+=1

        # return ans
