N, M = map(int, input().split())
lst = list(map(int, input().split()))
rn = (len(lst) - 3) + 1
result = 0
for f in range(rn):
    for m in range(f+1, rn + 1):
        for r in range(m+1, rn + 2):
            tmp = lst[f] + lst[m] + lst[r]
            if tmp > result and tmp <= M:
                result = tmp
print(result)