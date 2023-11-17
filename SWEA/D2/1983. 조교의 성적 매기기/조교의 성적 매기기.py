T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    # 중간고사[0], 기말고사[1], 과제[2]
    #    35%         45%        20%
    # A+ A0 A- B+ B0 B- C+ C0 C- D0 (10)
    student = [[999, 0]]
    for i in range(1 ,N+1):
        midterm, final, assignment = map(int, input().split())
        student.append([(midterm*0.35) + (final*0.45) + (assignment*0.20), i])

    student.sort(reverse = True)
    # print(student)
    grade = ['A+','A0','A-','B+','B0','B-','C+','C0','C-','D0']
    cut = N//10
    a = 0

    for rank in range(1,N+1):
        if K == student[rank][1]:
            gradeIdx = (rank - (rank - (cut*a))) // cut
            break
        if rank % (cut) == 0:
            a += 1
    
    print(f'#{tc} {grade[gradeIdx]}')