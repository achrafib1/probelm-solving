# https://leetcode.com/problems/binary-tree-preorder-traversal/


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """

        ans = []
        self.preordert(root, ans)

        return ans

    def preordert(self, node, ans):
        if node:
            ans.append(node.val)
            self.preordert(node.left, ans)
            self.preordert(node.right, ans)
