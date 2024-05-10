T = int(input())

for tc in range(1, T + 1):
    result = []
    N = int(input())
    P = list(map(int, input().split()))
    while len(result) < N:
        val = P.pop(0)
        result.append(val)
        regular = int(val/ 0.75)
        P.remove(regular)

    print(f'#{tc} ',end='')
    print(*result, sep=' ')