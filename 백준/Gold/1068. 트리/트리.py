
N=int(input())
tree=list(map(int,input().split()))
erase=int(input())
visited=[False]*N
visited[erase]=True
graph=[[] for _ in range(N)]

# 5
# -1 0 0 1 1
# 2
def dfs(erase,tree):
    tree[erase]=None
    for i in range(len(tree)):
        if erase==tree[i]:
            dfs(i,tree)


dfs(erase,tree)
cnt = 0
for i in range(len(tree)):
    if tree[i] is not None and i not in tree:
        cnt += 1
print(cnt)