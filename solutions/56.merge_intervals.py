class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        i = 0
        intervals = sorted(intervals, key=lambda i: i[0])
        while i < len(intervals) - 1:
            isOverlapped, newInterval = self.overlap(intervals[i], intervals[i + 1])
            if isOverlapped:
                intervals[i] = newInterval
                intervals.pop(i + 1)
                if i > 0:
                    i -= 1
            else:
                i += 1
        return intervals


    def overlap(self, a, b):
        if a[0] == b[0]:
            if a[1] < b[1]:
                return True, b
            else:
                return True, a
        if a[1] == b[1]:
            if a[0] < b[0]:
                return True, a
            else:
                return True, b
        if a[1] >= b[0] and a[1] <= b[1]:
            return True, [a[0], b[1]]
        if a[1] >= b[1]:
            return True, a
        if a[0] <= b[1] and a[1] >= b[1]:
            return True, [b[0], a[1]]
        return False, None
        