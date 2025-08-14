class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        cur_color = image[sr][sc]
        if cur_color == color:
            return image

        image[sr][sc] = color
        
        # 上
        if sc - 1 >= 0 and image[sr][sc - 1] == cur_color:
            image = self.floodFill(image, sr, sc - 1, color)
            image[sr][sc - 1] = color
            print(sr, sc - 1)
        # 下
        if sc + 1 < len(image[0]) and image[sr][sc + 1] == cur_color:
            image = self.floodFill(image, sr, sc + 1, color)
            image[sr][sc + 1] = color
            print(sr, sc + 1)
        # 左
        if sr - 1 >= 0 and image[sr - 1][sc] == cur_color:
            image = self.floodFill(image, sr - 1, sc, color)
            image[sr - 1][sc] = color
            print(sr - 1, sc)
        # 右
        if sr + 1 < len(image) and image[sr + 1][sc] == cur_color:
            image = self.floodFill(image, sr + 1, sc, color)
            image[sr + 1][sc] = color
            print(sr + 1, sc)

        return image
        