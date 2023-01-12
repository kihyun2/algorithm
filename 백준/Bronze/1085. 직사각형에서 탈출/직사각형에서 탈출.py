x,y,w,h=map(int,input().split())
temp=[x,y,w-x,h-y]
temp.sort()

print(temp[0])