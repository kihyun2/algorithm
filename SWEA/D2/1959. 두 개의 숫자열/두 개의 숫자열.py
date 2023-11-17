T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    result = 0


    if N > M:
        A, B = B, A

    for start in range(len(B)-len(A)+1):
        tmp = 0
        
        for i in range(len(A)):
            tmp += B[start+i]*A[i]
        
        if tmp > result:
            result = tmp

    print(f'#{tc} {result}')