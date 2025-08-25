from collections import deque

t = int(input())

for _ in range(t):
    n = int(input())
    lst = deque()
    for i in range(n, 0, -1):
        if i % 2 == 0:
            lst.appendleft(i)
        else:
            lst.append(i)
    print(*lst)