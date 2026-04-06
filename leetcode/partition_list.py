# https://leetcode.com/problems/partition-list/description/


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def partition(self, head, x):
        """
        :type head: Optional[ListNode]
        :type x: int
        :rtype: Optional[ListNode]
        """

        curr = head
        list1 = []
        list2 = []
        while curr:
            if curr.val < x:
                list1.append(curr)
            else:
                list2.append(curr)

            curr = curr.next

        ans = ListNode(-1)  # type: ignore
        curr = ans
        for i in range(len(list1)):
            print(list1[i].val)
            curr.next = list1[i]
            curr = curr.next

        for i in range(len(list2)):
            print(list2[i].val)
            curr.next = list2[i]
            curr = curr.next

        curr.next = None

        ans = ans.next

        return ans
