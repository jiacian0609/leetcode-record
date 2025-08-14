class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        for i in s:
            # print(i)
            if i in t:
                t = t.replace(i, "", 1)
            else: return False
            # print(t)
        if len(t) != 0:
            return False
        else: return True