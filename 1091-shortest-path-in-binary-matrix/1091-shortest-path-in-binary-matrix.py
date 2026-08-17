from collections import deque

class Solution:
    def isValid(self, row, col, m, n, mat, visited):

        return row >= 0 and row < m and \
            col >= 0 and col < n and \
            mat[row][col] != 1 and \
            not visited[row][col]

    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1

        m, n = len(grid), len(grid[0])

        visited = [[False for _ in range(n)] for _ in range(m)]

        q = deque()
        q.append([0, 0, 1])
        visited[0][0] = True

        # Direction vectors for moving: up, down, left, right, topleft, topright, bottomright, bottomleft
        dRow = [-1, 1, 0, 0, -1, 1, 1, -1]
        dCol = [0, 0, -1, 1, 1, 1, -1, -1]

        while q:
            curr = q.popleft()

            row, col, dist = curr[0], curr[1], curr[2]

            if row == m-1 and col == n-1:
                return dist

            for i in range(8):
                newRow = row + dRow[i]
                newCol = col + dCol[i]

                if self.isValid(newRow, newCol, m, n, grid, visited):
                    visited[newRow][newCol] = True

                    q.append([newRow, newCol, dist+1])


        return -1




