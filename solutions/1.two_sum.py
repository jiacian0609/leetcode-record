class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        id_1 = 0
        id_2 = 1
        while id_1 < len(nums) and id_2 < len(nums):
            if nums[id_1] + nums[id_2] == target:
                return [id_1, id_2]
            else:
                if id_2 == len(nums) - 1:
                    id_1 += 1
                    id_2 = id_1 + 1
                else:
                    id_2 += 1
        