class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        if len(points) == 0:
            return 0
        
        n = len(points)
        res = 0
        visited = [False] * n
        min_dist = [10**8] * n
        min_dist[0] = 0
        
        for _ in range(n):
            curr = -1
            for i in range(n):
                if not visited[i] and (curr == -1 or min_dist[i] < min_dist[curr]):
                    curr = i
            
            visited[curr] = True
            res += min_dist[curr]
            
            # Update distances for remaining points
            for j in range(n):
                if not visited[j]:
                    dist = abs(points[curr][0] - points[j][0]) + abs(points[curr][1] - points[j][1])
                    min_dist[j] = min(min_dist[j], dist)
        
        return res
