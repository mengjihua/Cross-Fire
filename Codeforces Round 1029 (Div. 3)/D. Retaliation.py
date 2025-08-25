t = int(input().strip())
results = []

for _ in range(t):
    n = int(input().strip())
    a = list(map(int, input().split()))
    
    # 位置1：x + n * y = a[0]
    # 位置2：2x + (n - 1) * y = a[1]
    A1 = a[0]
    A2 = a[1]
    total = n + 1
    num = 2 * A1 - A2
    
    # 保证 y 为非负整数
    if num < 0 or num % total != 0:
        results.append("NO")
        continue
        
    y = num // total
    x = A1 - n * y
    
    # 保证 x 为非负整数
    if x < 0:
        results.append("NO")
        continue
        
    valid = True
    for i in range(n):
        pos = i + 1
        value = x * pos + y * (n - pos + 1)
        if value != a[i]:
            valid = False
            break
            
    results.append("YES" if valid else "NO")

for res in results:
    print(res)