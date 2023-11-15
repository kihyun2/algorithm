T = int(input())

for tc in range(1, T+1):

    lst = list(map(int, input().split()))
    lst.sort()

    result = (sum(lst) - (lst[0] + lst[-1])) / (len(lst) - 2)

    if result % 1 < 0.5:
        result = int(result)
    else:
        result = int(result) + 1

    print(f'#{tc} {result}')