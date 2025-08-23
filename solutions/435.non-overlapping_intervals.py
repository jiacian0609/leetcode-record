class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        # 按結束時間排序
        intervals.sort(key=lambda x: x[1])
        count = 0
        end = float('-inf')

        for i, j in intervals:
            if i >= end:
                # 不重疊，更新 end
                end = j
            else:
                # 重疊，需要刪除一個
                count += 1

        return count