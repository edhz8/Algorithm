import sys
input = sys.stdin.readline
N,H=map(int,input().split())
answer=[N+1,0]
odd,even=[0]*(H+1),[0]*(H+1)
for i in range(N) :
    if i%2==0 : even[int(input())] += 1
    else : odd[int(input())] += 1
for i in range(H-1,0,-1) :
    even[i] += even[i+1]
    odd[i] += odd[i+1]
for i in range(1,H+1):
    cur = odd[i] + even[H-i+1]
    answer = [min(answer[0],cur),answer[1]+(cur==answer[0]) if cur>=answer[0] else 1]
print(*answer)