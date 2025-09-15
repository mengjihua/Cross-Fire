t = int(input())

def min_digit(n):
    res = 9
    while n > 0:
        res = min(res, n % 10)
        n //= 10
    return res

ans = []
for _ in range(t):
    x = int(input())
    ans.append(min_digit(x))

for i in ans:
    print(i)