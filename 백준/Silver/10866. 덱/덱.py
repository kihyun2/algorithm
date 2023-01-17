N=int(input())
inp=list()
temp=list()
for i in range(N):
    temp.append(input().split())
    if 'push' in temp[i][0]:
        inp.append([temp[i][0],int(temp[i][1])])
    else:
        inp.append(list(temp[i]))
del temp

deq=[]
for order in inp:
    if 'push_front' in order:
        if deq:
            deq.append(0)
            ln=len(deq)-1
            for i in range(ln):
                deq[ln-i]=deq[ln-1-i]
            deq[0]=order[1]
        else:
            deq.append(order[1])
    if 'push_back' in order:
        deq.append(order[1])
    if 'pop_front' in order:
        if deq:
            print(deq[0])
            del deq[0]
        else:
            print(-1)
    if 'pop_back' in order:
        if deq:
            print(deq[-1])
            del deq[-1] 
        else:
            print(-1) 
    if 'size' in order:
        print(len(deq))
    if 'empty' in order:
        print(0 if deq else 1)
    if 'front' in order:
        print(deq[0] if deq else -1)
    if 'back' in order:
        print(deq[-1] if deq else -1)
        


