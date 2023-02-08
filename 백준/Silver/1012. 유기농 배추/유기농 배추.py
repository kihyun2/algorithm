import sys
sys.setrecursionlimit(10000)


def dfs(x, y):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    # 상,하,좌,우 확인
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
    
        if (0 <= nx < N) and (0 <= ny < M):
            if matrix[nx][ny] == 1:
                matrix[nx][ny] = -1
                dfs(nx, ny)


T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    matrix = [[0]*M for _ in range(N)]
    cnt = 0

    # 행렬 생성
    for _ in range(K):
        m, n = map(int, input().split())
        matrix[n][m] = 1

    for i in range(N):  # 행 (바깥 리스트)
        for j in range(M):  # 열 (내부 리스트)
            if matrix[i][j] > 0:
                dfs(i, j)
                cnt += 1

    print(cnt)