T = int(input())
for test_case in range(1, T + 1):
    N,Q=map(int,input().split())
    boxes=[0 for _ in range(N)]
    for i in range(1,Q+1):
        Li, Ri=map(int, input().split())
        for idx in range(Li-1,Ri):
            boxes[idx]=i
        

    print(f"#{test_case}",end=' ')
    print(*boxes)