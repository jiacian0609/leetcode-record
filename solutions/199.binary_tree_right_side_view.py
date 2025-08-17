# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        elif not root.left and not root.right:
            return [root.val]
        
        q = deque([[root, 1]])
        level = 1
        result = []
        while q:
            cur_node, cur_level = q.popleft()
            if cur_level == level:
                result.append(cur_node.val)
                level += 1
            
            if cur_node.right:
                q.append([cur_node.right, level])
            
            if cur_node.left:
                q.append([cur_node.left, level])
        
        return result