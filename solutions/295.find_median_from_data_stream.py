class MedianFinder:

    def __init__(self):
        self.arr = []
        

    def addNum(self, num: int) -> None:
        insort(self.arr, num)

    def findMedian(self) -> float:
        count = len(self.arr)
        # print(self.arr)
        if count % 2 == 0:
            medium = (self.arr[(count - 1) // 2] + self.arr[count // 2]) / 2
        else:
            medium = self.arr[count // 2]
        # print(medium)
        return medium


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()