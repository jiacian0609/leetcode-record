class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for ch in s:
            if ch != ']':
                stack.append(ch)
            else:
                cur = stack.pop()
                temp = []
                while cur != '[':
                    temp.append(cur)
                    cur = stack.pop()
                word = ''.join(temp[::-1])

                temp = []
                while stack and stack[-1].isdigit():
                    cur = stack.pop()
                    temp.append(cur)
                num = int(''.join(temp[::-1]))

                stack.append(word * num)
        return ''.join(stack) 