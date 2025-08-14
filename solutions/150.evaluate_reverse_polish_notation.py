class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t in "+-*/":
                r = stack.pop()
                l = stack.pop()

                new_num = 0
                if t == "+":
                    new_num = l + r
                elif t == "-":
                    new_num = l - r
                elif t == "*":
                    new_num = l * r
                else:
                    new_num = int(l / r)
                # print(new_num)
                stack.append(new_num)
            else:
                stack.append(int(t))
        return stack[0]