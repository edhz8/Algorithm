import sys
I = sys.stdin.readline
class Node():
    def __init__(self,key):
        self.key = key
        self.children = dict()
class Trie():
    def __init__(self):
        self.head = Node(None)
    def insert(self,string):
        cNode = self.head
        for char in string:
            if char not in cNode.children: cNode.children[char] = Node(char)
        cNode = cNode.children[char]
    def printTrie(self,L,cNode):
        if L==0 : cNode = self.head
        for child in sorted(cNode.children.keys()):
            print('--'*L,child,sep='')
            self.printTrie(L+1,cNode.children[child])
trie = Trie()
for _ in range(int(I())): trie.insert(list(I().split())[1:])
trie.printTrie(0,None)