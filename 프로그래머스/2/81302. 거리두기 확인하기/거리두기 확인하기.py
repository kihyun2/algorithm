def solution(places):
    answer=[]
    
    dcheck = [
        [1,0], # 아래 한 칸
        [2,0]  # 아래 두 칸
        
    ]
    rcheck = [
        [0,1], # 오른쪽 한 칸
        [0,2]  # 오른쪽 두 칸
    ]
    ldiacheck = [
        [0,-1],# 왼쪽 한 칸
        [1,0], # 아래쪽 한칸
        [1,-1] # 대각선 왼쪽 아래 한 칸
    ]
    rdiacheck = [
        [0,1], # 오른쪽 한 칸
        [1,0], # 아래쪽 한칸
        [1,1]  # 대각선 오른 아래 한 칸
    ]
    
    for place in places:
        no = 0
        for r in range(5):
            for c in range(5):
                if place[r][c] == 'P':
                    if no == 1:
                        break
                    partition = 0
                    for cr,cc in dcheck:
                        if r+cr >= 5 or c+cc >= 5 or c+cc < 0:
                            continue
                        tr, tc = r+cr, c+cc
                        if place[tr][tc] == 'X':
                            partition += 1
                        if place[tr][tc] == 'P' and partition == 0:
                            no = 1
                            break
                    partition = 0
                    for cr,cc in rcheck:
                        if r+cr >= 5 or c+cc >= 5 or c+cc < 0:
                            continue
                        tr, tc = r+cr, c+cc
                        if place[tr][tc] == 'X':
                            partition += 1
                        if place[tr][tc] == 'P' and partition == 0:
                            no = 1
                            break
                    partition = 0
                    for cr,cc in ldiacheck:
                        if r+cr >= 5 or c+cc >= 5 or c+cc < 0:
                            continue
                        tr, tc = r+cr, c+cc
                        if place[tr][tc] == 'X':
                            partition += 1
                        if place[tr][tc] == 'P' and partition < 2:
                            no = 1
                            break
                    partition = 0
                    for cr,cc in rdiacheck:
                        if r+cr >= 5 or c+cc >= 5 or c+cc < 0:
                            continue
                        tr, tc = r+cr, c+cc
                        if place[tr][tc] == 'X':
                            partition += 1
                        if place[tr][tc] == 'P' and partition < 2:
                            no = 1
                            break
            if no == 1:
                break
        if no == 1:
            answer.append(0)
        else:
            answer.append(1)
                        
                        
                            
    
    return answer