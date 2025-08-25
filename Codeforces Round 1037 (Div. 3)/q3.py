t = int(input())

def solve():
    n, k = map(int, input().split())
    h_lst = list(map(int, input().split()))
    
    cur_time, cur_h = 1, h_lst[k - 1]
    
    h_lst.sort()
    for h in h_lst:
        if h <= cur_h:
            continue
        if cur_time + h - cur_h <= cur_h + 1:
            cur_time += h - cur_h
            cur_h = h
        else:
            return "NO"
    return "YES"
            

ans = []
for _ in range(t):
    ans.append(solve())

for i in ans:
    print(i)