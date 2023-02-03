N, M = map(int, input().split())
chess = []
result = []

for _ in range(N):
    chess.append(input())

for a in range(N-7):
    for b in range(M-7):
        draw1 = 0
        draw2 = 0
        for i in range(a, a+8):
            for j in range(b, b+8):
                if (i+j) % 2 == 0:
                    if chess[i][j] != 'W':
                        draw1 += 1
                    if chess[i][j] != 'B':
                        draw2 += 1
                else:
                    if chess[i][j] != 'B':
                        draw1 += 1
                    if chess[i][j] != 'W':
                        draw2 += 1
        result.append(draw1)
        result.append(draw2)

print(min(result))