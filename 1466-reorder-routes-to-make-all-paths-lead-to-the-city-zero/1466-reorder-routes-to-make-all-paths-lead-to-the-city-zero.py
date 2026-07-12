from collections import defaultdict

class Solution:
    def __init__(self):
        self.count = 0

    def _dfs(self, start_node, adj_lst, visited):
        if not visited[start_node]:
            visited[start_node] = 1
            for neighbor in adj_lst[start_node]:
                node, cost = neighbor
                if not visited[node]:
                    if cost == 1:
                        self.count += 1
                    self._dfs(node, adj_lst, visited)

    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        adj_lst = defaultdict(list)

        for u, v in connections:
            adj_lst[u].append((v, 1))
            adj_lst[v].append((u, 0))

        visited = [0]*n

        self._dfs(0, adj_lst, visited)

        return self.count

        