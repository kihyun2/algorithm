T = int(input())

for tc in range(1, T + 1):
    boxes = list(map(int, input().split()))
    result = 0
    correct = 0
    while correct < 2:
        correct = 0
        for idx in range(len(boxes)-1):
            if boxes[idx] >= boxes[idx+1]:
                result += boxes[idx] - boxes[idx+1] + 1
                boxes[idx] -= boxes[idx] - boxes[idx+1] + 1
                if boxes[idx] <= 0:
                    result = -1
                    break
            else:
                correct += 1
    
                


    print(f'#{tc} {result}')