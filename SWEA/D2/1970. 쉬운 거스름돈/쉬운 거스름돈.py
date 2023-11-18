T = int(input())

def balance(n, bill):
    global N
    lst.append(N//bill)
    N -= bill * lst[n]

for tc in range(1, T+1):
    N = int(input())
    lst = []
    paper = [50000,10000,5000,1000,500,100,50,10]

    for i in range(len(paper)):
        balance(i, paper[i])
    
    print(f'#{tc}')
    print(*lst)