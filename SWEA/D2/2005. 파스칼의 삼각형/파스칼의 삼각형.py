T = int(input())

for tc in range(1, T+1):
    n = int(input())
    nums=[]
    temp = []
    temp2 = []
    for i in range(1, n+1):
        temp2=[]
        if i > 1:
            temp2.append(1)
            for j in range(len(nums)-1):
                temp_num = nums[j] + nums[j+1]
                temp2.append(temp_num)
            temp2.append(1)
            temp.append(temp2)
                
        else:
            temp.append([1])
        nums = temp2
        
    print(f'#{tc}')
    for ele in temp:
        for mele in ele:
            print(mele, end=' ')
        print()
