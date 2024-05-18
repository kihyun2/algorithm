M , N = map(int, input().split())

lst = [[False for _ in range(N)] for _ in range(M)]
lst[0][0] = True
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


i = 0
r = c = 0
for _ in range(M*N - 1):
    nr = r + dr[i%4]
    nc = c + dc[i%4]   
    if nr >= M or nr < 0 or nc >= N or nc < 0 or lst[nr][nc]:
        i += 1
        nr = r + dr[i%4]
        nc = c + dc[i%4]   

    r, c = nr, nc
    lst[r][c] = True
        

print(i)