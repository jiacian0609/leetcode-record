class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        for l, r, k, v in queries:
            while l <= r:
                nums[l] = (nums[l] * v) % (10 ** 9 + 7)
                l += k

        result = nums[0]
        for n in nums[1:]:
            result = result ^ n
        return result
        