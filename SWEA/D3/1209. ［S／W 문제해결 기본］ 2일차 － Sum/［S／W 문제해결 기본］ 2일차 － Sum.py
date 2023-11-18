T = 10

for tc in range(1, T+1):
    lst = int(input())
    lst = []
    for _ in range(100):
        lst.append(list(map(int,input().split())))
    result = [0, 0, 0] #[0]: 열, 행의 합 중 큰 것 [1]:x-y = 0번 대각선의 합 [2]: x+y = 99번 대각선의 합
    digonal = []
    for i in range(100):
        h_sum, w_sum = 0,0 
        for j in range(100):
            h_sum += lst[j][i] #열 합
            w_sum += lst[i][j]
            if (j-i) == 0:
                result[1] += lst[j][i]
            elif (j+i) == 99:
                result[2] += lst[j][i]
        tmp = max(h_sum, w_sum)
        if tmp > result[0]:
            result[0] = tmp

    print(f'#{tc} {max(result)}')