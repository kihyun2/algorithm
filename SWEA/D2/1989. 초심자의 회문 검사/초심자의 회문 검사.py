T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    word = input()
    word_back = word[::-1]
    
    if word == word_back:
        print(f'#{test_case} 1')
    else:
        print(f'#{test_case} 0')