T = int(input())

def checkrook(chess, r, c):
    for i in range(1, 8):
        if r+i < 8:
            if chess[r+i][c] == 'O':
                return 'no'
        if r-i > -1:
            if chess[r-i][c] == 'O':
                return 'no'
        if c+i < 8:
            if chess[r][c+i] == 'O':
                return 'no'
        if c-i > -1:
            if chess[r][c-i] == 'O':
                return 'no'
    return 'yes'

for tc in range(1, T + 1):
    result = ''
    chess = []
    for i in range(8):
        chess.append(list(input()))
    cnt = 0
    for idxr, row in enumerate(chess):
        if result == 'no': break
        for idxc, col in enumerate(row):
            if col == 'O':
                cnt += 1
                result = checkrook(chess, idxr, idxc)
    if cnt >= 8:
        print(f'#{tc} {result}')
    else:
        print(f'#{tc} no')
