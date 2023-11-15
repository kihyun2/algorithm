N = int(input())
lst = list(map(str,[x for x in range(1, N+1)]))

for idx, val in enumerate(lst):
    if val.count('3') + val.count('6') + val.count('9'):
        jjak = val.count('3') + val.count('6') + val.count('9')

        lst[idx] = '-' * jjak

print(*lst)