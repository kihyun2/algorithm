# 2805
def serch(wood, lo, hi, M): 
    while lo+1<hi:
        target=((lo+hi)//2)
        wood_max=0
        for wood_inx in wood:
            if(wood_inx>target):
                wood_max+=(wood_inx-target)
        if wood_max >= M:
            lo=target
        elif wood_max <= M:
            hi=target

    return lo


N, M=map(int, input().split())
wood=sorted(list(map(int,input().split())))
lo=0
hi=wood[N-1]

print(serch(wood, lo, hi, M))

