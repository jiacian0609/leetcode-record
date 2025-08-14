# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        left = p if p.val <= q.val else q
        right = p if p.val > q.val else q

        if ((left.val < root.val and right.val > root.val)
            or left.val == root.val
            or right.val == root.val):
            return root
        # find left tree
        elif left.val < root.val and right.val < root.val: 
            return self.lowestCommonAncestor(root.left, p, q)
        # find right tree
        else:
            return self.lowestCommonAncestor(root.right, p, q)
        