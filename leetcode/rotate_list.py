# https://leetcode.com/problems/rotate-list/


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """

        size = 0
        curr = head
        while curr:
            size += 1
            curr = curr.next

        if size > 1 and k % size > 0:
            dummy = ListNode(-1)  # type: ignore
            dummy.next = head
            curr = dummy
            for i in range((size - (k % size)) + 1):
                curr = curr.next

            start = curr

            if start:
                curr = dummy
                while curr.next:
                    curr = curr.next

                curr.next = head

                curr = dummy
                while curr.next != start:
                    curr = curr.next

                curr.next = None

                head = start

        return head
