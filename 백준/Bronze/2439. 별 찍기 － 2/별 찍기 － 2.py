a=int(input())

for i in range(a,0,-1):
    for j in range(i-1):
        print(' ',end='')
    for m in range(a-i+1,0,-1):
        print('*',end='')
    print()