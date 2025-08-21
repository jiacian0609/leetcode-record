class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        uniqueNum = set(arr)
        counts = []
        for n in uniqueNum:
            count = arr.count(n)
            if count not in counts:
                counts.append(count)
            else: return False
        return True