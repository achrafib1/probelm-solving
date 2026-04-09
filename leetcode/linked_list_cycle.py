# https://leetcode.com/problems/linked-list-cycle/description/


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        fast = head
        slow = head

        ans = False
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                ans = True
                break

        return ans
