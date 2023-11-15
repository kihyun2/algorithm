T = int(input())

for tc in range(1, T+1):
    lst = [list(map(int,input().split())) for _ in range(9)]
    
    # 가로 확인
    rowCheck = True
    for row in lst:
        if len(set(row)) != 9:
            rowCheck = False
    
    # 세로 확인
    colCheck = True
    for col in range(9):
        tmp = set()
        for row in range(9):
            tmp.add(lst[row][col])
        if len(tmp) != 9:
            colCheck = False
    # 박스 확인
    boxCheck = True
    for r_step in range(0, 9, 3):
        for c_step in range(0, 9, 3):
            tmp = set()
            for row in range(3):
                for col in range(3):
                    tmp.add(lst[row][col])
            if len(tmp) != 9:
                boxCheck = False
    
    if rowCheck and colCheck and boxCheck:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')
        
