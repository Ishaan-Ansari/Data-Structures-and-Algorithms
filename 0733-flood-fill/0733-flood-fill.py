class Solution:
    def dfs(self, grid, i, j, m, n, original_color, color):
        if i<0 or j<0 or i>=m or j>=n or grid[i][j]!=original_color:
            return

        grid[i][j] = color
        self.dfs(grid, i+1, j, m, n, original_color, color)
        self.dfs(grid, i-1, j, m, n, original_color, color)
        self.dfs(grid, i, j+1, m, n, original_color, color)
        self.dfs(grid, i, j-1, m, n, original_color, color)

    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m = len(image)
        n = len(image[0])

        original_color = image[sr][sc]
        if original_color != color:
            self.dfs(image, sr, sc, m, n, original_color, color)

        return image