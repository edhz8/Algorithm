ts = [int(input()) for _ in ' '*int(input())]
MAX = max(ts)+1
arr = [[0,0] for _ in ' '*(MAX)]
arr[2] = [1,0]
arr[3] = [1,1]
for i in range(4,MAX) : arr[i] = [arr[i-2][0]+1,sum(arr[i-3])+1]
print(*[sum(arr[n])+1 for n in ts])