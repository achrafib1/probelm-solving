# https://leetcode.com/problems/add-two-numbers/


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        remainder = 0
        ans = ListNode(-1)  # type: ignore
        curr_ans = ans
        curr_l1 = l1
        curr_l2 = l2
        curr_sum = 0
        while curr_l1 and curr_l2:
            curr_sum = curr_l1.val + curr_l2.val
            node = ListNode(curr_sum + remainder)  # type: ignore
            if curr_sum + remainder >= 10:
                node.val -= 10
                remainder = 1
            else:
                remainder = 0

            curr_ans.next = node
            curr_ans = curr_ans.next
            curr_l1 = curr_l1.next
            curr_l2 = curr_l2.next

        while curr_l1:
            node = ListNode(curr_l1.val + remainder)  # type: ignore
            if curr_l1.val + remainder >= 10:
                node.val -= 10
                remainder = 1
            else:
                remainder = 0

            curr_ans.next = node
            curr_ans = curr_ans.next
            curr_l1 = curr_l1.next

        while curr_l2:
            node = ListNode(curr_l2.val + remainder)  # type: ignore
            if curr_l2.val + remainder >= 10:
                node.val -= 10
                remainder = 1
            else:
                remainder = 0

            curr_ans.next = node
            curr_ans = curr_ans.next
            curr_l2 = curr_l2.next

        if remainder == 1:
            node = ListNode(remainder)  # type: ignore
            curr_ans.next = node
            curr_ans = curr_ans.next

        ans = ans.next

        return ans
