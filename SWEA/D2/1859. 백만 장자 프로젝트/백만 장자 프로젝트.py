T = int(input())

for tc in range(1, T+1):
    N = int(input())
    prices = list(map(int, input().split()))
    profit = 0
    max_price = 0

    for idx in range(N-1, -1, -1):
        price = prices[idx]
        if price > max_price:
            max_price = price
        else:
            profit += max_price - price

    print(f'#{tc} {profit}')