t = int(input())

def solve(s):
    target = int(s)
    max_sum = int(target ** 0.5)

    if max_sum * max_sum != target:
        return None

    for a in range(max_sum + 1):
        b = max_sum - a
        if 0 <= b <= 99:
            return a, b

    return None

for _ in range(t):
    s = input().strip()
    res = solve(s)
    if res is None:
        print(-1)
    else:
        print(res[0], res[1])