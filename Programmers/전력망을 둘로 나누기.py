from collections import defaultdict
def solution(n, wires):
    graph=defaultdict(list)
    res = 101
    for a,b in wires:
        graph[a].append(b)
        graph[b].append(a)
    for a,b in wires:
        nodes,cnt,visited=[a],0,[b]
        while nodes:
            node = nodes.pop()
            if node in visited: continue
            visited.append(node)
            cnt+=1
            nodes+=graph[node]
        res = min(res,abs(n-cnt*2))
    return res