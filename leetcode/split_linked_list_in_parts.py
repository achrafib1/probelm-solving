# https://leetcode.com/problems/split-linked-list-in-parts/


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def splitListToParts(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: List[Optional[ListNode]]
        """

        size = 0
        curr = head
        while curr:
            size += 1
            curr = curr.next

        print(size)
        part_size = int(size // k)
        print(part_size)
        print(int(size // k))

        ans = []
        curr = head
        for i in range(k):
            part_size = int(size // k)
            if i < size % k:
                part_size = part_size + 1

            curr_ans_node = ListNode(-1)  # type: ignore
            curr_ans = curr_ans_node
            for j in range(part_size):
                if curr:
                    curr_ans.next = ListNode(curr.val)  # type: ignore
                    curr_ans = curr_ans.next
                    curr = curr.next

            ans.append(curr_ans_node.next)

        return ans
