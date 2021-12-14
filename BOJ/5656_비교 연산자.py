n=1
while True:
    i=input()
    if 'E' in i : break
    print('Case ',n,': ',str(eval(i)).lower(),sep='')
    n+=1