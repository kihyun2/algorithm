bal=[]
while True:
    tmp=input()
    if tmp=='.':
        break
    else:
        bal.append(tmp)


open=[]
close=[']',')']
correct=['[]','()']
for row in bal:
    tmp=True
    open.clear()
    for cal in row:
        if cal=='[' or cal=='(':
            open.append(cal)
        if cal in close:
            if open and open[-1]+cal in correct:
                del open[-1]
            else:
                tmp=False
                open.clear()
                break
    if tmp and not open:
        print('yes')
    else:
        print('no')