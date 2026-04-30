# https://leetcode.com/problems/insert-into-a-binary-search-tree/


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: Optional[TreeNode]
        :type val: int
        :rtype: Optional[TreeNode]
        """

        node_to_add = TreeNode(val)  # type: ignore
        curr_node = root

        prev_node = None
        while curr_node:
            prev_node = curr_node
            if curr_node.val > val:
                curr_node = curr_node.left
            else:
                curr_node = curr_node.right

        if prev_node:
            if prev_node.val > val:
                prev_node.left = node_to_add
            else:
                prev_node.right = node_to_add
        else:
            root = node_to_add

        return root
