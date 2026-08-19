import heapq 

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows, col = len(heights), len(heights[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

		# min-heap stores tuples of (current_max_effort, row, col)
        min_heap = [(0, 0, 0)]

        # Track min effort to reach each cell
        effort_to = [[float('inf')]*col for _ in range(rows)]
        effort_to[0][0] = 0

        while min_heap:
            effort, r, c = heapq.heappop(min_heap)

            if r == rows-1 and c == col-1:
                return effort

			# we've already found a better path to this cell already, we can skip
            if effort > effort_to[r][c]:
                continue

            for dr, dc in directions:
                nr, nc = r+dr, c+dc

                if 0 <= nr < rows and 0<= nc < col:
                    current_step_effort = abs(heights[r][c] - heights[nr][nc])
                    new_max_effort = max(effort, current_step_effort)

                    if new_max_effort < effort_to[nr][nc]:
                        effort_to[nr][nc] = new_max_effort
                        heapq.heappush(min_heap, (new_max_effort, nr, nc))


        return 0
