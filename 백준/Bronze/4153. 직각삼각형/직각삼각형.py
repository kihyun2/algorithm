while True:
    lst = list(map(int, input().split()))
    if not sum(lst):
        break
    lst.sort()
    a, b, c = lst
    if (a**2 + b**2) == c**2:
        print('right')
    else:
        print('wrong')
