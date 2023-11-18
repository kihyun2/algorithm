T = 10
for tc in range(1, T+1):
    N = int(input())
    lst = []
    deadlock = 0

    for _ in range(N):
        lst.append(input().split())
    
    for i in range(N):
        metOne = False
        for j in range(N):
            if lst[j][i] == '1':
                metOne = True
            if metOne and lst[j][i] == '2':
                deadlock += 1
                metOne = False
    
    print(f'#{tc} {deadlock}')
                