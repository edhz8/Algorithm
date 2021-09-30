n=int(input())
tree=[[] for _ in range(n)]
for index,num in enumerate(map(int,input().split())):
    if num != -1 : tree[num].append(index)
erase=int(input())
blackList=[erase]
while blackList:
    poped = blackList.pop(0)
    blackList+=tree[poped]
    tree[poped]=[-1]
cnt=0
for i in range(n):
        if erase in tree[i] : tree[i].remove(erase);break
print(tree.count([]))