N = input()

initN = int(N)

answer = 0
for i in range(initN):
    initN = str(int(initN) - 1)
    num = 0
    for i in initN:
        num += int(i)
    if num + int(initN) == int(N):
        answer = initN

print(answer)