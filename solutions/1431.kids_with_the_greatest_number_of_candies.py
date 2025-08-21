class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        cur_max = max(candies)
        result = []
        for kid in candies:
            if kid + extraCandies >= cur_max:
                result.append(True)
            else:
                result.append(False)
        return result