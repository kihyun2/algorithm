N = int(input())
tshirt = list(map(int,input().split()))
T,P = map(int, input().split())
tmook = 0

for i in tshirt:
    if i == 0:
        continue
    if i <= T:
        tmook += 1
    else:
        if i % T == 0:
            tmook += i // T
        else:
            tmook += (i // T) + 1
print(tmook)
print((N // P), (N % P))