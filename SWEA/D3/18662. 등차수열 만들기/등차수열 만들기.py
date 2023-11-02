
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):

    arry = list(map(int, input().split()))
    
    plus = 1001.0
    minus = 1001.0

    
    # 더하기
    for idx, val in enumerate(arry):
        x = 0.0
        cd2 = arry[2]-arry[1]
        cd1 = arry[1]-arry[0]
        if cd1 == cd2:
            plus, minus = 0.0, 0.0
            break
        if idx == 0:
            while cd1 > cd2:
                val += 0.1
                val = round(val,1)
                cd1 = arry[1] - val
                x += 0.1
                x = round(x,1)
                if cd1 == cd2:
                    if x < plus:
                        plus = x
                    break
        if idx == 1:
            before, after = cd2 - cd1, cd2 - cd1
            while abs(before) >= abs(after):
                before = round(cd2 - cd1,1)
                val += 0.1
                val = round(val,1)
                cd1 = val - arry[0]
                cd1 = round(cd1, 1)
                cd2 = arry[2] - val
                cd2 = round(cd2, 1)
                after = round(cd2 - cd1,1)
                x += 0.1
                x = round(x,1)
                if cd1 == cd2:
                    if x < plus:
                        plus = x
                    break
        if idx == 2:
            while cd1 > cd2:
                val += 0.1
                val = round(val,1)
                cd2 = val - arry[1]
                x += 0.1
                x = round(x,1)
                if cd1 == cd2:
                    if x < plus:
                        plus = x
                    break
    
    # 빼기
    for idx, val in enumerate(arry):
        x = 0.0
        cd1 = arry[1]-arry[0]
        cd2 = arry[2]-arry[1]
        if cd1 == cd2:
            minus = x
            break
        if idx == 0:
            while cd1 < cd2:
                val -= 0.1
                val = round(val,1)
                cd1 = arry[1] - val
                x += 0.1
                x = round(x,1)
                if cd1 == cd2:
                    if x < minus:
                        minus = x
                    break
        if idx == 1:
            before, after = cd2 - cd1, cd2 - cd1
            while abs(before) >= abs(after):
                before = round(cd2 - cd1,1)
                val -= 0.1
                val = round(val, 1)
                cd1 = val - arry[0]
                cd1 = round(cd1, 1)
                cd2 = arry[2] - val
                cd2 = round(cd2, 1)
                after = round(cd2 - cd1,1)
                x += 0.1
                x = round(x,1)
                if cd1 == cd2:
                    if x < minus:
                        minus = x
                    break
        if idx == 2:
            while cd1 < cd2:
                val -= 0.1
                val = round(val,1)
                cd2 = val - arry[1]
                x += 0.1
                x = round(x,1)
                if cd1 == cd2:
                    if x < minus:
                        minus = x
                    break
        

    minus = round(minus,1)
    plus = round(plus,1)
    print(f"#{test_case} {min(minus,plus)}")
