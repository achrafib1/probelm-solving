# https://leetcode.com/problems/remove-duplicates-from-sorted-list/


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(-1000)  # type: ignore
        dummy.next = head

        curr = dummy

        while curr and curr.next:
            if curr.val == curr.next.val:
                curr.next = curr.next.next

            else:
                curr = curr.next

        head = dummy.next

        return head
