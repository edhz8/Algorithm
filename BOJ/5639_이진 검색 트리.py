def solution(start, end):
    if start > end: return
    div = end + 1
    for i in range(start + 1, end + 1):
        if tree[start] < tree[i]:div = i;break
    solution(start + 1, div - 1)
    solution(div, end)
    print(tree[start])

import sys
sys.setrecursionlimit(10 ** 9)
tree = []
while True:
    try:
        temp = int(input())
    except: break
    tree.append(temp)
solution(0, len(tree) - 1)