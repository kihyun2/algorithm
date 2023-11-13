T = int(input())

def dfs(n,sum):

    global result


    if n == N:
        if sum == K:
            result += 1
        return
    
    dfs(n+1, sum+nums[n])
    dfs(n+1, sum)

for tc in range(1, T+1):
    N, K = map(int, input().split())
    nums = list(map(int, input().split()))

    result = 0

    dfs(0, 0)

    print(f'#{tc} {result}')