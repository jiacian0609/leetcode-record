class Solution(object):
    def gcdOfOddEvenSums(self, n):
        sumOdd = n * n
        sumEven = n * (n + 1)
        return math.gcd(sumOdd, sumEven)