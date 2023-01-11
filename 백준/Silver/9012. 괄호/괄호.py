T=int(input())
ps=list()
for _ in range(T):
    ps.append(list(input()))

for i in ps:
    left=0
    right=0
    switch=False
    for q in i:
        if q=='(': left+=1   
        elif left-right==0 and q==')':
            switch=True
        else:right+=1
    if switch:
        print('NO')
    else:
        print('YES' if left==right else 'NO')

# 이렇게 만드니까 ')(' 처럼 서로 반대를 보고있는 경우에 막을 수가 없음
# 해결-> 먼저 ')'가 오는 경우 'NO'를 출력