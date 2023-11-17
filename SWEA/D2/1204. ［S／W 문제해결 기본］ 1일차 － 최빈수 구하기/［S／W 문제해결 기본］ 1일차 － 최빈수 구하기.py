T = int(input())

for tc in range(1, T+1):
    bindo = input()
    lst = list(map(int,input().split()))
    
    # 어차피 안 쓰니까 재활용 개꿀
    bindo = [0 for _ in range(101)]
    
    for element in lst:
        bindo[element] += 1
    
    score = 0
    for i in range(len(bindo)):
        if score <= bindo[i]:
            score = bindo[i]
            result = i



    print(f'#{tc} {result}')