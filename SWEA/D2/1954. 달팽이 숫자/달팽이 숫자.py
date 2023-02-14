T = int(input())

# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    snail = [[0 for _ in range(N)] for _ in range(N)]
    direction = [
        [0, 1],
        [1, 0],
        [0, -1],
        [-1, 0]
    ]
    state = 0
    x = 0
    y = 0
    for cnt in range(1, N*N+1):
        state %= 4
        snail[y][x] = cnt
        x += direction[state][1]
        y += direction[state][0]

        if x<0 or y<0 or x>N-1 or y>N-1 or snail[y][x]:
            x -= direction[state][1]
            y -= direction[state][0]
            state = (state + 1) % 4
            x += direction[state][1]
            y += direction[state][0]





    print(f'#{test_case}')
    for jjindk in snail:
        print(*jjindk)