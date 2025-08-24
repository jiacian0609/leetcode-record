class Solution:
    def partitionArray(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        if n % k != 0:
            return False

        count = Counter(nums)
        print(count)
        return all(i <= n / k for _, i in count.items())