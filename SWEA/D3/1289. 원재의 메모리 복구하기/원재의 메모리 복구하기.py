T = int(input())

for tc in range(1,T+1):
    result = 0
    
    mem = input()
    bit = '0'

    for idx, val in enumerate(mem):
        if val != bit:
           bit = mem[idx]
           result += 1



    print(f'#{tc} {result}')