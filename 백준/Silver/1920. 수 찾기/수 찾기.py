N=int(input())
data=list(map(int,input().split()))
M=int(input())
search=list(map(int,input().split()))


data.sort()


for target in search:
    exist=False
    low=0
    high=len(data)-1
    while low<=high:
        mid=(low+high)//2
        if data[mid]==target:
            exist=True
            break
        elif data[mid]>target:
            high=mid-1
        elif data[mid]<target:
            low=mid+1

    if exist:
        print(1)
    else:
        print(0)


