class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        answer = [0] * n
        stack = []
        for i, temp in enumerate(temperatures):
            if i == 0 or temp <= stack[-1][1]:
                stack.append((i, temp))
                continue
            
            while stack:
                idx, prev = stack.pop()
                answer[idx] = i - idx
                
                if not stack or stack[-1][1] >= temp:
                    break
            stack.append((i, temp))
        return answer