class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        
        max_length = 0
        while left < n:
            # find first 1
            while left < n and nums[left] == 0:
                left += 1
            if left == n: break
            
            one_zero = True
            right = left + 1  # length = right - left + 1
            next_left = n
            cur_length = 1
            while right < n:
                if nums[right] == 0 and one_zero:
                    one_zero = False
                    next_left = right + 1
                elif nums[right] == 0:
                    break
                else:  # nums[right] == 1
                    cur_length += 1
                right += 1
            if one_zero and cur_length == n:
                cur_length -= 1
            # print(left, cur_length)
            left = next_left
            max_length = max(max_length, cur_length)

        return max_length