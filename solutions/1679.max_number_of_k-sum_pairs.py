class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        count = 0
        n = len(nums)
        i = 0
        j = n - 1
        while i < j:
            if nums[i] + nums[j] == k:
                count += 1
                i += 1
                j -= 1
            elif nums[i] + nums[j] > k:
                j -= 1
            else:
                i += 1
        return count