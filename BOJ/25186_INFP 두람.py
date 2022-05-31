N=int(input())
if N==1 : print('Happy' if int(input())==1 else 'Unhappy')
else :
    l=list(map(int,input().split()))
    print('Happy' if sum(l)/2>=max(l) else 'Unhappy')