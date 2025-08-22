n = int(input())
lst = []

for _ in range(n):
    lst.append(list(map(int, input().split())))
lst.sort(key=lambda x: (x[0], x[1]))

ans = lst[0][1]
for i in range(1, n):
    if ans < lst[i][1]:
        ans = lst[i][1]
    elif ans > lst[i][1]:
        ans = lst[i][0]
print(ans)