T = int(input())

for tc in range(1, T+1):
    N = int(input())
    a = [list(map(int, input())) for _ in range(N)]
    ans = 0  # output 변수

    # s: 시작포인트, e: 끝포인트
    s, e = N // 2, N // 2
    for i in range(N):
        for j in range(s, e+1):
            ans += a[i][j]
        # 행의 인덱스가 mid 전까지는 s-e 간격 늘리고 mid 이후로는 간격 줄임
        if i < N // 2:
            s -= 1
            e += 1
        else:
            s += 1
            e -= 1

    print("#{} {}".format(tc, ans))