import sys
I = sys.stdin.readline
class Node():
    def __init__(self,key):
        self.key=key
        self.children=dict()
        self.isPressed = False
class Trie():
    def __init__(self):
        self.head = Node(None)
    def insert(self,string):
        cNode=self.head
        self.head.isPressed = True
        for c in string:
            if c not in cNode.children : 
                if len(cNode.children)==1 : cNode.isPressed = True
                cNode.children[c] = Node(c)
            cNode=cNode.children[c]
    def count(self,string):
        cNode,cnt=self.head,0
        for c in string:
            if c=='\n' : break
            if cNode.isPressed : cnt+=1
            cNode = cNode.children[c]
        return cnt
try:
    while True:
        trie,n,cnt = Trie(),int(I()),0
        strs = [I() for _ in range(n)]
        for s in strs : trie.insert(s)
        for s in strs : cnt+=trie.count(s)
        print('%.2f' % (cnt/n))
except : 
    exit(0)