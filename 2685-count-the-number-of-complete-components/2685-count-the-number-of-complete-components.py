from collections import defaultdict, deque

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        lst = defaultdict(list)
        for u, v in edges:
            lst[u].append(v)
            lst[v].append(u)

        visited = [0]*n

        components = 0

        for i in range(n):
            if not visited[i]:
                q = deque()
                q.append(i)
                visited[i] = 1

                comp_nodes = [i]

                while q:
                    node = q.popleft()

                    for neighbor in lst[node]:
                        if not visited[neighbor]:
                            visited[neighbor] = 1
                            q.append(neighbor)
                            comp_nodes.append(neighbor)

                size = len(comp_nodes)
                is_complete = True
                for node in comp_nodes:
                    if len(lst[node])!=size-1:
                        is_complete = False
                        break

                if is_complete:
                    components += 1
                        
        return components
