def solution(h, w, n, board):
    ans = 0
    for i in range(h):
        for j in range(w):
            if board[i][j]=='0' : continue
            if i+n<=h and (i-1<0 or board[i-1][j]=='0') and (i+n>h-1 or board[i+n][j]=='0'):
                INMOK=True
                for k in range(i,i+n):
                    if board[k][j]=='0':
                        INMOK = False
                        break
                if INMOK : ans +=1
            if j+n<=w and (j-1<0 or board[i][j-1]=='0') and (j+n>w-1 or board[i][j+n]=='0'):
                JNMOK=True
                for k in range(j,j+n):
                    if board[i][k]=='0':
                        JNMOK = False
                        break
                if  JNMOK : ans += 1
            if i+n<=h and j+n<=w and ((i-1<0 or j-1<0) or board[i-1][j-1]=='0') and ((i+n>h-1 or j+n>w-1) or board[i+n][j+n]=='0'):
                DNMOK=True
                for k in range(0,n):
                    if board[i+k][j+k]=='0':
                        DNMOK = False
                        break
                if  DNMOK : ans += 1
            if i-n+1>=0 and j+n<=w and ((i+1>h-1 or j-1<0) or board[i+1][j-1]=='0') and ((i-n<0 or j+n>w-1) or board[i-n][j+n]=='0'):
                UNMOK=True
                for k in range(0,n):
                    if board[i-k][j+k]=='0':
                        UNMOK = False
                        break
                if  UNMOK : ans += 1
    return ans