T = int(input())

for tc in range(1, T+1):
    N = int(input())
    lst = [x for x in range(1, N+1)]
    result = 0
    for num in lst:
        if num % 2 == 1:
            result += num
        else:
            result -= num

    print(f'#{tc} {result}')