class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)
        left = 1
        right = 1
        
        left_id = 0
        right_id = len(nums) - 1

        while 0 <= left_id < len(nums):
            # print((left_id, right_id))
            left *= nums[left_id]
            if left_id + 1 < len(nums):
                result[left_id + 1] *= left
            left_id += 1

            right *= nums[right_id]
            if right_id - 1 >= 0:
                result[right_id - 1] *= right
            right_id -= 1
        
        return result