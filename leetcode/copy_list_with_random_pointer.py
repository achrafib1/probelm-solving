# https://leetcode.com/problems/copy-list-with-random-pointer/description/


"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        ans = None
        if head:
            curr = head
            i = 0
            node_dict = {}

            ans = Node(-1)  # type: ignore
            curr_copy_ans = ans

            while curr:
                node = Node(curr.val, None, curr.random)  # type: ignore
                curr_copy_ans.next = node
                node_dict[curr] = node
                curr = curr.next
                curr_copy_ans = curr_copy_ans.next

            curr_copy_ans = ans.next
            while curr_copy_ans:
                if curr_copy_ans.random:
                    curr_copy_ans.random = node_dict[curr_copy_ans.random]

                curr_copy_ans = curr_copy_ans.next

            ans = ans.next

        return ans
