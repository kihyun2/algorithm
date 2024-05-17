def merge_sort(array):
	if len(array) < 2:
		return array
	mid = len(array) // 2
	low_arr = merge_sort(array[:mid])
	high_arr = merge_sort(array[mid:])

	merged_arr = []
	l = h = 0
	while l < len(low_arr) and h < len(high_arr):
		if low_arr[l][1] < high_arr[h][1]:
			merged_arr.append(low_arr[l])
			l += 1
		elif low_arr[l][1] == high_arr[h][1]:
			if low_arr[l][0] < high_arr[h][0]:
				merged_arr.append(low_arr[l])
				l += 1
		else:
			merged_arr.append(high_arr[h])
			h += 1
	merged_arr += low_arr[l:]
	merged_arr += high_arr[h:]
	return merged_arr

N = int(input())
member = []
for i in range(1,N+1):
    a, b = input().split()
    member.append([i,int(a), b])



member = merge_sort(member)

for row in member:
    print(row[1],row[2])