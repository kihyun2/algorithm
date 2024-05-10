T = int(input())

for tc in range(1, T + 1):
    
    S = input()
    print(f'#{tc} {"YES" if S[:int((len(S)-1)/2)] == S[int((len(S)-1)/2)+1:] else "NO"}')