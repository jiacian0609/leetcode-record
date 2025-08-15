class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        if n == 1:
            return [nums]
        elif n == 2:
            return [nums, [nums[1], nums[0]]]

        result = []
        for i in nums:
            temp = nums.copy()
            temp.remove(i)
            prev = self.permute(temp)
            # print(prev)
            for p in prev:
                p.append(i)
                result.append(p)
        return result

        
    def swap(self, nums, i, j):
        result = nums.copy()
        temp = result[i]
        result[i] = result[j]
        result[j] = temp
        return result
