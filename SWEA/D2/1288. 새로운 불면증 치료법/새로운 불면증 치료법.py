T = int(input())

for tc in range(1, T+1):
    N = int(input())
    lst = [0 for _ in range(10)]
    cnt = 1
    A = N
    while 1:
        strN = str(N)

        for i in range(len(strN)):
            lst[int(strN[i])] = 1

        if sum(lst) == 10:
            print(f'#{tc} {N}')
            break

        cnt += 1
        N = cnt * A
    