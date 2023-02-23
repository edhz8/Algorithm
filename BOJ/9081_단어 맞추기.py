for _ in ' '*int(input()):
    line = list(input())
    i,j=-1,1
    for index in range(len(line)-2,-1,-1):
        if line[index]<line[index+1] : i = index;break
    for index in range(len(line)-1,-1,-1):
        if line[i]<line[index] : j=index;break
    if i==-1 : print(''.join(line));continue
    line[i],line[j]=line[j],line[i]
    print(''.join(line[:i+1]+line[i+1:][::-1]))