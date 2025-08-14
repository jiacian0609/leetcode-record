class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals) == 0:
            return [newInterval]

        new_start = newInterval[0]
        new_end = newInterval[1]

        intervals.insert(0, newInterval)
        print(intervals)
        
        i, j = 0, 1

        while i < len(intervals) and j < len(intervals):
            if self.overlapped(intervals[i], intervals[j]):
                intervals[j] = self.merge(intervals[i], intervals[j])
                intervals.pop(i)
                i = j - 1
            elif intervals[i][0] > intervals[j][1]:
                intervals[i], intervals[j] = intervals[j], intervals[i]
                i = j
                j = i + 1
            else:
                break

        return intervals


    def overlapped(self, a: List[int], b: List[int]) -> bool:
        l = a if a[0] <= b[0] else b
        r = a if a[0] > b[0] else b

        if l[0] == r[0] or l[1] == r[1]:
            return True

        if l[1] >= r[0]:
            return True
        
        return False

    def merge(self, a: List[int], b: List[int]) -> List[int]:
        if a[0] == b[0]:
            if a[1] <= b[1]:
                return b
            else:
                return a
        elif a[0] < b[0]:
            if a[1] <= b[1]:
                return [a[0], b[1]]
            else:
                return a
        else:
            if a[1] <= b[1]:
                return b
            else:
                return [b[0], a[1]]