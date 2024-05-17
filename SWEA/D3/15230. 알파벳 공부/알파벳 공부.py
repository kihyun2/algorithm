T = int(input())
for tc in range(1, T + 1):
    A = input()

    result = 0
    for i in range(len(A)):
        if A[i] == chr(ord('a')+i):
            result += 1
        else: break

    print(f'#{tc} {result}')
    
