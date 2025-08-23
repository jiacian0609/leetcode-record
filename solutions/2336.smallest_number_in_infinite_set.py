class SmallestInfiniteSet:

    def __init__(self):
        self.popped = []
        

    def popSmallest(self) -> int:
        # print(self.popped)
        if len(self.popped) == 0:
            self.popped.append(1)
            return 1

        i = 1
        idx = 0
        while idx < len(self.popped):
            if i < self.popped[idx]:
                insort(self.popped, i)
                return i
            else:
                i = self.popped[idx] + 1
                idx += 1
        insort(self.popped, i)
        return i
        

    def addBack(self, num: int) -> None:
        if num in self.popped:
            self.popped.remove(num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)

class SmallestInfiniteSet2:
    def __init__(self):
        self.heap = []       # min-heap，用來存被 addBack 的小於 next_num 的數
        self.added = set()   # 記錄 heap 中有哪些數字，避免重複加入
        self.next_num = 1    # 目前還沒 pop 過的最小正整數

    def popSmallest(self) -> int:
        # 如果 heap 裡有元素，代表之前被 addBack 的小數
        if self.heap:
            val = heapq.heappop(self.heap)  # 取 heap 中最小值
            self.added.remove(val)           # 從 set 中移除，表示已被 pop
            return val
        # 如果 heap 空，直接取 next_num
        val = self.next_num
        self.next_num += 1                   # 更新 next_num 為下一個未 pop 的數
        return val

    def addBack(self, num: int) -> None:
        # 只有 num < next_num 才需要加回
        # 因為大於等於 next_num 的數尚未 pop 過，本身就在集合中
        # 並且要確保 num 沒在 heap 中，避免重複加入
        if num < self.next_num and num not in self.added:
            heapq.heappush(self.heap, num)  # 加入 heap
            self.added.add(num)             # 記錄在 set 中
