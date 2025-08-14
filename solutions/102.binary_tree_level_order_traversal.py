from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        elif not root.left and not root.right:
            return [[root.val]]

        q = deque([root])
        next_q = deque()
        
        result = []
        cur_result = []

        while q:
            cur = q.popleft()
            if cur.left:
                next_q.append(cur.left)
            if cur.right:
                next_q.append(cur.right)
            cur_result.append(cur.val)

            if not q:
                result.append(cur_result)
                cur_result = []
                q = next_q
                next_q = deque()
        return result