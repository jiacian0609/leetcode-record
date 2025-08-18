class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
    
        m, n = len(board), len(board[0])
        visited = set()
        directions = [(1,0), (-1,0), (0,1), (0,-1)]  # 下、上、右、左

        def dfs(x, y, idx):
            if idx == len(word):
                return True

            if not (0 <= x < m) or not (0 <= y < n) or (x, y) in visited or board[x][y] != word[idx]:
                return False
            
            visited.add((x, y))

            found = False
            for dx, dy in directions:
                if dfs(x + dx, y + dy, idx + 1):
                    found = True
                    break

            visited.remove((x, y))
            return found
             
        # 預檢查：如果字母數量不符合，直接 False
        char_count = {}
        for ch in word:
            char_count[ch] = 1 + char_count.get(ch, 0)
        
        if char_count[word[0]] > char_count[word[-1]]:
            word = word[::-1]
        
        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True
        
        return False