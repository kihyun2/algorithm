N=int(input())

inp=[]

for _ in range(N):
    inp.append(int(input()))

men=round(sum(inp)/N)  # 산술평균값
inp.sort()
med=(inp[N//2])        # 중앙값
ext=abs(inp[-1]-inp[0])# 범위


tmp={}
for i in inp:
    i=str(i)
    if i not in tmp:
        tmp[i]=0
    else:
        tmp[i]+=1

mde=max(tmp.values()) # 최빈값
what=[k for k, v in tmp.items() if v == mde]
if len(what)>1:
    mde=what[1]
else:
    mde=what[0]

print(men)
print(med)
print(mde)
print(ext)