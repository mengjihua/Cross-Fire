t = int(input())

def solve():
    n, k = map(int, input().split())
    a_lst = list(map(int, input().split()))
    
    res, temp, idx = 0, 0, 0
    while idx < n:
        if a_lst[idx] == 0:
            temp += 1
        else:
            temp = 0
        if temp == k:
            res += 1
            temp = 0
            idx += 1
        idx += 1
    return res

ans = []
for _ in range(t):
    ans.append(solve())

for i in ans:
    print(i)