N,num,cnt = int(input()),0,0
while True:
    if '666' in str(num): 
        cnt +=1
        if N==cnt :
            print(num)
            break
    num+=1