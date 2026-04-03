# https://leetcode.com/problems/merge-two-sorted-lists/


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# 47min


class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        ans = ListNode(0)  # type: ignore

        curr_ans = ans

        curr1 = list1
        curr2 = list2

        while curr1 and curr2:
            if curr1.val < curr2.val:
                curr_ans.next = curr1
                curr1 = curr1.next
            else:
                curr_ans.next = curr2
                curr2 = curr2.next

            curr_ans = curr_ans.next

        if curr1:
            curr_ans.next = curr1
        else:
            curr_ans.next = curr2

        ans = ans.next

        return ans
