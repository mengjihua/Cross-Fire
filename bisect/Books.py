n, m = map(int, input().split())
lst = [0] + list(map(int, input().split()))

pre_sum = [0] * (n + 1)
for i in range(1, n + 1):
    pre_sum[i] = pre_sum[i - 1] + lst[i]

def check(judge):
    for l in range(1, n - judge + 2):
        r = l + judge - 1
        if pre_sum[r] - pre_sum[l - 1] <= m:
            return True
    return False

ans = 0  
l, r = 0, n
while l <= r:
    mid = (l + r) // 2
    if check(mid):
        ans = mid
        l = mid + 1
    else:
        r = mid - 1
print(ans)