# https://leetcode.com/problems/swap-nodes-in-pairs/


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        curr = head
        if head and head.next:
            head = head.next

            prev = None
            while curr and curr.next:
                next_curr = curr.next
                curr.next = curr.next.next
                next_curr.next = curr
                if prev:
                    prev.next = next_curr
                prev = curr
                curr = curr.next

        return head
