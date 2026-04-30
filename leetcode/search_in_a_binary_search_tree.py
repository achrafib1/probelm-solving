# https://leetcode.com/problems/search-in-a-binary-search-tree/description/


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: Optional[TreeNode]
        :type val: int
        :rtype: Optional[TreeNode]
        """

        ans = None
        curr_node = root
        while curr_node:
            if curr_node.val == val:
                ans = curr_node
                break
            elif curr_node.val > val:
                curr_node = curr_node.left
            else:
                curr_node = curr_node.right

        # if(not root):
        #     return None

        # if(root.val==val):
        #     return root

        # if(root.val>val):
        #     ans=self.searchBST(root.left,val)
        # else:
        #     ans=self.searchBST(root.right,val)

        return ans
