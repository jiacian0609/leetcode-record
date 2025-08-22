class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        i = 0
        while i < len(s):
            if s[i] != '*':
                stack.append(s[i])
            else:
                stack.pop()
            i += 1
        return ''.join(stack)