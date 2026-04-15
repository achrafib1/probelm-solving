# https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/description/?envType=problem-list-v2&envId=linked-list


"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""


class Solution(object):
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """

        stack = []
        dummy = Node(-1, None, None, None)  # type: ignore
        dummy.next = head
        curr = dummy
        stack.append(head)
        while len(stack) > 0:
            curr.next = stack.pop()

            if curr.next:
                curr.next.prev = curr

            while curr.next or curr.child:
                if curr.child:
                    stack.append(curr.next)
                    curr.next = curr.child
                    curr.next.prev = curr
                    curr.child = None
                    curr = curr.next

                else:
                    curr.next.prev = curr
                    curr = curr.next

            curr.next = None

        head = dummy.next
        if head:
            head.prev = None

        return head
