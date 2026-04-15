# https://leetcode.com/problems/next-greater-element-i/description/


class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        next_g_elment_dict = {nums1[i]: -1 for i in range(len(nums1))}
        stack = []
        ans = [-1] * len(nums1)

        for i in range(len(nums2)):

            while stack and nums2[i] > stack[-1]:
                next_g_elment_dict[stack[-1]] = nums2[i]
                stack.pop()

            stack.append(nums2[i])

        for i in range(len(nums1)):
            ans[i] = next_g_elment_dict[nums1[i]]

        return ans
