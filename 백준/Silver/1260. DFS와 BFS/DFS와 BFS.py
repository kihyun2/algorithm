from collections import deque
def dfs(v):
    visited[v]=True
    node.append(v)
    for i in graph[v]:
        if not visited[i]:
            dfs(i)
def bfs(v):
    visited[v]=True
    que = deque([v])
    while que:
        v=que.popleft()
        node.append(v)
        for i in graph[v]:
            if not visited[i]:
                visited[i]=True
                que.append(i)

N, M, V=map(int,input().split())
graph=[[] for _ in range(N+1)]
node=[]
for _ in range(M):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

for sor in graph:
    sor.sort()

visited=[False for _ in range(N+1)]
dfs(V)
print(*node)
node.clear()

visited=[False for _ in range(N+1)]
bfs(V)
print(*node)