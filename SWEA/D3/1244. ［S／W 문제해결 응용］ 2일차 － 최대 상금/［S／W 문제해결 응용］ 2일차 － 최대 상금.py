T = int(input())

def dfs(n):
    
    global result

    if n == chance:
        result = max(result, int("".join(map(str,lst))))
        return
    
    for i in range(N-1):
        for j in range(i+1,N):
            lst[i], lst[j] = lst[j], lst[i]
            if (n, int("".join(map(str,lst)))) not in check:
                dfs(n+1)
                check.append((n, int("".join(map(str,lst)))))
            lst[i], lst[j] = lst[j], lst[i]

for tc in range(1, T+1):
    lst, chance = input().split()
    lst = [int(i) for i in lst]
    chance = int(chance)
    N = len(lst)
    result = 0
    check = []

    dfs(0)
    print(f'#{tc} {result}')
