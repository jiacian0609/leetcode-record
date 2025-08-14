class Solution:
    def search(self, nums: List[int], target: int) -> int:
        print(nums)
        print("len:", len(nums))
        mid = len(nums) // 2 
        print("mid:", mid)

        if len(nums) == 0:
            return -1
        elif target == nums[mid]:
            print("find")
            return mid
        elif target < nums[mid]:
            print("small")
            return self.search(nums[:mid], target)
        else:
            print("big")
            if self.search(nums[mid + 1:], target) == -1:
                return -1
            return mid + self.search(nums[mid + 1:], target) + 1