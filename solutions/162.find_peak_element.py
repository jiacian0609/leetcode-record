class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        max_n = max(nums)
        return nums.index(max_n)
    
    def findPeakElementBS(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            # 取得左右相鄰元素的值，邊界用 -∞
            left_val = nums[mid - 1] if mid - 1 >= 0 else float('-inf')
            right_val = nums[mid + 1] if mid + 1 < len(nums) else float('-inf')

            # 如果 mid 比左右都大，就是峰值
            if nums[mid] > left_val and nums[mid] > right_val:
                return mid
            # 如果右邊比 mid 大 → 峰值在右邊
            elif nums[mid] < right_val:
                left = mid + 1
            # 否則峰值在左邊
            else:
                right = mid - 1

        # 理論上不會到這裡
        return -1