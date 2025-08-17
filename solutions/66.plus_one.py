class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = digits[::-1]
        digits[0] += 1

        i = 0
        while i < len(digits):
            if digits[i] >= 10:
                add = digits[i] // 10
                digits[i] = digits[i] % 10
                if i == len(digits) - 1:
                    digits.append(add)
                else:
                    digits[i + 1] += add
            i += 1
        return digits[::-1]