T = int(input())
for test_case in range(1, T + 1):

    N,M = map(int, input().split())
    lst = list()
    for _ in range(N):
        lst.append(list(map(int, input().split())))

    result = list()
    for lr in range(N-M+1):
        for lc in range(N-M+1):
            tmp = 0
            for sr in range(M):
                for sc in range(M):
                    tmp += lst[lr+sr][lc+sc]
            result.append(tmp)

    print(f"#{test_case} {max(result)}")