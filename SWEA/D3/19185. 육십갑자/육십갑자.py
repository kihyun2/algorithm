T = int(input())

for tc in range(1, T + 1):
    result = []
    N, M = map(int, input().split())
    gan = list(map(str, input().split()))
    jisin = list(map(str, input().split()))
    q = int(input())
    for _ in range(q):
        year = int(input())
        result.append(gan[(year-1)%N]+jisin[(year-1)%M])

    print(f'#{tc} {" ".join(result)}')