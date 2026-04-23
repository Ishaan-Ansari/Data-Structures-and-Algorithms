class Solution:
    def dfs(self, grid, i, j, m, n):
        if i<0 or j<0 or i>=m or j>=n or grid[i][j]=='0':
            return

        grid[i][j] = '0'
        self.dfs(grid, i+1, j, m, n)
        self.dfs(grid, i-1, j, m, n)
        self.dfs(grid, i, j+1, m, n)
        self.dfs(grid, i, j-1, m, n)


    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        cnt = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    cnt += 1
                    self.dfs(grid, i, j, m, n)


        return cnt


