def solution(board, moves):
    answer = 0
    basket = []
    sero = len(board[0])
    
    for m in moves :
        for i in range(0,sero):
            if board[i][m-1] != 0:
                if len(basket)==0:
                    basket.append(board[i][m-1])
                elif basket[-1] == board[i][m-1] :
                    basket.pop()
                    answer+=2
                else :
                    basket.append(board[i][m-1])
                board[i][m-1] = 0
                break               
    return answer