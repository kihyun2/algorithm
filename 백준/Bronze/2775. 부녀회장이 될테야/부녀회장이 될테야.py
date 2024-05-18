T = int(input())

for _ in range(T):
    k = int(input())
    n = int(input())
    apart = [[] for _ in range(k+1)]
    apart[0]= [x for x in range(1,n+1)]
    for i in range(k):
        for a in apart[i]:
            if not apart[i+1]:
                tmp = a
                apart[i+1].append(tmp)
            else:
                tmp += a
                apart[i+1].append(tmp)

            
    print(apart[k][n-1])