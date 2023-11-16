T = int(input())

def dfs(n):

    global result

    # 검문소에서 참만 걸려서 colCheck = [1,1,1,1]로 채우면 상으로 result ++ 해주고 내보냄
    if n == N:
        result += 1
        return
    
    for i in range(N):
        # 놓아도 되는 자리인지 체크
        if colCheck[i] == xpyCheck[n+i] == xmyCheck[n-i] == 0:
            colCheck[i] = xpyCheck[n+i] = xmyCheck[n-i] = 1 # 퀸 놓기
            dfs(n+1)    # 다음 행으로 넘어가서 놔도 되는 자리에 또 퀸 놓기
            
            # i range(N)만큼 도는 동안 검문소에서 참을 못 받아서 n == N 못 걸리고 끝나면 일로 옴
            colCheck[i] = xpyCheck[n+i] = xmyCheck[n-i] = 0 # 퀸 빼기


for tc in range(1, T+1):

    N = int(input())

    result = 0
    
    # 같은 열 확인
    colCheck = [0 for _ in range(N)]
    # 같은 대각선 선상에 있나 확인 (x plus y 번호의 대각선)
    xpyCheck = [0 for _ in range((N*2)-1)]
    # 같은 대각선 선상에 있나 확인 (x minus y 번호의 대각선)
    xmyCheck = [0 for _ in range((N*2)-1)]

    dfs(0)

    print(f'#{tc} {result}')