# https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/


class Solution(object):
    def smallestDivisor(self, nums, threshold):
        """
        :type nums: List[int]
        :type threshold: int
        :rtype: int
        """

        def checkdivisor(n, nums, threshold):
            n_nums = nums[::]
            for i in range(len(nums)):
                n_nums[i] = int(math.ceil(n_nums[i] / float(n)))  # type: ignore

            curr_sum = sum(n_nums)
            if curr_sum <= threshold:
                return True
            else:
                return False

        total_sum = sum(nums)
        left = 1
        right = total_sum
        ans = total_sum

        while left <= right:
            mid = int((left + right)) // 2

            if checkdivisor(mid, nums, threshold):
                ans = min(ans, mid)
                right = mid - 1
            else:
                left = mid + 1

        return ans
