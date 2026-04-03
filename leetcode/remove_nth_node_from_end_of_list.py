# https://leetcode.com/problems/remove-nth-node-from-end-of-list/


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        # size=0
        # curr=head
        # while curr:
        #     size+=1
        #     curr=curr.next

        # dummy=ListNode(-1)
        # dummy.next=head

        # prev=dummy
        # curr=head

        # for i in range(size-n):
        #     prev=curr
        #     curr=curr.next

        # prev.next=curr.next

        # return dummy.next

        dummy = ListNode(-1)  # type: ignore
        dummy.next = head

        fast = dummy
        slow = dummy

        for i in range(n + 1):
            fast = fast.next

        while fast:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next

        return dummy.next
