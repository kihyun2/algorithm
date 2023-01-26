N=int(input())
graph=list()
for _ in range(N):
    graph.append(list(map(int, input().split())))

graph=sorted(graph)

for i in graph:
    for a in i:
        print(a,end=' ')
    print('')