class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        sid = 0
        tid = 0
        while sid < len(s) and tid < len(t):
            if t[tid] != s[sid]:
                tid += 1
            else:
                sid += 1
                tid += 1
        if sid == len(s):
            return True
        else:
            return False