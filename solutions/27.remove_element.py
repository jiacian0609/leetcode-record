class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        count = nums.count(val)
        for _ in range(count):
            nums.remove(val)
        # print(nums)
        return n - count