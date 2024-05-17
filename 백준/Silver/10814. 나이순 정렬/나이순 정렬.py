N = int(input())
member = []
for i in range(1,N+1):
    a, b = input().split()
    member.append([int(a), b])

member.sort(key=lambda x : x[0])

for row in member:
    print(*row)