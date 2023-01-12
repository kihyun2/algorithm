import math
a,b,v=map(int,input().split())
n=0
n=(v-a)/(a-b)
print(math.ceil(n+1))