class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for e in s:
            if e == "(" or e == "[" or e == "{":
                stack.append(e)
            elif (len(stack) == 0
                or (e == ")" and stack.pop() != "(")
                or (e == "]" and stack.pop() != "[")
                or (e == "}" and stack.pop() != "{")):
                return False

        if len(stack) == 0:
            return True
        else: return False
        