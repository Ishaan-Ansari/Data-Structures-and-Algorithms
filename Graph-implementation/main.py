"""
Adjacency list & matrix implementation
"""

from collections import defaultdict
edges = [[1,2], [2,3], [3,4], [4,2], [1,3]]

N = 4

adj_lst = defaultdict(list)

for u, v in edges:
    adj_lst[u].append(v)
    adj_lst[v].append(u)
    
# Adjecency list
print(dict(adj_lst))

mat = [[0 for _ in range(N)] for _ in range(N)]

for u, v in edges:
    # print(edge)
    u -= 1
    v -= 1
    mat[u][v] = 1
    mat[v][u] = 1

# Adjacency matrix
print(mat)
