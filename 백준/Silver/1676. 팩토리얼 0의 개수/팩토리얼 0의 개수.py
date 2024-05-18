N = int(input())
p = 1
for i in range(2, N+1):
    p *= i
a=0
while True:
    if p % 10:
        break
    p = p // 10
    a += 1

print(a)
