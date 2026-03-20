# https://leetcode.com/problems/continuous-subarray-sum/


class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        ans = False
        p_sum = [0] * (len(nums) + 1)
        remainders_dict = {0: -1}

        for i in range(len(nums)):
            p_sum[i + 1] = p_sum[i] + nums[i]

        for i in range(len(nums)):
            if p_sum[i + 1] % k in remainders_dict:
                if i - remainders_dict[p_sum[i + 1] % k] >= 2:
                    ans = True
                    break
            else:
                remainders_dict[p_sum[i + 1] % k] = i

        return ans
