N=int(input())
people=[]
for _ in range(N):
    people.append(list(map(int,input().split())))

rank=[]

for person in people:
    cnt=0
    for target in people:
        if target[0]>person[0] and target[1]>person[1]:#자기 앞에 있는 등치 큰 사람 수
            cnt+=1
    print(cnt+1,end=' ') # 넌 쟤 뒤에 서 +1

