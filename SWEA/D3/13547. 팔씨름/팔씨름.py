T = int(input())

for tc in range(1, T+1):
    S = input()
    cnt = 0
    for i in S:
        if i == 'o':
            cnt += 1
    if 15 - len(S) >= 8 - cnt:
        print(f'#{tc} YES')
    else:
        print(f'#{tc} NO')