def solution(t, p):
    
    tl,pl=len(t),len(p)
    ps=int(p)
    cnt=tl-pl+1
    result=0
    cnt2=0
    for i in range(0, tl-pl+1):
        if int(t[cnt2:pl+i:])<=int(p):
            result +=1
        cnt2+=1
    
    
    
    answer = result
    return answer