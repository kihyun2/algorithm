import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

n = int(input())

answer = 0
graph = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]
distance = [0 for _ in range(n+1)]
for i in range(n-1):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

def dfs(cur):
    visited[cur] = True
    for next in graph[cur]:
        if visited[next] == False:
        	# distance에는 루트노드부터 모든 노드까지에 거리를 갱신해준다.
            distance[next] = distance[cur] + 1 
            dfs(next)

dfs(1)

# 리프노드를 찾아줌
for i in range(2,n+1):
    if len(graph[i]) == 1:
        answer += distance[i]

if answer % 2 == 0:
    print("No")
else:
    print("Yes")