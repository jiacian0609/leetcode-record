class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.split(" ")
        for w in s[::-1]:
            if w != '':
                return len(w)