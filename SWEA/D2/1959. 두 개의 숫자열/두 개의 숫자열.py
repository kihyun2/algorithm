T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    lst = []
    result = 0


    if N > M:
        longN = A
        shortN = B
    else:
        longN = B
        shortN = A

    for start in range(len(longN)-len(shortN)+1):
        tmp = 0
        for i in range(len(shortN)):
            tmp += longN[start+i]*shortN[i]
        lst.append(tmp)

    for i in lst:
        if result < i:
            result = i
            
    print(f'#{tc} {result}')