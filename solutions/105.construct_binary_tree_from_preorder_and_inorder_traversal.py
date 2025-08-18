# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        
        root_val = preorder[0]
        root = TreeNode(root_val)

        # 找到 root 在 inorder 的位置
        mid = inorder.index(root_val)

        # 左子樹用 inorder[:mid], preorder[1:1+mid]
        root.left = self.buildTree(preorder[1:1+mid], inorder[:mid])
        # 右子樹用 inorder[mid+1:], preorder[1+mid:]
        root.right = self.buildTree(preorder[1+mid:], inorder[mid+1:])

        return root