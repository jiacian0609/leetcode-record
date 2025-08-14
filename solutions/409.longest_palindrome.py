class Solution:
    def longestPalindrome(self, s: str) -> int:
        if len(s) <= 1: return len(s)
        words = set(s)
        # print(words)

        result = 0
        odd = False

        for w in words:
            count = s.count(w)
            # print(count)
            if count % 2 == 0:
                result += count
            else:
                result += count // 2 * 2
                odd = True
        
        if odd:
            result += 1

        return result
        