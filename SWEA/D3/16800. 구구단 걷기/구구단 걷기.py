t = int(input())

for tc in range(1, t+1):
    n = int(input())
    res = 0 
    res_list=[]

    for i in range(1, int(n**(1/2)) + 1):
        if n % i == 0:
            res = i-1 + n // i -1
            res_list.append(res)
            if ( i**2 != n ):
                res = i-1 + n // i -1
                res_list.append(res)
    print(f'#{tc} {min(res_list)}')