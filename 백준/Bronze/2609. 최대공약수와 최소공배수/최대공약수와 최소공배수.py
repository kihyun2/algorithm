a,b = map(int, input().split())
n, x = min(a,b), max(a,b)

while n > 0:
    n, x = x % n, n
print(x)
print((a*b)//x)