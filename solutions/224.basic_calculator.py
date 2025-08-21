class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        action = None
        for ch in s:
            if ch == ' ': continue
            
            if ch == ')':
                cur = stack.pop()
                temp = []
                while cur != '(':
                    temp.append(cur)
                    cur = stack.pop()
                stack.append(self.calculate(temp[::-1]))
            elif ch == '+' or ch == '-' or ch == '(':
                stack.append(ch)
            elif len(stack) == 0 or type(stack[-1]) != int:
                stack.append(int(ch))
            else:
                # print("merge", int(str(stack[-1]) + ch))
                stack[-1] = int(str(stack[-1]) + ch)
            # print(stack)

        if stack[0] == '-':
            stack[1] *= -1
            stack.pop(0)

        while len(stack) > 1:
            prev = stack.pop(0)
            action = stack.pop(0)
            cur = stack.pop(0)

            if action == '+':
                stack.insert(0, prev + cur)
            else:
                stack.insert(0, prev - cur)
            # print(stack)

        return stack[0]