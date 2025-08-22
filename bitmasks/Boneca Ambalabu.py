t = int(input())

# test = []
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    cnt = [0] * 30
    for i in range(n):
        num = a[i]
        for j in range(30):
            cnt[j] += (num >> j) & 1
    
    ans = 0
    for i in range(n):
        temp, num = 0, a[i]
        for j in range(30):
            if num & (1 << j):
                temp += (1 << j) * (n - cnt[j])
            else:
                temp += (1 << j) * cnt[j]
        ans = max(ans, temp)
    
    # test.append(ans)
    print(ans)

# for i in range(t):
#     print(test[i])