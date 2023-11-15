T = int(input())

for tc in range(1, T+1):

    N = int(input())
    pascal = [[] for _ in range(N)]
    pascal[0].append(1)
    for i in range(1, N):
        pascal[i].append(pascal[i-1][0])
        for a in range(i-1):
            pascal[i].append(pascal[i-1][a]+pascal[i-1][a+1])
        pascal[i].append(pascal[i-1][-1])

    print(f'#{tc}')
    for row in pascal:
        print(*row)