n = int(input())
lst = list(map(int, input().split()))
check_lst = lst.copy()
check_lst.sort()

ans = []
def solve():
    for i in range(n):
        temp1, temp2 = i, i + 1
        judge = False
        if lst[i] != check_lst[i]:
            for j in range(i + 1, n):
                if lst[j] == check_lst[i]:
                    temp2 = j
                    judge = True
                    break
        if judge:
            lst[temp1], lst[temp2] = lst[temp2], lst[temp1]
            ans.append((temp1, temp2))

solve()

print(len(ans))
for i in ans:
    print(*i)