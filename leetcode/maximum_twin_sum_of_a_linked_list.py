# https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/description/


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def pairSum(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """

        size = 0
        ans = 0

        curr = head
        while curr:
            size += 1
            curr = curr.next

        curr = head
        for i in range(size // 2):
            curr = curr.next

        prev = None
        while curr:
            next_curr = curr.next
            curr.next = prev
            prev = curr
            curr = next_curr

        curr = head
        curr_prev = prev
        while curr_prev:
            ans = max(ans, curr.val + curr_prev.val)
            curr = curr.next
            curr_prev = curr_prev.next

        return ans
