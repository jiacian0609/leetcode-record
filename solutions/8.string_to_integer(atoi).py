class Solution:
    def myAtoi(self, s: str) -> int:
        sign = None
        ans = ""
        for ch in s:
            if len(ans) == 0 and ch == ' ' and sign is None: continue
            elif len(ans) == 0 and sign is None and (ch == '+' or ch == '-'):
                sign = ch
            elif not ch.isdigit():
                break
            else:
                ans += ch

        ans = int(ans) if len(ans) > 0 else 0
        if sign is not None and sign == '-': ans *= -1

        # rounding
        if ans < -2 ** 31: ans = -2 ** 31
        elif ans > 2 ** 31 - 1: ans = 2 ** 31 - 1
        
        return ans