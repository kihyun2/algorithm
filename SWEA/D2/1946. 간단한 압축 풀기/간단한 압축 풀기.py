T = int(input())

for tc in range(1, T+1):
    N = int(input())
    lst = []
    text = ''
    for i in range(N):
        letter, cnt = input().split()
        cnt = int(cnt)
        text += letter * cnt

    print(f'#{tc}', end='')

    for i in range(len(text)):
        if i % 10 == 0:
            print()
        print(text[i], end='')

    print()