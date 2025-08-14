# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if (root == None
            or (root.left == None and root.right == None)
            or (root.left == None and self.calDepth(root.right) <= 1)
            or (root.right == None and self.calDepth(root.left) <= 1)):
            return True
        elif abs(self.calDepth(root.left) - self.calDepth(root.right)) <= 1:
            return self.isBalanced(root.left) and self.isBalanced(root.right)
        else:
            return False

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
        