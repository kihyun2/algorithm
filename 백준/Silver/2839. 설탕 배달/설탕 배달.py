n=int(input())
cnt=0


if n%5==0:
    print(n//5)
    n=0
else:
    while n>0:
        n-=3
        cnt+=1
        if n%5==0:
            print((n//5) + cnt)
            break
        elif n<3 and n>0:
            print(-1)
            break
        elif n==0:
            print(cnt)
            break
        