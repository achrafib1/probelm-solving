# https://leetcode.com/problems/merge-sorted-array/description/?envType=problem-list-v2&envId=sorting


class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        i = 0
        j = 0
        for i in range(len(nums1)):
            if j < len(nums2) and nums1[i] == 0:
                nums1[i] = nums2[j]
                j += 1

        nums1.sort()

        return nums1
