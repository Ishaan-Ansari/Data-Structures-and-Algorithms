from collections import defaultdict

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # 1. create an adjecency list
        adj_lst = defaultdict(list)
        indegree = [0]*numCourses

        for u, v in prerequisites:
            adj_lst[v].append(u)
            # If indegree[X] == 0, it means course X has absolutely zero prerequisites. You can take it on day one.
            indegree[u] += 1

        node_with_no_incoming_edges = []
        for i in range(len(indegree)):
            if indegree[i] == 0:
                # we are actually storing course that have no prereq.
                node_with_no_incoming_edges.append(i)

        course_order = []
        while node_with_no_incoming_edges:
            current_course = node_with_no_incoming_edges.pop()
            course_order.append(current_course)

            for course in adj_lst[current_course]:
                indegree[course] -= 1

                if indegree[course] == 0:
                    node_with_no_incoming_edges.append(course)

        if len(course_order)==numCourses:
            return course_order

        return []         
