T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    distance = 0
    speed = 0
    N=int(input())
    for _ in range(N):
        command = list(map(int,input().split()))
        if len(command) > 1:
            if command[0] == 1:
                speed += command[1]
            if command[0] == 2:
                speed -= command[1]
            if speed < 0:
                speed = 0
            distance += speed
        else:
            distance += speed
    print(f'#{test_case} {distance}')