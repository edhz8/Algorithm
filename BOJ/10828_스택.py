import sys
I,stack = sys.stdin.readline,[]
for _ in range(int(I())):
    line = I().strip()
    if 'push' in line : stack.append(line[5:])
    elif line == 'size' : print(len(stack))
    elif line == 'empty' : print(+(not stack))
    else : print(-1 if not stack else stack.pop() if line == 'pop' else stack[-1])