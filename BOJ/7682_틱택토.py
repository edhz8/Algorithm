def over(s):
    if all(s==S for S in [g[0],g[1],g[2]]): return 1
    if all(s==S for S in [g[3],g[4],g[5]]): return 1
    if all(s==S for S in [g[6],g[7],g[8]]): return 1

    if all(s==S for S in [g[0],g[3],g[6]]): return 1
    if all(s==S for S in [g[1],g[4],g[7]]): return 1
    if all(s==S for S in [g[2],g[5],g[8]]): return 1

    if all(s==S for S in [g[0],g[4],g[8]]): return 1
    if all(s==S for S in [g[2],g[4],g[6]]): return 1

    return 0

while (g:=input())!='end':
    xc,oc=g.count('X'),g.count('O')
    if xc-oc not in [0,1] :
        print('invalid')
        continue
    if over('X'):
        print('valid' if xc-oc==1 else 'invalid')
        continue
    if over('O'):
        print('valid' if xc-oc==0 else 'invalid')
        continue
    if xc+oc<9 : 
        print('invalid')
        continue
    else : print('valid')