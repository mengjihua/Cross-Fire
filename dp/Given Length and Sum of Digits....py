import sys

length, sum_digits = map(int, input().split())
if length == 1 and sum_digits == 0:
    print(0, 0)
    sys.exit()
if sum_digits == 0 or sum_digits > 9 * length:
    print(-1, -1)
    sys.exit()

dp_smallest = [[float('inf')] * (sum_digits + 1) for _ in range(length + 1)]
for j in range(1, min(9, sum_digits) + 1):
    dp_smallest[1][j] = j

for i in range(2, length + 1):
    for k in range(10):
        for j in range(1, sum_digits + 1):
            if j > k:
                dp_smallest[i][j] = min(dp_smallest[i][j], dp_smallest[i - 1][j - k] * 10 + k)
            else:
                dp_smallest[i][j] = min(dp_smallest[i][j], dp_smallest[i - 1][j] * 10)

dp_largest = [[-1] * (sum_digits + 1) for _ in range(length + 1)]
for j in range(1, min(9, sum_digits) + 1):
    dp_largest[1][j] = j
for i in range(2, length + 1):
    for k in range(10):
        for j in range(1, sum_digits + 1):
            if j > k:
                dp_largest[i][j] = max(dp_largest[i][j], dp_largest[i - 1][j - k] * 10 + k)
            else:
                dp_largest[i][j] = max(dp_largest[i][j], dp_largest[i - 1][j] * 10)

if dp_smallest[length][sum_digits] == float('inf'):
    dp_smallest[length][sum_digits] = -1
    
# print(dp_smallest, dp_largest)
print(dp_smallest[length][sum_digits], dp_largest[length][sum_digits])