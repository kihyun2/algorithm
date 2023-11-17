for tc in range(1,11):
    N = int(input())
    lst = list(map(int,input().split()))

    # 100 * 100 * 1000 = 10^7    
    for _ in range(N):
        lst[lst.index(max(lst))] -= 1
        lst[lst.index(min(lst))] += 1
    
    result = lst[lst.index(max(lst))] - lst[lst.index(min(lst))]
    print(f'#{tc} {result}')
