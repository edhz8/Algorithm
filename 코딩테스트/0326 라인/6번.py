from collections import defaultdict
from heapq import heappush,heappop
def solution(req_id, req_info):
    gold,silver = defaultdict(int),defaultdict(int)
    buy,sell = [],[]
    for id,[type,amount,price] in zip(req_id,req_info):
        heappush(buy if type else sell,[price,amount,id])
        if not buy or not sell : continue
        minBuy,minSell = buy[0],sell[0]
        if minBuy[0] < minSell[0] : continue
        minBuy,minSell = heappop(buy),heappop(sell)

        tamount = min(minBuy[1] , minSell[1])
        tprice = tamount * minSell[0]
                
        gold[minBuy[2]] += tamount
        silver[minBuy[2]] -= tprice 
        gold[minSell[2]] -= tamount
        silver[minSell[2]] += tprice 
        
        if minBuy[0] == minSell[0] : continue
        if minBuy[0] > tamount : 
            minBuy[1] -= tamount
            heappush(buy,minBuy)
        else : 
            minSell[1] -= tamout
            heappush(sell,minSell)