T = int(input())
for tc in range(1, T+1):
    A, B, C, D = map(int, input().split())
    answer = 0
    for i in range(A, B):
        if C <= i < D:
            answer += 1
    print(f"#{tc} {answer}")