for tc in range(1,11):
    N = int(input())
    lst = list(map(int,input().split()))

    avg = (min(lst)+max(lst)) // 2

    for _ in range(N):
        mini = min(lst)
        if mini != avg:
            maxIndex = lst.index(max(lst))
            minIndex = lst.index(mini)
            lst[maxIndex] -= 1
            lst[minIndex] += 1
        else:
            break
    result = lst[lst.index(max(lst))] - lst[lst.index(min(lst))]
    print(f'#{tc} {result}')
