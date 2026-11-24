# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        res = 1
        if root is None:
            return 0
        else:
            leftside = self.maxDepth(root.left)
            rightside = self.maxDepth(root.right)
            res += max(leftside,rightside)
            return res