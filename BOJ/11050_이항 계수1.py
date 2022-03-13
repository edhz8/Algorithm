from math import factorial as f
a,b=map(int,input().split());print(f(a)//(f(b)*f(a-b)))