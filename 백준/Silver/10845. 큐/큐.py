N=int(input())
inp=list()
temp=list()
# 입력 받기
for i in range(N):
    temp.append(input().split())
    if temp[i][0] =='push':
        inp.append([temp[i][0],int(temp[i][1])])
    else:
        inp.append(list(temp[i]))
del temp

que=[]
for order in inp:
    #print(que)
    if 'push' in order:
        que.append(order[1])
    if 'pop' in order:
        if que:
            print(que[0])
            del que[0] 
        else:
            print(-1) 
    if 'size' in order:
        print(len(que))
    if 'empty' in order:
        print(0 if que else 1)
    if 'front' in order:
        print(que[0] if que else -1)
    if 'back' in order:
        print(que[-1] if que else -1)
        



