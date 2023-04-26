T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    
    N, M = map(int,input().split())
    fly = list()
    for _ in range(N):
        fly.append(list(map(int,input().split())))
    dead = list()
    for col in range(N-(M-1)):
        for row in range(N-(M-1)):
            tmp = 0
            for c in range(M):
                for r in range(M):
                    tmp += fly[col+c][row+r]
            dead.append(tmp)
    print(f"#{test_case} {max(dead)}")