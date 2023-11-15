T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    puzzle = [list(map(int, input().split())) for _ in range(N)]
    blank = []

    #가로 카운트
    for row in puzzle:
        tmp = 0
        cnt = 1
        for ele in row:
            if ele and tmp:
                cnt += 1
            elif ele == 0 and tmp:
                blank.append(cnt)
                cnt = 1
            tmp = ele
        if cnt > 1:
            blank.append(cnt)
    
    #세로 카운트
    for col in range(N):
        tmp = 0
        cnt = 1
        for row in range(N):
            if puzzle[row][col] and tmp:
                cnt += 1
            elif puzzle[row][col] == 0 and tmp:
                blank.append(cnt)
                cnt = 1
            tmp = puzzle[row][col]
        if cnt > 1:
            blank.append(cnt)

    print(f'#{tc} {blank.count(K)}')