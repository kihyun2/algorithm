N = int(input())
ncard = list(map(int, input().split()))
M = int(input())
mcard = list(map(int, input().split()))

cnt = {}
for a in ncard:
    if a in cnt:
        cnt[a] += 1
    else:
        cnt[a] = 1
for a in mcard:
    if a in cnt:
        print(cnt[a], end=' ')
    else:
        print(0, end=' ')

