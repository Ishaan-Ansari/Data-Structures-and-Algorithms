from collections import defaultdict, deque

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adj_lst = defaultdict(list)

        # create a adjacency list
        for u, v in edges:
            adj_lst[u].append(v)
            adj_lst[v].append(u)


        q = deque([source])
        visited = set([source])

        while q:
            node = q.popleft()

            if node == destination:
                return True

            for neighbor in adj_lst[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    q.append(neighbor)

        
        return False

