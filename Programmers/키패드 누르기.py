def solution(numbers, hand):
    answer = ''
    lastL,lastR=9,11
    for i in range(len(numbers)):
        if numbers[i]==0: numbers[i]=11
        numbers[i]-=1
    
    for num in numbers:
        if num%3==0: answer+='L';lastL=num
        elif num%3==2: answer+='R';lastR=num
        else:
            dl=abs(num//3-lastL//3)+abs(num%3-lastL%3)
            dr=abs(num//3-lastR//3)+abs(num%3-lastR%3)
            if dl > dr:answer+='R';lastR=num
            elif dl < dr:answer+='L';lastL=num
            else :
                if hand=='right':answer+='R';lastR=num
                else :answer+='L';lastL=num  
    return answer