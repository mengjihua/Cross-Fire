from typing import List, Tuple, Dict, Set, Optional
from collections import defaultdict, Counter, deque
from itertools import permutations, combinations
from datetime import datetime, date, time, timedelta
from time import time as timestamp, sleep
from functools import cmp_to_key, lru_cache, reduce
from math import gcd, sqrt, log, ceil, floor, inf
from bisect import bisect_left, bisect_right
from heapq import heappush, heappop, heapify, nsmallest, nlargest
from sys import setrecursionlimit, stdin, stdout
from random import getrandbits
setrecursionlimit(5 * 10 ** 4 + 1)
input = lambda: stdin.readline().rstrip()
RD = getrandbits(31)
def fmax(a, b): return a if a > b else b
def fmin(a, b): return a if a < b else b
def lcm(a, b): return a * b // gcd(a, b)

t = int(input())

# 计算 n 经过多少次操作变为0
def cal_op_cnt(n):
    # return int(log(n, 3)) + 1  存在精度问题
    res = 0
    while n > 0:
        n //= 3
        res += 1
    return res

# 预处理, 计算 n 经过多少次操作变为0
op_cnt = [0] * (2 * 10 ** 5 + 2)
for i in range(1, len(op_cnt)):
    op_cnt[i] = op_cnt[i // 3] + 1

# 判断是否为3的幂, 超时
# def not_is_power_of_3(n):
#     if n < 1:
#         return False
#     while n % 3 == 0:
#         n //= 3
#     return n != 1

# 预处理, 判断是否为3的幂
not_is_power_of_3 = [True] * (2 * 10 ** 5 + 2)
# print(log(2 * 10 ** 5 + 1, 3))
for i in range(12):
    not_is_power_of_3[3 ** i] = False

def solve():
    l, r = map(int, input().split())
    ans = op_cnt[l]
    
    # 超时, 不能一个一个计算
    # l_bound, r_bound = l, r
    # while not_is_power_of_3[l_bound] and l_bound <= r_bound:
    #     ans += op_cnt[l_bound]
    #     l_bound += 1
    # while not_is_power_of_3[r_bound + 1] and l_bound <= r_bound:
    #     ans += op_cnt[r_bound]
    #     r_bound -= 1
    
    # 存在 一个区间内 op_cnt 恒定的情况, 直接计算贡献
    if op_cnt[l] == op_cnt[r]:
        return ans + op_cnt[l] * (r - l + 1)
    # 找到 左右边界, 方便后续计算循环
    if not_is_power_of_3[l]:
        l_bound = bisect_left(op_cnt, op_cnt[l] + 1, l, r + 1)
        ans += op_cnt[l] * (l_bound - l)
    else: l_bound = l
    if not_is_power_of_3[r + 1]:
        r_bound = bisect_left(op_cnt, op_cnt[r + 1], l, r + 1) - 1
        ans += op_cnt[r] * (r - r_bound)
    else: r_bound = r
    # 计算 每个区间(op_cnt恒定) 的贡献
    start, end = op_cnt[l_bound], op_cnt[r_bound]
    while start <= end:
        loop_len = 2 * 3 ** (start - 1)  # 每个区间的长度
        ans += loop_len * start
        start += 1

    return ans

# 不使用 op_cnt 预处理
# def solve():
#     l, r = map(int, input().split())
#     ans = cal_op_cnt(l)
    
#     # 存在 一个区间内 op_cnt 恒定的情况, 直接计算贡献
#     if cal_op_cnt(l) == cal_op_cnt(r):
#         return ans + cal_op_cnt(l) * (r - l + 1)
#     # 找到 左右边界, 方便后续计算循环
#     if not_is_power_of_3[l]:
#         l_op_cnt = cal_op_cnt(l)
#         l_bound = 3 ** l_op_cnt
#         ans += l_op_cnt * (l_bound - l)
#     else: l_bound = l
#     if not_is_power_of_3[r + 1]:
#         r_op_cnt = cal_op_cnt(r + 1)
#         r_bound = 3 ** (r_op_cnt - 1) - 1
#         ans += r_op_cnt * (r - r_bound)
#     else: r_bound = r
#     # 计算 每个区间(op_cnt恒定) 的贡献
#     start, end = cal_op_cnt(l_bound), cal_op_cnt(r_bound)
#     while start <= end:
#         loop_len = 2 * 3 ** (start - 1)  # 每个区间的长度
#         ans += loop_len * start
#         start += 1

#     return ans

ans = []
for _ in range(t):
    ans.append(solve())
print(*ans, sep='\n')