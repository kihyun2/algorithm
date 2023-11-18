T = 10
for tc in range(1, T+1):
    N = int(input())
    lst = []
    for _ in range(8):
        lst.append(input())

    result = 0
    for row in range(8):
        for i in range(8-N+1):
            w_word, h_word = '', ''
            for j in range(i, i+N):
                w_word += lst[row][j]
                h_word += lst[j][row]
            if w_word == w_word[::-1]:
                result += 1
            if h_word == h_word[::-1]:
                result += 1
    
    print(f'#{tc} {result}')
            