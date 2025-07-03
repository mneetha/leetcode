#Array of edges (directed) [Start End]
n=8
A=[[0,1], [1,2], [0,3], [3,4], [3,6],[3,7], [4,2],[4,5], [5,2]]

#convert array of edges -> adjacency matrix
M=[]
for i in range(n):
    M.append([0]*n)

for u, v in A:

    M[u][v] = 1
    print(f'M[{u}][{v}] = {M[u][v]}')

print(M)

#convert array of edges -> adjacency list
from collections import defaultdict

D = defaultdict(list)
print(D)
for u,v in A:
    D[u].append(v)

print(D)

print(D[3])


#DFS with recursion - O(V + E) where V is the number of nodes and E is the number
#of edges

source = 0
seen = set()
seen.add(source)

def dfs_recursive(node):
    print(node)
    print(D[node])
    for nei_node in D[node]:
        if nei_node not in seen:
            seen.add(nei_node)
            dfs_recursive(nei_node)

dfs_recursive(source)

# Iterative DFS with Stack - O(V+E)

source = 0
seen = set()
