# https://leetcode.com/problems/reverse-linked-list-ii/


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: Optional[ListNode]
        :type left: int
        :type right: int
        :rtype: Optional[ListNode]
        """

        dummy = ListNode(-1)  # type: ignore
        dummy.next = head
        first_half_list = dummy

        for i in range(left - 1):
            first_half_list = first_half_list.next

        left_node = first_half_list.next
        curr = first_half_list.next
        prev = first_half_list
        for i in range(right - left + 1):
            next_curr = curr.next
            curr.next = prev
            prev = curr
            curr = next_curr

        left_node.next = curr
        first_half_list.next = prev

        return dummy.next
