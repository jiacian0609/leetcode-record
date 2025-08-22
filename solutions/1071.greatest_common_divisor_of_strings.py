class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        a = str1 if len(str1) <= len(str2) else str2  # shorter
        b = str2 if len(str1) <= len(str2) else str1  # longer

        if self.canDivide(a, b): return a

        divisor = a[:-1]
        while len(divisor) > 0:
            print(divisor)
            if self.canDivide(divisor, a) and self.canDivide(divisor, b):
                return divisor
            divisor = divisor[:-1]
        return ""

    def canDivide(self, a, b):
        ori_a = a
        while len(a) < len(b):
            a += ori_a
        return a == b