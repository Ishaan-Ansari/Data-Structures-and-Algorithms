from collections import deque

class Solution:
    def topoSort(self, V, edges):
        # Step 1: Calculate the indegree of the node
        indegree = [0]*V
        for u, v in edges:
            indegree[v] += 1
            
        # Step 2: Add all the nodes with an indegree of 0 to a queue
        q = deque()
        
        for i in range(V):
            if indegree[i]==0:
                q.append(i)
                
        # Step 3: While the queue is not empty
        top_order = []
        
        while q:
            node = q.popleft()
            # Dequeue the first node from the queue and add it to the topological order.
            top_order.append(node)
            
            # For each neighbor of the node, decrement its indegree by 1. 
            for u, v in edges:
                # If the neighbor's indegree is now 0, add it to the queue.
                if u==node:
                    indegree[v] -= 1
                    
                if indegree[v] == 0:
                    q.append(v)
                    
        return top_order
