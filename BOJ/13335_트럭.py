n,w,L = map(int,input().split())
cars,t,bridge = list(map(int,input().split())),0,[]
while cars or bridge:
    t+=1
    while bridge and bridge[0][0] < 2 : bridge.pop(0)
    for i in range(len(bridge)): bridge[i][0] -=1
    if cars and len(bridge)<=w and sum(a for _,a in bridge)+cars[0]<=L: bridge.append([w,cars.pop(0)])
print(t)