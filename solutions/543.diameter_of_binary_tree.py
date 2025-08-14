# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_diameter = 0
        self.calDepth(root)
        return self.max_diameter

    def calDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        left_depth = self.calDepth(root.left)
        right_depth = self.calDepth(root.right)

        # 更新最大直徑
        self.max_diameter = max(self.max_diameter, left_depth + right_depth)

        return 1 + max(left_depth, right_depth)
