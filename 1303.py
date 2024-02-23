from collections import deque
def bfs(graph, startnode, visited):
    bfslist = []
    queue = deque([startnode])
    visited[startnode[0]][startnode[1]] = True
    dirlist = [(0,1), (1,0), (-1,0), (0,-1)]
    
    while queue:
        v = queue.popleft()
        bfslist.append(v)
        for dir in dirlist:
            if 0 <= v[0] + dir[0] <= len(graph)-1 and 0 <= v[1] + dir[1] <= len(graph[0]) - 1:
                if (not visited[v[0] + dir[0]][v[1] + dir[1]]) and graph[v[0]][v[1]] == graph[v[0] + dir[0]][v[1] + dir[1]]:
                    queue.append([v[0] + dir[0],v[1] + dir[1]])
                    visited[v[0] + dir[0]][v[1] + dir[1]] = True
    return (len(bfslist), visited)
N, M = map(int, input().split())
graph = [[] * i for i in range(M)]
visited = [[False for _ in range(N)] for _ in range(M)]
for i in range(M):
    line = map(str, input())
    graph[i].extend(line)
answ = 0
ansb = 0    
for i in range(M):
    for j in range(N):
        if not visited[i][j]:
            if graph[i][j] == 'W':
                answ += (bfs(graph, [i,j], visited)[0] ** 2)
                visited = bfs(graph, [i,j], visited)[1]
            else:
                ansb += (bfs(graph, [i,j], visited)[0] ** 2)
                visited = bfs(graph, [i,j], visited)[1]    
print(answ, ansb)
