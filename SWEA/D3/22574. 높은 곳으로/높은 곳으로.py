T = int(input())
for _ in range(T):
    N, P = map(int, input().split())
    coord = 0
    for i in range(N+1):
        coord += i
        if coord == P:
            coord -= 1
    print(coord)
