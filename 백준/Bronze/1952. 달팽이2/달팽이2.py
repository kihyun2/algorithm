M , N = map(int, input().split())

lst = [[False for _ in range(N)] for _ in range(M)]
lst[0][0] = True
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


cnt = 0
i = 0
nr, nc = 0,0
for _ in range(M*N - 1):
    nr += dr[i%4]
    nc += dc[i%4]   
    if nr >= M or nr < 0 or nc >= N or nc < 0:
        nr -= dr[i%4]
        nc -= dc[i%4]
        i += 1
        nr += dr[i%4]
        nc += dc[i%4]  
    else:
        if lst[nr][nc]:
            nr -= dr[i%4]
            nc -= dc[i%4]
            i += 1
            nr += dr[i%4]
            nc += dc[i%4]  
    lst[nr][nc] = True
        
    

        


print(i)