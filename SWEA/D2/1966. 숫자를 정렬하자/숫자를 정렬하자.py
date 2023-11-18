T = int(input())

for tc in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))

    for head in range(N):
        min = head
        for i in range(head+1, N):
            if lst[min] > lst[i]:
                min = i
        lst[head], lst[min] = lst[min], lst[head]
    
    print(f'#{tc}',*lst)