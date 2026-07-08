from collections import defaultdict, deque

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        # 1. Create a adjecency list
        adj_lst = defaultdict(list)
        for u, v in edges:
            adj_lst[u].append(v)
            adj_lst[v].append(u)

        visited = [0]*n
        q = deque([source])

        while q:
            node = q.popleft()
            if node == destination:
                return True

            if not visited[node]:
                visited[node] = 1
                for neighbor in adj_lst[node]:
                    if not visited[neighbor]:
                        q.append(neighbor)
                    
        return False
