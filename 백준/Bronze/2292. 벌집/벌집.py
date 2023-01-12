room=int(input())
cnt=0
if room == 1: cnt=1
while room > 1:
    room=room-(6*cnt)
    cnt+=1
print(cnt)