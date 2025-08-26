from heapq import heappush, heappop
from operator import itemgetter

class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        res, prefixSum, minHeap = 0, 0, []

        # 將 (nums1[i], nums2[i]) 配對後，依照 nums2 值由大到小排序
        # 因為 nums2 的最小值會影響公式中的乘積 (score = sum(nums1_subseq) * min(nums2_subseq))
        for a, b in sorted(list(zip(nums1, nums2)), key=itemgetter(1), reverse=True):
            # 把 nums1 的值累加進 prefixSum
            prefixSum += a
            # 同時存進 minHeap，方便隨時移除最小的元素 (保持 subsequence 大小為 k)
            heappush(minHeap, a)

            # 當目前挑選的元素數量到達 k 個
            if len(minHeap) == k:
                # 計算分數：nums1 子序列總和 * 當前 nums2 的值 (此時 b 為目前最小的 nums2)
                res = max(res, prefixSum * b)
                # 移除最小的 nums1 元素，準備讓 subsequence 繼續 sliding
                prefixSum -= heappop(minHeap)

        return res