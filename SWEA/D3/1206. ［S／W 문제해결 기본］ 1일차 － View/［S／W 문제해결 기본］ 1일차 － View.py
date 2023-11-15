for tc in range(1, 11):
    N = int(input())
    lst  = list(map(int, input().split()))
    result = 0

    for idx in range(2, N-2):
        maximum = max(lst[idx-2],lst[idx-1],lst[idx+1],lst[idx+2])
        if (lst[idx] - maximum) > 0:
            result += lst[idx] - maximum

    print(f'#{tc} {result}')