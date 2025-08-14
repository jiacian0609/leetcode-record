class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        num_set = set(nums)
        print(num_set)
        if len(num_set) == 1:
            return num_set.pop()
            
        thres = len(nums) // 2
        counts = {}

        for n in num_set:
            if nums.count(n) > thres:
                return n