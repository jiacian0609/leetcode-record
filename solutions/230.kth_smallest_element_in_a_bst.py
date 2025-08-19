# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # 記錄目前已經訪問的節點數量
        self.count = 0
        # 存放第 k 小的節點值
        self.result = None
        
        # 定義中序遍歷函式 (左 -> 根 -> 右)
        def dfs(node):
            if not node:
                return  # 遇到空節點就返回
            
            # 遞迴左子樹
            dfs(node.left)
            
            # 訪問當前節點
            self.count += 1
            if self.count == k:
                # 找到第 k 個節點，存結果
                self.result = node.val
                return  # 可返回，節省後續不必要遍歷
            
            # 遞迴右子樹
            dfs(node.right)

        # 從 root 開始遍歷
        dfs(root)
        # 回傳找到的第 k 小值
        return self.result