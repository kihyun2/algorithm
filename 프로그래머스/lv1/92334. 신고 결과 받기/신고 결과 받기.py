def solution(id_list, report, k):

    answer = [0*m for m in range(len(id_list))]
    report_lst = []
    report_count = {}
    report_dict = {}
    report=list(set(report))
    for target in report:
        report_lst.append(target.split())
        idx, value = target.split()
        if idx in report_dict.keys():
            report_dict[idx].append(value)
        else:
            report_dict[idx] = []
            report_dict[idx].append(value)

    for target in report_lst:
        if target[1] not in report_count:
            report_count[target[1]] = 1
        else:
            report_count[target[1]] += 1
    freeze_lst = []
    for key, value in report_count.items():
        if value >= k:
            freeze_lst.append(key)


    for idx, id in enumerate(id_list):
        if id in report_dict:
            for freeze in freeze_lst:
                if freeze in report_dict[id]:
                    answer[idx] += 1

    return answer