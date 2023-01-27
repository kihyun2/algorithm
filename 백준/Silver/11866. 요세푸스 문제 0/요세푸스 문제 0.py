N,K=map(int,input().split())
que=[]
result=[]
for i in range(1,N+1):
    que.append(i)
cnt=0
while True:
    for idx in range(len(que)):
        if que[idx]!=0:
            cnt+=1
        if cnt==K:
            result.append(que[idx])
            que[idx]=0
            cnt=0
        
    if que.count(0)>=N:
        break

print("<",end="")
for i in result:
    
    if i == result[-1]:
        print(i,end="")
    else:
        print(i,end=", ")

print(">")