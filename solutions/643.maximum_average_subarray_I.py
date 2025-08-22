class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_sum = sum(nums[:k])
        cur_sum = max_sum
        i = 0  # remove i, add i + k
        while i < len(nums) - k:
            cur_sum -= nums[i]
            cur_sum += nums[i + k]
            if cur_sum > max_sum:
                max_sum = cur_sum
            i += 1
        return max_sum / k