# https://leetcode.com/problems/palindrome-linked-list/description/


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        ans = True
        slow = head
        fast = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        curr = slow
        prev = None
        while curr:
            next_curr = curr.next
            curr.next = prev
            prev = curr
            curr = next_curr

        fast = prev

        slow = head
        while fast:
            if fast.val != slow.val:
                ans = False
                break
            fast = fast.next
            slow = slow.next

        return ans
