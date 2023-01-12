n=int(input())
a=[]

for i in range(n):
    a.append(int(input()))

a.sort()
for i in a:
    print(i)