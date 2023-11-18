T = int(input())

for tc in range(1, T+1):
    now_month, now_day, target_month, target_day = map(int,input().split())
    month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    result = sum(month[now_month:target_month], target_day + 1) - (now_day)

    print(f'#{tc} {result}')