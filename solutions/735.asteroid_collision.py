from typing import List

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for ast in asteroids:
            alive = True
            # 只有 ast < 0 且 stack 最後是正數，才會撞
            while alive and ast < 0 and stack and stack[-1] > 0:
                if stack[-1] < -ast:      # stack 的比較小 → 爆掉
                    stack.pop()
                    continue              # 繼續看前一顆
                elif stack[-1] == -ast:   # 一樣大 → 兩顆都爆
                    stack.pop()
                # 如果 stack[-1] > -ast → 當前 ast 爆
                alive = False
            if alive:
                stack.append(ast)
        return stack