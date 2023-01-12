n = int(input())
strings = []
for _ in range(n):
    strings.append(input())

strings.sort()
strings.sort(key=len)


res = []
for i in strings:
    if i not in res:
        res.append(i)
        print(i)