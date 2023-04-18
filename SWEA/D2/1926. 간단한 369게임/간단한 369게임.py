T = int(input())

    
samyogu=['3', '6', '9']
lst=[list(map(str,str(x))) for x in range(1,T+1)]



for idx in range(len(lst)):
    tmp=0
    for el in lst[idx]:
        if el in samyogu:
            tmp+=1
    if tmp > 0:
        lst[idx]='-'*tmp

for idx in range(len(lst)):
    if idx != 0:
        print(' ',end='')
    for idxe in range(len(lst[idx])):
        print(lst[idx][idxe], end='')

