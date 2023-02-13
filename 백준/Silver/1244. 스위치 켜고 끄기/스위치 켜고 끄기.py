N=int(input())
swt=list(map(int,input().split()))
student=int(input())

def switch_swt(swt, idx):
    if swt[idx]:
        swt[idx]=0
    else:
        swt[idx]=1

for _ in range(student):
    gender, num=map(int, input().split())
    if gender==1: # 남학생
        for i in range(1,(len(swt)//num)+1):
            multiple=(i*num)-1
            switch_swt(swt, multiple)
    else: #여학생
        if num > len(swt)//2:
            switch_swt(swt,num-1)
            for i in range(1,(len(swt)-num)+1):
                low=num-i-1
                high=num+i-1
                if swt[low]==swt[high]:
                    switch_swt(swt, low)
                    switch_swt(swt, high)
                else:
                    break
        if num <= len(swt)//2:
            switch_swt(swt,num-1)
            for i in range(1,num):
                low=num-i-1
                high=num+i-1
                if swt[low]==swt[high]:
                    switch_swt(swt, low)
                    switch_swt(swt, high)
                else:
                    break
cnt=0
while cnt < len(swt):

    print(swt[cnt], end=" ")
    if cnt % 20 == 19:
        print()
    cnt += 1

