class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False

        nums.sort(reverse=True)
        target = sum(nums) // 2

        dp = [False] * (target + 1)
        dp[0] = True
        for n in nums:
            for i in range(target, n - 1, -1):
                if dp[i]: continue
                if dp[i - n]: dp[i] = True
                if dp[-1]: return True
        print(dp)
        return dp[-1]