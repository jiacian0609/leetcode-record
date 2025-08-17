class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        if m == 1 and n == 1:
            return matrix[0]

        # 右下左上
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        dir_id = 0
        result = [matrix[0][0]]
        matrix[0][0] = float(inf)
        x, y = 0, 0

        while True:
            dx, dy = directions[dir_id]
            x += dx
            y += dy
            # print((dx, dy))
            while 0 <= x < m and 0 <= y < n and matrix[x][y] < float(inf):
                result.append(matrix[x][y])
                matrix[x][y] = float(inf)
                # print((x, y), result)
                x += dx
                y += dy
            x -= dx
            y -= dy
            dir_id += 1
            if dir_id == len(directions):
                dir_id = 0
            
            if len(result) == m * n:
                break
        
        return result