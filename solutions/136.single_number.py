class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        unique = set(nums)

        for n in unique:
            if nums.count(n) == 1:
                return n