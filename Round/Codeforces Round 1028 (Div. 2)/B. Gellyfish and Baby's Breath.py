mod = 998244353
MAX_EXP = 10 ** 5

P2 = [1] * (MAX_EXP + 1)
for i in range(1, MAX_EXP + 1):
    P2[i] = (P2[i - 1] * 2) % mod

t = int(input())
out_lines = []
for _ in range(t):
    n = int(input())
    p = list(map(int, input().split()))
    q = list(map(int, input().split()))
    
    current_max_a = -1
    idx_max_a = -1
    current_max_b = -1
    idx_max_b = -1
    res = []
    
    for i in range(n):
        if p[i] > current_max_a:
            current_max_a = p[i]
            idx_max_a = i
        if q[i] > current_max_b:
            current_max_b = q[i]
            idx_max_b = i
            
        k1 = i - idx_max_a
        exp_a1 = current_max_a
        exp_b1 = q[k1]
        
        j1 = i - idx_max_b
        exp_a2 = p[j1]
        exp_b2 = current_max_b
        
        max1 = max(exp_a1, exp_b1)
        min1 = min(exp_a1, exp_b1)
        max2 = max(exp_a2, exp_b2)
        min2 = min(exp_a2, exp_b2)
        
        if (max1, min1) > (max2, min2):
            value = (P2[exp_a1] + P2[exp_b1]) % mod
        elif (max1, min1) < (max2, min2):
            value = (P2[exp_a2] + P2[exp_b2]) % mod
        else:
            value = (P2[exp_a1] + P2[exp_b1]) % mod
            
        res.append(value)
        
    print(*res)