A,B=map(int,input().split())
B+=int(input())
print((A+(B//60))%24,B%60)