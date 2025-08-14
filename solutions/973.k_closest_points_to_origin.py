class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = [(self.calDis(p), p) for p in points]
        distances.sort()
        return [p for _, p in distances[:k]]

    def calDis(self, p: List[int]) -> float:
        return sqrt(p[0] ** 2 + p[1] ** 2)