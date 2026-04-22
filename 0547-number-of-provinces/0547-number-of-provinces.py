class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = set()
        provinces = 0

        def dfs(city):
            for friend in range(n):
                if isConnected[city][friend] == 1 and friend not in visited:
                    visited.add(friend)
                    dfs(friend)


        for i in range(n):
            if i not in visited:
                provinces += 1
                visited.add(i)
                dfs(i)



        return provinces