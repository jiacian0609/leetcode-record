import math
class Solution:
    def minSensors(self, n: int, m: int, k: int) -> int:
        cover = k * 2 + 1
        cover_m = math.ceil(m / cover)
        cover_n = math.ceil(n / cover)
        return cover_m * cover_n

    def minSensors2(self, n: int, m: int, k: int) -> int:
        if k == 0:
            return m * n

        cover = k * 2 + 1

        if m <= cover and n <= cover:
            return 1

        count = 1
        if n - cover > 0:
            print((n - cover, cover))
            count += self.minSensors(n - cover, cover, k)
        if m - cover > 0:
            print((cover, m - cover))
            count += self.minSensors(cover, m - cover, k)
        if n - cover > 0 and m - cover > 0:
            print((n - cover, m - cover))
            count += self.minSensors(n - cover, m - cover, k)

        return count
        