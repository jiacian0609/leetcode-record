class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # stack 用來存索引，stack[-1] 永遠保持比當前高度小的元素索引
        # 初始化為 -1 方便計算寬度
        stack = [-1]
        max_area = 0

        # 遍歷所有高度
        for i in range(len(heights)):
            # 如果目前高度比 stack 頂端高度小，表示可以計算矩形面積
            while stack[-1] != -1 and heights[i] <= heights[stack[-1]]:
                # 取出高度
                height = heights[stack.pop()]
                # 計算寬度，i - stack[-1] - 1 是矩形寬度
                width = i - stack[-1] - 1
                # 更新最大面積
                # print(stack, height, width)
                max_area = max(max_area, height * width)
            # 將當前索引加入 stack
            stack.append(i)
        
        # 處理 stack 中剩餘的元素
        while stack[-1] != -1:
            height = heights[stack.pop()]
            width = len(heights) - stack[-1] - 1
            max_area = max(max_area, height * width)
            # print(stack, height, width)
        
        return max_area