class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        M, N = len(grid), len(grid[0])
        num_of_islands = 0
        visited = set() # <-- NEW: Track seen cells here
        directions=[(1,0), (0, 1), (0, -1), (-1, 0)]

        # for i in range(M):
        #     for j in range(N):
        #         if grid[i][j]=='1':
        #             num_of_islands += 1
        #             q = deque()
        #             q.append((i, j))
        #             grid[i][j] = '0'

        #             while q:
        #                 R, C = q.popleft()
        #                 for dr, dc in directions:
        #                     new_r, new_c = R+dr, C+dc
        #                     if 0 <= new_r < M and 0 <= new_c < N:
        #                         if grid[new_r][new_c]=='1':
        #                             grid[new_r][new_c]='0'
        #                             q.append((new_r, new_c))

        # NOTE 1: - When you do grid[i][j] = '0', you are actively destroying the original data that was passed into your function.

        # NOTE 2: - To make this safe for production, we treat the grid as read-only.

        for i in range(M):
            for j in range(N):
                if grid[i][j]=='1' and (i, j) not in visited:
                    num_of_islands += 1
                    q = deque([(i, j)])
                    visited.add((i, j))

                    while q:
                        R, C = q.popleft()
                        for dr, dc in directions:
                            new_r, new_c = R+dr, C+dc
                            if 0 <= new_r < M and 0 <= new_c < N:
                                if grid[new_r][new_c]=='1' and (new_r, new_c) not in visited:
                                    visited.add((new_r, new_c))
                                    q.append((new_r, new_c))
        return num_of_islands
