T = int(input())

for _ in range(T):
    n = int(input())
    lst = list(map(int, input().split()))
    print(max(lst))