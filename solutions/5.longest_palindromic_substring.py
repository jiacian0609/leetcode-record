class Solution:
    def longestPalindrome(self, s: str) -> str:
        length = 1
        substr = s[0]

        i = 0
        j = i + length
        while i < len(s) and j < len(s):
            # print((i, j))
            cur = s[i:j+1]
            if self.isPalindrome(cur) and len(cur) > length:
                length = len(cur)
                substr = cur
            j += 1

            if j == len(s):
                i += 1
                j = i + length
        return substr

    def isPalindrome(self, s: str) -> bool:
        return s == s[::-1]