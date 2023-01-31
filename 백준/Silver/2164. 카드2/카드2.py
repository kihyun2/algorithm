from collections import deque

N=int(input())
graph=deque()
for i in range(1,N+1):
    graph.append(i)



while len(graph)>1:
    del graph[0]
    a=graph.popleft()
    graph.append(a)

a=graph.popleft()
print(a)
