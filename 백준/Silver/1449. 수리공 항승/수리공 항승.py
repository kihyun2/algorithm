N, L = map(int,input().split())
hole = list(map(int,input().split()))
pipe = ['x' for _ in range(1000)]
for idx in hole:
    pipe[idx-1]='o'
cut=0

for idx in range(len(pipe)):
    if pipe[idx] == 'o':
        cut += 1
        for patch in range(idx, idx+L):
            if patch < len(pipe):
                pipe[patch] = 'x'
            else:
                break


print(cut)