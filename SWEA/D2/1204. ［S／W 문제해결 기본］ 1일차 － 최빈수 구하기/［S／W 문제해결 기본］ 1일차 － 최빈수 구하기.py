T = int(input())

for tc in range(1, T+1):
    result = 0
    q = input()
    lst = list(map(int,input().split()))
    q = [0 for _ in range(101)]
    for element in lst:
        q[element] += 1
    tmp = 0
    for i in range(len(q)):
        if tmp < q[i]:
            tmp = q[i]
            result = i
        elif tmp == q[i]:
            result = i



    print(f'#{tc} {result}')