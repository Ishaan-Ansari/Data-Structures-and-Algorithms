class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])

        q = deque()

        # STEP 1: Find all boundary land cells and queue them up
        for i in range(M):
            for j in range(N):
                if (grid[i][j]==1 and (i==0 or i==M-1 or j==0 or j==N-1)):
                    q.append((i,j))
                    grid[i][j]=0

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        # STEP 2: Flood inward from the boundaries using BFS
        while q:
            r, c = q.popleft()
            for dr, dc in directions:
                new_r = r + dr
                new_c = c + dc

                if 0<=new_r<M and 0<=new_c<N and grid[new_r][new_c]==1:
                    grid[new_r][new_c]=0
                    q.append((new_r, new_c))

        # STEP 3: Count the surviving enclaves
        ans = 0
        for i in range(M):
            for j in range(N):
                if (grid[i][j]==1):
                    ans += 1

        return ans


