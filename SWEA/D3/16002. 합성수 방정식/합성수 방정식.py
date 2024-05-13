T = int(input())

for tc in range(1, T+1):
    result = 0
    N = int(input())

    for y in range(N+1, (10**9)-(N+1)):
        bxy = 0
        x = y + N
        for i in range(2, int(y**0.5)+1):
            if y % i == 0:
                bxy += 1
                break
        else:
            continue
        for i in range(2, int(x**0.5)+1):
            if x % i == 0:
                bxy += 1
                break
        if bxy == 2:
            result = x
            break

                

    print(f'#{tc} {result} {result-N}')