T = int(input())
orders = list()
for tc in range(T):
    orders.append(input())

for order in orders:
    quesmrk = 0
    coord = 0
    answer = 0
    for word in order:
        if word == 'L':
            coord -= 1
        elif word == 'R':
            coord += 1
        else:
            quesmrk += 1

        if answer < abs(coord)+quesmrk:
            answer = abs(coord)+quesmrk
    print(answer)