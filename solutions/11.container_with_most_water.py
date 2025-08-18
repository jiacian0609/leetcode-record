class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        if n == 2:
            return min(height[0], height[1])

        water = 0
        i = 0
        j = n - 1
        while i < j:
            x = j - i
            y = min(height[i], height[j])
            if x * y > water:
                water = x * y

            j -= 1
            if i == j or (x * height[i] < water):
                i += 1
                j = n - 1
        return water