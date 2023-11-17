T = int(input())

for tc in range(1,T+1):
    N = int(input())
    board = []
    for _ in range(N):
        board.append(input().split())
    
    degree90 = [[0 for _ in range(N)] for _ in range(N)]
    degree180 = [[0 for _ in range(N)] for _ in range(N)]
    degree270 = [[0 for _ in range(N)] for _ in range(N)]

    for i in range(N):
        for j in range(N):
            degree90[j][N-1-i] = board[i][j]
    for i in range(N):
        for j in range(N):
            degree180[j][N-1-i] = degree90[i][j]
    for i in range(N):
        for j in range(N):
            degree270[j][N-1-i] = degree180[i][j]
    
    print(f'#{tc}')
    for row in range(N):
        rowStr = ''
        for i in range(N):
            rowStr += degree90[row][i]
        rowStr += ' '
        for i in range(N):
            rowStr += degree180[row][i]
        rowStr += ' '
        for i in range(N):
            rowStr += degree270[row][i]
        print(rowStr)
        
