# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(node):
            if not node:
                # is_bst, min, max
                return True, float(inf), float(-inf)
            
            l_bst, l_min, l_max = helper(node.left)
            r_bst, r_min, r_max = helper(node.right)

            is_bst = (
                l_bst and r_bst
                and l_max < node.val
                and r_min > node.val
            )

            return is_bst, min(l_min, node.val), max(r_max, node.val)
        
        return helper(root)[0]