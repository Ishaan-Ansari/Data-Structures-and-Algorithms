class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        N = len(graph)
        visited = [0]*N

        for i in range(N):
            if visited[i]==0:
                q = deque([i])
                visited[i] = 1

                while q:
                    node = q.popleft()
                    
                    for neighbor in graph[node]:
                        if visited[neighbor] == 0:
                            visited[neighbor] = -visited[node]
                            q.append(neighbor)

                        elif visited[neighbor] == visited[node]:
                            return False


        return True

            


        
        