N=int(input())
lst=list()
a=0
for _ in range(N):
    lst.append(int(input()))
    if lst[a]==0:
        del lst[a]
        del lst[a-1]
        a-=1
    else:
        a+=1

print(sum(lst))



