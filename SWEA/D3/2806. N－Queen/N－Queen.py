T = int(input())

def dfs(n):
    global result
    if n == N:
        result += 1
        return
    for i in range(N):
        if colCheck[i] == xpyCheck[n+i] == xmyCheck[n-i] == 0:
            colCheck[i] = xpyCheck[n+i] = xmyCheck[n-i] = 1
            # print('\n',colCheck)
            dfs(n+1)
            colCheck[i] = xpyCheck[n+i] = xmyCheck[n-i] = 0


for tc in range(1, T+1):

    N = int(input())
    board = [[0 for _ in range(N)] for _ in range(N)]
    result = 0
    
    colCheck = [0 for _ in range(N)]
    xpyCheck = [0 for _ in range((N*2)-1)]
    xmyCheck = [0 for _ in range((N*2)-1)]

    dfs(0)

    print(f'#{tc} {result}')