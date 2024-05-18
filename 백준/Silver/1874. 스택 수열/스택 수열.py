n = int(input())
targets = []
for _ in range(n):
    targets.append(int(input()))

stack = []
result = ''
cnt = 0
for target in targets:
    if cnt < target:
        for a in range(cnt+1,target+1):
            stack.append(a)
            result += '+'
        cnt = stack.pop()
        result += '-'
    elif stack[-1] == target:
        stack.pop()
        result += '-'
    else:
        result = ''
        break

if result:
    for i in result:
        print(i)
else:
    print('NO')

