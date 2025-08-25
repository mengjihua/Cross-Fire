t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    s = input()
    
    cnt0 = s.count('0')
    
    m = n // 2
    lower = m - k
    upper = m + k

    if cnt0 >= lower and cnt0 <= upper and (cnt0 - lower) % 2 == 0:
        print('YES')
    else:
        print('NO') 