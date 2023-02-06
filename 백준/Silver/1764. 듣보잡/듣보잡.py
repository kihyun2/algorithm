N,M=map(int,input().split())
dt=set()
dtbo=set()
for _ in range(N):
    dt.add(input())
for _ in range(M):
    tmp=input()
    if tmp in dt:
        dtbo.add(tmp)

dtbo=list(dtbo)
dtbo.sort()
print(len(dtbo))
for dtbo in dtbo:
    print(dtbo)