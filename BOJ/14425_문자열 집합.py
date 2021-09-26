import sys
I = sys.stdin.readline
class Node():
    def __init__(self,key):
        self.key=key
        self.children=dict()
class Trie():
    def __init__(self):
        self.head = Node(None)
    def insert(self,string):
        cNode=self.head
        for s in string:
            if s not in cNode.children : cNode.children[s] = Node(s)
            cNode = cNode.children[s]
    def isExist(self,string):
        cNode=self.head
        for s in string:
            if s not in cNode.children : return 0
            cNode = cNode.children[s]
        return int('\n' in cNode.children)
        

N,M=map(int,I().split())
trie,ret=Trie(),0
for _ in range(N) : trie.insert(I())
for _ in range(M) : ret+=trie.isExist(I().rstrip())
print(ret)