# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None

        if root.val == key:  # 找到要刪除的節點
            if not root.left and not root.right:
                return None
            elif root.right:
                cur = root.right
                # print(cur.val)
                while cur.left:  # 找到右邊的數的最小值作為新的 root
                    cur = cur.left
                root.val = cur.val
                root.right = self.deleteNode(root.right, cur.val)
                return root
            else:
                return root.left
        
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            root.right = self.deleteNode(root.right, key)
        return root
        