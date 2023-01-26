N=int(input())
graph=list()
for _ in range(N):
    x,y=map(int, input().split())
    graph.append([y,x])

graph=sorted(graph)

for i in graph:
    print(*[i[1],i[0]])