N = int(input())
lst = list(map(int, input().split()))
mxscore = max(lst)
for i in range(len(lst)):
    lst[i] = lst[i] / mxscore * 100
print(sum(lst)/len(lst))