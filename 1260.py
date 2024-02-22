def dfs(graph, startnode, visitied = []):
    visitied.append(startnode)
    
    for node in graph[startnode]:
        if node not in visitied:
            dfs(graph, node, visitied)
    return visitied
from collections import deque
def bfs(graph, startnode, visited):
    bfslist = []
    queue = deque([startnode])
    visited[startnode] = True
    while queue:
        v = queue.popleft()
        bfslist.append(v)
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
    return bfslist

n, m, v = map(int, input().split())
graph = {}
for i in range(1,n+1):
    graph[i] = []

for i in range(m):
    p1, p2 = map(int, input().split())
    graph[p1].append(p2) 
    graph[p2].append(p1)
for pi in graph:
    graph[pi] = sorted(graph[pi])
visited = [False * i for i in range(n+1)]
anslist = []
anslist.append(dfs(graph,v))
anslist.append(bfs(graph,v,visited))
for ans in anslist:
    result = " ".join(map(str,ans))
    print(result)
