# https://leetcode.com/problems/sort-colors/description/


class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            min_v_i = i
            for j in range(i + 1, len(nums)):
                if nums[j] < nums[min_v_i]:
                    min_v_i = j

            nums[min_v_i], nums[i] = nums[i], nums[min_v_i]

        return nums

        # for i in range(1,len(nums)):
        #     key=nums[i]
        #     j=i-1
        #     while j>=0 and nums[j]>key:
        #         nums[j+1]=nums[j]
        #         j-=1

        #     nums[j+1]=key

        # return nums

        # for i in range(len(nums)):
        #     swap=False
        #     for j in range(0,len(nums)-i-1):
        #         if(nums[j]>nums[j+1]):
        #             nums[j],nums[j+1]=nums[j+1], nums[j]
        #             swap=True

        #     if(swap==False):
        #         break

        # return nums

        # count_0=0
        # count_1=0
        # count_2=0
        # for i in range(len(nums)):
        #     if(nums[i]==0):
        #         count_0+=1
        #     if(nums[i]==1):
        #         count_1+=1
        #     if(nums[i]==2):
        #         count_2+=1

        # i=0
        # while(i<len(nums)):

        #     for j in range(count_0):
        #         nums[i+j]=0
        #     i+=count_0

        #     for j in range(count_1):
        #         nums[i+j]=1
        #     i+=count_1

        #     for j in range(count_2):
        #         nums[i+j]=2

        #     i+=count_2

        # return nums
