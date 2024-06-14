def solution(numbers, hand):
    answer = ''
    pad = [[1,2,3],
           [4,5,6],
           [7,8,9],
           ['*',0,'#']]
    left = [3,0]
    right = [3,2]
    for num in numbers:
        for r in range(4):
            for c in range(3):
                if pad[r][c] == num:
                    tr,tc = r,c
                    break
        if num in [1,4,7]:
            left = [tr, tc]
            answer += 'L'
            continue
        elif num in [3,6,9]:
            right = [tr, tc]
            answer += 'R'
            continue
        left_diff = abs(left[0] - tr) + abs(left[1] - tc)
        right_diff = abs(right[0] - tr) + abs(right[1] - tc)
        if left_diff > right_diff:
            right = [tr, tc]
            answer += 'R'
        elif left_diff < right_diff:
            left = [tr, tc]
            answer += 'L'
        elif left_diff == right_diff:
            if hand == 'left':
                left = [tr, tc]
                answer += 'L'
            elif hand == 'right':
                right = [tr, tc]
                answer += 'R'

    return answer