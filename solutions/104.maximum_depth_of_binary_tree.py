# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.calDepth(root)
        
    def calDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        elif root.left == None and root.right == None:
            return 1
        elif root.left == None:
            return 1 + self.calDepth(root.right)
        elif root.right == None:
            return 1 + self.calDepth(root.left)
        else:
            return 1 + max(self.calDepth(root.left), self.calDepth(root.right))