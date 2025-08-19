class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        count = 0

        left = 0
        while left < len(nums) and nums[left] != 0:
            left += 1
        if left == len(nums):
            return 0
        
        right = left
        while left < len(nums):
            while right < len(nums) and nums[right] == 0:
                right += 1
            n = right - left
            # print((left, right), n)
            for i in range(1, n + 1):
                # print(i)
                count += i
                # print(count)
            left = right
            while left < len(nums) and nums[left] != 0:
                left += 1
            right = left + 1
        return count    