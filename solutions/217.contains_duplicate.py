class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        _set = set(nums)
        return len(nums) > len(_set)
        