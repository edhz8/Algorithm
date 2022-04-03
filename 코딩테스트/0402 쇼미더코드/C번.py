# 17차 제출 : 16:48 / 1896ms / 1029B
import sys
input = sys.stdin.readline
N,S,ans,LIMIT = int(input()),input().strip(),0,10**9+7
W,H,E=[],[],[]
for i in range(len(S)):
    if S[i] == 'W': W.append(i)
    if S[i] == 'H': H.append(i)
    if S[i] == 'E': E.append(i)
dpw,dpe=[0 for _ in range(len(H))],[0 for _ in range(len(H))]
if W and H and len(E)>1:
    windex,hindex = 0,0
    while windex<len(W) and hindex<len(H):
        if hindex>0 : dpw[hindex] = dpw[hindex-1]
        while windex<len(W) and W[windex]<H[hindex]:
            dpw[hindex] += 1
            windex += 1
        hindex += 1
    for i in range(hindex,len(H)): dpw[i] = dpw[hindex-1]

    hindex,eindex = len(H)-1,len(E)-1
    while eindex>=0 and hindex>=0 :
        if hindex < len(H)-1 : dpe[hindex] = dpe[hindex+1]
        while eindex>=0 and E[eindex]>H[hindex]:
            dpe[hindex] += 1
            eindex -= 1
        hindex -= 1
    for i in range(hindex,-1,-1) : dpe[i] = dpe[hindex+1]

    for e,w in zip(dpe,dpw):
        ans += (2**e -(1+e))*w
        if ans>=LIMIT : ans%=LIMIT
print(ans)