class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []   # 用來存柱子的索引（index），不是高度
        result = 0   # 最後要回傳的積水量

        for idx, h in enumerate(height):
            # Case 1: stack 空的，或目前柱子比 stack 最上面的柱子低/一樣高
            # 代表地形在下降或持平，先存起來，等右邊有更高的牆再計算水
            if not stack or h <= height[stack[-1]]:
                stack.append(idx)

            else:
                # Case 2: 出現上升（h > height[stack[-1]]）
                # 代表有可能形成一個水坑，要來計算積水
                while stack and height[stack[-1]] < h:
                    # 取出最低的柱子，當作水坑的底
                    bottom = stack.pop()

                    # 如果沒有左牆（stack 空了），就無法形成水坑
                    if not stack:
                        break

                    # 此時 stack[-1] 是左牆，idx 是右牆
                    left = stack[-1]

                    # 水坑的寬度 = 右牆索引 - 左牆索引 - 1
                    width = idx - left - 1

                    # 水坑的高度 = min(左牆高, 右牆高) - 底部高度
                    bounded_height = min(height[left], h) - height[bottom]

                    # 加入水坑面積
                    result += width * bounded_height

                # 不管怎樣，最後還要把右牆存進 stack
                stack.append(idx)

        return result