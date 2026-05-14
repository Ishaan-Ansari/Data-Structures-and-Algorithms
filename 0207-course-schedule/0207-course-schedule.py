class Solution:
    def dfs(self, adj, visited, current_course):
        if visited[current_course] == 1: return True
        if visited[current_course] == 2: return False

        visited[current_course] = 1

        for course in adj[current_course]:
            if self.dfs(adj, visited, course):
                return True

        visited[current_course] = 2

        return False

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for _ in range(numCourses)]

        for u,v in prerequisites:
            adj[u].append(v)

        visited = [0]*numCourses

        for idx in range(numCourses):
            if visited[idx]==0:
                if self.dfs(adj, visited, idx):
                    return False
        return True
