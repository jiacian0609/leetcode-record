class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0

        longest = 1
        start, end = 0, 1

        words = {s[start]}
        while start < len(s) and end < len(s):
            if s[end] not in words:
                words.add(s[end])
                if end - start + 1 > longest:
                    print((start, end))
                    longest = end - start + 1
                end += 1
            else:
                start += 1
                end = start + 1
                words = {s[start]}
        
        return longest