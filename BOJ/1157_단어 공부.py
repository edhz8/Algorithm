from collections import Counter
n=Counter(input().upper()).most_common(2)
print('?' if len(n)>1 and n[0][1]==n[1][1] else n[0][0])