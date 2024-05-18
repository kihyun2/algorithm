N, K = map(int, input().split())

def fac(x):
    t = 1
    for i in range(2, x+1):
        t *= i
    return t
result = fac(N) // (fac(N-K) * fac(K))
print(result)