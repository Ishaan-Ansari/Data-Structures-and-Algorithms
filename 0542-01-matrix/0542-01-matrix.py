class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        M = len(mat)
        N = len(mat[0])

        ans = [[float('inf') for _ in range(N)] for _ in range(M)]

        q = deque()

        for i in range(M):
            for j in range(N):
                if mat[i][j]==0:
                    ans[i][j] = 0
                    q.append((i,j))
                
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while q:
            r, c = q.popleft()
            for dr, dc in directions:
                new_r = r + dr
                new_c = c + dc

                if 0 <= new_r < M and 0 <= new_c < N:
                    if ans[r][c] + 1 < ans[new_r][new_c]:
                        ans[new_r][new_c] = ans[r][c] + 1
                        q.append((new_r, new_c))

        return ans