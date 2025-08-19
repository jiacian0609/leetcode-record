from collections import Counter, deque
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # 統計每個 task 的數量
        counter = Counter(tasks)

        # 建 max heap (用負數模擬)
        heap = [-cnt for cnt in counter.values()]
        heapq.heapify(heap)

        # 冷卻隊列: [(釋放時間, -剩餘數)]
        cool_down = deque()
        
        time = 0
        while heap or cool_down:
            time += 1

            # 如果 heap 有任務可以執行
            if heap:
                cnt = heapq.heappop(heap) + 1   # 執行一次 (cnt 是負的，+1 代表減少)
                if cnt < 0:  # 還有剩，放進冷卻隊列
                    cool_down.append((time + n, cnt))

            # 冷卻期結束，任務可以重新進 heap
            if cool_down and cool_down[0][0] == time:
                _, cnt = cool_down.popleft()
                heapq.heappush(heap, cnt)

        return time