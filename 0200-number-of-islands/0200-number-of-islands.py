class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        M, N = len(grid), len(grid[0])
        num_of_islands = 0

        directions=[(1,0), (0, 1), (0, -1), (-1, 0)]

        for i in range(M):
            for j in range(N):
                if grid[i][j]=='1':
                    num_of_islands += 1
                    q = deque()
                    q.append((i, j))
                    grid[i][j] = '0'

                    while q:
                        R, C = q.popleft()
                        for dr, dc in directions:
                            new_r, new_c = R+dr, C+dc
                            if 0 <= new_r < M and 0 <= new_c < N:
                                if grid[new_r][new_c]=='1':
                                    grid[new_r][new_c]='0'
                                    q.append((new_r, new_c))


        return num_of_islands
