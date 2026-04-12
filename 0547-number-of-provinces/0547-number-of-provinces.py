class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = set()
        provinces = 0

        def dfs(node):
            for neighbor in range(n):
                if isConnected[node][neighbor] == 1 and neighbor not in visited:
                    visited.add(neighbor)
                    dfs(neighbor)


        for city in range(n):
            if city not in visited:
                provinces += 1
                visited.add(city)
                dfs(city)

        return provinces