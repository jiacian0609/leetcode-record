# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        self.leaf1 = []
        self.leaf2 = []

        def dfs(root, leaf):
            # print(root.val)
            if not root.left and not root.right:
                # print(f"leaf: {root.val}")
                leaf.append(root.val)
            
            if root.left:
                leaf = dfs(root.left, leaf)
            if root.right:
                leaf = dfs(root.right, leaf)
            return leaf

        self.leaf1 = dfs(root1, self.leaf1)
        self.leaf2 = dfs(root2, self.leaf2)
        # print(self.leaf1, self.leaf2)

        return self.leaf1 == self.leaf2