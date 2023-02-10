def solution(id_list, report, k):
    answer = [0 for _ in range(len(id_list))]
    report=list(set(report))
    report_dict={}

    for target in report:
        idx, value = target.split()
        if idx in report_dict.keys():
            report_dict[idx].append(value)
        else:
            report_dict[idx] = []
            report_dict[idx].append(value)
    

    for id in id_list:
        cnt=0
        for key in report_dict:
            if id in report_dict[key]:
                cnt+=1
        if cnt>=k:
            for idx, id2 in enumerate(id_list):
                if id2 in report_dict.keys():
                    if id in report_dict[id2]:
                        answer[idx]+=1
    
    return answer