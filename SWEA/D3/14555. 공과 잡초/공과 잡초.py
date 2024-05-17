T = int(input())

for tc in range(1, T + 1):
    result = 0

    S = input()
    for i in range(len(S)-1):
        if S[i] == '(':
            result += 1
        if S[i] == '|' and S[i+1] == ')':
            result += 1

    print(f'#{tc} {result}')
