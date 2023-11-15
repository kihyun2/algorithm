T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    puzzle = [list(map(int, input().split())) for _ in range(N)]
    blank = []

    # 가로 카운트
    for row in puzzle:
        cnt = 0
        for ele in row:
            if ele == 1:
                cnt += 1
            else:
                if cnt > 1:
                    blank.append(cnt)
                cnt = 0
        if cnt > 1:
            blank.append(cnt)
    
    #세로 카운트
    for col in range(N):
        cnt = 0
        for row in range(N):
            if puzzle[row][col] == 1:
                cnt += 1
            else:
                if cnt > 1:
                    blank.append(cnt)
                cnt = 0
        if cnt > 1:
            blank.append(cnt)
    
    print(f'#{tc} {blank.count(K)}')