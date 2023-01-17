while True:
    pal=input()
    if pal == '0':break
    if len(pal) == 2:
        if pal[0]==pal[1]:
            print('yes')
        else:
            print('no')
    else:
        front=pal[0:len(pal)//2]
        rear=pal[:(len(pal)//2)-1:-1]
        if len(pal)%2!=0:
            if front==rear[:-1]:print('yes')
            else: print('no')
        else:
            if front==rear:print('yes')
            else: print('no')