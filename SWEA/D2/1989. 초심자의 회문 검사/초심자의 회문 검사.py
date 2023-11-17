T = int(input())

for tc in range(1, T+1):
    word = input()
    word_L = int((len(word)/2) + 0.5)
    result = 1

    j = -1
    for i in range(word_L):
        if word[i] != word[j-i]:
            result = 0
    
    print(f'#{tc} {result}')