# https://leetcode.com/problems/two-sum/


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        freq_dict = {}
        ans = []
        for i in range(len(nums)):
            freq_dict[nums[i]] = freq_dict.get(nums[i], 0) + 1

        for i in range(len(nums)):
            if freq_dict.get((target - nums[i]), 0) != 0:
                if nums[i] != target - nums[i] or (
                    nums[i] == target - nums[i] and freq_dict[nums[i]] > 1
                ):
                    ans.append(i)
                    ans.append(target - nums[i])
                    break

        for i in range(len(nums)):
            if nums[i] == ans[1] and i != ans[0]:
                ans[1] = i
                break

        return ans
