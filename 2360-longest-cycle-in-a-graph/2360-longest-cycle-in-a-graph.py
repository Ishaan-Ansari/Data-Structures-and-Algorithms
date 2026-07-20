class Solution:
    def __init__(self):
        self.max_cycle = -1

    def _dfs(self, node, edges, visited, in_path, dist):
        if not visited[node]:
            visited[node] = 1
            in_path[node] = dist
            dist += 1

            neighbor = edges[node]
            if neighbor != -1:
                if not visited[neighbor]:
                    self._dfs(neighbor, edges, visited, in_path, dist)

                elif in_path[neighbor]:
                    current_dist = dist-in_path[neighbor]
                    self.max_cycle = max(self.max_cycle, current_dist)
            
            in_path[node] = 0
            dist = 0

    def longestCycle(self, edges: List[int]) -> int:
        N = len(edges)
        visited = [0]*N
        in_path = [0]*N

        for i in range(N):
            if not visited[i]:
                self._dfs(i, edges, visited, in_path, 1)

        return self.max_cycle
        