class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [[], nums]

        subset = self.subsets(nums[1:])
        # print(f"subset: {subset}")
        result = []
        for s in subset:
            result.append(s.copy())
            s.append(nums[0])
            result.append(s.copy())
            # print(result)
        return result