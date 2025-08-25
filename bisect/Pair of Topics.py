# t = int(input())
# for _ in range(t):
#     n, k = map(int, input().split())
#     a = list(map(int, input().split()))
#     b = list(map(int, input().split()))
import sys
import bisect
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

lst = [0] * n
for i in range(n):
    lst[i] = a[i] - b[i]
# print(lst)
lst.sort()
# print(lst)
# print(lst)
ans = 0
for i in range(n):
    idx = bisect.bisect_left(lst, -lst[i] + 1)
    # print(i, idx, lst[i], -lst[i] + 1)
    if idx > i:
        ans += n - idx
    else:
        ans += n - i - 1

print(ans)