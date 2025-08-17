from bisect import bisect_left, bisect_right
from typing import List

class Solution:
    def perfectPairs(self, nums: List[int]) -> int:
        # 1) 只跟絕對值有關，先取絕對值並排序
        abs_nums = sorted(abs(x) for x in nums)
        n = len(abs_nums)
        count = 0

        for i, x in enumerate(abs_nums):
            # 2) 對於固定的 x=|a|，找所有 j>i 的 y=|b|
            #    使得 y ∈ [ceil(x/2), 2x]   ← 由上面的等價條件
            lo = bisect_left(abs_nums, (x + 1) // 2, i + 1)  # ceil(x/2)
            hi = bisect_right(abs_nums, 2 * x, i + 1)        # ≤ 2x 的最右界 + 1

            # 3) [lo, hi) 都是能和 i 構成 perfect 的 j
            count += hi - lo

        return count
