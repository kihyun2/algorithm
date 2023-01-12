K,N=map(int,input().split())
lan=[]
for _ in range(K):
    lan.append(int(input()))

lan=sorted(lan)

lo=1
hi=lan[K-1]

while lo<=hi:
    cnt=0
    mid= (lo+hi)//2
    for dt in lan:
        cnt+=(dt//mid)
    # print(f'cnt={cnt}')
    # print(f'low={lo}')
    # print(f'mid={mid}')
    # print(f'high={hi}')
    if cnt>=N:
        lo=mid+1
    else:
        hi=mid-1


if N==1:
     lo=hi
print(hi)
