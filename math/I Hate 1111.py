t = int(input())
for _ in range(t):
    n = int(input())
    
    while n >= 11:
        length = len(str(n))
        temp = int('1' * length)
        num = n // 10 ** (length - 1)
        n -= temp * num
    
    if n == 0:
        print('YES')
    else:
        print('NO')
        
# def solve():
#     import sys
#     input = sys.stdin.read
#     data = input().split()
#     t = int(data[0])
#     queries = list(map(int, data[1:t+1]))
    
#     max_x = max(queries)
#     if max_x > 10**6:  # 如果 x 太大，不能用 DP
#         print("\n".join("YES" if (x >= 111 * (x % 11)) else "NO" for x in queries))
#         return
    
#     nums = [11, 111, 1111, 11111, 111111]  # 可以动态生成更大的数
#     dp = [False] * (max_x + 1)
#     dp[0] = True
#     for i in range(1, max_x + 1):
#         for num in nums:
#             if num > i:
#                 break
#             if dp[i - num]:
#                 dp[i] = True
#                 break
    
#     for x in queries:
#         print("YES" if dp[x] else "NO")

# solve()