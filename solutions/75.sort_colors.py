class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        for i in range(n - 1):
            # 每輪把最大的數往右推
            for j in range(n - 1 - i):
                if nums[j] > nums[j + 1]:  # 比較的是值，不是索引
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
        