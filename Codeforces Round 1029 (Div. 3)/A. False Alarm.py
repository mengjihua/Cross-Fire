t = int(input())

for _ in range(t):
    n, x = map(int, input().split())
    lst_a = list(map(int, input().split()))
    
    start, end = n - 1, 0
    for i in range(n):
        if lst_a[i] == 1:
            start = min(i, start)
            end = max(i, end)
    
    if end - start + 1 <= x:
        print('YES')
    else:
        print('NO')