
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for tc in range(1, T + 1):
    # 입력단
    N = int(input())
    farm = [[] for i in range(N)]
    for row in range(N):
        tmp = input()
        for idx in range(N):
            farm[row].append(int(tmp[idx]))
    
    # 사용할 변수 선언
    half = N//2
    result = 0
    opposite = half

    # 마름모 참조
    for row in range(0,N):
        
        if row <= half:
            result += sum(farm[row][half-row:half+row+1])
        
        if row > half:
            opposite -= 1
            result += sum(farm[row][half-opposite:half+opposite+1])

    
    print(f"#{tc} {result}")

