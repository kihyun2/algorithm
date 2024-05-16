T = int(input())

for tc in range(1, T + 1):
    result = 'yes'
    a, b = input().split()
    a, b = a*2, b*2

    if len(a) > len(b):
        for idx, element in enumerate(a):
            if b[idx % len(b)] != element:
                result = 'no'
    elif len(a) < len(b):
        for idx, element in enumerate(b):
            if a[idx % len(a)] != element:
                result = 'no'
    else:
        if a != b:
            result = 'no'



    print(f'#{tc} {result}')
